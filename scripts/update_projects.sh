#!/bin/bash

# Update GitHub Projects Script
# This script analyzes your GitHub repositories and updates the Jekyll project pages

set -e

# Configuration
USERNAME="rl337"
OUTPUT_DIR="docs/_projects"
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
REPO_ROOT="$(dirname "$SCRIPT_DIR")"

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

echo -e "${GREEN}🚀 Updating GitHub Projects for $USERNAME${NC}"

# Check if Python is available
if ! command -v python3 &> /dev/null; then
    echo -e "${RED}❌ Python 3 is required but not installed${NC}"
    exit 1
fi

# Install requirements if needed
if [ ! -d "$SCRIPT_DIR/venv" ]; then
    echo -e "${YELLOW}📦 Creating virtual environment...${NC}"
    cd "$SCRIPT_DIR"
    python3 -m venv venv
    . venv/bin/activate
    pip install -r requirements.txt
else
    echo -e "${YELLOW}📦 Activating virtual environment...${NC}"
    cd "$SCRIPT_DIR"
    . venv/bin/activate
fi

# Check for GitHub token
if [ -z "$GITHUB_TOKEN" ]; then
    echo -e "${YELLOW}⚠️  No GITHUB_TOKEN found. Using unauthenticated requests (lower rate limit)${NC}"
    echo -e "${YELLOW}   To increase rate limits, set GITHUB_TOKEN environment variable${NC}"
    TOKEN_ARG=""
else
    echo -e "${GREEN}✅ Using GitHub token for higher rate limits${NC}"
    TOKEN_ARG="--token $GITHUB_TOKEN"
fi

# Create backup of existing projects
if [ -d "$REPO_ROOT/$OUTPUT_DIR" ] && [ "$(ls -A "$REPO_ROOT/$OUTPUT_DIR")" ]; then
    echo -e "${YELLOW}💾 Creating backup of existing projects...${NC}"
    BACKUP_DIR="$REPO_ROOT/docs/_projects_backup_$(date +%Y%m%d_%H%M%S)"
    cp -r "$REPO_ROOT/$OUTPUT_DIR" "$BACKUP_DIR"
    echo -e "${GREEN}✅ Backup created at $BACKUP_DIR${NC}"
fi

# Run the analysis
echo -e "${GREEN}🔍 Analyzing repositories...${NC}"
cd "$REPO_ROOT"
python3 "$SCRIPT_DIR/analyze_repos.py" \
    --username "$USERNAME" \
    --output "$OUTPUT_DIR" \
    "$TOKEN_ARG"

# Check if any files were created
if [ -d "$OUTPUT_DIR" ] && [ "$(ls -A "$OUTPUT_DIR")" ]; then
    echo -e "${GREEN}✅ Successfully updated project files!${NC}"
    echo -e "${GREEN}📁 Files saved to: $OUTPUT_DIR${NC}"
    
    # Show summary
    echo -e "${YELLOW}📊 Project Summary:${NC}"
    find "$OUTPUT_DIR" -name "*.md" -type f | wc -l | xargs echo "Total project files:"
    
    # Show top 5 most active projects
    echo -e "${YELLOW}🔥 Most Active Projects:${NC}"
    grep -l "activity_level: very_active\|activity_level: active" "$OUTPUT_DIR"/*.md | head -5 | while read -r file; do
        title=$(grep "title:" "$file" | head -1 | sed 's/title: //' | tr -d '"')
        echo "  - $title"
    done
else
    echo -e "${RED}❌ No project files were created${NC}"
    exit 1
fi

echo -e "${GREEN}🎉 Project update complete!${NC}"
echo -e "${YELLOW}💡 Next steps:${NC}"
echo -e "   1. Review the generated project files"
echo -e "   2. Commit and push changes to update your site"
echo -e "   3. Consider setting up automated updates with GitHub Actions"
