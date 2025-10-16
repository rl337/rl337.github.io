---
layout: post
title: "June - A Coding Agent with Web Interface"
date: 2025-01-15 14:00:00 -0500
categories: [projects, ai, python, web-development]
tags: [ai, coding-agent, together-ai, flask, web-interface, automation]
author: Richard Lee
---

![June AI Agent]({{ '/assets/images/blog/june-ai-agent.png' | relative_url }}})
*June's web interface showing the AI coding agent in action*

Have you ever wished you had a coding assistant that could just... work in the b
ackground, handling the tedious parts of development while you focus on the big picture? T
hat's exactly what I was thinking when I started building **June** - an AI-powered co
ding agent that's become one of my most experimental and surprisingly useful project
s.

What began as a simple experiment with Together.ai's API quickly evolved into so
mething much more interesting: a persistent coding assistant that could actually execut
e code, save files, and provide real-time feedback through a web interface. Let m
e tell you about the journey.

## 🤖 The AI Assistant Experiment

![AI Development]({{ '/assets/images/blog/june-development.png' | relative_url }}
})
*The evolution from simple API calls to a full-featured coding assistant*

The idea for June came from a simple frustration: I was spending too much time o
n boilerplate code and repetitive tasks. I'd heard about Together.ai's API and th
ought "what if I could just ask an AI to handle the boring stuff?"

But here's the thing - most AI coding assistants are just chat interfaces. They 
can suggest code, but they can't actually *do* anything with it. I wanted something
 that could take action, execute code, save files, and give me real results.

Looking at the commit history, I can see exactly where this project took off. Th
e early commits show me struggling with basic API integration, but then something
 interesting happened in commit `24cf0631` - I added function calling capabiliti
es.

That's when June went from being a fancy chatbot to being a real coding assistan
t.

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

## 🧪 The Testing Challenge

![Testing AI]({{ '/assets/images/blog/june-testing.png' | relative_url }}})
*Testing an AI agent that can modify its own code - a unique challenge*

One of the most interesting aspects of developing June was figuring out how to t
est an AI system. How do you write tests for something that's designed to be unpred
ictable and creative?

The breakthrough came when I realized I needed to test the *system*, not the AI'
s responses. I focused on testing the function calling mechanism, the file operat
ions, and the web interface - the parts that needed to work reliably regardless of wh
at the AI decided to do.

Looking at commits like `43cddf7e` ("Add context to scenario test assertions"), 
I can see the evolution of my testing approach. I started with simple unit tests,
 then moved to scenario-based testing where I'd give June a task and verify it c
ould complete it end-to-end.

The most fascinating part? June actually helped me improve its own tests. I'd as
k it to write test cases, and it would come up with scenarios I hadn't thought of
.

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

## 💡 What I Learned About AI Development

![AI Insights]({{ '/assets/images/blog/june-insights.png' | relative_url }}})
*The surprising lessons from building an AI coding assistant*

Building June taught me more about AI development than I expected. The biggest s
urprise? The AI isn't the hard part - it's everything around it.

### The Real Challenges

The Together.ai API is actually quite straightforward to use. The real challenge
s were:

1. **Function calling reliability** - Making sure the AI could consistently call
 the right functions with the right parameters
2. **Error handling** - What happens when the AI generates invalid code or tries
 to access files it shouldn't?
3. **Security** - How do you give an AI agent the ability to execute code withou
t creating a security nightmare?
4. **Testing** - How do you test a system that's designed to be unpredictable?

### The Unexpected Benefits

The most surprising thing about June isn't what it can do - it's how it changed 
my own development process. Having an AI that can actually execute code and save f
iles means I can offload the tedious parts of development and focus on the interesti
ng problems.

I've used June to:
- Generate boilerplate code for new projects
- Write test cases for complex functions
- Refactor large codebases
- Debug issues by having it analyze error logs

### The Name

I named it "June" because it's like having a helpful assistant available year-ro
und, but also because "June" sounds friendly and approachable - not intimidating lik
e "AI Agent" or "Coding Bot."

---

*If you're curious about AI-powered development tools or want to experiment with
 automated coding assistance, check out [June](https://github.com/rl337/june). I
t might just change how you think about the future of software development!*
