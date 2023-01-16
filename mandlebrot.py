#!/usr/bin/env python
# -*- coding: utf-8 -*-

# From http://warp.povusers.org/MandScripts/python.html

minX = -2.0
maxX = 1.0
width = 128
height = 64
aspectRatio = 2

chars = " .,-:;i+hHM$*#@ "

rangeX = maxX-minX
yScale = (rangeX)*(float(height)/width)*aspectRatio

for y in range(height):
    line = ""
    ytemp = y*yScale/height-yScale/2
    for x in range(width):
        c = complex(minX+x*(rangeX)/width, ytemp)
        z = c
        for char in chars:
            if abs(z) > 2:
                break
            z = z*z+c
        line += char
    print(line)
