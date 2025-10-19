#!/usr/bin/env python3
"""
Alternative AI image generation script using Replicate API.
This is a fallback when Midjourney MCP is not working.
"""

import os
import sys
import asyncio
import aiohttp
import base64
from typing import Dict, List

# Replicate API configuration
REPLICATE_API_TOKEN = os.getenv("REPLICATE_API_TOKEN")
REPLICATE_API_URL = "https://api.replicate.com/v1/predictions"

# Image specifications for each blog post
BLOG_IMAGES = {
    "curioshelf": {
        "images": [
            {
                "filename": "curioshelf-interface.png",
                "prompt": "A modern, clean interface for a visual asset management tool called Curioshelf. Shows a tabbed workflow with organized folders, image thumbnails, and a sleek dark theme. The interface displays various game development assets like sprites, textures, and UI elements neatly organized in a grid layout. Professional software interface design with a focus on organization and workflow efficiency.",
                "style": "professional software interface, clean design, dark theme"
            },
            {
                "filename": "asset-chaos.png", 
                "prompt": "A chaotic scene showing scattered game development assets - sprites, textures, UI elements, and 3D models scattered across a messy desktop. Files with random names like 'sprite_final_v3_new.png' and 'texture_temp_backup.psd' scattered everywhere. The scene represents the chaos of unorganized asset management before using a proper tool.",
                "style": "chaotic desktop scene, scattered files, messy organization"
            },
            {
                "filename": "curioshelf-development.png",
                "prompt": "A developer working on a computer with code on the screen, surrounded by testing tools and debugging interfaces. The scene shows the development process of building a software tool, with multiple monitors showing code, tests, and documentation. Modern development environment with clean, professional setup.",
                "style": "development environment, coding, professional setup"
            },
            {
                "filename": "curioshelf-reflection.png",
                "prompt": "A thoughtful developer looking at a completed software project on their screen, with a sense of accomplishment and reflection. The scene shows the journey from chaos to order, with before/after representations of organized vs unorganized assets. Professional, contemplative atmosphere.",
                "style": "contemplative developer, reflection, professional atmosphere"
            }
        ]
    },
    "june": {
        "images": [
            {
                "filename": "june-ai-agent.png",
                "prompt": "An AI coding assistant interface showing a chat window with code suggestions, function calls, and automated programming assistance. The interface displays Python code, API calls, and intelligent responses. Modern, clean design with a focus on AI-human collaboration in software development.",
                "style": "AI interface, coding assistant, modern design"
            },
            {
                "filename": "june-development.png",
                "prompt": "A developer working with an AI assistant, showing code generation, testing, and debugging processes. The scene depicts modern AI-assisted development with multiple screens showing code, tests, and AI responses. Professional development environment with AI integration.",
                "style": "AI-assisted development, professional environment"
            },
            {
                "filename": "june-testing.png",
                "prompt": "A testing environment showing automated tests, code coverage reports, and AI-generated test cases. The scene represents the unique challenges of testing AI systems, with various testing tools and metrics displayed on multiple monitors.",
                "style": "testing environment, AI testing, professional setup"
            },
            {
                "filename": "june-insights.png",
                "prompt": "A developer reflecting on AI collaboration, with insights about function calling, error handling, and the future of AI-assisted development. The scene shows learning and growth in AI development practices.",
                "style": "AI insights, reflection, professional development"
            }
        ]
    },
    "metro": {
        "images": [
            {
                "filename": "metro-city-simulation.png",
                "prompt": "A detailed city simulation showing urban development, buildings, roads, and infrastructure evolving over time. The scene depicts a metropolitan area with Roman grid system layout, showing the growth and development of a city from ancient times to modern day.",
                "style": "city simulation, urban planning, detailed visualization"
            },
            {
                "filename": "metro-migration.png",
                "prompt": "A developer migrating code from Java to Python, showing the transformation of a codebase with modern tools and frameworks. The scene represents the technical migration process with code, documentation, and testing tools.",
                "style": "code migration, Java to Python, technical process"
            },
            {
                "filename": "metro-evolution.png",
                "prompt": "A timeline visualization showing the evolution of cities through different eras - from Roman grid systems to modern metropolitan areas. The scene shows temporal evolution with historical and modern city elements.",
                "style": "timeline visualization, city evolution, historical progression"
            },
            {
                "filename": "metro-reflection.png",
                "prompt": "A developer contemplating city complexity and urban patterns, with insights about simulation, modeling, and the intricate systems that make up metropolitan areas.",
                "style": "urban planning reflection, city complexity, professional contemplation"
            }
        ]
    },
    "dark-closet": {
        "images": [
            {
                "filename": "dark-closet-game.png",
                "prompt": "A 2D platformer game scene inspired by Pinocchio, showing a dark closet environment with wooden toys, strings, and a puppet character. The scene has a mysterious, slightly eerie atmosphere with warm lighting and detailed pixel art style.",
                "style": "2D platformer, Pinocchio-inspired, pixel art, mysterious atmosphere"
            },
            {
                "filename": "dark-closet-procedural.png",
                "prompt": "A developer working on procedural generation algorithms, showing code that generates consistent sprites and game assets. The scene represents the challenge of creating usable procedural content with testing and iteration processes.",
                "style": "procedural generation, game development, technical process"
            },
            {
                "filename": "dark-closet-callbacks.png",
                "prompt": "A technical diagram showing object callback systems and brick breaking mechanics in game development. The scene represents the programming concepts behind interactive game elements and physics systems.",
                "style": "technical diagram, game programming, callback systems"
            }
        ]
    },
    "trouble": {
        "images": [
            {
                "filename": "trouble-cli.png",
                "prompt": "A command-line interface showing documentation generation tools and automated processes. The scene depicts CLI tools, terminal windows, and automated documentation workflows with a clean, professional terminal aesthetic.",
                "style": "CLI interface, terminal, documentation tools"
            },
            {
                "filename": "trouble-development.png",
                "prompt": "A developer working with AI assistance on documentation automation, showing the collaboration between human and AI in solving complex technical problems. The scene represents modern AI-assisted development practices.",
                "style": "AI collaboration, documentation automation, technical development"
            },
            {
                "filename": "trouble-reflection.png",
                "prompt": "A developer reflecting on the challenges of documentation and the value of AI collaboration in solving technical problems. The scene shows insights about automation, documentation, and the future of technical writing.",
                "style": "documentation reflection, AI insights, technical writing"
            }
        ]
    }
}

# Sugar glider decorative images for website
SUGAR_GLIDER_IMAGES = {
    "logo": {
        "filename": "sugar-glider-logo.png",
        "prompt": "A cute, stylized sugar glider character obsessively hugging a large, juicy strawberry with the same intensity as Scrat from Ice Age with his acorn. The sugar glider should have large, wide eyes filled with pure obsession and determination, clutching the strawberry with both tiny hands and feet, as if it's the most precious thing in the world. The strawberry should be oversized compared to the glider, bright red and glossy. The glider's expression should show complete focus and adoration for the strawberry. Clean, modern illustration style suitable for use as a personal logo, with vibrant colors and a warm, friendly aesthetic.",
        "style": "cute mascot, strawberry obsession, Scrat-style, logo design"
    },
    "mascot": {
        "filename": "sugar-glider-mascot.png",
        "prompt": "A cute, stylized sugar glider character in a friendly pose, designed as a website mascot. The glider should have large, expressive eyes, soft fur texture, and a welcoming expression. Clean, modern illustration style suitable for web use, with a warm color palette.",
        "style": "cute mascot, friendly, web design, warm colors"
    },
    "hero": {
        "filename": "sugar-glider-hero.png", 
        "prompt": "A majestic sugar glider gliding through a digital landscape with code symbols, circuit patterns, and tech elements floating around. The scene represents the journey of software development and creativity. Modern, stylized illustration with a tech aesthetic.",
        "style": "digital landscape, tech elements, majestic, modern illustration"
    },
    "footer": {
        "filename": "sugar-glider-footer.png",
        "prompt": "A small, cute sugar glider sitting peacefully in the corner of a website footer, looking content and friendly. Simple, minimalist design that works well as a small decorative element. Soft colors and clean lines.",
        "style": "minimalist, peaceful, decorative, soft colors"
    },
    "loading": {
        "filename": "sugar-glider-loading.png",
        "prompt": "A playful sugar glider in various poses showing different stages of activity - coding, thinking, celebrating. Perfect for loading animations or progress indicators. Clean, animated-style illustration with bright, cheerful colors.",
        "style": "playful, animated-style, bright colors, activity poses"
    },
    "error": {
        "filename": "sugar-glider-error.png",
        "prompt": "A concerned but still cute sugar glider looking at a broken computer or error message, with a helpful and empathetic expression. The glider should look like it's trying to help fix the problem. Friendly, approachable design.",
        "style": "concerned but cute, helpful, empathetic, friendly design"
    },
    "success": {
        "filename": "sugar-glider-success.png",
        "prompt": "A happy, celebrating sugar glider with arms raised in victory, surrounded by success symbols like checkmarks, stars, and celebration elements. Bright, positive colors and an energetic pose.",
        "style": "celebrating, victory pose, success symbols, bright colors"
    },
    "strawberry-obsession": {
        "filename": "sugar-glider-strawberry-obsession.png",
        "prompt": "A sugar glider in a state of pure strawberry obsession, eyes wide with determination, clutching multiple strawberries with both hands and feet, similar to Scrat from Ice Age with his acorn. The glider should look completely focused and slightly manic, with strawberries scattered around. The expression should show that nothing else matters except the strawberries. Clean, modern illustration style.",
        "style": "pure obsession, manic energy, multiple strawberries, Scrat-style"
    },
    "logo-minimal": {
        "filename": "sugar-glider-logo-minimal.png",
        "prompt": "A minimal, clean version of a sugar glider hugging a strawberry, designed for use as a small logo or favicon. Simple lines, high contrast, easily recognizable at small sizes. The sugar glider should still show the characteristic obsession with the strawberry but in a more simplified, icon-like style.",
        "style": "minimal design, high contrast, icon-like, simplified"
    }
}

async def generate_image_with_replicate(prompt: str, style: str) -> str:
    """Generate an image using Replicate API."""
    if not REPLICATE_API_TOKEN:
        return f"Error: REPLICATE_API_TOKEN not set. Please set your Replicate API token."
    
    # Use Stable Diffusion model
    model = "stability-ai/stable-diffusion:db21e45d3f7023abc2a46e38a2466335b4c603fd818909461976d149bcf2713b"
    
    headers = {
        "Authorization": f"Token {REPLICATE_API_TOKEN}",
        "Content-Type": "application/json"
    }
    
    data = {
        "version": "db21e45d3f7023abc2a46e38a2466335b4c603fd818909461976d149bcf2713b",
        "input": {
            "prompt": f"{prompt}, {style}, high quality, detailed, professional",
            "width": 512,
            "height": 512,
            "num_inference_steps": 20
        }
    }
    
    async with aiohttp.ClientSession() as session:
        # Create prediction
        async with session.post(REPLICATE_API_URL, headers=headers, json=data) as response:
            if response.status != 201:
                return f"Error creating prediction: {response.status} - {await response.text()}"
            
            prediction = await response.json()
            prediction_id = prediction["id"]
        
        # Poll for completion
        while True:
            async with session.get(f"{REPLICATE_API_URL}/{prediction_id}", headers=headers) as response:
                if response.status != 200:
                    return f"Error checking prediction: {response.status} - {await response.text()}"
                
                prediction = await response.json()
                status = prediction["status"]
                
                if status == "succeeded":
                    return prediction["output"][0]
                elif status == "failed":
                    return f"Error: Prediction failed - {prediction.get('error', 'Unknown error')}"
                elif status in ["starting", "processing"]:
                    await asyncio.sleep(2)
                else:
                    return f"Error: Unknown status - {status}"

async def generate_all_images():
    """Generate all images using Replicate API."""
    print("🎨 Starting AI image generation using Replicate API...")
    print("=" * 60)
    
    if not REPLICATE_API_TOKEN:
        print("❌ Error: REPLICATE_API_TOKEN not set!")
        print("Please set your Replicate API token:")
        print("export REPLICATE_API_TOKEN='your_token_here'")
        print("\nYou can get a token from: https://replicate.com/account/api-tokens")
        return
    
    results = {}
    
    # Generate sugar glider decorative images
    print(f"\n🦎 Generating sugar glider decorative images...")
    results["sugar_gliders"] = []
    
    for image_type, image_spec in SUGAR_GLIDER_IMAGES.items():
        print(f"  🖼️  Generating {image_spec['filename']}...")
        result = await generate_image_with_replicate(image_spec["prompt"], image_spec["style"])
        results["sugar_gliders"].append({
            "filename": image_spec["filename"],
            "type": image_type,
            "result": result
        })
        print(f"     ✅ Generated: {image_spec['filename']}")
    
    # Generate blog post images
    for project, data in BLOG_IMAGES.items():
        print(f"\n📸 Generating images for {project}...")
        results[project] = []
        
        for image_spec in data["images"]:
            print(f"  🖼️  Generating {image_spec['filename']}...")
            result = await generate_image_with_replicate(image_spec["prompt"], image_spec["style"])
            results[project].append({
                "filename": image_spec["filename"],
                "result": result
            })
            print(f"     ✅ Generated: {image_spec['filename']}")
    
    # Save results to a file
    with open("image_generation_results_replicate.json", "w") as f:
        import json
        json.dump(results, f, indent=2)
    
    print("\n🎉 Image generation complete!")
    print("Results saved to image_generation_results_replicate.json")
    print("\nNext steps:")
    print("1. Review the generated images")
    print("2. Download the images you like")
    print("3. Replace the placeholder images in docs/assets/images/blog/")
    print("4. Add sugar glider images to website decorations")

if __name__ == "__main__":
    asyncio.run(generate_all_images())
