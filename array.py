array = [
        [1, 0, 0, 0, 0, 0, 0, 0],
        [1, 1, 1, 0, 0, 1, 1, 0],
        [1, 1, 1, 0, 0, 1, 1, 0],
        [1, 0, 0, 0, 0, 0, 0, 0],
        [1, 0, 1, 1, 1, 1, 0, 0],
        [1, 1, 0, 0, 0, 0, 1, 0],
        [1, 0, 0, 0, 0, 0, 0, 0],
        [1, 0, 0, 0, 0, 0, 0, 0],
]

for i in range(0,7):
    print(array[i])

array2 = list(zip(*array[::-1]))

for i in range(0,7):
    print(array2[i])
