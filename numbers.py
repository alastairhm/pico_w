digits = [
    [ 0x2, 0x5, 0x5, 0x5, 0x2 ],
    [ 0x2, 0x6, 0x2, 0x2, 0x7 ],
    [ 0x6, 0x1, 0x2, 0x4, 0x7 ],
    [ 0x6, 0x1, 0x2, 0x1, 0x6 ],
    [ 0x1, 0x5, 0x7, 0x1, 0x1 ],
    [ 0x7, 0x4, 0x6, 0x1, 0x6 ],
    [ 0x3, 0x4, 0x6, 0x5, 0x2 ],
    [ 0x7, 0x1, 0x2, 0x2, 0x2 ],
    [ 0x2, 0x5, 0x2, 0x5, 0x2 ],
    [ 0x2, 0x5, 0x3, 0x1, 0x6 ],
]

print(digits)

for i in range(0,10):
    for r in digits[i]:
        print("{0:08b}".format(r))
    print("")
