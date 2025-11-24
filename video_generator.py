from moviepy import ImageClip, TextClip, CompositeVideoClip, concatenate_videoclips, AudioFileClip, ColorClip
from PIL import Image, ImageDraw, ImageFont
import numpy as np
import os
from video_effects import (
    create_text_clip, apply_fade_in, apply_fade_out, 
    create_background_clip, apply_disintegrate_effect, apply_reintegrate_effect
)

def generate_video(template, images, text_overlays, audio_file, output_path):
    video_size = (1280, 720)
    duration = template['duration']
    bg_color = template.get('bg_color', (30, 60, 114))
    
    background = create_background_clip(duration, video_size, bg_color)
    
    clips = [background]
    
    if images:
        images_per_slot = len(images)
        slot_duration = duration / max(images_per_slot, 1)
        
        for i, img_path in enumerate(images):
            start_time = i * slot_duration
            img_duration = min(slot_duration, duration - start_time)
            
            if img_duration <= 0:
                continue
            
            try:
                img_clip = ImageClip(img_path, duration=img_duration)
                img_clip = img_clip.resize(height=video_size[1] * 0.6)
                
                if img_clip.w > video_size[0]:
                    img_clip = img_clip.resize(width=video_size[0] * 0.8)
                
                img_clip = img_clip.set_position('center').set_start(start_time)
                
                effects = template.get('effects', [])
                if i < len(effects):
                    effect = effects[i % len(effects)]
                    if effect == 'disintegrate' and i == 0:
                        img_clip = apply_fade_out(img_clip, 1)
                    elif effect == 'reintegrate':
                        img_clip = apply_fade_in(img_clip, 1)
                    else:
                        img_clip = apply_fade_in(img_clip, 0.5)
                        img_clip = apply_fade_out(img_clip, 0.5)
                else:
                    img_clip = apply_fade_in(img_clip, 0.5)
                    img_clip = apply_fade_out(img_clip, 0.5)
                
                clips.append(img_clip)
            except Exception as e:
                print(f"Error processing image {img_path}: {e}")
                continue
    
    for overlay in text_overlays:
        try:
            text = overlay['text']
            start = overlay['start']
            text_duration = overlay['duration']
            
            if start + text_duration > duration:
                text_duration = duration - start
            
            if text_duration <= 0:
                continue
            
            text_clip = create_text_clip(
                text, 
                text_duration, 
                size=video_size,
                fontsize=50,
                color='white',
                bg_color=(0, 0, 0, 0)
            )
            
            text_clip = text_clip.set_position('center').set_start(start)
            text_clip = apply_fade_in(text_clip, 0.3)
            text_clip = apply_fade_out(text_clip, 0.3)
            
            clips.append(text_clip)
        except Exception as e:
            print(f"Error creating text overlay: {e}")
            continue
    
    try:
        final_video = CompositeVideoClip(clips, size=video_size)
        final_video = final_video.set_duration(duration)
        
        if audio_file and os.path.exists(audio_file):
            try:
                audio = AudioFileClip(audio_file)
                if audio.duration > duration:
                    audio = audio.subclip(0, duration)
                elif audio.duration < duration:
                    loops = int(duration / audio.duration) + 1
                    audio = concatenate_audioclips([audio] * loops).subclip(0, duration)
                
                final_video = final_video.set_audio(audio)
            except Exception as e:
                print(f"Error adding audio: {e}")
        
        final_video.write_videofile(
            output_path,
            fps=24,
            codec='libx264',
            audio_codec='aac',
            temp_audiofile='uploads/temp-audio.m4a',
            remove_temp=True,
            logger=None
        )
        
        for clip in clips:
            clip.close()
        if audio_file and os.path.exists(audio_file):
            try:
                audio.close()
            except:
                pass
        
        temp_files = [f for f in os.listdir('uploads') if f.startswith('temp_')]
        for temp_file in temp_files:
            try:
                os.remove(os.path.join('uploads', temp_file))
            except:
                pass
                
    except Exception as e:
        print(f"Error generating final video: {e}")
        raise

def concatenate_audioclips(clips):
    from moviepy.audio.AudioClip import CompositeAudioClip
    if not clips:
        return None
    
    current_time = 0
    positioned_clips = []
    for clip in clips:
        positioned_clips.append(clip.set_start(current_time))
        current_time += clip.duration
    
    return CompositeAudioClip(positioned_clips)
