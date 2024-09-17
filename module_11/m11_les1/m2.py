"""
Библиотека Pillow позволяет работать с изображениями
- создавать новые
- изменять размер, масштаб, цветовую схему и тд
- вставлять текст
- комбинировать изображения
карманный фотошоп
"""
from PIL import Image, ImageDraw, ImageFont


def run():
    img_1 = Image.new('RGB', (500, 500), (235, 205, 135))
    img_2 = Image.new('RGB', (100, 200), (135, 105, 135))
    img_2 = img_2.rotate(45, expand=True, fillcolor=(235, 205, 135))
    img_1.paste(img_2, (0 + img_2.width, 0 + img_2.height))
    draw = ImageDraw.Draw(img_1)
    draw.text((0, 0), 'Wow! Pillow', color=(0, 0, 0), font_size=40)
    img_1.save('pillow.png')
    img_1.show()


