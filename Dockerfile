FROM python:3.12-slim

# Install git and other utilities needed for setup and compiling
RUN apt-get update && apt-get install -y \
    git \
    curl \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

# Install python dependencies first (caching layer)
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Create necessary directories
RUN mkdir -p /app/chroma_db

# Copy skills folder directly into the image
COPY skills /app/skills

# Copy application code
COPY indexer.py server.py /app/

# Environment Variables
ENV SKILLS_DIR=/app/skills
ENV CHROMA_DB=/app/chroma_db
ENV MCP_HOST=0.0.0.0
ENV MCP_PORT=3001
ENV LOG_LEVEL=INFO

EXPOSE 3001

# Start the MCP server using SSE
# Using Uvicorn explicitly to run the FastMCP app properly with the token injection
CMD ["sh", "-c", "python server.py"]
