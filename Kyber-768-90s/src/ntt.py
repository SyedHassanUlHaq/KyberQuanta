# -*- coding: utf-8 -*-
"""ntt.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1WV3iSHzcwu7SxZh6fAVrkkHMbCCX8TIG
"""

#Referenced from FIPS-203
import random
def bit_reversal(i, k):
    bin_i = bin(i & (2**k - 1))[2:].zfill(k)
    return int(bin_i[::-1], 2)

def compute_ntt(coeffs):
    """
    Convert a polynomial to number-theoretic transform (NTT) form.
    The input is in standard order, the output is in bit-reversed order.
    """
    q=3329
    n = 256
    l = 128
    k = 1
    zetas = [pow(17, bit_reversal(i, 7), q) for i in range(128)]

    # Perform the NTT transformation
    while l >= 2:
        # print("l",l)
        start = 0
        while start < n:
            # print("start",start)
            zeta = zetas[k]
            k += 1
            for j in range(start, start + l):
                t = (zeta * coeffs[j + l]) % q
                # print("t",j,t)
                coeffs[j + l] = (coeffs[j] - t) % q
                
                coeffs[j] = (coeffs[j] + t) % q 
               
            start = l + (j +1)
            # print("start",start)
        l = l >> 1
        # print("l",l)

    # Ensure the coefficients are in range [0, q)
    for j in range(n):
        coeffs[j] %= q
    return coeffs
#driverscode
# Initialize f with 256 elements (all set to 0 initially)
f = [0] * 256

# Assign the given values to specific indices
f[0] = 0
f[1] = 1
f[2] = 0
f[3] = -1
f[4] = 0
f[5] = 1
f[6] = 0
f[7] = -1
f[8] = 0  
f[9] = 1
f[10] = 0
f[11] = -1
f[12] = 0
f[100] = -1
f[101] = 0
f[102] = 1
f[103] = 0
f[104] = -1
f[105] = 0
f[106] = 1
f[180] = -1
f[181] = 0
f[182] = 1
f[190] = 0
f[191] = -1
f[205] = 1
f[206] = 0
f[207] = -1
f[208] = 0
f[209] = 1
f[230] = 0
f[231] = -1
f[232] = 0
f[250] = -1
f[251] = 0
f[252] = 1
f[253] = 0
f[254] = 1
f[255] = -1
print("f",f)
f_ntt = compute_ntt(f)
print(f_ntt)
# print(len(f_ntt))