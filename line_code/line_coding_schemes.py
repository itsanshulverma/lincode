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

def pol_NRZL(bits, high=1):
    bits = list(bits)
    x = np.arange(0, len(bits), 0.001)
    y = np.empty(0)
    for bit in bits:
        bit = int(bit)
        if bit == 0:
            if high==0:
                y = np.concatenate((y, np.ones(1000)))
            else:
                y = np.concatenate((y, np.zeros(1000)-1))
        elif bit == 1:
            if high==1:
                y = np.concatenate((y, np.ones(1000)))
            else:
                y = np.concatenate((y, np.zeros(1000)-1))
    return x,y

def pol_NRZI(bits, startbit=1):
    bits = list(bits)
    x = np.arange(0, len(bits), 0.001)
    y = np.empty(0)
    prevbit = startbit if startbit == 1 else -1
    for bit in bits:
        bit = int(bit)
        if bit == 0:
            y = np.concatenate((y, np.ones(1000)*prevbit))
        elif bit == 1:
            if prevbit==1:
                y = np.concatenate((y, np.zeros(1000)-1))
                prevbit = -1
            else:
                y = np.concatenate((y, np.ones(1000)))
                prevbit = 1
    return x,y

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
    prevbit = startbit if startbit == 1 else -1
    for bit in bits:
        bit = int(bit)
        if bit == 0:
            prevbit = -1 if prevbit==1 else 1
            y = np.concatenate((y, np.ones(500)*prevbit))
            prevbit = -1 if prevbit==1 else 1
            y = np.concatenate((y, np.ones(500)*prevbit))
        elif bit == 1:
            y = np.concatenate((y, np.ones(500)*prevbit))
            prevbit = -1 if prevbit==1 else 1
            y = np.concatenate((y, np.ones(500)*prevbit))
    return x,y

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