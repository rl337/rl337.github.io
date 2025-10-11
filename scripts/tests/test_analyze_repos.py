#!/usr/bin/env python3
"""Basic tests for analyze_repos.py"""

import unittest
import sys
import os
from unittest.mock import Mock, patch

# Add the parent directory to the path so we can import the module
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from analyze_repos import GitHubRepoAnalyzer

class TestGitHubRepoAnalyzer(unittest.TestCase):
    def test_init(self):
        """Test GitHubRepoAnalyzer initialization"""
        analyzer = GitHubRepoAnalyzer("testuser")
        self.assertEqual(analyzer.username, "testuser")
        self.assertIsNone(analyzer.token)
        
        # Test with token
        analyzer_with_token = GitHubRepoAnalyzer("testuser", "fake_token")
        self.assertEqual(analyzer_with_token.username, "testuser")
        self.assertEqual(analyzer_with_token.token, "fake_token")
    
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
        # Should be 10*2 + 5*5 + 2*1 + 5 = 47 (includes size bonus for >1000)
        self.assertEqual(score, 47)
    
    def test_get_activity_level(self):
        """Test activity level determination"""
        analyzer = GitHubRepoAnalyzer("testuser")
        
        # Test archived repo
        repo = {'archived': True, 'disabled': False}
        level = analyzer.get_activity_level(100, repo)
        self.assertEqual(level, 'archived')
        
        # Test disabled repo
        repo = {'archived': False, 'disabled': True}
        level = analyzer.get_activity_level(100, repo)
        self.assertEqual(level, 'archived')
        
        # Test very active repo
        repo = {'archived': False, 'disabled': False}
        level = analyzer.get_activity_level(100, repo)
        self.assertEqual(level, 'very_active')
        
        # Test active repo
        level = analyzer.get_activity_level(75, repo)
        self.assertEqual(level, 'active')
        
        # Test moderate repo
        level = analyzer.get_activity_level(30, repo)
        self.assertEqual(level, 'moderate')
        
        # Test low activity repo
        level = analyzer.get_activity_level(10, repo)
        self.assertEqual(level, 'low')
        
        # Test idle repo
        level = analyzer.get_activity_level(2, repo)
        self.assertEqual(level, 'idle')
    
    def test_calculate_language_percentages(self):
        """Test language percentage calculation"""
        analyzer = GitHubRepoAnalyzer("testuser")
        
        # Test with empty languages
        result = analyzer.calculate_language_percentages({})
        self.assertEqual(result, {})
        
        # Test with normal languages
        languages = {'Python': 1000, 'JavaScript': 500, 'CSS': 100}
        result = analyzer.calculate_language_percentages(languages)
        
        self.assertAlmostEqual(result['Python'], 62.5, places=1)
        self.assertAlmostEqual(result['JavaScript'], 31.2, places=1)
        self.assertAlmostEqual(result['CSS'], 6.2, places=1)
    
    def test_generate_project_frontmatter(self):
        """Test project frontmatter generation"""
        analyzer = GitHubRepoAnalyzer("testuser")
        
        analysis = {
            'name': 'test-project',
            'description': 'A test project',
            'url': 'https://github.com/user/test-project',
            'homepage': 'https://example.com',
            'activity_level': 'active',
            'stars': 10,
            'forks': 5,
            'pushed_at': '2023-01-01T00:00:00Z',
            'created_at': '2022-01-01T00:00:00Z',
            'primary_language': 'Python',
            'language_percentages': {'Python': 80.0, 'JavaScript': 20.0},
            'topics': ['python', 'web', 'api'],
            'license': 'MIT',
            'archived': False
        }
        
        frontmatter = analyzer.generate_project_frontmatter(analysis)
        
        self.assertEqual(frontmatter['title'], 'Test Project')
        self.assertEqual(frontmatter['description'], 'A test project')
        self.assertEqual(frontmatter['github'], 'https://github.com/user/test-project')
        self.assertEqual(frontmatter['live_url'], 'https://example.com')
        self.assertEqual(frontmatter['activity_level'], 'active')
        self.assertEqual(frontmatter['stars'], 10)
        self.assertEqual(frontmatter['forks'], 5)
        self.assertEqual(frontmatter['last_updated'], '2023-01-01')
        self.assertEqual(frontmatter['created'], '2022-01-01')
        self.assertEqual(frontmatter['language'], 'Python')
        self.assertEqual(frontmatter['license'], 'MIT')
        self.assertFalse(frontmatter['archived'])
        self.assertIn('Python', frontmatter['technologies'])
        self.assertIn('python', frontmatter['technologies'])

if __name__ == '__main__':
    unittest.main()
