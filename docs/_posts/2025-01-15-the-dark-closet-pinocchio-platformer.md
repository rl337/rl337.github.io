---
layout: post
title: "The Dark Closet - A Pinocchio-Inspired 2D Platformer"
date: 2025-01-15 10:00:00 -0500
categories: [projects, games, python]
tags: [pygame, procedural-generation, 2d-platformer, python]
author: Richard Lee
---

![The Dark Closet Game]({{ '/assets/images/blog/dark-closet-game.png' | relative_url }})
*The Dark Closet - where a boy discovers a portal in his closet and chooses conq
uest over wonder*

What if Pinocchio wasn't about becoming a real boy, but about a boy who discover
s a magical portal in his closet and decides to conquer whatever lies beyond? Tha
t's the twisted premise behind **The Dark Closet**, a 2D platformer that became one
 of my most technically challenging and personally rewarding projects.

This isn't just a game - it's an experiment in procedural generation, a deep div
e into Python game development, and a journey through the surprisingly complex wo
rld of making things that are both fun to play and maintainable to develop.

## 🎮 What is The Dark Closet?

The Dark Closet is a 2D platformer where you play as a boy who discovers a
portal in his closet. Rather than seeking wonder, he chooses conquest - a twist
on the classic Pinocchio tale. The game features procedurally generated
character sprites, comprehensive testing, and modern development practices.

## 🎨 Key Features

### Procedural Asset Generation

All character sprites, facial features, and gear are generated procedurally at
build time using Python and Pygame drawing primitives. This creates unique
characters every time the game is built, adding variety and replayability.

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

## 🛠️ The Procedural Generation Challenge

![Procedural Generation]({{ '/assets/images/blog/dark-closet-procedural.png' | relative_url }})
*The procedural generation system creating unique character sprites*

One of the most fascinating aspects of The Dark Closet is the procedural generat
ion system. Looking at the commit history, I can see exactly where this became a ma
jor focus - commits like `77add47a` ("Implement intelligent frame selection for tes
t sequences") show the evolution of this system.

The challenge wasn't just generating random sprites - it was creating sprites th
at looked good, were consistent with the game's art style, and could be used in ac
tual gameplay without looking jarring or out of place.

### The Art Style Problem

The biggest challenge was maintaining visual consistency. How do you generate th
ousands of unique characters while ensuring they all look like they belong in the same 
game? The solution involved:

1. **Layered generation** - Building characters from consistent base components
2. **Style constraints** - Ensuring all generated elements follow the same color
 palette and proportions
3. **Quality filtering** - Automatically rejecting combinations that don't look 
right

### The Testing Nightmare

Testing procedural generation is... interesting. How do you write tests for some
thing that's designed to be random? Looking at commits like `6bd13e78` ("Fix headless
 operation and full level capture"), I can see the evolution of my testing appro
ach.

The solution was to test the *system*, not the output. I focused on testing that
 the generation process was deterministic when given the same seed, that it coul
d handle edge cases without crashing, and that the generated assets were valid an
d usable.

## 📊 Project Status

The project is actively maintained with:

- ✅ **CI/CD Pipeline**: Passing
- 🧪 **Tests**: 20/20 passing
- 📊 **Code Quality**: 10/10
- 🎮 **Game Features**: Fully functional

## 🔗 Links and Resources

- **[View Live Documentation](https://rl337.github.io/the-dark-closet/)** -
  Comprehensive documentation with screenshots and test sequences
- **[GitHub Repository](https://github.com/rl337/the-dark-closet)** - Source
  code and development history
- **[Asset Gallery](https://rl337.github.io/the-dark-closet/assets.html)** -
  View all procedurally generated assets
- **[Test Sequences](https://rl337.github.io/the-dark-closet/tests.html)** -
  Visual test results and game mechanics

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

## 💡 The Callback System Breakthrough

![Callback System]({{ '/assets/images/blog/dark-closet-callbacks.png' | relative_url }})
*The object callback system that made interactive gameplay possible*

One of the most interesting technical challenges was implementing the object cal
lback system. Looking at commit `0ce8b255` ("Implement object OnAction callbacks and 
brick breaking mechanics"), I can see exactly when this became a reality.

The problem was simple: how do you make objects in the game world interactive? H
ow do you make bricks breakable, ladders climbable, and switches functional? The s
olution was a callback system that allows objects to define their own behavior when int
eracted with.

### The Brick Breaking Test

The most satisfying part was getting the brick breaking mechanics working. I spe
nt hours debugging why the character wasn't actually breaking bricks when jumping 
into them. The issue? The collision detection was working, but the callback system w
asn't properly triggering the "OnBreak" behavior.

When it finally worked, it was like magic - the character would jump up, hit a b
rick, and it would disappear with a satisfying visual effect. It's amazing how such a
 simple interaction can feel so rewarding when it works correctly.

### What I Learned

Building The Dark Closet taught me more about game development than I expected. 
The biggest lesson? Games are incredibly complex systems where every small detail m
atters. A tiny bug in the collision detection can break the entire gameplay experience.


But it also taught me that good software engineering practices - testing, docume
ntation, modular design - aren't just for business applications. They're essential for c
reating games that are both fun and maintainable.

---

*If you're interested in procedural generation, Python game development, or just
 want to see how a simple platformer can become a complex technical project, che
ck out [The Dark Closet](https://github.com/rl337/the-dark-closet). It might just 
inspire your next game development adventure!*
