import os
import time
from openai import OpenAI

def generate_video_with_sora(prompt, duration=8, size="1280x720", output_path="output.mp4"):
    """
    Generate a video using OpenAI's Sora API
    
    Args:
        prompt (str): Text description of the video to generate
        duration (int): Video duration in seconds (4, 8, or 12)
        size (str): Video resolution ("720x1280", "1280x720", "1080x1920")
        output_path (str): Path to save the generated video
    
    Returns:
        dict: Result with status and video path or error message
    """
    openai_api_key = os.environ.get("OPENAI_API_KEY")
    if not openai_api_key:
        return {
            'success': False,
            'error': 'OPENAI_API_KEY not found. Please add your OpenAI API key in Secrets.'
        }
    
    try:
        # Validate and convert duration to allowed string values
        allowed_durations = ['4', '8', '12']
        if isinstance(duration, int):
            # Map any duration to nearest allowed value
            if duration <= 4:
                duration_str = '4'
            elif duration <= 8:
                duration_str = '8'
            else:
                duration_str = '12'
        else:
            duration_str = str(duration)
        
        if duration_str not in allowed_durations:
            duration_str = '8'  # Default to 8 if invalid
        
        client = OpenAI(api_key=openai_api_key)
        
        print(f"Creating Sora video generation job...")
        print(f"Prompt: {prompt}")
        print(f"Duration: {duration_str}s, Size: {size}")
        
        # Create video generation job
        video = client.videos.create(
            model="sora-2",
            prompt=prompt,
            size=size,
            seconds=duration_str
        )
        
        print(f"Video ID: {video.id}")
        print(f"Initial Status: {video.status}")
        
        # Poll for completion
        max_wait_time = 300  # 5 minutes max
        start_time = time.time()
        
        while video.status in ["queued", "in_progress"]:
            if time.time() - start_time > max_wait_time:
                return {
                    'success': False,
                    'error': 'Video generation timed out after 5 minutes'
                }
            
            time.sleep(10)
            video = client.videos.retrieve(video.id)
            progress = getattr(video, 'progress', 0)
            print(f"Progress: {progress}% - Status: {video.status}")
        
        if video.status == "completed":
            # Download the video
            print("Downloading generated video...")
            video_data = client.videos.download(video.id)
            
            with open(output_path, "wb") as f:
                f.write(video_data)
            
            print(f"Video saved to {output_path}")
            
            return {
                'success': True,
                'video_path': output_path,
                'video_id': video.id
            }
        else:
            error_msg = getattr(video, 'error', 'Unknown error')
            return {
                'success': False,
                'error': f"Video generation failed: {error_msg}"
            }
    
    except Exception as e:
        error_message = str(e)
        
        # Handle common errors
        if "organization must be verified" in error_message.lower():
            return {
                'success': False,
                'error': 'Your OpenAI organization needs verification. Visit platform.openai.com/settings/organization/general'
            }
        elif "rate_limit" in error_message.lower():
            return {
                'success': False,
                'error': 'Rate limit exceeded. Please wait and try again.'
            }
        elif "insufficient_quota" in error_message.lower():
            return {
                'success': False,
                'error': 'Insufficient API credits. Please check your OpenAI account balance.'
            }
        elif "invalid_api_key" in error_message.lower():
            return {
                'success': False,
                'error': 'Invalid API key. Please check your OPENAI_API_KEY in Secrets.'
            }
        else:
            return {
                'success': False,
                'error': f'Sora API error: {error_message}'
            }


def generate_video_with_image(prompt, image_path, duration=8, size="1280x720", output_path="output.mp4"):
    """
    Generate a video from an image using OpenAI's Sora API (Image-to-Video)
    
    Args:
        prompt (str): Text description of how the image should animate
        image_path (str): Path to the input image
        duration (int): Video duration in seconds (4, 8, or 12)
        size (str): Video resolution
        output_path (str): Path to save the generated video
    
    Returns:
        dict: Result with status and video path or error message
    """
    openai_api_key = os.environ.get("OPENAI_API_KEY")
    if not openai_api_key:
        return {
            'success': False,
            'error': 'OPENAI_API_KEY not found. Please add your OpenAI API key in Secrets.'
        }
    
    try:
        # Validate and convert duration to allowed string values
        allowed_durations = ['4', '8', '12']
        if isinstance(duration, int):
            if duration <= 4:
                duration_str = '4'
            elif duration <= 8:
                duration_str = '8'
            else:
                duration_str = '12'
        else:
            duration_str = str(duration)
        
        if duration_str not in allowed_durations:
            duration_str = '8'
        
        client = OpenAI(api_key=openai_api_key)
        
        print(f"Creating Sora image-to-video job...")
        print(f"Image: {image_path}")
        print(f"Prompt: {prompt}")
        print(f"Duration: {duration_str}s")
        
        with open(image_path, "rb") as img_file:
            video = client.videos.create(
                model="sora-2",
                prompt=prompt,
                size=size,
                seconds=duration_str,
                input_reference=img_file
            )
        
        print(f"Video ID: {video.id}")
        
        # Poll for completion
        max_wait_time = 300
        start_time = time.time()
        
        while video.status in ["queued", "in_progress"]:
            if time.time() - start_time > max_wait_time:
                return {
                    'success': False,
                    'error': 'Video generation timed out'
                }
            
            time.sleep(10)
            video = client.videos.retrieve(video.id)
            progress = getattr(video, 'progress', 0)
            print(f"Progress: {progress}% - Status: {video.status}")
        
        if video.status == "completed":
            video_data = client.videos.download(video.id)
            
            with open(output_path, "wb") as f:
                f.write(video_data)
            
            return {
                'success': True,
                'video_path': output_path,
                'video_id': video.id
            }
        else:
            error_msg = getattr(video, 'error', 'Unknown error')
            return {
                'success': False,
                'error': f"Video generation failed: {error_msg}"
            }
    
    except Exception as e:
        return {
            'success': False,
            'error': f'Sora API error: {str(e)}'
        }
