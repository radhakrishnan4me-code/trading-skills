# Custom MCP Skillset Server

A standalone Python Model Context Protocol (MCP) server designed to host and serve a curated list of ~70 Indian trading and analysis skills. The server provides an SSE transport endpoint and includes built-in ChromaDB vector search capabilities.

## Features

- **Built-in Skills**: Automatically clones and bakes in a comprehensive list of trading skills during the Docker build process.
- **FastMCP**: Uses the official Python MCP SDK with Starlette/Uvicorn for high performance.
- **Semantic Search**: Uses `sentence-transformers` and ChromaDB to semantically index skills.
- **7 MCP Tools**: Search, load, create, list categories, recommend, and reindex skills.

## Quick Start

### 1. Configure Environment

Copy the example environment file and set your secure token.

```bash
cp .env.example .env
# Edit .env to set your MCP_AUTH_TOKEN
```

### 2. Build and Run (Docker)

To build the image locally and start the server:

```bash
docker-compose up -d --build
```

### 3. Portainer Deployment

1. Make sure you have pushed this repository to GitHub or another Git host.
2. In Portainer, go to **Stacks** -> **Add Stack**.
3. Select **Repository** and provide your repository URL.
4. Point to `docker-compose.yml`.
5. Under Environment variables, add `MCP_AUTH_TOKEN` with your secure value.
6. Click **Deploy**.

## Available Tools

Once connected to your MCP client (like N8N), the following tools are available:
- `skills_search(query)`: Semantic search across skills
- `skill_get(name)`: Read a skill's full markdown content
- `skills_recommend(context)`: Auto-recommend skills based on current context
- `skill_categories()`: List available categories
- `skill_create(...)`: Template-based skill creation
- `skill_templates_list()`: Show available skill templates
- `skills_reindex()`: Rebuild the semantic search index

## Adding Custom Skills

To add custom skills, simply place them in the `custom-skills/` directory (inside subfolders, e.g. `custom-skills/my-new-skill/SKILL.md`) and rebuild the Docker image:

```bash
docker-compose up -d --build
```

Alternatively, you can uncomment the volume mount in `docker-compose.yml` to map the `custom-skills` folder directly into the container, allowing you to add skills on the fly without rebuilding. If you add skills on the fly, call the `skills_reindex` tool via MCP to update the search index.
