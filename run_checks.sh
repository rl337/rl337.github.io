#!/bin/bash

# run_checks.sh - Comprehensive validation script for rl337.org
# This script runs all automated tests, static checks, style linting, and test coverage
# as required by AGENTS.md

set -e

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

# Configuration
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
REPO_ROOT="$SCRIPT_DIR"
PYTHON_SCRIPT_DIR="$REPO_ROOT/scripts"
JEKYLL_DIR="$REPO_ROOT/docs"
PYTHON_VENV="$PYTHON_SCRIPT_DIR/venv"

# Docker detection
IN_DOCKER=false
if [ -f /.dockerenv ] || [ -n "${DOCKER_CONTAINER:-}" ]; then
    IN_DOCKER=true
    echo -e "${BLUE}🐳 Running inside Docker container${NC}"
    echo -e "${BLUE}🐳 DOCKER_CONTAINER=${DOCKER_CONTAINER:-unset}${NC}"
    echo -e "${BLUE}🐳 /.dockerenv exists: $([ -f /.dockerenv ] && echo 'yes' || echo 'no')${NC}"
else
    echo -e "${YELLOW}🐳 Running outside Docker container${NC}"
    echo -e "${YELLOW}🐳 DOCKER_CONTAINER=${DOCKER_CONTAINER:-unset}${NC}"
    echo -e "${YELLOW}🐳 /.dockerenv exists: $([ -f /.dockerenv ] && echo 'yes' || echo 'no')${NC}"
fi

# Counters for reporting
TOTAL_CHECKS=0
PASSED_CHECKS=0
FAILED_CHECKS=0

# Function to run a check and track results
run_check() {
    local check_name="$1"
    local check_command="$2"
    
    echo -e "${BLUE}🔍 Running: $check_name${NC}"
    TOTAL_CHECKS=$((TOTAL_CHECKS + 1))
    
    if eval "$check_command"; then
        echo -e "${GREEN}✅ PASSED: $check_name${NC}"
        PASSED_CHECKS=$((PASSED_CHECKS + 1))
        return 0
    else
        echo -e "${RED}❌ FAILED: $check_name${NC}"
        FAILED_CHECKS=$((FAILED_CHECKS + 1))
        return 1
    fi
}

# Function to check if a command exists
command_exists() {
    command -v "$1" >/dev/null 2>&1
}

# Function to setup Python environment
setup_python_env() {
    echo -e "${YELLOW}🐍 Setting up Python environment...${NC}"
    
    if [ "$IN_DOCKER" = true ]; then
        echo -e "${YELLOW}🐳 Using system Python in Docker container${NC}"
        cd "$PYTHON_SCRIPT_DIR"
        # In Docker, we use system Python with globally installed packages
        # No need for virtual environment
    else
        if [ ! -d "$PYTHON_VENV" ]; then
            echo -e "${YELLOW}📦 Creating Python virtual environment...${NC}"
            cd "$PYTHON_SCRIPT_DIR"
            python3 -m venv venv
        fi
        
        echo -e "${YELLOW}📦 Activating Python virtual environment...${NC}"
        cd "$PYTHON_SCRIPT_DIR"
        source venv/bin/activate
    fi
    
    echo -e "${YELLOW}📦 Installing Python dependencies...${NC}"
    pip install -r requirements.txt
    
    # Install additional tools for validation (only if not in Docker)
    if [ "$IN_DOCKER" = false ]; then
        pip install pytest pytest-cov flake8 black isort mypy
    fi
}

# Function to setup Ruby/Jekyll environment
setup_ruby_env() {
    echo -e "${YELLOW}💎 Setting up Ruby/Jekyll environment...${NC}"
    
    if ! command_exists bundle; then
        echo -e "${YELLOW}⚠️  Bundler not found. Skipping Jekyll validation${NC}"
        return 0
    fi
    
    cd "$JEKYLL_DIR"
    echo -e "${YELLOW}📦 Installing Jekyll dependencies...${NC}"
    
    if [ "$IN_DOCKER" = true ]; then
        # In Docker, install gems globally
        if ! bundle install 2>/dev/null; then
            echo -e "${YELLOW}⚠️  Could not install Jekyll dependencies. Skipping Jekyll validation${NC}"
            return 0
        fi
    else
        # Try to install without sudo, fall back to system gems if needed
        if ! bundle install --path vendor/bundle 2>/dev/null; then
            echo -e "${YELLOW}⚠️  Could not install Jekyll dependencies. Skipping Jekyll validation${NC}"
            return 0
        fi
    fi
}

# Main validation function
main() {
    echo -e "${GREEN}🚀 Starting comprehensive validation for rl337.org${NC}"
    echo -e "${GREEN}================================================${NC}"
    
    # Setup environments
    setup_python_env
    setup_ruby_env
    
    # Set up Python activation command based on Docker detection
    if [ "$IN_DOCKER" = true ]; then
        PYTHON_ACTIVATE=""
    else
        PYTHON_ACTIVATE="source venv/bin/activate &&"
    fi
    
    echo -e "\n${BLUE}🔧 PYTHON VALIDATION${NC}"
    echo -e "${BLUE}===================${NC}"
    
    # Python syntax check
    run_check "Python syntax validation" "cd '$PYTHON_SCRIPT_DIR' && python3 -m py_compile analyze_repos.py"
    
    # Python linting with flake8
    run_check "Python linting (flake8)" "cd '$PYTHON_SCRIPT_DIR' && $PYTHON_ACTIVATE flake8 analyze_repos.py --max-line-length=100 --ignore=E501,W503"
    
    # Python code formatting check with black
    run_check "Python code formatting (black)" "cd '$PYTHON_SCRIPT_DIR' && $PYTHON_ACTIVATE black --check analyze_repos.py"
    
    # Python import sorting check with isort
    run_check "Python import sorting (isort)" "cd '$PYTHON_SCRIPT_DIR' && $PYTHON_ACTIVATE isort --check-only analyze_repos.py"
    
    # Python type checking with mypy (if available)
    if command_exists mypy; then
        run_check "Python type checking (mypy)" "cd '$PYTHON_SCRIPT_DIR' && $PYTHON_ACTIVATE mypy analyze_repos.py --ignore-missing-imports"
    else
        echo -e "${YELLOW}⚠️  Skipping mypy (not installed)${NC}"
    fi
    
    # Python unit tests (if they exist)
    if [ -d "$PYTHON_SCRIPT_DIR/tests" ] || [ -f "$PYTHON_SCRIPT_DIR/test_*.py" ]; then
        run_check "Python unit tests (pytest)" "cd '$PYTHON_SCRIPT_DIR' && $PYTHON_ACTIVATE pytest -v"
    else
        echo -e "${YELLOW}⚠️  No Python tests found - creating basic test structure${NC}"
        # Create a basic test file
        mkdir -p "$PYTHON_SCRIPT_DIR/tests"
        cat > "$PYTHON_SCRIPT_DIR/tests/test_analyze_repos.py" << 'EOF'
#!/usr/bin/env python3
"""Basic tests for analyze_repos.py"""

import unittest
import sys
import os

# Add the parent directory to the path so we can import the module
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from analyze_repos import GitHubRepoAnalyzer

class TestGitHubRepoAnalyzer(unittest.TestCase):
    def test_init(self):
        """Test GitHubRepoAnalyzer initialization"""
        analyzer = GitHubRepoAnalyzer("testuser")
        self.assertEqual(analyzer.username, "testuser")
        self.assertIsNone(analyzer.token)
    
    def test_calculate_activity_score(self):
        """Test activity score calculation"""
        analyzer = GitHubRepoAnalyzer("testuser")
        
        # Test with minimal repo data
        repo = {
            'stargazers_count': 10,
            'forks_count': 5,
            'open_issues_count': 2,
            'size': 1000,
            'pushed_at': None
        }
        
        score = analyzer.calculate_activity_score(repo, [])
        self.assertIsInstance(score, int)
        self.assertGreaterEqual(score, 0)
    
    def test_get_activity_level(self):
        """Test activity level determination"""
        analyzer = GitHubRepoAnalyzer("testuser")
        
        # Test archived repo
        repo = {'archived': True, 'disabled': False}
        level = analyzer.get_activity_level(100, repo)
        self.assertEqual(level, 'archived')
        
        # Test active repo
        repo = {'archived': False, 'disabled': False}
        level = analyzer.get_activity_level(100, repo)
        self.assertEqual(level, 'very_active')

if __name__ == '__main__':
    unittest.main()
EOF
        run_check "Python unit tests (pytest)" "cd '$PYTHON_SCRIPT_DIR' && $PYTHON_ACTIVATE pytest tests/ -v"
    fi
    
    # Python test coverage
    run_check "Python test coverage" "cd '$PYTHON_SCRIPT_DIR' && $PYTHON_ACTIVATE pytest --cov=analyze_repos --cov-report=term-missing tests/"
    
    echo -e "\n${BLUE}💎 JEKYLL/RUBY VALIDATION${NC}"
    echo -e "${BLUE}========================${NC}"
    
    # Jekyll configuration validation (only if bundle is available)
    if command_exists bundle && [ -f "$JEKYLL_DIR/Gemfile" ]; then
        run_check "Jekyll configuration validation" "cd '$JEKYLL_DIR' && bundle exec jekyll doctor" || echo -e "${YELLOW}⚠️  Jekyll validation skipped${NC}"
        
        # Jekyll build test
        run_check "Jekyll build test" "cd '$JEKYLL_DIR' && bundle exec jekyll build --safe" || echo -e "${YELLOW}⚠️  Jekyll build test skipped${NC}"
        
        # Jekyll syntax validation (check for liquid syntax errors)
        run_check "Jekyll syntax validation" "cd '$JEKYLL_DIR' && bundle exec jekyll build --safe --verbose 2>&1 | grep -v 'warning' | grep -v 'deprecated'" || echo -e "${YELLOW}⚠️  Jekyll syntax validation skipped${NC}"
    else
        echo -e "${YELLOW}⚠️  Skipping Jekyll validation (bundle not available)${NC}"
    fi
    
    # Ruby Gemfile security check
    if command_exists bundle-audit; then
        run_check "Ruby security audit" "cd '$JEKYLL_DIR' && bundle audit"
    else
        echo -e "${YELLOW}⚠️  Skipping bundle audit (not installed)${NC}"
    fi
    
    echo -e "\n${BLUE}📄 MARKDOWN VALIDATION${NC}"
    echo -e "${BLUE}=====================${NC}"
    
    # Markdown linting (if markdownlint is available)
    if command_exists markdownlint; then
        run_check "Markdown linting" "find '$JEKYLL_DIR' -name '*.md' -not -path '*/_site/*' -not -path '*/vendor/*' | xargs markdownlint"
    else
        echo -e "${YELLOW}⚠️  Skipping markdown linting (markdownlint not installed)${NC}"
    fi
    
    # Check for broken links (if linkchecker is available)
    if command_exists linkchecker; then
        run_check "Link validation" "cd '$JEKYLL_DIR' && bundle exec jekyll build --safe && linkchecker --check-extern _site/index.html"
    else
        echo -e "${YELLOW}⚠️  Skipping link validation (linkchecker not installed)${NC}"
    fi
    
    echo -e "\n${BLUE}🔧 SHELL SCRIPT VALIDATION${NC}"
    echo -e "${BLUE}==========================${NC}"
    
    # Shell script linting
    run_check "Shell script linting (shellcheck)" "find '$REPO_ROOT' -name '*.sh' -exec shellcheck {} +"
    
    # Shell script syntax validation
    run_check "Shell script syntax validation" "bash -n '$REPO_ROOT/run_checks.sh' && bash -n '$PYTHON_SCRIPT_DIR/update_projects.sh'"
    
    echo -e "\n${BLUE}📊 YAML VALIDATION${NC}"
    echo -e "${BLUE}==================${NC}"
    
    # YAML syntax validation
    run_check "YAML syntax validation" "python3 -c 'import yaml; [yaml.safe_load(open(f)) for f in [\"$JEKYLL_DIR/_config.yml\"]]'"
    
    echo -e "\n${BLUE}📁 FILE STRUCTURE VALIDATION${NC}"
    echo -e "${BLUE}============================${NC}"
    
    # Check for required files
    run_check "Required files exist" "[ -f '$REPO_ROOT/AGENTS.md' ] && [ -f '$REPO_ROOT/README.md' ] && [ -f '$JEKYLL_DIR/_config.yml' ]"
    
    # Check for proper permissions
    run_check "Script permissions" "[ -x '$REPO_ROOT/run_checks.sh' ] && [ -x '$PYTHON_SCRIPT_DIR/update_projects.sh' ]"
    
    # Check for sensitive data
    run_check "No sensitive data exposure" "! grep -r 'password\\|secret\\|key\\|token' '$REPO_ROOT' --exclude-dir=venv --exclude-dir=_site --exclude-dir=.git --exclude='*.pyc' | grep -v 'GITHUB_TOKEN' | grep -v 'token.*github'"
    
    echo -e "\n${GREEN}📊 VALIDATION SUMMARY${NC}"
    echo -e "${GREEN}===================${NC}"
    echo -e "Total checks run: ${TOTAL_CHECKS}"
    echo -e "Passed: ${GREEN}${PASSED_CHECKS}${NC}"
    echo -e "Failed: ${RED}${FAILED_CHECKS}${NC}"
    
    if [ $FAILED_CHECKS -eq 0 ]; then
        echo -e "\n${GREEN}🎉 All validation checks passed!${NC}"
        exit 0
    else
        echo -e "\n${RED}❌ Some validation checks failed. Please fix the issues above.${NC}"
        exit 1
    fi
}

# Run main function
main "$@"
