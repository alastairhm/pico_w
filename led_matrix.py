import max7219
import time
from machine import Pin, SPI
from framebuf import MONO_HLSB, MONO_HMSB, MONO_VLSB

def display_str(display, text):
    for c in range(0, len(text)):
        display.text(text[c], 0, 0, 1)
        display.show()
        time.sleep(0.3)
        display.text(text[c], 0, 0, 0)
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
    "a": [
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 1, 1, 0, 0, 1, 1, 0],
        [0, 1, 1, 0, 0, 1, 1, 0],
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0, 1, 0],
        [0, 0, 1, 1, 1, 1, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0],
    ],
    "b": [
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 1, 1, 0, 0, 1, 1, 0],
        [0, 1, 1, 0, 0, 1, 1, 0],
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 1, 1, 1, 1, 1, 1, 0],
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0],
    ],
    "c": [
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 1, 1, 0, 0, 1, 1, 0],
        [0, 1, 1, 0, 0, 1, 1, 0],
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 1, 1, 1, 1, 0, 0],
        [0, 1, 0, 0, 0, 0, 1, 0],
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0],
    ],
}

spi = SPI(0, baudrate=10000000, polarity=1, phase=0, sck=Pin(2), mosi=Pin(3))
ss = Pin(5, Pin.OUT)
display = max7219.Matrix8x8(spi, ss, 1)

display.brightness(1)
display.fill(0)

# Test all pixels light up
for x in range(0, 8):
    for y in range(0, 8):
        display.pixel(x, y, 1)
        display.show()
        time.sleep(0.01)

for x in range(0, 8):
    for y in range(0, 8):
        display.pixel(x, y, 0)
        display.show()
        time.sleep(0.01)

#Test Text
text = "Hello World!"
display_str(display, text)

#Test Custom Glyphs
display.text_from_glyph("X", GLYPHS)
display.show()
display.fill(0)
time.sleep(0.5)

animation = "abccba"
for i in range(0, len(animation)):
    display.fill(0)
    display.text_from_glyph(animation[i], GLYPHS)
    display.show()
    time.sleep(0.25)


#Test Different Mapping Options
display = max7219.Matrix8x8(spi, ss, 1, MONO_VLSB)
display.fill(0)
display.text("P")
display.show()
time.sleep(0.5)
display = max7219.Matrix8x8(spi, ss, 1, MONO_HMSB)
display.fill(0)
display.text("P")
display.show()
time.sleep(0.5)
display = max7219.Matrix8x8(spi, ss, 1, MONO_HLSB)
display.fill(0)
display.text("P")
display.show()
time.sleep(0.5)
