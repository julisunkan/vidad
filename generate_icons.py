
from PIL import Image, ImageDraw, ImageFont
import os

os.makedirs('static/icons', exist_ok=True)

sizes = [72, 96, 128, 144, 152, 192, 384, 512]

def create_gradient_circle(size):
    """Create a circular gradient background"""
    img = Image.new('RGB', (size, size), color='white')
    draw = ImageDraw.Draw(img)
    
    # Create gradient from purple to blue
    for i in range(size):
        # Calculate gradient color
        ratio = i / size
        r = int(102 + (103 - 102) * ratio)  # 102 -> 103 (purple to blue)
        g = int(126 + (110 - 126) * ratio)  # 126 -> 110
        b = int(234 + (234 - 234) * ratio)  # 234 -> 234
        
        color = (r, g, b)
        draw.rectangle([(0, i), (size, i + 1)], fill=color)
    
    # Create circular mask
    mask = Image.new('L', (size, size), 0)
    mask_draw = ImageDraw.Draw(mask)
    mask_draw.ellipse([0, 0, size, size], fill=255)
    
    # Apply mask
    output = Image.new('RGB', (size, size), (255, 255, 255))
    output.paste(img, (0, 0), mask)
    
    return output

def draw_video_camera(draw, size):
    """Draw a modern video camera icon"""
    # Scale factor for the icon elements
    scale = size / 512
    
    # Camera body (rounded rectangle)
    body_left = int(120 * scale)
    body_top = int(180 * scale)
    body_right = int(320 * scale)
    body_bottom = int(332 * scale)
    body_radius = int(20 * scale)
    
    # Draw camera body with rounded corners
    draw.rounded_rectangle(
        [body_left, body_top, body_right, body_bottom],
        radius=body_radius,
        fill='white'
    )
    
    # Lens (circle)
    lens_center_x = int(200 * scale)
    lens_center_y = int(240 * scale)
    lens_radius = int(40 * scale)
    
    draw.ellipse(
        [lens_center_x - lens_radius, lens_center_y - lens_radius,
         lens_center_x + lens_radius, lens_center_y + lens_radius],
        fill=(200, 200, 255)
    )
    
    # Inner lens detail
    inner_radius = int(25 * scale)
    draw.ellipse(
        [lens_center_x - inner_radius, lens_center_y - inner_radius,
         lens_center_x + inner_radius, lens_center_y + inner_radius],
        fill=(150, 150, 220)
    )
    
    # Record button (small red circle)
    record_x = int(280 * scale)
    record_y = int(200 * scale)
    record_radius = int(12 * scale)
    
    draw.ellipse(
        [record_x - record_radius, record_y - record_radius,
         record_x + record_radius, record_y + record_radius],
        fill=(255, 80, 80)
    )
    
    # Viewfinder triangle (play button shape)
    triangle_points = [
        (int(340 * scale), int(220 * scale)),
        (int(400 * scale), int(256 * scale)),
        (int(340 * scale), int(292 * scale))
    ]
    draw.polygon(triangle_points, fill='white')
    
    # Microphone lines (top of camera)
    mic_x = int(160 * scale)
    mic_y_start = int(195 * scale)
    mic_spacing = int(8 * scale)
    mic_width = int(3 * scale)
    mic_height = int(15 * scale)
    
    for i in range(3):
        x = mic_x + (i * mic_spacing)
        draw.rectangle(
            [x, mic_y_start, x + mic_width, mic_y_start + mic_height],
            fill=(220, 220, 255)
        )

for size in sizes:
    # Create gradient background
    img = create_gradient_circle(size)
    draw = ImageDraw.Draw(img)
    
    # Draw video camera icon
    draw_video_camera(draw, size)
    
    # Add sparkle effect for larger icons
    if size >= 192:
        sparkle_size = int(size * 0.03)
        sparkles = [
            (int(size * 0.15), int(size * 0.15)),
            (int(size * 0.85), int(size * 0.2)),
            (int(size * 0.2), int(size * 0.8)),
            (int(size * 0.8), int(size * 0.85))
        ]
        
        for sx, sy in sparkles:
            draw.ellipse(
                [sx - sparkle_size, sy - sparkle_size,
                 sx + sparkle_size, sy + sparkle_size],
                fill=(255, 255, 255, 200)
            )
    
    # Save the icon
    img.save(f'static/icons/icon-{size}x{size}.png')
    print(f'Generated icon-{size}x{size}.png')

print('All beautiful gradient icons generated successfully!')
