#!/usr/bin/env python
# -*- coding: utf-8 -*-

# From http://warp.povusers.org/MandScripts/python.html

import machine
import ssd1306

sda = machine.Pin(0)
scl = machine.Pin(1)
i2c = machine.I2C(0, sda=sda, scl=scl, freq=400000)
print("Scanning for IC2 devices")
devices = i2c.scan()
if len(devices) == 0:
    print("No i2c Devices found.")
else:
    for device in devices:
        print("Decimal address: ", device, " | Hexa address: ", hex(device))
    display = ssd1306.SSD1306_I2C(128, 64, i2c)
    display.fill(0)
    display.show()

minX = -2.0
maxX = 1.0
width = 128
height = 64
aspectRatio = 2

chars = " .,-:;i+hHM$*#@ "
clen = len(chars)

rangeX = maxX-minX
yScale = (rangeX)*(float(height)/width)*aspectRatio

for y in range(height):
    line = ""
    ytemp = y*yScale/height-yScale/2
    for x in range(width):
        c = complex(minX+x*(rangeX)/width, ytemp)
        z = c
        colour = 0
        while abs(z) <= 2 and colour < clen:
            colour +=1
            z = z*z+c
        display.pixel(x,y,(colour % 2))
        line += chars[colour % clen ]
    print(line)
    display.show()

