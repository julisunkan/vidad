# AI Video Ads Generator

## Overview
A web application that allows users to generate professional video advertisements using AI-powered templates, pre-written text prompts, and customizable visual effects. Built with Flask and MoviePy, this tool simplifies video ad creation for businesses of all sizes.

## Features
- **10 Pre-Built Templates**: Corporate, Product Launch, Testimonial, Sale Promotion, Event Announcement, Service Showcase, App Demo, Restaurant Menu, Fashion Collection, and Fitness Program
- **50+ Text Prompts**: Pre-written prompts for various industries and use cases
- **Custom Image Upload**: Support for multiple images per video project
- **Background Music**: Upload custom audio or use default tracks
- **Video Effects**: Fade in/out, zoom, slide transitions, and special image effects
- **Instant Preview**: Preview generated videos before downloading
- **Download Options**: MP4 format with H.264 codec

## Project Architecture

### Backend (Python/Flask)
- **app.py**: Main Flask application with routes for video generation, preview, and download
- **templates.py**: Video template definitions and text prompt library
- **video_generator.py**: Core video composition logic using MoviePy
- **video_effects.py**: Visual effects and transitions implementation

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
- `GEMINI_API_KEY`: (Optional) Google Gemini API for AI enhancements

## Recent Changes
- **2024-11-24**: Initial project setup with 10 templates and 50 prompts
- Implemented complete video generation pipeline with MoviePy
- Created responsive UI with Bootstrap 5
- Added support for image uploads and background music
- Configured Flask workflow for development

## User Preferences
- None documented yet

## Notes
- Video generation can take 10-60 seconds depending on template complexity and number of images
- Maximum upload size: 50MB per request
- Generated videos are stored in the `uploads/` folder
- Temporary files are automatically cleaned up after video generation
