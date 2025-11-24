from flask import Flask, render_template, request, send_file, jsonify, session
from werkzeug.utils import secure_filename
import os
import uuid
from datetime import datetime
from templates import VIDEO_TEMPLATES, TEXT_PROMPTS
from video_generator import generate_video
from sora_generator import generate_video_with_sora, generate_video_with_image
from replicate_generator import generate_video_with_replicate
import json

app = Flask(__name__)
app.secret_key = os.environ.get("SESSION_SECRET")
app.config['UPLOAD_FOLDER'] = 'uploads'
app.config['MAX_CONTENT_LENGTH'] = 50 * 1024 * 1024
app.config['ALLOWED_IMAGE_EXTENSIONS'] = {'png', 'jpg', 'jpeg', 'gif', 'webp'}
app.config['ALLOWED_AUDIO_EXTENSIONS'] = {'mp3', 'wav', 'ogg', 'm4a'}

os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

def allowed_file(filename, file_type='image'):
    if '.' not in filename:
        return False
    ext = filename.rsplit('.', 1)[1].lower()
    if file_type == 'image':
        return ext in app.config['ALLOWED_IMAGE_EXTENSIONS']
    elif file_type == 'audio':
        return ext in app.config['ALLOWED_AUDIO_EXTENSIONS']
    return False

@app.route('/')
def index():
    return render_template('index.html', 
                         templates=VIDEO_TEMPLATES, 
                         prompts=TEXT_PROMPTS)

@app.route('/settings')
def settings():
    return render_template('settings.html')

@app.route('/save_settings', methods=['POST'])
def save_settings():
    """Save settings to session"""
    try:
        data = request.get_json()
        if not data:
            return jsonify({'error': 'Invalid request'}), 400

        # Store API keys in session (or clear them if empty)
        openai_key = data.get('openai_api_key', '').strip()
        replicate_key = data.get('replicate_api_key', '').strip()
        
        if openai_key:
            session['openai_api_key'] = openai_key
        elif 'openai_api_key' in session:
            session.pop('openai_api_key')
            
        if replicate_key:
            session['replicate_api_key'] = replicate_key
        elif 'replicate_api_key' in session:
            session.pop('replicate_api_key')
        
        session.modified = True
        
        return jsonify({'success': True}), 200
    except Exception as e:
        print(f"Error saving settings: {str(e)}")
        return jsonify({'error': str(e)}), 500

@app.route('/get_settings')
def get_settings():
    """Get settings from session"""
    try:
        return jsonify({
            'openai_api_key': session.get('openai_api_key', ''),
            'replicate_api_key': session.get('replicate_api_key', '')
        }), 200
    except Exception as e:
        print(f"Error getting settings: {str(e)}")
        return jsonify({'error': str(e)}), 500

@app.route('/static/manifest.json')
def manifest():
    return send_file('static/manifest.json', mimetype='application/manifest+json')

@app.route('/static/sw.js')
def service_worker():
    return send_file('static/sw.js', mimetype='application/javascript')

@app.route('/get_template/<int:template_id>')
def get_template(template_id):
    template = next((t for t in VIDEO_TEMPLATES if t['id'] == template_id), None)
    if template:
        return jsonify(template)
    return jsonify({'error': 'Template not found'}), 404

@app.route('/generate_video', methods=['POST'])
def generate_video_route():
    try:
        template_id_str = request.form.get('template_id')
        if not template_id_str:
            return jsonify({'error': 'Template ID is required'}), 400

        template_id = int(template_id_str)
        selected_prompt = request.form.get('text_prompt', '')
        custom_text = request.form.get('custom_text', '')
        background_color = request.form.get('background_color', '#1e3c72')

        # Convert hex color to RGB tuple
        bg_color_hex = background_color.lstrip('#')
        bg_color_rgb = tuple(int(bg_color_hex[i:i+2], 16) for i in (0, 2, 4))

        template = next((t for t in VIDEO_TEMPLATES if t['id'] == template_id), None)
        if not template:
            return jsonify({'error': 'Invalid template selected'}), 400

        uploaded_images = []
        for i in range(template['image_slots']):
            file_key = f'image_{i}'
            if file_key in request.files:
                file = request.files[file_key]
                if file and file.filename and allowed_file(file.filename, 'image'):
                    filename = secure_filename(f"{uuid.uuid4()}_{file.filename}")
                    filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
                    file.save(filepath)
                    uploaded_images.append(filepath)

        audio_file = None
        if 'background_music' in request.files:
            file = request.files['background_music']
            if file and file.filename and allowed_file(file.filename, 'audio'):
                filename = secure_filename(f"{uuid.uuid4()}_{file.filename}")
                filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
                file.save(filepath)
                audio_file = filepath

        text_overlays = []
        for slot in template['text_slots']:
            text = slot['text']
            if '[' in text and ']' in text:
                if custom_text:
                    placeholder = text[text.find('[')+1:text.find(']')]
                    text = text.replace(f'[{placeholder}]', custom_text)
                else:
                    text = text.replace('[Business Name]', 'Your Business')
                    text = text.replace('[Product Name]', 'Product')
                    text = text.replace('[Service Type]', 'Service')
                    text = text.replace('[Event Name]', 'Event')
                    text = text.replace('[App Name]', 'App')
            text_overlays.append({
                'text': text,
                'start': slot['start'],
                'duration': slot['duration']
            })

        video_filename = f"video_{uuid.uuid4()}.mp4"
        video_path = os.path.join(app.config['UPLOAD_FOLDER'], video_filename)

        generate_video(
            template=template,
            images=uploaded_images,
            text_overlays=text_overlays,
            audio_file=audio_file,
            output_path=video_path,
            background_color=bg_color_rgb
        )

        session['last_video'] = video_filename

        return jsonify({
            'success': True,
            'video_url': f'/download_video/{video_filename}',
            'message': 'Video generated successfully!'
        })

    except Exception as e:
        print(f"Error generating video: {str(e)}")
        return jsonify({'error': str(e)}), 500

@app.route('/download_video/<filename>')
def download_video(filename):
    try:
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], secure_filename(filename))
        if os.path.exists(filepath):
            return send_file(filepath, as_attachment=True, download_name=filename)
        return "Video not found", 404
    except Exception as e:
        return str(e), 500

@app.route('/preview_video/<filename>')
def preview_video(filename):
    try:
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], secure_filename(filename))
        if os.path.exists(filepath):
            return send_file(filepath, mimetype='video/mp4')
        return "Video not found", 404
    except Exception as e:
        return str(e), 500

@app.route('/generate_sora_video', methods=['POST'])
def generate_sora_video_route():
    """Generate video using OpenAI Sora or Replicate API"""
    try:
        # Handle JSON request
        if request.is_json:
            data = request.get_json()
        else:
            return jsonify({'error': 'Request must be JSON'}), 400
            
        if not data:
            return jsonify({'error': 'Invalid JSON request body'}), 400

        prompt = data.get('prompt', '').strip()
        if not prompt:
            return jsonify({'error': 'Prompt is required'}), 400

        try:
            duration = int(data.get('duration', 8))
            duration = max(4, min(20, duration))
        except (ValueError, TypeError):
            return jsonify({'error': 'Invalid duration value'}), 400

        size = data.get('size', '1280x720')
        use_image = data.get('use_image', False)
        api_provider = data.get('api_provider', 'sora')

        video_filename = f"{api_provider}_{uuid.uuid4()}.mp4"
        video_path = os.path.join(app.config['UPLOAD_FOLDER'], video_filename)

        # Get session API keys
        session_openai_key = session.get('openai_api_key')
        session_replicate_key = session.get('replicate_api_key')

        print(f"Generating video with {api_provider}")
        print(f"Prompt: {prompt}")
        print(f"Duration: {duration}s, Size: {size}")
        print(f"Session OpenAI key present: {bool(session_openai_key)}")
        print(f"Session Replicate key present: {bool(session_replicate_key)}")

        # Text-to-video generation (no image)
        if api_provider == 'replicate':
            result = generate_video_with_replicate(
                prompt=prompt,
                duration=duration,
                size=size,
                output_path=video_path,
                session_api_key=session_replicate_key
            )
        else:
            result = generate_video_with_sora(
                prompt=prompt,
                duration=duration,
                size=size,
                output_path=video_path,
                session_api_key=session_openai_key
            )

        if result.get('success'):
            session['last_video'] = video_filename
            return jsonify({
                'success': True,
                'video_url': f'/download_video/{video_filename}',
                'video_id': result.get('video_id', ''),
                'message': f'{api_provider.capitalize()} video generated successfully!'
            }), 200
        else:
            error_msg = result.get('error', 'Unknown error occurred')
            print(f"Video generation failed: {error_msg}")
            return jsonify({'error': error_msg}), 400

    except Exception as e:
        error_msg = str(e)
        print(f"Error generating video: {error_msg}")
        import traceback
        traceback.print_exc()
        return jsonify({'error': f'Server error: {error_msg}'}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)