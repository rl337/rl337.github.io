# Replicate API Setup for AI Image Generation

This guide explains how to set up Replicate API for generating AI images for the website.

## Why Replicate?

Since the Midjourney MCP server is experiencing API issues (404 errors on websocket token endpoint), we're using Replicate as an alternative. Replicate provides access to various AI models including Stable Diffusion.

## Setup Steps

### 1. Create a Replicate Account

1. Go to [replicate.com](https://replicate.com)
2. Sign up for a free account
3. Navigate to your account settings

### 2. Get Your API Token

1. Go to [replicate.com/account/api-tokens](https://replicate.com/account/api-tokens)
2. Create a new API token
3. Copy the token (it starts with `r8_`)

### 3. Set Up Environment Variables

Add your Replicate API token to the `env.sh` file:

```bash
# Add this line to env.sh
export REPLICATE_API_TOKEN="r8_your_token_here"
```

### 4. Generate Images

Run the image generation script:

```bash
# Make sure you're in the project directory
cd /Users/rlee/dev/rl337.org

# Source the environment variables
source env.sh

# Run the image generation script in Docker
docker run --rm -v "$(pwd)":/workspace -w /workspace -e REPLICATE_API_TOKEN="$REPLICATE_API_TOKEN" rl337-dev python3 scripts/generate_images_alternative.py
```

## What Gets Generated

The script will generate:

### Sugar Glider Decorative Images (9 images):
- `sugar-glider-logo.png` - Main logo with strawberry obsession
- `sugar-glider-mascot.png` - Friendly mascot
- `sugar-glider-hero.png` - Hero section image
- `sugar-glider-footer.png` - Footer decoration
- `sugar-glider-loading.png` - Loading animation
- `sugar-glider-error.png` - Error page image
- `sugar-glider-success.png` - Success state
- `sugar-glider-strawberry-obsession.png` - Pure obsession scene
- `sugar-glider-logo-minimal.png` - Minimal logo version

### Blog Post Images (17 images):
- **Curioshelf** (4 images): Interface, asset chaos, development, reflection
- **June** (4 images): AI agent, development, testing, insights
- **Metro** (4 images): City simulation, migration, evolution, reflection
- **Dark Closet** (3 images): Game scene, procedural generation, callbacks
- **Trouble** (3 images): CLI tool, development, reflection

## Cost Information

- Replicate offers free credits for new accounts
- Stable Diffusion model costs approximately $0.002 per image
- Total cost for all 26 images: ~$0.05
- Free tier should cover this easily

## Troubleshooting

### Common Issues:

1. **"REPLICATE_API_TOKEN not set"**
   - Make sure you've added the token to `env.sh`
   - Source the file: `source env.sh`

2. **"Error creating prediction"**
   - Check that your API token is valid
   - Ensure you have sufficient credits

3. **Docker issues**
   - Make sure Docker is running
   - Try rebuilding the image: `docker build -t rl337-dev .`

### Getting Help:

- Replicate documentation: [replicate.com/docs](https://replicate.com/docs)
- Check your account usage: [replicate.com/account](https://replicate.com/account)

## Next Steps

After generating images:

1. Review the generated images in the results JSON file
2. Download the images you like
3. Replace the placeholder images in `docs/assets/images/blog/` and `docs/assets/images/sugar-gliders/`
4. Test the website build: `docker run --rm -v "$(pwd)":/workspace -w /workspace rl337-dev /bin/bash -c "cd docs && bundle exec jekyll build"`

## Alternative Options

If Replicate doesn't work, other options include:
- Hugging Face Inference API
- Stability AI API
- DALL-E API (OpenAI)
- Local Stable Diffusion installation

The script can be easily modified to use any of these alternatives.
