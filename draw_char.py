#coding=UTF-8
from PIL import Image, ImageDraw, ImageFont

if __name__ == "__main__":
    font = ImageFont.truetype("simsun.ttc", 60)
    background = Image.new('RGB',(224,224),color = 'black')
    draw = ImageDraw.Draw(background)
    word = u"䦂".encode('utf-8').decode('utf-8')
    _, _, w, h = draw.textbbox((0, 0), word,font = font)
    draw.text(((224-w)/2, (224-h)/2), word, font = font, fill='white')
    background.show()