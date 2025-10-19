#!/usr/bin/env python3
"""
Script to generate AI images for blog posts using Midjourney MCP server.
This script will generate contextually appropriate images for each blog post.
"""

import os
import sys
import asyncio
import json
from typing import Dict, List

# Add the midjourney_mcp to the path
sys.path.append('/usr/local/lib/python3.10/dist-packages')

try:
    from midjourney_mcp.midjourney import generating_image
except ImportError:
    print("Error: midjourney_mcp not found. Make sure it's installed in the Docker container.")
    sys.exit(1)

# Image specifications for each blog post
BLOG_IMAGES = {
    "curioshelf": {
        "images": [
            {
                "filename": "curioshelf-interface.png",
                "prompt": "A modern, clean interface for a visual asset management tool called Curioshelf. Shows a tabbed workflow with organized folders, image thumbnails, and a sleek dark theme. The interface displays various game development assets like sprites, textures, and UI elements neatly organized in a grid layout. Professional software interface design with a focus on organization and workflow efficiency.",
                "aspect_ratio": "16:9"
            },
            {
                "filename": "asset-chaos.png", 
                "prompt": "A chaotic scene showing scattered game development assets - sprites, textures, UI elements, and 3D models scattered across a messy desktop. Files with random names like 'sprite_final_v3_new.png' and 'texture_temp_backup.psd' scattered everywhere. The scene represents the chaos of unorganized asset management before using a proper tool.",
                "aspect_ratio": "16:9"
            },
            {
                "filename": "curioshelf-development.png",
                "prompt": "A developer working on a computer with code on the screen, surrounded by testing tools and debugging interfaces. The scene shows the development process of building a software tool, with multiple monitors showing code, tests, and documentation. Modern development environment with clean, professional setup.",
                "aspect_ratio": "16:9"
            },
            {
                "filename": "curioshelf-reflection.png",
                "prompt": "A thoughtful developer looking at a completed software project on their screen, with a sense of accomplishment and reflection. The scene shows the journey from chaos to order, with before/after representations of organized vs unorganized assets. Professional, contemplative atmosphere.",
                "aspect_ratio": "16:9"
            }
        ]
    },
    "june": {
        "images": [
            {
                "filename": "june-ai-agent.png",
                "prompt": "An AI coding assistant interface showing a chat window with code suggestions, function calls, and automated programming assistance. The interface displays Python code, API calls, and intelligent responses. Modern, clean design with a focus on AI-human collaboration in software development.",
                "aspect_ratio": "16:9"
            },
            {
                "filename": "june-development.png",
                "prompt": "A developer working with an AI assistant, showing code generation, testing, and debugging processes. The scene depicts modern AI-assisted development with multiple screens showing code, tests, and AI responses. Professional development environment with AI integration.",
                "aspect_ratio": "16:9"
            },
            {
                "filename": "june-testing.png",
                "prompt": "A testing environment showing automated tests, code coverage reports, and AI-generated test cases. The scene represents the unique challenges of testing AI systems, with various testing tools and metrics displayed on multiple monitors.",
                "aspect_ratio": "16:9"
            },
            {
                "filename": "june-insights.png",
                "prompt": "A developer reflecting on AI collaboration, with insights about function calling, error handling, and the future of AI-assisted development. The scene shows learning and growth in AI development practices.",
                "aspect_ratio": "16:9"
            }
        ]
    },
    "metro": {
        "images": [
            {
                "filename": "metro-city-simulation.png",
                "prompt": "A detailed city simulation showing urban development, buildings, roads, and infrastructure evolving over time. The scene depicts a metropolitan area with Roman grid system layout, showing the growth and development of a city from ancient times to modern day.",
                "aspect_ratio": "16:9"
            },
            {
                "filename": "metro-migration.png",
                "prompt": "A developer migrating code from Java to Python, showing the transformation of a codebase with modern tools and frameworks. The scene represents the technical migration process with code, documentation, and testing tools.",
                "aspect_ratio": "16:9"
            },
            {
                "filename": "metro-evolution.png",
                "prompt": "A timeline visualization showing the evolution of cities through different eras - from Roman grid systems to modern metropolitan areas. The scene shows temporal evolution with historical and modern city elements.",
                "aspect_ratio": "16:9"
            },
            {
                "filename": "metro-reflection.png",
                "prompt": "A developer contemplating city complexity and urban patterns, with insights about simulation, modeling, and the intricate systems that make up metropolitan areas.",
                "aspect_ratio": "16:9"
            }
        ]
    },
    "dark-closet": {
        "images": [
            {
                "filename": "dark-closet-game.png",
                "prompt": "A 2D platformer game scene inspired by Pinocchio, showing a dark closet environment with wooden toys, strings, and a puppet character. The scene has a mysterious, slightly eerie atmosphere with warm lighting and detailed pixel art style.",
                "aspect_ratio": "16:9"
            },
            {
                "filename": "dark-closet-procedural.png",
                "prompt": "A developer working on procedural generation algorithms, showing code that generates consistent sprites and game assets. The scene represents the challenge of creating usable procedural content with testing and iteration processes.",
                "aspect_ratio": "16:9"
            },
            {
                "filename": "dark-closet-callbacks.png",
                "prompt": "A technical diagram showing object callback systems and brick breaking mechanics in game development. The scene represents the programming concepts behind interactive game elements and physics systems.",
                "aspect_ratio": "16:9"
            }
        ]
    },
    "trouble": {
        "images": [
            {
                "filename": "trouble-cli.png",
                "prompt": "A command-line interface showing documentation generation tools and automated processes. The scene depicts CLI tools, terminal windows, and automated documentation workflows with a clean, professional terminal aesthetic.",
                "aspect_ratio": "16:9"
            },
            {
                "filename": "trouble-development.png",
                "prompt": "A developer working with AI assistance on documentation automation, showing the collaboration between human and AI in solving complex technical problems. The scene represents modern AI-assisted development practices.",
                "aspect_ratio": "16:9"
            },
            {
                "filename": "trouble-reflection.png",
                "prompt": "A developer reflecting on the challenges of documentation and the value of AI collaboration in solving technical problems. The scene shows insights about automation, documentation, and the future of technical writing.",
                "aspect_ratio": "16:9"
            }
        ]
    }
}

async def generate_image(prompt: str, aspect_ratio: str) -> str:
    """Generate an image using Midjourney MCP server."""
    try:
        result = await generating_image(prompt, aspect_ratio)
        return result
    except Exception as e:
        return f"Error generating image: {str(e)}"

async def generate_all_images():
    """Generate all images for blog posts."""
    print("🎨 Starting AI image generation for blog posts...")
    print("=" * 60)
    
    # Check if environment variables are set
    if not os.getenv("TOKEN_R") or not os.getenv("TOKEN_I"):
        print("❌ Error: Midjourney authentication tokens not set!")
        print("Please set TOKEN_R and TOKEN_I environment variables.")
        print("You can get these from your Midjourney account.")
        return
    
    results = {}
    
    for project, data in BLOG_IMAGES.items():
        print(f"\n📸 Generating images for {project}...")
        results[project] = []
        
        for image_spec in data["images"]:
            print(f"  🖼️  Generating {image_spec['filename']}...")
            result = await generate_image(image_spec["prompt"], image_spec["aspect_ratio"])
            results[project].append({
                "filename": image_spec["filename"],
                "result": result
            })
            print(f"     ✅ Generated: {image_spec['filename']}")
    
    # Save results to a file
    with open("image_generation_results.json", "w") as f:
        json.dump(results, f, indent=2)
    
    print("\n🎉 Image generation complete!")
    print("Results saved to image_generation_results.json")
    print("\nNext steps:")
    print("1. Review the generated images")
    print("2. Download the images you like")
    print("3. Replace the placeholder images in docs/assets/images/blog/")

if __name__ == "__main__":
    asyncio.run(generate_all_images())
