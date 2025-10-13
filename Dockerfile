# Multi-stage Dockerfile for rl337.org development environment
# This container provides all necessary tools for Python, Jekyll, and shell script validation

FROM ubuntu:22.04

# Set environment variables
ENV DEBIAN_FRONTEND=noninteractive
ENV PYTHONUNBUFFERED=1
ENV LANG=C.UTF-8
ENV LC_ALL=C.UTF-8

# Install system dependencies
RUN apt-get update && apt-get install -y \
    # Python and pip
    python3 \
    python3-pip \
    python3-venv \
    python3-dev \
    # Ruby and Jekyll dependencies
    ruby \
    ruby-dev \
    build-essential \
    zlib1g-dev \
    libssl-dev \
    libffi-dev \
    # Shell script validation
    shellcheck \
    # Link validation
    curl \
    wget \
    # Git for version control
    git \
    # Other utilities
    make \
    && rm -rf /var/lib/apt/lists/*

# Install Node.js 20+ for markdownlint compatibility
RUN curl -fsSL https://deb.nodesource.com/setup_20.x | bash - \
    && apt-get install -y nodejs

# Install Node.js packages for markdown validation
RUN npm install -g markdownlint-cli

# Install Python packages globally (will be overridden by venv in scripts)
RUN pip3 install --no-cache-dir \
    pytest \
    pytest-cov \
    flake8 \
    black \
    isort \
    mypy \
    types-requests \
    types-PyYAML

# Install Ruby gems
RUN gem install bundler jekyll

# Set working directory
WORKDIR /workspace

# Copy project files
COPY . /workspace/

# Install Jekyll dependencies from Gemfile
RUN cd docs && bundle install --path vendor/bundle

# Make scripts executable
RUN chmod +x run_checks.sh scripts/*.sh

# Set default command
CMD ["/bin/bash"]