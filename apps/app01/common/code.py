from PIL import Image, ImageDraw, ImageFont, ImageFilter
import random
from io import StringIO, BytesIO

width = 60 * 4
height = 60


# 随机数字
def range_char():
    return chr(random.randint(65, 90))


# 随机底板颜色
def range_color():
    return (random.randint(64, 255), random.randint(64, 255), random.randint(64, 255))


# 随机字体颜色
def range_char_color():
    return (random.randint(32, 127), random.randint(32, 127), random.randint(32, 127))


def ret_code_img():
    img_obj = Image.new('RGB', (width, height), (255, 255, 255))
    font = ImageFont.truetype('Arial.ttf', 36)
    draw = ImageDraw.Draw(img_obj)
    # 填充Drow底色的每一个像素
    for i in range(width):
        for y in range(height):
            draw.point((i, y), fill=range_color())

    # 填充文字,width = 60 * 4
    code = ''
    for i in range(4):
        _font = range_char()
        draw.text((60 * i + 10, 10), _font, font=font, fill=range_char_color())
        code += _font
    img_obj = img_obj.filter(ImageFilter.BLUR)
    io = BytesIO()
    img_obj.save(io, 'png')
    return (code, io.getvalue())
