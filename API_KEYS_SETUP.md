# 🔑 API Keys Setup Guide

## ⚠️ Important Security Update

**The app now uses Replit Secrets for secure API key management.**  
API keys are NO LONGER stored in your browser - they're managed server-side for maximum security.

---

## How to Add Your API Keys

### Step 1: Open Replit Secrets
1. Look for the **🔐 Secrets** tab in the left sidebar (under Tools section)
2. Click to open the Secrets panel

### Step 2: Add Your API Keys

Add one or both of these secrets depending on which AI provider you want to use:

| Secret Name | Description | Where to Get |
|------------|-------------|--------------|
| `OPENAI_API_KEY` | For OpenAI Sora video generation | [platform.openai.com/api-keys](https://platform.openai.com/api-keys) |
| `REPLICATE_API_KEY` | For Replicate AI generation (budget option) | [replicate.com/account/api-tokens](https://replicate.com/account/api-tokens) |

### Step 3: Save and Test
1. Click "Add new secret" in the Secrets panel
2. Enter the secret name exactly as shown above
3. Paste your API key value
4. The app will detect the new secrets automatically - no restart needed!

---

## 💰 Cost Comparison

### OpenAI Sora
- **Quality:** High-end AI video generation
- **Cost:** ~$0.10-$0.50 per second of video
- **Best for:** Professional, high-quality video ads
- **Requires:** Paid OpenAI account with Sora access

### Replicate (Stable Video Diffusion)
- **Quality:** Good AI video generation
- **Cost:** ~$0.006 per second of video (much cheaper!)
- **Best for:** Budget-friendly video generation, testing
- **Bonus:** Free tier available with $5 credits to start

---

## 🔒 Why This Is Secure

✅ **Server-side storage** - Keys never leave the server  
✅ **Encrypted by Replit** - Industry-standard encryption  
✅ **No XSS vulnerabilities** - Not exposed to browser attacks  
✅ **Best practice** - Recommended way to handle credentials  

---

## ❓ Troubleshooting

### Error: "REPLICATE_API_KEY not found"
→ You haven't added the `REPLICATE_API_KEY` secret yet. Follow Step 2 above.

### Error: "OPENAI_API_KEY not found"
→ You haven't added the `OPENAI_API_KEY` secret yet. Follow Step 2 above.

### Error: "Invalid API key"
→ Check that you copied the entire API key correctly (no extra spaces)

### Video generation fails immediately
→ Your API key might be invalid or expired. Generate a new one from the provider's website.

---

## 📝 Quick Start

1. **Get a free Replicate API key** (recommended for testing):
   - Visit [replicate.com](https://replicate.com)
   - Sign up (free $5 credits)
   - Go to [Account → API Tokens](https://replicate.com/account/api-tokens)
   - Copy your token

2. **Add it to Replit Secrets**:
   - Name: `REPLICATE_API_KEY`
   - Value: (paste your token)

3. **Generate a video**:
   - Select "Sora AI Generation" mode
   - Choose "Replicate SVD" as provider
   - Enter a description and click Generate!

---

## 🎬 Template-Based Videos

Don't need AI generation? You can create videos using pre-built templates without any API keys! Just:
- Select "Template-Based" mode
- Choose a template
- Upload your images
- Generate!
