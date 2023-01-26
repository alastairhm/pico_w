import max7219
import time
from machine import Pin, SPI
from framebuf import MONO_HLSB, MONO_HMSB, MONO_VLSB


def compact_number(display, number, offx=0, offy=0):
    """Display compact numbers so two digits fit in 8x5 LED grid"""

    digits = [
        [0x2, 0x5, 0x5, 0x5, 0x2],
        [0x2, 0x6, 0x2, 0x2, 0x7],
        [0x6, 0x1, 0x2, 0x4, 0x7],
        [0x6, 0x1, 0x2, 0x1, 0x6],
        [0x1, 0x5, 0x7, 0x1, 0x1],
        [0x7, 0x4, 0x6, 0x1, 0x6],
        [0x3, 0x4, 0x6, 0x5, 0x2],
        [0x7, 0x1, 0x2, 0x2, 0x2],
        [0x2, 0x5, 0x2, 0x5, 0x2],
        [0x2, 0x5, 0x3, 0x1, 0x6],
    ]
    num = []
    for row in range(0, 5):
        num.append(
            "{0:08b}".format(digits[number // 10][row] << 4 | digits[number % 10][row])
        )
    display.fill(0)
    for y in range(0, len(num)):
        for x in range(0, 8):
            if num[y][x] == "1":
                display.pixel(x + offx, y + offy, 1)
    display.show()


if __name__ == "__main__":
    spi = SPI(0, baudrate=10000000, polarity=1, phase=0, sck=Pin(2), mosi=Pin(3))
    ss = Pin(5, Pin.OUT)
    display = max7219.Matrix8x8(spi, ss, 1)

    display.brightness(1)
    display.fill(0)
    display.show()

    for number in range(0, 100):
        compact_number(display, number)
        time.sleep(0.2)
