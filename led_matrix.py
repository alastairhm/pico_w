import max7219
import time
from machine import Pin, SPI

spi = SPI(0, baudrate=10000000, polarity=1, phase=0, sck=Pin(2), mosi=Pin(3))
ss = Pin(5, Pin.OUT)
display = max7219.Matrix8x8(spi, ss, 1)

display.brightness(1)
display.fill(0)

for x in range(0,8):
    for y in range(0,8):
        display.pixel(x,y,1)
        display.show()
        time.sleep(0.025)
        
for x in range(0,8):
    for y in range(0,8):
        display.pixel(x,y,0)
        display.show()
        time.sleep(0.025)
        
text = "Hello World!"
for c in range(0,len(text)):
    display.text(text[c],0,0,1)
    display.show()
    time.sleep(0.3)
    display.text(text[c],0,0,0)
    display.show()
    time.sleep(0.05)
   
GLYPHS = {
    "X": [
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0, 1, 0],
        [0, 0, 1, 0, 0, 1, 0, 0],
        [0, 0, 0, 1, 1, 0, 0, 0],
        [0, 0, 0, 1, 1, 0, 0, 0],
        [0, 0, 1, 0, 0, 1, 0, 0],
        [0, 1, 0, 0, 0, 0, 1, 0],
        [0, 0, 0, 0, 0, 0, 0, 0],
    ],
}
display.text_from_glyph("X", GLYPHS)
display.show()

