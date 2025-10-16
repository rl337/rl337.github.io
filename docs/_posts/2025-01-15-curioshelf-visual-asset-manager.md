---
layout: post
title: "Curioshelf - A Visual Asset Manager for 2D Games"
date: 2025-01-15 12:00:00 -0500
categories: [projects, tools, python, game-development]
tags: [asset-management, 2d-games, python, pyside6, game-development]
author: Richard Lee
---

![Curioshelf Interface]({{ '/assets/images/blog/curioshelf-interface.png' | relative_url }})
*The Curioshelf interface showing the tabbed workflow for asset management*

You know that moment when you're working on a 2D game and suddenly realize you have hundreds of sprites scattered across folders, with no clear system for organizing them? That's exactly where I found myself a few months ago, and it led me down a rabbit hole that became **Curioshelf** - a visual asset manager that's become one of my most personally satisfying projects.

What started as a simple "I need to organize my game assets" problem turned into a deep dive into PySide6, testing frameworks, and the surprisingly complex world of asset management workflows. Let me take you through this journey.

## 🎨 The Problem That Started It All

![Asset Chaos]({{ '/assets/images/blog/asset-chaos.png' | relative_url }})
*The typical state of game assets before proper organization*

I was working on a 2D platformer when I hit a wall. Not a literal wall in the game, but the kind of organizational wall that every indie developer faces. I had character sprites in one folder, environment tiles in another, UI elements scattered everywhere, and no clear system for tracking what was complete, what needed work, or what views were missing.

The breaking point came when I spent 30 minutes looking for a specific character animation frame that I *knew* I had created, but couldn't find because it was buried in a folder structure that made sense when I created it but was completely incomprehensible three weeks later.

That's when I realized I needed a tool that could handle the complexity of 2D game asset management while keeping things organized and trackable. Thus, Curioshelf was born.

## 🚀 Key Features

### Import and Tag System

- **Large file support** for SVG and raster source files
- **Flexible tagging system** for organizing assets
- **Visual preview** of imported assets
- **Metadata storage** in clean JSON format

### View-Based Slice Creation

- **1:1 correspondence** between views and slices
- **Visual slice creation** with intuitive drawing tools
- **Multiple layers** (concept, working, production)
- **Template system** for defining required views/states

### Template Management

Create and manage templates that define required views for different object
types:

- **Character templates**: front, back, left, right, walk1, walk2, idle
- **Tile templates**: base, variant1, variant2
- **UI element templates**: normal, hover, pressed, disabled

### Visual Feedback

- **Progress indicators** for object completeness
- **Template compliance** tracking
- **Visual status** for each object and view
- **Real-time updates** across all tabs

## 🛠️ The Development Journey

![Development Process]({{ '/assets/images/blog/curioshelf-development.png' | relative_url }})
*The evolution from V1 to V2 - a complete architectural overhaul*

Looking back at the commit history, I can see exactly where this project took some interesting turns. The first version was... well, let's just say it was functional but not elegant. I was learning PySide6 as I went, and the code showed it.

The real breakthrough came when I decided to completely rewrite it (commit `fb1d11ca` - "rearranged repo to be neater"). That's when I realized I needed to separate concerns properly. The UI was getting tangled with business logic, and testing was becoming a nightmare.

### The Testing Nightmare

One of the most challenging parts was getting the testing right. Looking at commits like `95b4b0a3` ("a lot of heartache to get a couple of e2e tests to pass"), I remember spending entire evenings debugging why my UI tests were hanging. The issue? Modal dialogs were blocking the test execution.

The solution came in commit `d3b642b5` ("pretty big milestone in testability") where I finally figured out how to make the UI testable without blocking on modal dialogs. That was a huge win - suddenly I could iterate quickly without worrying about breaking things.

### The Scripting System Surprise

One of the most unexpected features that emerged was the scripting system. Looking at commit `1ffd30dc` ("first pass at a working curioscript"), I remember thinking "wait, why am I building a scripting language for an asset manager?"

The answer became clear when I realized that asset management workflows are incredibly repetitive. Instead of clicking through the same sequence of actions for every character, I could write a script that would automate the entire process. The "Curioscript" system (yes, I'm terrible at naming things) allows users to define sequences of actions that can be replayed across multiple assets.

This feature alone saved me hours of manual work and made the tool genuinely useful for production workflows.

### Core Components

```text
curioshelf/
├── curioshelf/          # Core Python module
│   ├── models.py        # Data models
│   └── __init__.py
├── gui/                 # Qt GUI code
│   ├── tabbed_main_window.py  # Main application
│   ├── sources_tab.py   # Asset import and management
│   ├── templates_tab.py # Template creation and management
│   ├── objects_tab.py   # Object and slice management
│   └── canvas_widget.py # Image canvas and selection
├── assets/              # Test images and examples
├── metadata/            # Object and template definitions
└── build/               # Output files
```

## 🎯 Workflow

### V2 Improved Workflow

1. **Sources Tab**: Import and manage source images (simplified)
2. **Templates Tab**: Create templates with visual representation of required
   views
3. **Objects Tab**: Create objects, assign templates, and create slices for
   views

### Detailed Steps

1. **Import Source**: Load image files in the Sources tab
2. **Create Template**: Define required views (e.g., "front", "back", "walk1")
3. **Create Object**: Create objects and assign templates
4. **Create Slices**: Select source, select view, draw selection, create slice
5. **Track Progress**: Monitor template compliance with visual progress bars

## 🚀 Getting Started

### Installation

```bash
# Install Python 3.8 or higher
# Install Poetry: https://python-poetry.org/docs/#installation

# Clone and install
git clone https://github.com/rl337/curioshelf
cd curioshelf
poetry install
```

### Running the Application

```bash
# Using Poetry
poetry run python main.py

# Or install and run directly
poetry install
poetry run curioshelf

# Or activate virtual environment
poetry shell
python main.py
```

## 🎨 Use Cases

Curioshelf is perfect for:

- **2D game development** with character sprites
- **Animation projects** requiring organized asset management
- **UI design** with multiple states and variants
- **Tile-based games** with multiple tile variants
- **Art projects** with structured workflows

## 📊 Project Status

### Current Features (V2)

- ✅ Modern tabbed interface with dedicated views
- ✅ Sources tab for image import and slice creation
- ✅ Templates tab with visual template cards
- ✅ Objects tab with compliance tracking
- ✅ Core data models with JSON persistence
- ✅ PySide6 GUI framework
- ✅ Image loading and rectangular region selection
- ✅ Template compliance with progress indicators
- ✅ Cross-tab communication and real-time updates

### Planned Features

- 🔄 Image slicing and export
- 🔄 SVG support
- 🔄 Filters (pixelation, palettization)
- 🔄 Spritesheet generation
- 🔄 Batch operations

## 🔗 Links and Resources

- **[GitHub Repository](https://github.com/rl337/curioshelf)** - Source code
  and documentation
- **[Project README](https://github.com/rl337/curioshelf/blob/main/README.md)**
  - Detailed setup and usage instructions
- **[PySide6 Documentation](https://doc.qt.io/qtforpython/)** - GUI framework
  documentation

## 🎯 Why Curioshelf?

The name "Curioshelf" reflects the tool's purpose - it's like a curious shelf
where you can organize and explore your creative assets. The tool addresses the
common problem of asset management in game development, where artists and
developers need to:

- **Organize large collections** of game assets
- **Maintain consistency** across different views and states
- **Track progress** on complex projects
- **Export assets** in the right format and organization

## 💡 What I Learned

![Project Reflection]({{ '/assets/images/blog/curioshelf-reflection.png' | relative_url }})
*The journey from chaos to organization - both in code and assets*

Building Curioshelf taught me more about software development than I expected. The biggest lesson? Sometimes the best features emerge organically from solving real problems, not from following a predetermined plan.

The scripting system wasn't in my original design, but it became one of the most valuable features. The testing challenges forced me to learn proper separation of concerns. The UI refactoring taught me that good architecture isn't just about making code clean - it's about making it maintainable and testable.

### The Real Value

What started as a simple asset organizer became a comprehensive workflow tool. It's not just about managing files - it's about understanding how creative people actually work and building tools that fit into their process rather than forcing them to adapt to the tool.

The name "Curioshelf" reflects this philosophy. It's like a curious shelf where you can explore and organize your creative assets, but it's also curious about your workflow - learning from how you use it and adapting to make your process smoother.

---

*If you're working on 2D games or animation projects and find yourself drowning in asset management chaos, check out [Curioshelf](https://github.com/rl337/curioshelf). It might just save you from the same organizational nightmare that started this whole journey!*
