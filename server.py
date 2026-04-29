import os
from pathlib import Path
from mcp.server.fastmcp import FastMCP
from pydantic import BaseModel
from indexer import SkillIndexer

# Configuration
SKILLS_DIR = os.environ.get("SKILLS_DIR", "/app/skills")
CHROMA_DB = os.environ.get("CHROMA_DB", "/app/chroma_db")

# Initialize MCP Server
mcp = FastMCP("mcp-skillset")
indexer = SkillIndexer(skills_dir=SKILLS_DIR, db_path=CHROMA_DB)

@mcp.tool()
def skills_search(query: str, n_results: int = 5) -> str:
    """Semantic search across all skills using a text query."""
    results = indexer.search(query, n_results)
    
    if not results or not results['documents'] or not results['documents'][0]:
        return "No skills found matching the query."
    
    response = "Found the following skills:\n\n"
    metadatas = results['metadatas'][0]
    
    for i, meta in enumerate(metadatas):
        response += f"{i+1}. **{meta['name']}** (Category: {meta['category']})\n"
        response += f"   Description: {meta['description']}\n"
        response += f"   Tags: {meta['tags']}\n\n"
        
    return response

@mcp.tool()
def skill_get(name: str) -> str:
    """Load the full markdown content of a skill by name."""
    try:
        results = indexer.collection.get(ids=[name])
        if not results['metadatas']:
            return f"Skill '{name}' not found."
            
        filepath = results['metadatas'][0]['filepath']
        with open(filepath, 'r', encoding='utf-8') as f:
            return f.read()
    except Exception as e:
        return f"Error retrieving skill: {e}"

@mcp.tool()
def skills_recommend(context: str) -> str:
    """Auto-recommend skills based on current context."""
    return skills_search(f"Best skills for: {context}", n_results=3)

@mcp.tool()
def skill_categories() -> str:
    """Browse available skill categories."""
    path = Path(SKILLS_DIR)
    categories = [d.name for d in path.iterdir() if d.is_dir()]
    return f"Available categories:\n- " + "\n- ".join(categories)

@mcp.tool()
def skills_reindex() -> str:
    """Rebuild the search index after adding or modifying skills."""
    count = indexer.reindex()
    return f"Successfully reindexed {count} skills."

@mcp.tool()
def skill_create(name: str, category: str, description: str, content: str) -> str:
    """Create a new skill from parameters."""
    target_dir = Path(SKILLS_DIR) / category / name
    target_dir.mkdir(parents=True, exist_ok=True)
    
    filepath = target_dir / "SKILL.md"
    
    file_content = f"---\nname: {name}\ndescription: {description}\ntags: [{category}]\n---\n{content}"
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(file_content)
        
    indexer.reindex()
    return f"Skill {name} created in {category} and index updated."

@mcp.tool()
def skill_templates_list() -> str:
    """List creation templates for new skills."""
    return """
1. **Basic Trading Skill**:
---
name: [skill_name]
description: [short description]
tags: [tag1, tag2]
---
# Rules
...

2. **OpenAlgo Action**:
---
name: [action_name]
description: [action description]
tags: [openalgo]
---
# API Endpoint
...
"""

if __name__ == "__main__":
    try:
        indexer.collection.get(limit=1)
    except Exception:
        indexer.reindex()
        
    host = os.environ.get("MCP_HOST", "0.0.0.0")
    port = int(os.environ.get("MCP_PORT", "3001"))
    
    print(f"Starting MCP Server on Streamable HTTP at {host}:{port}...")
    
    import uvicorn
    app = mcp.streamable_http_app()
    uvicorn.run(
        app,
        host=host,
        port=port,
        forwarded_allow_ips="*",
        proxy_headers=True,
        server_header=False
    )
