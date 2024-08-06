import math

def BytesToBits(byte_array):
    bits_array = []
    for i in range(8 * len(byte_array)):
            bits_array.append(math.ceil(byte_array[i//8][i%8] / (2 ** (i % 8))) % 2)
    return bits_array
     
b = [
        [1,0,0,1,0,0,1,0],
        [0,0,1,1,1,0,1,1],
        [1,0,1,1,1,0,0,1],
        [1,0,1,0,0,0,1,1],
        [0,1,0,1,0,1,1,0],
        [0,0,0,0,1,0,1,1]
    ]


print(BytesToBits(b))