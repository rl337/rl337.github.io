# Midjourney MCP Setup Guide

This guide will help you set up the Midjourney MCP server to generate AI images for your blog posts.

## Prerequisites

1. **Midjourney Account**: You need an active Midjourney subscription
2. **Authentication Tokens**: You need to extract your authentication tokens from Midjourney

## Step 1: Get Your Midjourney Tokens

To get your authentication tokens:

1. **Open your browser** and go to [midjourney.com](https://midjourney.com)
2. **Log in** to your Midjourney account
3. **Open Developer Tools** (F12 or right-click → Inspect)
4. **Go to the Network tab**
5. **Refresh the page** or navigate around the site
6. **Look for requests** to `midjourney.com` or `www.midjourney.com`
7. **Find a request** that includes cookies in the headers
8. **Look for these cookies**:
   - `__Host-Midjourney.AuthUserTokenV3_r`
   - `__Host-Midjourney.AuthUserTokenV3_i`

## Step 2: Set Environment Variables

Once you have your tokens, set them as environment variables:

```bash
export TOKEN_R="your_token_r_value_here"
export TOKEN_I="your_token_i_value_here"
```

## Step 3: Run the Image Generation Script

Run the script in the Docker container:

```bash
# Run the image generation script
docker run --rm \
  -v "$(pwd)":/workspace \
  -w /workspace \
  -e TOKEN_R="$TOKEN_R" \
  -e TOKEN_I="$TOKEN_I" \
  rl337-dev \
  python3 scripts/generate_blog_images.py
```

## Step 4: Review and Download Images

The script will generate images for all blog posts:

- **Curioshelf**: 4 images (interface, chaos, development, reflection)
- **June**: 4 images (AI agent, development, testing, insights)
- **Metro**: 4 images (city simulation, migration, evolution, reflection)
- **The Dark Closet**: 3 images (game, procedural, callbacks)
- **Trouble**: 3 images (CLI, development, reflection)

## Step 5: Replace Placeholder Images

1. **Download the generated images** from the Midjourney results
2. **Replace the placeholder images** in `docs/assets/images/blog/`
3. **Update the blog posts** if needed

## Troubleshooting

### Common Issues

1. **"Authentication tokens not set"**
   - Make sure you've set both `TOKEN_R` and `TOKEN_I` environment variables
   - Check that the tokens are correct and not expired

2. **"Failed to get websocket token"**
   - Your tokens might be expired or incorrect
   - Try getting fresh tokens from Midjourney

3. **"No success status received"**
   - The image generation might have failed
   - Check your Midjourney account status and credits

### Getting Fresh Tokens

If your tokens expire:

1. **Clear your browser cookies** for midjourney.com
2. **Log out and log back in** to Midjourney
3. **Follow Step 1** to get fresh tokens
4. **Update your environment variables**

## Cost Considerations

- **Midjourney charges per image generation**
- **Each blog post has 3-4 images** (18 total images)
- **Consider generating images in batches** to manage costs
- **You can modify the script** to generate fewer images per post

## Customization

You can modify the image prompts in `scripts/generate_blog_images.py`:

- **Change the prompts** to better match your vision
- **Adjust aspect ratios** (16:9, 1:1, 4:3, etc.)
- **Add or remove images** for specific blog posts
- **Modify the image specifications** as needed

## Next Steps

Once you have the images:

1. **Review the generated images**
2. **Download the ones you like**
3. **Replace the placeholder images**
4. **Test the blog posts** to ensure images display correctly
5. **Commit and push** your changes

The images will make your blog posts much more engaging and professional!
