import time
import random
import board
import neopixel
import random

pixels = neopixel.NeoPixel(board.NEOPIXEL, 4, auto_write=True)


#Define colors
pink = (12,10,12)
gold = (50, 40, 5)
blue = (0,0,8)
orange = (25, 10, 0)
blank = (0,0,0)
grn = (0,20,0)
green  = (0,20,0)
red = (20,0,0)
zero = (2,2,2)
colors = [pink, gold, blue, orange,green,red]


def docolor(color):
    for i in range(4):
        pixels[i] = color


    pixels.show()
    time.sleep(.25)

    for i in range(4):
        pixels[i] = blank

    pixels.show()


def blinknum(num,color):
    for i in range(num):
        docolor(color)
        time.sleep(.25)

def compthink(): #blink out all the colors when computer "thinking"
    for clr in colors:
        blinknum(1,clr)

def binnum(num,color):
    docolor(blank)
    num = num % 16
    if num == 0:
        pixels.fill(zero)
    else:
        for i in range(4):
            if ((2**i)&num)>0:
                pixels[i] = color

    pixels.show()
    time.sleep(.5)


