#!/usr/bin/env python3
"""
Create simple placeholder images for the website.
This is a fallback when Midjourney API is not available.
"""

import os
from PIL import Image, ImageDraw, ImageFont
import textwrap

def create_placeholder_image(filename, text, size=(400, 400), bg_color=(240, 240, 240), text_color=(100, 100, 100)):
    """Create a simple placeholder image with text."""
    img = Image.new('RGB', size, bg_color)
    draw = ImageDraw.Draw(img)
    
    # Try to use a default font, fallback to basic if not available
    try:
        font = ImageFont.truetype("/System/Library/Fonts/Arial.ttf", 20)
    except:
        try:
            font = ImageFont.load_default()
        except:
            font = None
    
    # Wrap text to fit in image
    wrapped_text = textwrap.fill(text, width=30)
    
    # Get text bounding box
    if font:
        bbox = draw.textbbox((0, 0), wrapped_text, font=font)
        text_width = bbox[2] - bbox[0]
        text_height = bbox[3] - bbox[1]
    else:
        text_width = len(wrapped_text) * 6
        text_height = 20
    
    # Center the text
    x = (size[0] - text_width) // 2
    y = (size[1] - text_height) // 2
    
    # Draw text
    draw.text((x, y), wrapped_text, fill=text_color, font=font)
    
    # Save image
    img.save(filename)
    print(f"Created placeholder: {filename}")

def main():
    """Create all placeholder images."""
    print("🎨 Creating placeholder images...")
    
    # Create directories
    os.makedirs("docs/assets/images/blog", exist_ok=True)
    os.makedirs("docs/assets/images/sugar-gliders", exist_ok=True)
    
    # Sugar glider images
    sugar_glider_images = [
        ("docs/assets/images/sugar-gliders/sugar-glider-logo.png", "🦎🍓\nSugar Glider\nLogo\n(Strawberry Obsessed)"),
        ("docs/assets/images/sugar-gliders/sugar-glider-mascot.png", "🦎\nSugar Glider\nMascot"),
        ("docs/assets/images/sugar-gliders/sugar-glider-hero.png", "🦎\nSugar Glider\nHero Image\n(Digital Landscape)"),
        ("docs/assets/images/sugar-gliders/sugar-glider-footer.png", "🦎\nSugar Glider\nFooter"),
        ("docs/assets/images/sugar-gliders/sugar-glider-loading.png", "🦎\nSugar Glider\nLoading\n(Animated)"),
        ("docs/assets/images/sugar-gliders/sugar-glider-error.png", "🦎\nSugar Glider\nError\n(Concerned)"),
        ("docs/assets/images/sugar-gliders/sugar-glider-success.png", "🦎\nSugar Glider\nSuccess\n(Celebrating)"),
        ("docs/assets/images/sugar-gliders/sugar-glider-strawberry-obsession.png", "🦎🍓🍓🍓\nSugar Glider\nStrawberry\nObsession\n(Scrat Style)"),
        ("docs/assets/images/sugar-gliders/sugar-glider-logo-minimal.png", "🦎🍓\nMinimal\nLogo"),
    ]
    
    # Blog post images
    blog_images = [
        # Curioshelf
        ("docs/assets/images/blog/curioshelf-interface.png", "🖥️\nCurioshelf\nInterface\n(Asset Manager)"),
        ("docs/assets/images/blog/asset-chaos.png", "📁\nAsset Chaos\n(Unorganized Files)"),
        ("docs/assets/images/blog/curioshelf-development.png", "💻\nDevelopment\nProcess\n(Testing & Debugging)"),
        ("docs/assets/images/blog/curioshelf-reflection.png", "🤔\nReflection\n(Learning & Growth)"),
        
        # June
        ("docs/assets/images/blog/june-ai-agent.png", "🤖\nJune AI Agent\n(Coding Assistant)"),
        ("docs/assets/images/blog/june-development.png", "💻\nAI Development\n(Collaboration)"),
        ("docs/assets/images/blog/june-testing.png", "🧪\nAI Testing\n(Unique Challenges)"),
        ("docs/assets/images/blog/june-insights.png", "💡\nAI Insights\n(Learning)"),
        
        # Metro
        ("docs/assets/images/blog/metro-city-simulation.png", "🏙️\nMetro City\nSimulation\n(Urban Development)"),
        ("docs/assets/images/blog/metro-migration.png", "🔄\nJava to Python\nMigration\n(Modernization)"),
        ("docs/assets/images/blog/metro-evolution.png", "⏰\nTemporal Evolution\n(Timeline)"),
        ("docs/assets/images/blog/metro-reflection.png", "🤔\nCity Complexity\nReflection"),
        
        # Dark Closet
        ("docs/assets/images/blog/dark-closet-game.png", "🎮\nDark Closet\nPinocchio\nPlatformer"),
        ("docs/assets/images/blog/dark-closet-procedural.png", "🎲\nProcedural\nGeneration\n(Sprites)"),
        ("docs/assets/images/blog/dark-closet-callbacks.png", "⚙️\nCallback System\n(Brick Breaking)"),
        
        # Trouble
        ("docs/assets/images/blog/trouble-cli.png", "💻\nTrouble CLI\n(Documentation)"),
        ("docs/assets/images/blog/trouble-development.png", "🤖\nAI Collaboration\n(Development)"),
        ("docs/assets/images/blog/trouble-reflection.png", "📚\nDocumentation\nInsights"),
    ]
    
    # Create all images
    for filename, text in sugar_glider_images + blog_images:
        create_placeholder_image(filename, text)
    
    print("\n✅ All placeholder images created!")
    print("These are temporary placeholders until AI-generated images are available.")
    print("You can replace them with actual images when ready.")

if __name__ == "__main__":
    main()
