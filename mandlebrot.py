#!/usr/bin/env python
# -*- coding: utf-8 -*-

# From http://warp.povusers.org/MandScripts/python.html

minX = -2.0
maxX = 1.0
width = 128
height = 64
aspectRatio = 2

chars = " .,-:;i+hHM$*#@ "

yScale = (maxX-minX)*(float(height)/width)*aspectRatio

for y in range(height):
    line = ""
    for x in range(width):
        c = complex(minX+x*(maxX-minX)/width, y*yScale/height-yScale/2)
        z = c
        for char in chars:
            if abs(z) > 2:
                break
            z = z*z+c
        line += char
    print(line)
