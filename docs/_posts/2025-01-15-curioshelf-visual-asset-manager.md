---
layout: post
title: "Curioshelf - A Visual Asset Manager for 2D Games"
date: 2025-01-15 12:00:00 -0500
categories: [projects, tools, python, game-development]
tags: [asset-management, 2d-games, python, pyside6, game-development]
author: Richard Lee
---

I'm excited to share **Curioshelf**, a visual asset manager I've developed
specifically for 2D games and structured art projects. This tool addresses the
common challenge of managing large collections of game assets while maintaining
organization and workflow efficiency.

## 🎨 What is Curioshelf?

Curioshelf is a visual asset manager built with Python and PySide6, designed to
help game developers and artists manage large collections of 2D assets. It's
particularly useful for animation projects, 2D games, and any structured art
workflow that requires organized asset management.

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

## 🛠️ Technical Implementation

### Modern Architecture

Curioshelf V2 features a completely redesigned architecture with:

- **Tabbed interface** with dedicated views for different workflows
- **Clean separation** between UI and business logic
- **PySide6** for modern Qt-based GUI
- **JSON persistence** for metadata storage

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

## 💡 Development Philosophy

Curioshelf represents my approach to building tools that solve real problems in
creative workflows. It's not just about managing files - it's about
understanding the creative process and building tools that enhance rather than
hinder creativity.

The V2 redesign focuses on:

- **Simplicity** in the interface
- **Power** in the underlying system
- **Flexibility** for different workflows
- **Reliability** through robust data management

---

*Working on 2D games or animation projects? Check out
[Curioshelf](https://github.com/rl337/curioshelf) and see how it can streamline
your asset management workflow!*
