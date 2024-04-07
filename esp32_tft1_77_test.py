"""
MicroPython/Espressif ESP32-C3-DevKitM-1 exercise
+ 1.8" 128 x 160 TFT ST7735 SPI

using library boochow/MicroPython-ST7735
https://github.com/boochow/MicroPython-ST7735
"""
import os
import sys
import time
import random
import ST7735
from seriffont import seriffont
from sysfont import sysfont
from terminalfont import terminalfont
from machine import SPI

print("====================================")
print(sys.implementation[0], os.uname()[3],
      "\nrun on", os.uname()[4])
print("====================================")

tft_CS = 15
tft_RESET=5
tft_A0=4      # DC
tft_SDA=23    # MOSI
tft_SCK=18    # CLK

spi = SPI(2, baudrate=20000000, polarity=0, phase=0, miso=None) # using default sck/mosi
display=ST7735.TFT(spi,tft_A0,tft_RESET,tft_CS)

# spi = SPI(2, baudrate=20000000, polarity=0, phase=0, sck=Pin(14), mosi=Pin(13), miso=Pin(12))
# tft=TFT(spi,16,17,18)

displaysize = display.size()
print(displaysize)

display.initg() # or initr()/initb() according to your display

display.rotation(1)

display.fill(display.BLACK)
display.text((0,0),
             sys.implementation[0]+' '+os.uname()[3],
             display.WHITE,
             terminalfont)
time.sleep(1)
display.text((0,30),
             "run on "+os.uname()[4],
             ST7735.TFTColor(0xFF, 0xFF, 0xFF),
             terminalfont)
time.sleep(3)

#font test
display.fill(display.BLACK)
display.text((0,0),
             "seriffont",
             display.RED,
             seriffont)
display.text((0,10),
             "abcdefghijklmnopqrstuvwxyz",
             display.WHITE,
             seriffont)
display.text((0,30),
             "ABCDEFGHIJKLMNOPQRSTUVWXYZ",
             display.WHITE,
             seriffont)
display.text((0,50),
             "sysfont",
             display.RED,
             sysfont)
display.text((0,60),
             "abcdefghijklmnopqrstuvwxyz",
             display.WHITE,
             sysfont)
display.text((0,70),
             "ABCDEFGHIJKLMNOPQRSTUVWXYZ",
             display.WHITE,
             sysfont)
display.text((0,80),
             "terminalfont",
             display.RED,
             terminalfont)
display.text((0,90),
             "abcdefghijklmnopqrstuvwxyz",
             display.WHITE,
             terminalfont)
display.text((0,110),
             "ABCDEFGHIJKLMNOPQRSTUVWXYZ",
             display.WHITE,
             terminalfont)
time.sleep(5)

display.rotation(0)
display.fill(display.RED)
display.text((10,10),
             "RED",
             ST7735.TFTColor(0xFF, 0xFF, 0xFF),
             terminalfont,
             aSize=2)
time.sleep(1)

display.fill(display.GREEN)
display.text((10,10),
             "GREEN",
             ST7735.TFTColor(0xFF, 0xFF, 0xFF),
             terminalfont,
             aSize=2)
time.sleep(1)

display.fill(display.BLUE)
display.text((10,10),
             "BLUE",
             ST7735.TFTColor(0xFF, 0xFF, 0xFF),
             terminalfont,
             aSize=2)
time.sleep(1)

def sub_Disp_rot_info():
    display.fill(display.BLACK)
    display.fillrect((1,1),
                     (display.size()[0]-2, display.size()[1]-2),
                     display.WHITE)
    display.fillrect((2,2),
                     (display.size()[0]-4, display.size()[1]-4),
                     display.BLACK)
    display.text((5,5),
                 "rotate = "+str(display.rotate),
                 display.WHITE,
                 terminalfont)
    display.text((5,20),
                 str(display.size()),
                 display.WHITE,
                 terminalfont)
    print("rotate = "+str(display.rotate)+" : "+str(display.size())) 
    

#rotation test
display.rotation(0)
sub_Disp_rot_info()
time.sleep(2)

display.rotation(1)
sub_Disp_rot_info()
time.sleep(2)

display.rotation(2)
sub_Disp_rot_info()
time.sleep(2)

display.rotation(3)
sub_Disp_rot_info()
time.sleep(2)


display.fill(display.BLACK)

#Random pixel
for p in range(1000):
    x = random.randint(5, display.size()[0]-10)
    y = random.randint(5, display.size()[1]-10)
    c = ST7735.TFTColor(random.randint(0, 0xFF),
                        random.randint(0, 0xFF),
                        random.randint(0, 0xFF))
    display.pixel((x, y), c)
    
#Random line
for l in range(100):
    display.line((random.randint(5, display.size()[0]-10),
                  random.randint(5, display.size()[1]-10)),
                 (random.randint(5, display.size()[0]-10),
                  random.randint(5, display.size()[1]-10)),
                 ST7735.TFTColor(random.randint(0, 0xFF),
                        random.randint(0, 0xFF),
                        random.randint(0, 0xFF)))

#Random circle
for l in range(20):
    display.circle((random.randint(5, display.size()[0]-10),
                    random.randint(5, display.size()[1]-10)),
                   random.randint(1, 50),
                   ST7735.TFTColor(random.randint(0, 0xFF),
                                   random.randint(0, 0xFF),
                        random.randint(0, 0xFF)))
    
#Random fillcircle
for l in range(20):
    display.fillcircle((random.randint(5, display.size()[0]-10),
                    random.randint(5, display.size()[1]-10)),
                   random.randint(1, 50),
                   ST7735.TFTColor(random.randint(0, 0xFF),
                                   random.randint(0, 0xFF),
                        random.randint(0, 0xFF)))

print("~ bye ~")
