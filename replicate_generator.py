
import os
import time
import replicate

REPLICATE_API_KEY = os.environ.get("REPLICATE_API_KEY")

def generate_video_with_replicate(prompt, duration=4, size="1280x720", output_path="output.mp4", api_key=None):
    """
    Generate a video using Replicate's Stable Video Diffusion
    
    Args:
        prompt (str): Text description of the video to generate
        duration (int): Video duration in seconds (2-4 recommended)
        size (str): Video resolution
        output_path (str): Path to save the generated video
        api_key (str): Replicate API key (optional)
    
    Returns:
        dict: Result with status and video path or error message
    """
    api_key_to_use = api_key or REPLICATE_API_KEY
    if not api_key_to_use:
        return {
            'success': False,
            'error': 'REPLICATE_API_KEY not found. Please add your Replicate API key in Secrets.'
        }
    
    try:
        os.environ["REPLICATE_API_TOKEN"] = api_key_to_use
        
        # Map size to aspect ratio
        width, height = map(int, size.split('x'))
        aspect_ratio = f"{width}:{height}"
        
        print(f"Creating Replicate video generation job...")
        print(f"Prompt: {prompt}")
        print(f"Duration: {duration}s, Size: {size}")
        
        # Use Stable Video Diffusion model
        output = replicate.run(
            "stability-ai/stable-video-diffusion:3f0457e4619daac51203dedb472816fd4af51f3149fa7a9e0b5ffcf1b8172438",
            input={
                "input_image": None,  # Text-to-video mode
                "prompt": prompt,
                "fps": 24,
                "motion_bucket_id": 127,
                "cond_aug": 0.02,
                "decoding_t": 14,
                "video_length": min(duration * 24, 96)  # Max 96 frames (4 seconds at 24fps)
            }
        )
        
        # Download the video
        if output:
            print("Downloading generated video...")
            import urllib.request
            urllib.request.urlretrieve(output, output_path)
            
            print(f"Video saved to {output_path}")
            
            return {
                'success': True,
                'video_path': output_path
            }
        else:
            return {
                'success': False,
                'error': 'No output received from Replicate'
            }
    
    except Exception as e:
        error_message = str(e)
        
        if "invalid_api_key" in error_message.lower() or "authentication" in error_message.lower():
            return {
                'success': False,
                'error': 'Invalid Replicate API key. Get one free at replicate.com'
            }
        elif "rate_limit" in error_message.lower():
            return {
                'success': False,
                'error': 'Rate limit exceeded. Please wait and try again.'
            }
        elif "insufficient" in error_message.lower():
            return {
                'success': False,
                'error': 'Insufficient credits. Visit replicate.com to add credits.'
            }
        else:
            return {
                'success': False,
                'error': f'Replicate API error: {error_message}'
            }


def generate_video_with_replicate_img2vid(prompt, image_path, duration=4, output_path="output.mp4"):
    """
    Generate a video from an image using Replicate's Stable Video Diffusion
    
    Args:
        prompt (str): Optional text guidance
        image_path (str): Path to the input image
        duration (int): Video duration in seconds (2-4)
        output_path (str): Path to save the generated video
    
    Returns:
        dict: Result with status and video path or error message
    """
    if not REPLICATE_API_KEY:
        return {
            'success': False,
            'error': 'REPLICATE_API_KEY not found. Please add your Replicate API key in Secrets.'
        }
    
    try:
        os.environ["REPLICATE_API_TOKEN"] = REPLICATE_API_KEY
        
        print(f"Creating Replicate image-to-video job...")
        print(f"Image: {image_path}")
        
        with open(image_path, "rb") as img_file:
            output = replicate.run(
                "stability-ai/stable-video-diffusion:3f0457e4619daac51203dedb472816fd4af51f3149fa7a9e0b5ffcf1b8172438",
                input={
                    "input_image": img_file,
                    "fps": 24,
                    "motion_bucket_id": 127,
                    "cond_aug": 0.02,
                    "decoding_t": 14,
                    "video_length": min(duration * 24, 96)
                }
            )
        
        if output:
            import urllib.request
            urllib.request.urlretrieve(output, output_path)
            
            return {
                'success': True,
                'video_path': output_path
            }
        else:
            return {
                'success': False,
                'error': 'No output received from Replicate'
            }
    
    except Exception as e:
        return {
            'success': False,
            'error': f'Replicate API error: {str(e)}'
        }
