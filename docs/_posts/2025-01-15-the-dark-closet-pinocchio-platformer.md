---
layout: post
title: "The Dark Closet - A Pinocchio-Inspired 2D Platformer"
date: 2025-01-15 10:00:00 -0500
categories: [projects, games, python]
tags: [pygame, procedural-generation, 2d-platformer, python]
author: Richard Lee
---

# The Dark Closet - A Pinocchio-Inspired 2D Platformer

I'm excited to share **The Dark Closet**, a unique 2D platformer game I've been developing that combines procedural asset generation with classic platformer mechanics. This project represents my exploration into procedural content generation and modern Python game development practices.

## 🎮 What is The Dark Closet?

The Dark Closet is a 2D platformer where you play as a boy who discovers a portal in his closet. Rather than seeking wonder, he chooses conquest - a twist on the classic Pinocchio tale. The game features procedurally generated character sprites, comprehensive testing, and modern development practices.

## 🎨 Key Features

### Procedural Asset Generation
All character sprites, facial features, and gear are generated procedurally at build time using Python and Pygame drawing primitives. This creates unique characters every time the game is built, adding variety and replayability.

### Comprehensive Testing Suite
The project includes a full test suite with:
- **Unit tests** for individual components
- **Integration tests** for game systems
- **Performance benchmarks** to ensure smooth gameplay
- **Visual regression testing** using pytest

### Modern Development Practices
- **Poetry** for dependency management
- **mypy** for type checking
- **pylint** for code quality
- **GitHub Actions** for CI/CD
- **Automated documentation generation**

### Game Mechanics
- 2D platformer movement with jumping
- Brick breaking mechanics
- Ladder climbing system
- Camera following for smooth gameplay
- Procedurally generated character customization

## 🛠️ Technical Implementation

The game is built using:
- **Python 3.10+** as the core language
- **Pygame** for graphics and game loop
- **Poetry** for dependency management
- **pytest** for comprehensive testing
- **GitHub Actions** for automated builds and deployment

The procedural generation system creates unique character sprites by combining different body parts, facial features, and equipment. This approach allows for thousands of unique character combinations while maintaining a consistent art style.

## 📊 Project Status

The project is actively maintained with:
- ✅ **CI/CD Pipeline**: Passing
- 🧪 **Tests**: 20/20 passing
- 📊 **Code Quality**: 10/10
- 🎮 **Game Features**: Fully functional

## 🔗 Links and Resources

- **[View Live Documentation](https://rl337.github.io/the-dark-closet/)** - Comprehensive documentation with screenshots and test sequences
- **[GitHub Repository](https://github.com/rl337/the-dark-closet)** - Source code and development history
- **[Asset Gallery](https://rl337.github.io/the-dark-closet/assets.html)** - View all procedurally generated assets
- **[Test Sequences](https://rl337.github.io/the-dark-closet/tests.html)** - Visual test results and game mechanics

## 🚀 Getting Started

To run the game locally:

```bash
# Install dependencies
poetry install

# Run the game
poetry run the-dark-closet

# Run headless for testing
TDC_MAX_FRAMES=3 poetry run the-dark-closet
```

## 🎯 Future Development

The project continues to evolve with plans for:
- Enhanced procedural generation algorithms
- Additional game mechanics and levels
- Performance optimizations
- Web-based playable demo

The Dark Closet represents my passion for combining creative game design with robust software engineering practices. It's a testament to how modern Python development tools can create engaging, well-tested games that are both fun to play and maintainable to develop.

---

*Interested in procedural generation or Python game development? Check out the [source code](https://github.com/rl337/the-dark-closet) and feel free to contribute or ask questions!*
