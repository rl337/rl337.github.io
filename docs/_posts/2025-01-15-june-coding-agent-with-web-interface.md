---
layout: post
title: "June: what happens between agent runs"
date: 2025-01-15 14:00:00 -0500
categories: [projects, ai, python, web-development]
tags: [agents, orchestration, python, mechaharness]
author: Richard Lee
permalink: /projects/ai/python/web-development/2025/01/15/june-coding-agent-with-web-interface.html
last_modified_at: 2026-11-27
---

<p class="post-meta">Revised November 27, 2026.</p>

Suppose I give an agent a goal that needs more than one run. It finishes the first
task and produces a result. What tells it whether to continue, what to do next,
or what to keep for the next run?

That's the part of the system that [June](https://github.com/rl337/june) is
concerned with. Its current design puts persistent goals, scheduling, and the
work ledger around the execution machinery in
[MechaHarness](https://github.com/rl337/mechaharness).

<figure class="post-illustration">
  <img src="{{ '/assets/images/blog/june-ai-agent.webp' | relative_url }}"
       alt="Two crows working together on a small mechanical puzzle."
       width="1280" height="720" loading="eager" decoding="async">
  <figcaption>
    Crow illustration of collaborating with a coding assistant. Generated with Qwen-Image 2.1.
  </figcaption>
</figure>

If the second task depends on what the first produces, remembering that dependency
belongs with the application. So does deciding whether the result is sufficient
and making the second task runnable. Executing a task and deciding what it means
for the goal are different responsibilities.

MechaHarness supplies reusable graph templates, checkpoints, and verification
hooks. June chooses the concrete templates and bindings for the work it is
managing. The runner shouldn't have to acquire a new understanding of goals
every time the application changes how it schedules them.

<figure class="architecture-figure">
  <a href="{{ '/assets/images/blog/june-architecture.svg' | relative_url }}">
    <img src="{{ '/assets/images/blog/june-architecture.svg' | relative_url }}"
         alt="June owns goals and work records; its runner calls MechaHarness graph execution and receives the result."
         width="1600" height="533" loading="lazy" decoding="async">
  </a>
  <figcaption>
    Conceptual architecture showing selected responsibilities, based on June's
    <a href="https://github.com/rl337/june/blob/main/src/june/runner/task_runner.py">TaskRunner</a>
    and <a href="https://github.com/rl337/june/blob/main/src/june/harness/__init__.py">MechaHarnessClient</a>.
    Open the diagram for a larger view.
  </figcaption>
</figure>

One small piece of that application state is a stored goal. This example
reopens the same directory through a new store and reads the goal back:

```python
from pathlib import Path
from tempfile import TemporaryDirectory

from june.goals import Goal, GoalStore
from june.persist import JsonStore

with TemporaryDirectory() as folder:
    first = GoalStore(JsonStore(Path(folder)))
    goal = first.put(Goal("Revise a draft", "Draft reviewed"))

    reopened = GoalStore(JsonStore(Path(folder)))
    print(reopened.get(goal.id).title)
```

Output:

```text
Revise a draft
```

This only demonstrates saving and reopening a goal; it doesn't start a model
run. The goal's identity and completion criteria can exist outside any one
execution.

In [Getting your agents to use Dependency Injection](https://rl337.substack.com/p/getting-your-agents-to-use-dependency),
I wrote about how easy patterns can keep spreading as an agent adds more code.
This is another place where the boundary matters. If scheduling decisions and
application state keep accumulating inside the reusable execution layer, that
layer gradually becomes tied to the application it was meant to support.

A successful model call is one event in the life of the work. The application
still has to know what that event means.
