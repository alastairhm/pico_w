#!/usr/bin/env python
# -*- coding: utf-8 -*-

import time

# From http://warp.povusers.org/MandScripts/python.html

start = time.time()

minX = -2.0
maxX = 1.0
width = 128
height = 64
aspectRatio = 2

chars = " .,-:;i+hHM$*#@ "
clen = len(chars)

rangeX = maxX-minX
yScale = (rangeX)*(float(height)/width)*aspectRatio
yScaleHalf = yScale/2

for y in range(height):
    line = ""
    ytemp = y*yScale/height-yScaleHalf
    for x in range(width):
        c = complex(minX+x*(rangeX)/width, ytemp)
        z = c
        colour = 0
        while abs(z) <= 2 and colour < clen:
            colour +=1
            z = z*z+c
        line += chars[colour % clen ]
    print(line)

print("Time taken %.4f seconds" %(time.time()-start))
