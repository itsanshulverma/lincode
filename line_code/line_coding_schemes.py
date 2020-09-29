###########################################
#   Author: Anshul Verma
#   github.com/itsanshulverma
###########################################

import numpy as np

def uni_NRZ(bits):
    bits = list(bits)
    x = np.arange(0, len(bits), 0.001)
    y = np.empty(0)
    for bit in bits:
        bit = int(bit)
        if bit == 0:
            y = np.concatenate((y, np.zeros(1000)))
        elif bit == 1:
            y = np.concatenate((y, np.ones(1000)))
    return x,y

def pol_NRZL(bits, high=-1):
    bits = list(bits)
    x = np.arange(0, len(bits), 0.001)
    y = np.empty(0)
    for bit in bits:
        bit = int(bit)
        if bit == 0:
            if high==-1:
                y = np.concatenate((y, np.ones(1000)))
            else:
                y = np.concatenate((y, np.zeros(1000)-1))
        elif bit == 1:
            if high==1:
                y = np.concatenate((y, np.ones(1000)))
            else:
                y = np.concatenate((y, np.zeros(1000)-1))
    return x,y

def pol_NRZI(bits, startbit=0):
    bits = list(bits)
    x = np.arange(0, len(bits), 0.001)
    y = np.empty(0)
    i0 = list() # No Inversion
    ix0 = list()
    i1 = list() # Inversion
    ix1 = list()
    encoded = list()
    prevbit = startbit if startbit == 1 else -1
    for bit in bits:
        bit = int(bit)
        if bit == 0:
            y = np.concatenate((y, np.ones(1000)*prevbit))
            encoded.append(prevbit)
        elif bit == 1:
            if prevbit==1:
                y = np.concatenate((y, np.zeros(1000)-1))
                encoded.append(-1)
                prevbit = -1
            else:
                y = np.concatenate((y, np.ones(1000)))
                encoded.append(1)
                prevbit = 1

    for i in range(0,len(bits)-1): 
        if encoded[i] == encoded[i+1]:
            i0.append(encoded[i])
            ix0.append(i+1)
        else:
            i1.append(encoded[i])
            ix1.append(i+1)

    return x, y, ix0, i0, ix1, i1

def pol_RZ(bits):
    bits = list(bits)
    x = np.arange(0, len(bits)+0.001, 0.001)
    y = np.empty(0)
    for bit in bits:
        bit = int(bit)
        if bit == 0:
            y = np.concatenate((y, np.zeros(500)-1))
        elif bit == 1:
            y = np.concatenate((y, np.ones(500)))
        y = np.concatenate((y, np.zeros(500)))
    y = np.concatenate((y, np.array([1])))
    return x,y

def MANCHESTER(bits):
    bits = list(bits)
    x = np.arange(0, len(bits), 0.001)
    y = np.empty(0)
    for bit in bits:
        bit = int(bit)
        if bit == 0:
            y = np.concatenate((y, np.ones(500)))
            y = np.concatenate((y, np.zeros(500)-1))
        elif bit == 1:
            y = np.concatenate((y, np.zeros(500)-1))
            y = np.concatenate((y, np.ones(500)))
    return x,y

def diff_MANCHESTER(bits, startbit=1):
    bits = list(bits)
    x = np.arange(0, len(bits), 0.001)
    y = np.empty(0)
    i0 = list() # No Inversion
    ix0 = list()
    i1 = list() # Inversion
    ix1 = list()
    encoded = list()
    prevbit = startbit if startbit == 1 else -1
    for bit in bits:
        bit = int(bit)
        if bit == 0:
            prevbit = -1 if prevbit==1 else 1
            y = np.concatenate((y, np.ones(500)*prevbit))
            temp = f'{prevbit}'
            prevbit = -1 if prevbit==1 else 1
            y = np.concatenate((y, np.ones(500)*prevbit))
            temp += f'{prevbit}'
            encoded.append(temp)
        elif bit == 1:
            y = np.concatenate((y, np.ones(500)*prevbit))
            temp = f'{prevbit}'
            prevbit = -1 if prevbit==1 else 1
            y = np.concatenate((y, np.ones(500)*prevbit))
            temp += f'{prevbit}'
            encoded.append(temp)

    for i in range(0,len(bits)-1): 
        curr = -1 if encoded[i][1] == '-' else 1
        nxt = -1 if encoded[i+1][0] == '-' else 1 
        if curr == nxt:
            i0.append(curr)
            ix0.append(i+1)
        else:
            i1.append(curr)
            ix1.append(i+1)

    return x, y, ix0, i0, ix1, i1

def AMI(bits):
    bits = list(bits)
    x = np.arange(0, len(bits), 0.001)
    y = np.empty(0)
    prev_one = -1
    for bit in bits:
        bit = int(bit)
        if bit == 0:
            y = np.concatenate((y, np.zeros(1000)))
        elif bit == 1:
            if prev_one==1:
                y = np.concatenate((y, np.zeros(1000)-1))
                prev_one = -1
            else:
                y = np.concatenate((y, np.ones(1000)))
                prev_one = 1
    return x,y

def Pseudoternary(bits):
    bits = list(bits)
    x = np.arange(0, len(bits)+0.001, 0.001)
    y = np.empty(0)
    prev_one = -1
    for bit in bits:
        bit = int(bit)
        if bit == 0:
            if prev_one==1:
                y = np.concatenate((y, np.zeros(1000)-1))
                prev_one = -1
            else:
                y = np.concatenate((y, np.ones(1000)))
                prev_one = 1
        elif bit == 1:
            y = np.concatenate((y, np.zeros(1000)))
    y = np.concatenate((y, np.array([0])))
    return x,y