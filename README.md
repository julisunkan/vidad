# 🎬 AI Video Ads Generator

A powerful web application that generates professional video advertisements using AI-powered templates, pre-written text prompts, and customizable visual effects.

## ✨ Features

- **10 Professional Templates**: Choose from Corporate Introduction, Product Launch, Testimonial, Sale Promotion, Event Announcement, Service Showcase, App Demo, Restaurant Menu, Fashion Collection, and Fitness Program
- **50+ Text Prompts**: Pre-written prompts covering various industries and use cases
- **Custom Image Upload**: Add multiple images per video (varies by template)
- **Background Music**: Upload custom audio tracks in MP3, WAV, OGG, or M4A formats
- **Visual Effects**: Fade in/out, zoom, slide transitions, and special image effects
- **Instant Preview**: Watch your video before downloading
- **One-Click Download**: Get your video in MP4 format with H.264 codec

## 🚀 Getting Started

### Prerequisites

**For AI Video Generation (Optional)**:
- You'll need API keys from OpenAI or Replicate
- See [API_KEYS_SETUP.md](API_KEYS_SETUP.md) for detailed setup instructions
- Template-based generation works WITHOUT any API keys

### How to Use

#### Template-Based Video Generation (No API Keys Required)
1. **Select a Template**: Choose from 10 professionally designed video templates
2. **Pick a Prompt**: Select from 50+ pre-written prompts or leave blank for defaults
3. **Add Custom Text**: Enter your business name, product name, etc. to personalize the video
4. **Upload Images**: Add images for your video (number depends on the template)
5. **Add Music** (Optional): Upload background music to enhance your video
6. **Generate**: Click "Generate Video" and wait 10-30 seconds for processing
7. **Preview & Download**: Watch your video and download when ready

#### AI Video Generation (Requires API Keys)
1. **Setup API Keys**: Follow instructions in [API_KEYS_SETUP.md](API_KEYS_SETUP.md)
2. **Select AI Mode**: Choose "Sora AI Generation" mode
3. **Pick Provider**: OpenAI Sora (high quality) or Replicate (budget-friendly)
4. **Describe Your Video**: Write a detailed description
5. **Generate**: Wait 1-5 minutes for AI to create your video
6. **Download**: Get your AI-generated video

### Template Details

Each template has:
- Predefined duration (8-15 seconds)
- Specific number of image slots
- Custom text overlays with timing
- Unique transition effects
- Professional color scheme

## 🛠️ Technology Stack

- **Backend**: Flask (Python 3.11)
- **Video Processing**: MoviePy 2.1.2, Pillow
- **Frontend**: HTML5, Bootstrap 5, Vanilla JavaScript
- **Video Codec**: H.264 (libx264) with AAC audio

## 📋 Requirements

- Python 3.11+
- Flask
- MoviePy
- Pillow
- FFmpeg (installed automatically with MoviePy)

## 🎨 Available Templates

1. **Corporate Introduction** - Professional business introduction (2 images)
2. **Product Launch** - Exciting product announcement (3 images)
3. **Testimonial Video** - Customer success stories (2 images)
4. **Sale Promotion** - Special offers and discounts (2 images)
5. **Event Announcement** - Conference and seminar promotion (2 images)
6. **Service Showcase** - Professional service highlights (3 images)
7. **App Demo** - Mobile/web app showcase (4 images)
8. **Restaurant Menu** - Food and dining showcase (3 images)
9. **Fashion Collection** - Fashion line display (4 images)
10. **Fitness Program** - Health and fitness promotion (2 images)

## 💡 Tips

- **Image Quality**: Use high-resolution images (recommended: 1920x1080 or higher)
- **File Size**: Maximum upload size is 50MB per request
- **Music**: Audio will automatically loop to match video duration
- **Text Customization**: Use the custom text field to replace placeholders like [Business Name], [Product Name]
- **Processing Time**: Video generation typically takes 10-60 seconds depending on complexity

## 🤖 AI Features

### OpenAI Sora
- High-quality AI video generation
- Cost: ~$0.10-$0.50 per second
- Best for professional, high-quality ads

### Replicate (Stable Video Diffusion)
- Budget-friendly AI generation
- Cost: ~$0.006 per second
- Free tier with $5 credits
- Great for testing and prototypes

### Security
🔒 **API keys are securely managed using Replit Secrets** - they never touch your browser and are encrypted server-side.

## 🔧 Advanced Features (Coming Soon)

- Advanced image disintegration/reintegration particle effects
- Custom font selection
- Video length customization
- Batch video generation
- User accounts with project history

## 📝 Notes

- Generated videos are stored temporarily and can be downloaded immediately
- Temporary files are automatically cleaned up after generation
- The app runs in debug mode - use a production WSGI server for deployment

## 🤝 Support

For issues or questions, please check the application logs or contact support.

---

**Enjoy creating professional video ads in minutes!** 🎉
