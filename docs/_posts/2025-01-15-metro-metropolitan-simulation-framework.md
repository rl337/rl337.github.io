---
layout: post
title: "Metro - A Python Framework for Metropolitan Area Simulation"
date: 2025-01-15 13:00:00 -0500
categories: [projects, python, simulation, visualization]
tags: [python, simulation, matplotlib, demographics, visualization, urban-planni
ng]
author: Richard Lee
---

![Metro City Simulation]({{ '/assets/images/blog/metro-city-simulation.png' | re
lative_url }})
*A generated metropolitan area showing the complex interplay of zones, roads, an
d demographics*

Have you ever looked at a city and wondered "how did this all come together?" Th
e intricate web of roads, the way neighborhoods evolve, the complex dance between
 commercial centers and residential areas - it's like watching a living organism
 grow and change over time.

That fascination led me to build **Metro**, a Python framework for simulating an
d visualizing metropolitan areas. What started as a simple "what if I could model
 a city?" experiment became one of my most ambitious and rewarding projects, tak
ing me from Java to Python, from static visualizations to interactive web applicati
ons, and from basic shapes to complex temporal evolution systems.

## 🏙️ What is Metro?

Metro is a unified Python framework designed to simulate and visualize
metropolitan areas through a combination of 2D rendering, geometric modeling,
and demographic analysis. It provides tools for creating, rendering, and
analyzing metropolitan area models with both visual and statistical
capabilities.

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

## 🛠️ The Great Migration

![Java to Python]({{ '/assets/images/blog/metro-migration.png' | relative_url }}}
)
*The complete rewrite from Java to Python - a journey of modernization*

One of the most significant decisions I made with Metro was to completely rewrit
e it from Java to Python. Looking at commit `04648ba8` ("Implement GitHub Pages w
ebapp with hierarchical seed system"), I can see exactly when this transformation hap
pened.

The original Java version was functional but limited. It was hard to extend, dif
ficult to test, and didn't integrate well with modern web technologies. The Python rew
rite wasn't just a language change - it was a complete architectural overhaul.

### Why Python?

The decision to switch to Python came from several realizations:

1. **Matplotlib integration** - Python's matplotlib library is incredibly powerf
ul for data visualization
2. **Web integration** - Python's Flask made it easy to create web interfaces
3. **Testing ecosystem** - pytest and the broader Python testing ecosystem is mu
ch more mature
4. **Community** - The Python data science community has amazing tools for this 
kind of work

### The Rewrite Process

The migration wasn't just a port - it was a complete reimagining. I kept the cor
e concepts (zones, demographics, rendering) but rebuilt everything from the groun
d up with modern Python practices:

- **Type hints throughout** for better code clarity
- **Comprehensive testing** with pytest and coverage
- **Modern packaging** with pyproject.toml
- **Docker support** for consistent development environments

### Core Components

```text
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

## 🎯 The Temporal Evolution Breakthrough

![City Evolution]({{ '/assets/images/blog/metro-evolution.png' | relative_url }}}
)
*Watching a city grow from founding to modern times - the temporal evolution fea
ture*

One of the most exciting features I added was the temporal evolution system. Loo
king at commit `40111925` ("Implement temporal city evolution with Roman grid system
"), I can see exactly when this became a reality.

The idea came from a simple question: "What if I could watch a city grow over ti
me?" Not just generate a static city, but actually simulate how it would develop fro
m its founding to the present day.

### The Roman Grid System

The temporal evolution starts with a Roman grid system - the classic cardo and d
ecumanus roads intersecting at 90 degrees. This isn't just historical accuracy; it's bas
ed on real urban planning principles that have influenced city development for tho
usands of years.

The system simulates four distinct eras:
- **Founding Era (0-50 AD)**: Roman grid, mixed-use core, basic infrastructure
- **Growth Era (50-200 AD)**: Zone differentiation, secondary roads, first monum
ents
- **Expansion Era (200-500 AD)**: Diagonal roads, key monuments, specialized zon
es
- **Modernization Era (500-1500 AD)**: Complex infrastructure, modern zones, tra
nsportation hubs

### The Interactive Timeline

The web interface includes a timeline slider that lets you scrub through time an
d watch the city evolve. It's mesmerizing to see how a simple Roman settlement gr
ows into a complex metropolitan area with specialized zones, transportation network
s, and key landmarks.

This feature alone took weeks to get right, but the result is something I'm genu
inely proud of - a tool that doesn't just generate cities, but tells the story of how
 they develop.

## 🔗 Links and Resources

- **[GitHub Repository](https://github.com/rl337/metro)** - Source code and
  documentation
- **[Project README](https://github.com/rl337/metro/blob/main/README.md)** -
  Detailed setup and usage instructions
- **[Matplotlib Documentation](https://matplotlib.org/)** - Graphics library
  documentation

## 💡 What I Learned About Cities and Code

![Project Reflection]({{ '/assets/images/blog/metro-reflection.png' | relative_u
rl }})
*The intersection of urban planning, data science, and software development*

Building Metro taught me more about cities than I expected. The biggest revelati
on? Cities are incredibly complex systems that follow patterns, but those patterns 
are often hidden beneath layers of history, politics, and human behavior.

### The Patterns That Emerged

As I built the simulation engine, I started noticing patterns that I hadn't anti
cipated:

- **Road networks** naturally evolve to connect important points, not just follo
w grids
- **Zone specialization** happens gradually, not all at once
- **Key landmarks** influence development in ways that ripple outward
- **Transportation** shapes everything - where people live, work, and shop

### The Technical Challenges

The most challenging part wasn't the urban planning theory - it was making the s
imulation both realistic and performant. How do you simulate a city with a million people
 without grinding to a halt? How do you make the temporal evolution smooth and b
elievable?

The solution involved hierarchical modeling, efficient data structures, and a lo
t of optimization. But the result is something that can generate and animate comp
lex cities in real-time.

### The Name

I named it "Metro" because metropolitan areas are the most complex and interesti
ng urban systems. They're not just big cities - they're interconnected networks of
 cities, suburbs, and infrastructure that create something greater than the sum 
of their parts.

---

*If you're fascinated by cities, data visualization, or just want to watch virtu
al cities grow and evolve, check out [Metro](https://github.com/rl337/metro). It m
ight just change how you see the urban world around you!*
