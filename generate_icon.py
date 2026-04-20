from PIL import Image, ImageDraw, ImageFont
import os

def create_icon(size, output_path):
    img = Image.new('RGB', (size, size), (102, 126, 234))
    draw = ImageDraw.Draw(img)
    
    center = size // 2
    margin = size // 5
    icon_size = size - margin * 2
    
    draw.rounded_rectangle(
        [(margin, margin), (size - margin, size - margin)],
        radius=size // 10,
        fill=(118, 75, 162)
    )
    
    draw.rectangle(
        [(center - icon_size // 6, center - icon_size // 3), 
         (center + icon_size // 6, center + icon_size // 3)],
        fill=(255, 255, 255)
    )
    
    draw.rectangle(
        [(center - icon_size // 3, center - icon_size // 6), 
         (center + icon_size // 3, center + icon_size // 6)],
        fill=(255, 255, 255)
    )
    
    img.save(output_path, 'PNG')
    print(f'已创建 {output_path}')

try:
    create_icon(192, 'icon-192.png')
    create_icon(512, 'icon-512.png')
    print('图标创建成功！')
except ImportError:
    print('PIL库未安装，正在安装...')
    import subprocess
    import sys
    subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'Pillow'])
    create_icon(192, 'icon-192.png')
    create_icon(512, 'icon-512.png')
    print('图标创建成功！')
