import os
import yaml
from pathlib import Path
from chromadb import PersistentClient
from sentence_transformers import SentenceTransformer

class SkillIndexer:
    def __init__(self, skills_dir: str, db_path: str = "./chroma_db"):
        self.skills_dir = Path(skills_dir)
        self.db_path = db_path
        self.client = PersistentClient(path=self.db_path)
        self.collection = self.client.get_or_create_collection(name="skills")
        self.model = SentenceTransformer("all-MiniLM-L6-v2")

    def parse_skill_file(self, filepath: Path):
        content = filepath.read_text(encoding="utf-8")
        if content.startswith("---"):
            parts = content.split("---", 2)
            if len(parts) >= 3:
                try:
                    frontmatter = yaml.safe_load(parts[1])
                    body = parts[2].strip()
                    return frontmatter, body
                except Exception as e:
                    print(f"Error parsing {filepath}: {e}")
        return None, content

    def reindex(self):
        print(f"Reindexing skills from {self.skills_dir}...")
        # Clear existing
        try:
            self.client.delete_collection("skills")
            self.collection = self.client.create_collection("skills")
        except Exception:
            pass

        skill_files = list(self.skills_dir.rglob("SKILL.md"))
        
        docs = []
        metadatas = []
        ids = []

        for f in skill_files:
            frontmatter, body = self.parse_skill_file(f)
            
            # Combine fields for embedding
            text_to_embed = body
            name = f.parent.name
            desc = ""
            tags = []
            
            if frontmatter:
                name = frontmatter.get("name", name)
                desc = frontmatter.get("description", "")
                tags = frontmatter.get("tags", [])
                text_to_embed = f"{name} {desc} {' '.join(tags)} {body}"

            docs.append(text_to_embed)
            
            # Chroma metadata must be strings or ints/floats
            metadatas.append({
                "name": str(name),
                "description": str(desc),
                "tags": ",".join(tags) if isinstance(tags, list) else str(tags),
                "filepath": str(f.absolute()),
                "category": str(f.parent.parent.name)
            })
            ids.append(str(name))

        if docs:
            # Generate embeddings and add
            print(f"Generating embeddings for {len(docs)} skills...")
            embeddings = self.model.encode(docs).tolist()
            
            self.collection.add(
                documents=docs,
                embeddings=embeddings,
                metadatas=metadatas,
                ids=ids
            )
            print(f"Indexed {len(docs)} skills successfully.")
        else:
            print("No SKILL.md files found.")
        
        return len(docs)

    def search(self, query: str, n_results: int = 5):
        query_embedding = self.model.encode([query]).tolist()
        results = self.collection.query(
            query_embeddings=query_embedding,
            n_results=n_results
        )
        return results

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("--skills-dir", default="/app/skills")
    parser.add_argument("--db-path", default="/app/chroma_db")
    args = parser.parse_args()
    
    indexer = SkillIndexer(args.skills_dir, args.db_path)
    indexer.reindex()
