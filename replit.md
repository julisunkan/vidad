# AI Video Ads Generator

## Overview
A web application that allows users to generate professional video advertisements using either template-based generation (MoviePy) or AI-powered generation (OpenAI Sora API). This dual-mode tool simplifies video ad creation for businesses of all sizes with both traditional templates and cutting-edge AI generation.

## Features

### Template-Based Generation
- **10 Pre-Built Templates**: Corporate, Product Launch, Testimonial, Sale Promotion, Event Announcement, Service Showcase, App Demo, Restaurant Menu, Fashion Collection, and Fitness Program
- **50+ Text Prompts**: Pre-written prompts for various industries and use cases
- **Custom Image Upload**: Support for multiple images per video project
- **Background Music**: Upload custom audio or use default tracks with automatic looping
- **Background Color**: Customizable background colors for professional video appearance
- **Text Overlays**: Animated text overlays with customizable timing

### Sora AI Generation
- **Text-to-Video**: Generate videos from text descriptions using OpenAI Sora API
- **Flexible Duration**: 4-20 seconds of video content
- **Multiple Resolutions**: 1280x720 (16:9), 720x1280 (9:16), 1080x1920 (9:16 Full HD)
- **AI-Powered**: Leverages OpenAI's Sora model for photorealistic video generation
- **Status Tracking**: Real-time polling of generation status with timeout handling

### General Features
- **Dual-Mode Interface**: Easy toggle between template-based and AI generation
- **Instant Preview**: Preview generated videos before downloading
- **Download Options**: MP4 format with H.264 codec

## Project Architecture

### Backend (Python/Flask)
- **app.py**: Main Flask application with routes for video generation, preview, download, and Sora integration
- **templates.py**: Video template definitions and text prompt library
- **video_generator.py**: Core video composition logic using MoviePy
- **video_effects.py**: Visual effects and transitions implementation
- **sora_generator.py**: OpenAI Sora API integration with polling and status tracking

### Frontend
- **templates/index.html**: Main UI with Bootstrap 5
- **static/css/style.css**: Custom styling with gradient backgrounds
- **static/js/app.js**: Form handling and AJAX requests

### File Structure
```
/
├── app.py                 # Flask backend
├── templates.py           # Template and prompt definitions
├── video_generator.py     # Video composition engine
├── video_effects.py       # Effects and transitions
├── sora_generator.py      # Sora AI integration
├── templates/
│   └── index.html        # Main UI
├── static/
│   ├── css/
│   │   └── style.css     # Styling
│   └── js/
│       └── app.js        # Frontend logic
├── uploads/              # User uploads and generated videos
└── database/             # Session data (future use)
```

## How to Use

1. **Select a Template**: Choose from 10 professional video templates
2. **Pick a Prompt**: Select from 50+ pre-written prompts or enter custom text
3. **Upload Images**: Add images for your video (number varies by template)
4. **Add Music** (Optional): Upload background music in MP3, WAV, OGG, or M4A format
5. **Generate**: Click "Generate Video" and wait for processing (typically 10-30 seconds)
6. **Preview & Download**: Watch your video and download when ready

## Technology Stack
- **Backend**: Flask (Python 3.11)
- **Video Processing**: MoviePy, Pillow
- **Frontend**: HTML5, Bootstrap 5, Vanilla JavaScript
- **Video Codec**: H.264 (libx264) with AAC audio

## Environment Variables
- `SESSION_SECRET`: Flask session encryption key (configured via Replit Secrets)
- `OPENAI_API_KEY`: OpenAI API key for Sora video generation (required for AI mode)
- `GEMINI_API_KEY`: (Optional) Google Gemini API for AI enhancements

## Recent Changes
- **2024-11-24**: 
  - **Security Fix**: Removed insecure localStorage API key storage, now using Replit Secrets exclusively
  - **Runtime Environment Variables**: API keys are now read from environment at runtime instead of module import time
  - **Updated Settings Page**: Settings now guide users to add API keys via Replit Secrets tab
  - **Enhanced Documentation**: Created API_KEYS_SETUP.md with step-by-step security setup guide
  - **Backend Security**: Modified app.py, sora_generator.py, and replicate_generator.py to only use environment variables
  - **Added OpenAI Sora Integration**: Implemented dual-mode UI for template-based and AI-powered video generation
  - **Created sora_generator.py**: Sora API module with polling, status tracking, and error handling
  - **Updated UI**: Added mode selector to switch between template and Sora generation modes
  - **Enhanced JavaScript**: Added mode switching logic and Sora form handling
  - **Improved Error Handling**: Added validation for malformed JSON in Sora endpoint
  - Completed migration from Replit Agent to Replit environment
  - Fixed MoviePy 2.1.2 compatibility by removing unsupported fade effects
  - Simplified video generation to use background color, images, text overlays, and audio
  - Installed all required packages (Flask, MoviePy, Pillow, NumPy, OpenAI, etc.)
  - Configured Gunicorn workflow for production-ready deployment
  - Set up deployment configuration for autoscale mode
  - Initial project setup with 10 templates and 50 prompts
  - Implemented complete video generation pipeline with MoviePy
  - Created responsive UI with Bootstrap 5
  - Added support for image uploads and background music

## User Preferences
- None documented yet

## Notes
- **Template-Based Generation**: Takes 10-60 seconds depending on template complexity and number of images
- **Sora AI Generation**: Takes 1-5 minutes depending on video duration and complexity
- **Sora API Pricing**: ~$0.10-$0.50 per second of video (requires paid OpenAI subscription with Sora access)
- Maximum upload size: 50MB per request
- Generated videos are stored in the `uploads/` folder
- Temporary files are automatically cleaned up after video generation
