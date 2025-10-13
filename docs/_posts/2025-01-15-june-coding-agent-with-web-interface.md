---
layout: post
title: "June - A Coding Agent with Web Interface"
date: 2025-01-15 14:00:00 -0500
categories: [projects, ai, python, web-development]
tags: [ai, coding-agent, together-ai, flask, web-interface, automation]
author: Richard Lee
---

I'm excited to share **June**, a coding agent I've developed that uses
Together.ai as its backend to provide automated coding assistance through a web
interface. This project represents my exploration into AI-powered development
tools and their practical applications.

## 🤖 What is June?

June is a coding agent that leverages Together.ai's API to provide intelligent
coding assistance. It's designed as a long-running process with a web interface
that allows users to submit coding tasks and receive automated solutions.

## 🎯 Key Features

### AI-Powered Coding

- **Together.ai integration** for intelligent code generation
- **Task-based workflow** for structured coding assistance
- **Automated processing** of coding requests
- **Error handling** and result management

### Web Interface

- **Real-time status** monitoring
- **Task management** with status tracking
- **Live updates** with automatic refresh
- **Form-based** task submission
- **Activity logging** for transparency

### API Endpoints

- **GET /status**: Current agent status and task counts
- **GET /tasks**: List all tasks with statuses and results
- **POST /tasks**: Submit new coding tasks via JSON

## 🛠️ Technical Implementation

### Modern Python Architecture

June is built with modern Python practices:

- **Python 3.x** with Poetry for dependency management
- **Flask** for the web service
- **Together.ai API** for AI-powered coding
- **Modular design** for maintainability
- **Comprehensive testing** with pytest

### Core Components

```text
june_agent/
├── __init__.py           # Package initialization
├── __main__.py          # Main entry point and agent loop
├── request.py           # API request handling
├── task.py              # Task management and processing
├── web_service.py       # Flask web server
├── svg.py               # SVG generation utilities
└── chart.py             # Chart generation utilities
```

### Web Service Architecture

The Flask web service provides:

- **RESTful API** for task management
- **Real-time updates** through automatic refresh
- **Error handling** for robust operation
- **Status monitoring** for system health

## 🚀 Getting Started

### Prerequisites

- **Python 3.8+**
- **Poetry** for dependency management
- **Together.ai API key**

### Installation

```bash
# Clone the repository
git clone https://github.com/rl337/june
cd june

# Install dependencies
poetry install

# Set up API key
export TOGETHER_API_KEY="your_api_key_here"
```

### Running the Agent

```bash
# Using Poetry
poetry run python -m june_agent

# Or activate virtual environment
poetry shell
python -m june_agent
```

The agent will start and be available at `http://localhost:8080`.

## 🌐 Web Interface

### Dashboard Features

- **Agent Status**: Current operational status
- **Task Queue**: Pending, processing, completed, and failed tasks
- **Task Submission**: Form for submitting new coding tasks
- **Activity Log**: Recent agent activities and updates

### API Usage

#### Submit a Task

```bash
curl -X POST -H "Content-Type: application/json" \
  -d '{"description":"Write a python function to calculate factorial"}' \
  http://localhost:8080/tasks
```

#### Check Status

```bash
curl http://localhost:8080/status
```

#### List Tasks

```bash
curl http://localhost:8080/tasks
```

## 🧪 Testing

The project includes comprehensive testing:

```bash
# Run all tests
poetry run pytest

# Run with coverage
poetry run pytest --cov=june_agent

# Run specific test files
poetry run pytest tests/test_task.py
```

## 📊 Project Status

### Current Features

- ✅ **AI-powered coding** with Together.ai
- ✅ **Web interface** for task management
- ✅ **RESTful API** for programmatic access
- ✅ **Task queuing** and status tracking
- ✅ **Error handling** and result management
- ✅ **Comprehensive testing** with pytest
- ✅ **Modern Python packaging** with Poetry

### Planned Features

- 🔄 **Enhanced AI models** for better code generation
- 🔄 **Task prioritization** and scheduling
- 🔄 **Result caching** for improved performance
- 🔄 **User authentication** and access control
- 🔄 **Advanced task types** beyond coding

## 🎯 Use Cases

June is perfect for:

- **Automated coding assistance** for developers
- **Code generation** for repetitive tasks
- **Learning and experimentation** with AI coding
- **Prototype development** and rapid iteration
- **Educational tools** for programming courses

## 🔗 Links and Resources

- **[GitHub Repository](https://github.com/rl337/june)** - Source code and
  documentation
- **[Project README](https://github.com/rl337/june/blob/main/README.md)** -
  Detailed setup and usage instructions
- **[Together.ai Documentation](https://docs.together.ai/)** - AI API
  documentation
- **[Flask Documentation](https://flask.palletsprojects.com/)** - Web framework
  documentation

## 💡 Why June?

The name "June" reflects the project's purpose - it's like having a helpful
assistant available year-round to help with coding tasks. The agent is designed
to be:

- **Reliable** and always available
- **Intelligent** in understanding coding requests
- **Helpful** in providing practical solutions
- **Accessible** through a simple web interface

## 🎨 Development Philosophy

June represents my approach to building AI-powered tools that are both powerful
and accessible. It's not just about using AI for the sake of it - it's about
creating tools that genuinely help developers be more productive:

- **Simple interface** for complex AI capabilities
- **Reliable operation** through robust error handling
- **Transparent process** with clear status updates
- **Extensible design** for future enhancements

## 🚀 Future Development

Planned enhancements include:

- **Enhanced AI models** for better code understanding
- **Task scheduling** and prioritization
- **Result caching** for improved performance
- **User management** and authentication
- **Advanced task types** and workflows

---

*Interested in AI-powered development tools or automated coding assistance?
Check out [June](https://github.com/rl337/june) and see how it can enhance your
development workflow!*
