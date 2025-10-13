---
layout: post
title: "Metro - A Python Framework for Metropolitan Area Simulation"
date: 2025-01-15 13:00:00 -0500
categories: [projects, python, simulation, visualization]
tags: [python, simulation, matplotlib, demographics, visualization, urban-planning]
author: Richard Lee
---

# Metro - A Python Framework for Metropolitan Area Simulation

I'm excited to share **Metro**, a comprehensive Python framework I've developed for metropolitan area simulation and visualization. This project represents my exploration into urban planning, demographic modeling, and data visualization using modern Python tools.

## 🏙️ What is Metro?

Metro is a unified Python framework designed to simulate and visualize metropolitan areas through a combination of 2D rendering, geometric modeling, and demographic analysis. It provides tools for creating, rendering, and analyzing metropolitan area models with both visual and statistical capabilities.

## 🎯 Key Features

### 2D Rendering Engine
- **Matplotlib-based graphics** for high-quality visualization
- **Z-ordered rendering** with depth sorting
- **Geometric shape system** with collision detection
- **High-quality output** for presentations and analysis

### Shape System
- **Geometric primitives**: Circle, Rectangle, Group
- **Collision detection** for interactive simulations
- **Bounding box functionality** for spatial queries
- **Composite shapes** for complex objects

### Population Modeling
- **Demographic modeling** with age/gender distributions
- **Occupational data processing** and analysis
- **Statistical modeling** using normal distributions
- **Workforce demographic calculations**

### SVG Generation
- **Scalable vector graphics** creation
- **Shape generation** (circles, rectangles, lines, polylines)
- **Export capabilities** for web and print

## 🛠️ Technical Implementation

### Modern Python Architecture
Metro has been completely converted to Python with modern development practices:

- **Python 3.8+** with type hints throughout
- **Comprehensive testing** with pytest
- **Modern packaging** with pyproject.toml
- **Code quality tools** (black, flake8, mypy)
- **Docker support** for consistent development

### Core Components

```
metro/
├── metro/                    # Main Python package
│   ├── app.py               # Main application
│   ├── renderer.py          # 2D graphics renderer
│   └── model/               # Core data models
│       ├── color.py         # Color management
│       ├── point2d.py       # 2D point mathematics
│       ├── bounded.py       # Bounding box functionality
│       ├── thing_stack.py   # Object management
│       ├── shapes/          # Geometric primitives
│       └── things/          # Renderable objects
├── population/              # Legacy demographic components
│   ├── metro.py            # City modeling
│   ├── population.py       # Demographics
│   └── svg.py              # SVG generation
└── tests/                  # Comprehensive test suite
```

## 🎨 Use Cases

Metro is perfect for:

- **Urban planning** and city design
- **Demographic analysis** and modeling
- **Transportation planning** and simulation
- **Economic modeling** of metropolitan areas
- **Educational tools** for urban studies
- **Research projects** in urban planning

## 🚀 Getting Started

### Quick Start with Docker

```bash
# Build the development container
docker build -t metro-dev .

# Run the container with project mounted
docker run -it -v $(pwd):/workspace metro-dev
```

### Local Development

```bash
# Install in development mode
pip install -e ".[dev,test]"

# Run the main application
python -m metro.app

# Run tests
pytest

# Run validation script
./run_checks.sh
```

## 📊 Project Status

### Current State
- ✅ **Complete Python rendering engine** with matplotlib
- ✅ **Comprehensive shape system** with collision detection
- ✅ **Full test coverage** with pytest
- ✅ **Modern Python packaging** with pyproject.toml
- ✅ **Type hints and code quality** tools
- ✅ **Legacy population modeling** framework
- ✅ **SVG generation** capabilities

### Development Environment
- **Docker support** for isolated development
- **Comprehensive testing** following AGENTS.md practices
- **Code quality tools** (black, flake8, mypy)
- **Validation script** for all checks

## 🧪 Testing and Quality

The project follows comprehensive testing practices:

### Python Testing
- **Framework**: pytest with coverage
- **Coverage**: Comprehensive unit tests for all components
- **Run**: `pytest` or `python -m pytest`
- **Coverage Report**: `pytest --cov=metro --cov-report=html`

### Code Quality
- **Formatting**: black
- **Linting**: flake8
- **Type Checking**: mypy
- **All Tools**: `./run_checks.sh`

## 🎯 Future Development

### Planned Enhancements
- **Enhanced visualization** capabilities with interactive plots
- **Performance optimizations** for large-scale simulations
- **Integration with geographic data** formats (GeoJSON, Shapefile)
- **Real-time rendering** capabilities
- **Web-based visualization** interface
- **Advanced demographic modeling** features

### Migration Notes
The project has been fully converted from Java to Python, preserving all functionality while adding modern Python features including type hints, comprehensive testing, and modern packaging.

## 🔗 Links and Resources

- **[GitHub Repository](https://github.com/rl337/metro)** - Source code and documentation
- **[Project README](https://github.com/rl337/metro/blob/main/README.md)** - Detailed setup and usage instructions
- **[Matplotlib Documentation](https://matplotlib.org/)** - Graphics library documentation

## 💡 Why Metro?

The name "Metro" reflects the project's focus on metropolitan areas - the complex, interconnected systems that make up our cities. The framework is designed to help researchers, planners, and developers understand and model these systems through:

- **Visual representation** of urban spaces
- **Statistical modeling** of demographics
- **Interactive simulation** capabilities
- **Export tools** for analysis and presentation

## 🎨 Development Philosophy

Metro represents my approach to building tools that bridge the gap between data analysis and visual understanding. It's not just about creating pretty pictures - it's about providing insights into complex urban systems through:

- **Clear visualization** of spatial relationships
- **Statistical rigor** in demographic modeling
- **Modular design** for extensibility
- **Modern development practices** for maintainability

---

*Interested in urban planning, demographic modeling, or data visualization? Check out [Metro](https://github.com/rl337/metro) and see how it can enhance your research or development projects!*
