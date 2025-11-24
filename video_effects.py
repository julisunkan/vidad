from moviepy.editor import ImageClip, TextClip, CompositeVideoClip, concatenate_videoclips, AudioFileClip
from PIL import Image, ImageDraw, ImageFont
import numpy as np
import os

def create_text_clip(text, duration, size=(1280, 720), fontsize=60, color='white', bg_color=(0, 0, 0)):
    img = Image.new('RGB', size, color=bg_color)
    draw = ImageDraw.Draw(img)
    
    try:
        font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", fontsize)
    except:
        font = ImageFont.load_default()
    
    bbox = draw.textbbox((0, 0), text, font=font)
    text_width = bbox[2] - bbox[0]
    text_height = bbox[3] - bbox[1]
    
    position = ((size[0] - text_width) // 2, (size[1] - text_height) // 2)
    draw.text(position, text, fill=color, font=font)
    
    temp_path = f"uploads/temp_text_{hash(text)}.png"
    img.save(temp_path)
    
    clip = ImageClip(temp_path, duration=duration)
    return clip

def apply_fade_in(clip, duration=1):
    return clip.fadein(duration)

def apply_fade_out(clip, duration=1):
    return clip.fadeout(duration)

def apply_zoom_effect(clip, zoom_factor=1.5):
    def zoom(t):
        scale = 1 + (zoom_factor - 1) * (t / clip.duration)
        return clip.resize(scale).set_position('center')
    
    return clip.fl(lambda gf, t: zoom(t).get_frame(t), apply_to=[])

def apply_slide_effect(clip, direction='right'):
    w, h = clip.size
    
    if direction == 'right':
        return clip.set_position(lambda t: (int(-w + w * t / clip.duration), 'center'))
    elif direction == 'left':
        return clip.set_position(lambda t: (int(w - w * t / clip.duration), 'center'))
    elif direction == 'down':
        return clip.set_position(lambda t: ('center', int(-h + h * t / clip.duration)))
    else:
        return clip.set_position(lambda t: ('center', int(h - h * t / clip.duration)))

def apply_disintegrate_effect(image_path, duration=3, size=(1280, 720)):
    clip = ImageClip(image_path, duration=duration).resize(size)
    
    def disintegrate(t):
        progress = t / duration
        opacity = 1 - progress
        scale = 1 - (progress * 0.5)
        rotation = progress * 45
        
        frame = clip.get_frame(0)
        rotated = clip.resize(scale).rotate(rotation).set_opacity(opacity)
        return rotated.get_frame(t)
    
    return clip.fl(lambda gf, t: disintegrate(t), apply_to=[])

def apply_reintegrate_effect(image_path, duration=3, size=(1280, 720)):
    clip = ImageClip(image_path, duration=duration).resize(size)
    
    def reintegrate(t):
        progress = t / duration
        opacity = progress
        scale = 0.5 + (progress * 0.5)
        rotation = (1 - progress) * 45
        
        frame = clip.get_frame(0)
        transformed = clip.resize(scale).rotate(rotation).set_opacity(opacity)
        return transformed.get_frame(t)
    
    return clip.fl(lambda gf, t: reintegrate(t), apply_to=[])

def create_background_clip(duration, size=(1280, 720), color=(30, 60, 114)):
    img = Image.new('RGB', size, color=color)
    temp_path = f"uploads/temp_bg_{hash(str(color))}.png"
    img.save(temp_path)
    
    clip = ImageClip(temp_path, duration=duration)
    return clip
