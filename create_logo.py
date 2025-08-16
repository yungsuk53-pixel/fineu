#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
FINEU 로고 이미지 개선 스크립트
"""

from PIL import Image, ImageDraw, ImageFont
import os

def create_logo_image():
    """FINEU 로고가 포함된 상단 이미지 생성"""
    width, height = 1125, 400
    
    # 그라데이션 배경 생성
    image = Image.new('RGB', (width, height))
    draw = ImageDraw.Draw(image)
    
    # 보라색-파란색 그라데이션
    color1 = (102, 126, 234)  # 밝은 파란색
    color2 = (118, 75, 162)   # 보라색
    
    for i in range(height):
        ratio = i / height
        r = int(color1[0] * (1 - ratio) + color2[0] * ratio)
        g = int(color1[1] * (1 - ratio) + color2[1] * ratio)
        b = int(color1[2] * (1 - ratio) + color2[2] * ratio)
        draw.rectangle([(0, i), (width, i+1)], fill=(r, g, b))
    
    # FINEU 로고 텍스트 추가
    try:
        # 큰 폰트 시도
        font_large = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 80)
        font_small = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 24)
    except:
        # 기본 폰트 사용
        font_large = ImageFont.load_default()
        font_small = ImageFont.load_default()
    
    # FINEU 텍스트
    main_text = "FINE U"
    sub_text = "금융 교육의 새로운 시작"
    
    # 메인 텍스트 위치 계산
    main_bbox = draw.textbbox((0, 0), main_text, font=font_large)
    main_width = main_bbox[2] - main_bbox[0]
    main_height = main_bbox[3] - main_bbox[1]
    
    main_x = (width - main_width) // 2
    main_y = (height - main_height) // 2 - 30
    
    # 서브 텍스트 위치 계산
    sub_bbox = draw.textbbox((0, 0), sub_text, font=font_small)
    sub_width = sub_bbox[2] - sub_bbox[0]
    
    sub_x = (width - sub_width) // 2
    sub_y = main_y + main_height + 20
    
    # 텍스트 그림자 효과
    shadow_offset = 3
    draw.text((main_x + shadow_offset, main_y + shadow_offset), main_text, 
              fill=(0, 0, 0, 100), font=font_large)
    draw.text((sub_x + shadow_offset, sub_y + shadow_offset), sub_text, 
              fill=(0, 0, 0, 100), font=font_small)
    
    # 메인 텍스트
    draw.text((main_x, main_y), main_text, fill=(255, 255, 255), font=font_large)
    draw.text((sub_x, sub_y), sub_text, fill=(255, 255, 255, 200), font=font_small)
    
    # 장식적 요소 추가 (별 모양)
    star_size = 15
    for i in range(3):
        star_x = main_x - 50 + (i * 25)
        star_y = main_y - 40
        draw.polygon([
            (star_x, star_y - star_size),
            (star_x + star_size//3, star_y - star_size//3),
            (star_x + star_size, star_y),
            (star_x + star_size//3, star_y + star_size//3),
            (star_x, star_y + star_size),
            (star_x - star_size//3, star_y + star_size//3),
            (star_x - star_size, star_y),
            (star_x - star_size//3, star_y - star_size//3)
        ], fill=(255, 215, 0, 180))
    
    image.save('/workspaces/fineu/images/FINEU-복사_01.png', 'PNG')
    print("개선된 로고 이미지 생성 완료!")

if __name__ == "__main__":
    create_logo_image()
