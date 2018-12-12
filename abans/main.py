##
 #  @filename   :   main.py
 #  @author     :   Xavier Cantos Roman
 ##

import epd7in5b
import time
from PIL import Image,ImageDraw,ImageFont

def chooseImage(num):
    if num == '1': image = '1.bmp'
    else: image = '2.bmp'
    return image


if __name__ == '__main__':
    epd = epd7in5b.EPD()
    epd.init()
    print("Clear...")
    epd.Clear(0xFF)
    x = raw_input('Input: ')
    while x != '0':
        imageBlack = Image.open('bmp/' + chooseImage(x))
        imageRed = Image.open('bmp/blank.bmp')
        epd.display(epd.getbuffer(imageBlack),epd.getbuffer(imageRed))
        x = raw_input('Input: ')
    print 'End'

