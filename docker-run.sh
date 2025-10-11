#!/bin/bash

# Script to run commands in Docker container
# Usage: ./docker-run.sh <command>
# Example: ./docker-run.sh ./run_checks.sh

set -e

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

echo -e "${BLUE}🐳 Running command in Docker container: $@${NC}"

# Check if Docker is running
if ! docker info >/dev/null 2>&1; then
    echo -e "${RED}❌ Docker is not running. Please start Docker and try again.${NC}"
    exit 1
fi

# Build the image if it doesn't exist
if ! docker image inspect rl337-dev >/dev/null 2>&1; then
    echo -e "${YELLOW}📦 Building Docker image...${NC}"
    docker build -t rl337-dev .
fi

# Run the command in the container
docker run --rm \
    -v "$(pwd)":/workspace \
    -v /workspace/scripts/venv \
    -w /workspace \
    rl337-dev \
    "$@"
