# coding=utf-8
# 读取图片上的数字。数独截图的图片不能读取
# https://pypi.org/project/pytesseract/ pytesseract库的官方文档

import pytesseract
from PIL import Image

# 设置PATH
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'


# 访问相对路径如下图，绝对路径是下一行代码
image = Image.open('D:\Script\sudoku\shuzi.JPG')
# tessdata_dir_config = '--tessdata-dir "C:\\Program Files (x86)\\Tesseract-OCR\\tessdata"'
code1 = pytesseract.image_to_string(image)
print('------------------------START----------------------------')
print(code1)
print('------------------------END------------------------------')


# 识别英文及数字
image1 = Image.open('d:\Script\sudoku\eng.JPG')
code2 = pytesseract.image_to_string(image1)
print('------------------------START----------------------------')
print(code2)
print('------------------------END------------------------------')






