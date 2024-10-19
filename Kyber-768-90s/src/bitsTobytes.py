def bits_to_bytes(bit_array, l):
   
    if len(bit_array) != 8 * l:
        raise ValueError(f"Bit array length must be {8 * l} bits for l = {l} bytes.")

    B = [0] * l

    for i in range(len(bit_array)):
        B[i // 8] = B[i // 8] + bit_array[i] * (2 ** (7 - (i % 8))) 

    return B

l = 32 
bit_array = [
    1, 0, 1, 1, 0, 0, 1, 0,
    1, 0, 1, 1, 0, 0, 1, 0,
    1, 0, 1, 1, 0, 0, 1, 0,
    1, 0, 1, 1, 0, 0, 1, 0,
    1, 0, 1, 1, 0, 0, 1, 0,
    1, 0, 1, 1, 0, 0, 1, 0,
    1, 0, 1, 1, 0, 0, 1, 0,
    1, 0, 1, 1, 0, 0, 1, 0,
    1, 0, 1, 1, 0, 0, 1, 0,
    1, 0, 1, 1, 0, 0, 1, 0,
    1, 0, 1, 1, 0, 0, 1, 0,  
    0, 1, 0, 1, 1, 0, 0, 1,  
    1, 1, 0, 0, 0, 1, 1, 1,  
    0, 1, 1, 0, 1, 0, 0, 0, 
    1, 0, 1, 1, 0, 0, 1, 0,  
    0, 1, 0, 1, 1, 0, 0, 1,  
    1, 1, 0, 0, 0, 1, 1, 1,  
    0, 1, 1, 0, 1, 0, 0, 0, 
    1, 0, 1, 1, 0, 0, 1, 0,  
    0, 1, 0, 1, 1, 0, 0, 1,  
    1, 1, 0, 0, 0, 1, 1, 1,  
    0, 1, 1, 0, 1, 0, 0, 0, 
    1, 0, 1, 1, 0, 0, 1, 0,  
    0, 1, 0, 1, 1, 0, 0, 1,  
    1, 1, 0, 0, 0, 1, 1, 1,  
    0, 1, 1, 0, 1, 0, 0, 0,
    1, 0, 1, 1, 0, 0, 1, 0,  
    0, 1, 0, 1, 1, 0, 0, 1,  
    1, 1, 0, 0, 0, 1, 1, 1,
    1, 0, 1, 1, 0, 0, 1, 0,
    1, 0, 1, 1, 0, 0, 1, 0,
    1, 0, 1, 1, 0, 0, 1, 0 
]  
byte_array = bits_to_bytes(bit_array, l)

print(byte_array)  