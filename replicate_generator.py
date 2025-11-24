import os
import time
import replicate

def generate_video_with_replicate(prompt, duration=8, size="1280x720", output_path="output.mp4", session_api_key=None):
    """
    Generate video using Replicate's Stable Video Diffusion

    Args:
        prompt: Text description for the video
        duration: Video duration in seconds (ignored for SVD, uses ~2-4 seconds)
        size: Video resolution
        output_path: Path where the video will be saved
        session_api_key: Optional API key from session

    Returns:
        dict with 'success', 'video_url', and 'error' keys
    """
    api_key = session_api_key or os.environ.get('REPLICATE_API_KEY')
    if not api_key:
        return {
            'success': False,
            'error': 'REPLICATE_API_KEY not found. Please add your Replicate API key in Secrets or provide it for the session.'
        }

    try:
        os.environ["REPLICATE_API_TOKEN"] = api_key

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
            # Handle both URL string and FileOutput object
            video_url = str(output) if not isinstance(output, str) else output
            urllib.request.urlretrieve(video_url, output_path)

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
    replicate_api_key = os.environ.get("REPLICATE_API_KEY")
    if not replicate_api_key:
        return {
            'success': False,
            'error': 'REPLICATE_API_KEY not found. Please add your Replicate API key in Secrets.'
        }

    try:
        os.environ["REPLICATE_API_TOKEN"] = replicate_api_key

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
            # Handle both URL string and FileOutput object
            video_url = str(output) if not isinstance(output, str) else output
            urllib.request.urlretrieve(video_url, output_path)

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