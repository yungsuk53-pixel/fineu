#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
FINEU 로그인 화면용 샘플 이미지 생성 스크립트
"""

from PIL import Image, ImageDraw, ImageFont
import os

def create_gradient_image(width, height, color1, color2, filename):
    """그라데이션 이미지 생성"""
    image = Image.new('RGB', (width, height), color1)
    draw = ImageDraw.Draw(image)
    
    for i in range(height):
        ratio = i / height
        r = int(color1[0] * (1 - ratio) + color2[0] * ratio)
        g = int(color1[1] * (1 - ratio) + color2[1] * ratio)
        b = int(color1[2] * (1 - ratio) + color2[2] * ratio)
        draw.line([(0, i), (width, i)], fill=(r, g, b))
    
    image.save(filename, 'PNG')
    print(f"Created: {filename}")

def create_text_image(width, height, text, bg_color, text_color, filename):
    """텍스트가 포함된 이미지 생성"""
    image = Image.new('RGB', (width, height), bg_color)
    draw = ImageDraw.Draw(image)
    
    # 폰트 크기 조정
    font_size = min(width, height) // 8
    try:
        font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", font_size)
    except:
        font = ImageFont.load_default()
    
    # 텍스트 중앙 정렬
    bbox = draw.textbbox((0, 0), text, font=font)
    text_width = bbox[2] - bbox[0]
    text_height = bbox[3] - bbox[1]
    
    x = (width - text_width) // 2
    y = (height - text_height) // 2
    
    draw.text((x, y), text, fill=text_color, font=font)
    
    image.save(filename, 'PNG')
    print(f"Created: {filename}")

def main():
    # images 디렉토리 생성
    os.makedirs('/workspaces/fineu/images', exist_ok=True)
    
    print("FINEU 로그인 화면용 샘플 이미지 생성 중...")
    
    # 1. 로고 영역 (상단)
    create_gradient_image(1125, 400, (102, 126, 234), (118, 75, 162), 
                         '/workspaces/fineu/images/FINEU-복사_01.png')
    
    # 2. 좌측 배경
    create_gradient_image(243, 600, (229, 231, 235), (209, 213, 219), 
                         '/workspaces/fineu/images/FINEU-복사_02.png')
    
    # 3. 아이디 입력 영역
    create_text_image(640, 89, "아이디를 입력하세요", (240, 147, 251), (255, 255, 255), 
                     '/workspaces/fineu/images/FINEU-복사_03.png')
    
    # 4. 우측 배경
    create_gradient_image(242, 600, (229, 231, 235), (209, 213, 219), 
                         '/workspaces/fineu/images/FINEU-복사_04.png')
    
    # 5. 간격 영역
    create_gradient_image(640, 33, (243, 244, 246), (229, 231, 235), 
                         '/workspaces/fineu/images/FINEU-복사_05.png')
    
    # 6. 비밀번호 입력 영역
    create_text_image(640, 89, "비밀번호를 입력하세요", (251, 191, 36), (255, 255, 255), 
                     '/workspaces/fineu/images/PW.png')
    
    # 7. 간격 영역 2
    create_gradient_image(640, 33, (243, 244, 246), (229, 231, 235), 
                         '/workspaces/fineu/images/FINEU-복사_07.png')
    
    # 8. 로그인 버튼
    create_text_image(640, 89, "로그인", (79, 172, 254), (255, 255, 255), 
                     '/workspaces/fineu/images/FINEU-복사_08.png')
    
    # 9. 하단 영역
    create_gradient_image(640, 583, (67, 233, 123), (56, 249, 215), 
                         '/workspaces/fineu/images/FINEU-복사_09.png')
    
    print("모든 이미지 생성 완료!")

if __name__ == "__main__":
    main()
