# SEND black "128.141.118.75"

UDP_IP = "128.141.118.251" #IP de l'altre


UDP_PORT = 5005

# import libraries
import sys
import pygame as pg
import os
import time
import epd7in5b
from PIL import Image,ImageDraw,ImageFont
import RPi.GPIO as GPIO
import socket

def buttonCallback(channel):
    global x
    x=channel
    #print channel

def chooseImage(picFile):
    if picFile == '1':
        image = '1.bmp'
    elif picFile == '2':
        image = '2.bmp'
    return image

def playMusic(musicFile):
    clock = pg.time.Clock()
    try:
        pg.mixer.music.load(musicFile)
        print("Music file {} loaded!".format(musicFile))
    except pygame.error:
        print("File {} not found! {}".format(musicFile, pg.get_error()))
        return
    pg.mixer.music.play()
    while pg.mixer.music.get_busy():
        clock.tick(30)

if __name__ == '__main__':
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(12, GPIO.IN, pull_up_down = GPIO.PUD_DOWN) #button_right
    GPIO.setup(16, GPIO.IN, pull_up_down = GPIO.PUD_DOWN) #button_B
    GPIO.setup(20, GPIO.IN, pull_up_down = GPIO.PUD_DOWN) #button_A
    GPIO.setup(22, GPIO.IN, pull_up_down = GPIO.PUD_DOWN) #button_left
    GPIO.setup(23, GPIO.IN, pull_up_down = GPIO.PUD_DOWN) #button_down
    GPIO.setup(27, GPIO.IN, pull_up_down = GPIO.PUD_DOWN) #button_up
    GPIO.add_event_detect(12,GPIO.RISING,callback = buttonCallback)
    GPIO.add_event_detect(16,GPIO.RISING,callback = buttonCallback)
    GPIO.add_event_detect(20,GPIO.RISING,callback = buttonCallback)
    GPIO.add_event_detect(22,GPIO.RISING,callback = buttonCallback)
    GPIO.add_event_detect(23,GPIO.RISING,callback = buttonCallback)
    GPIO.add_event_detect(27,GPIO.RISING,callback = buttonCallback)
    x = 0
    freq = 44100    # audio CD quality
    bitsize = -16   # unsigned 16 bit
    channels = 2    # 1 is mono, 2 is stereo
    buffer = 2048   # number of samples (experiment to get right sound)
    pg.mixer.init(freq, bitsize, channels, buffer)
    pg.mixer.music.set_volume(1.0) # optional volume 0 to 1.0
    epd = epd7in5b.EPD()
    epd.init()
    #print("Clear...")
    #epd.Clear(0xFF)
    print('Press button...')


    while True:

        # DEMO EXERCISE
        x=0

        imageBlack = Image.open('bmp/' + chooseImage('2')) # Demo exercise
        imageRed = Image.open('bmp/blank.bmp')
        epd.display(epd.getbuffer(imageBlack),epd.getbuffer(imageRed))
        #playMusic('mp3/' + '2' + '.wav') # Demo exercise audio





    print 'End'
