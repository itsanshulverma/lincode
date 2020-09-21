###########################################
#   Author: Anshul Verma
#   github.com/itsanshulverma
###########################################

import matplotlib.pyplot as plt
from . import line_coding_schemes as lcs

def plot_UNRZ(bits):
    fig, axs = plt.subplots()
    x, y = lcs.uni_NRZ(bits)
    axs.plot(x,y)
    axs.set_title('Unipolar: NRZ')
    plt.show()

def plot_PNRZ(bits):
    fig, axs = plt.subplots(2)
    x, y = lcs.pol_NRZL(bits)
    axs[0].plot(x,y)
    axs[0].set_title('Polar: NRZ-L')
    x, y = lcs.pol_NRZI(bits)
    axs[1].plot(x,y)
    axs[1].set_title('Polar: NRZ-I')
    plt.show()

def plot_PRZ(bits):
    fig, axs = plt.subplots()
    x, y = lcs.pol_RZ(bits)
    axs.plot(x,y)
    axs.set_title('Polar RZ')
    plt.show()

def plot_Biphase(bits):
    fig, axs = plt.subplots(2)
    x, y = lcs.MANCHESTER(bits)
    axs[0].plot(x,y)
    axs[0].set_title('Biphase: Manchester')
    x, y = lcs.diff_MANCHESTER(bits)
    axs[1].plot(x,y)
    axs[1].set_title('Differential Manchester')
    plt.show()

def plot_Bipolar(bits):
    fig, axs = plt.subplots(2)
    x, y = lcs.AMI(bits)
    axs[0].plot(x,y)
    axs[0].set_title('Bipolar: AMI(Alternate Mark Inversion)')
    x, y = lcs.Pseudoternary(bits)
    axs[1].plot(x,y)
    axs[1].set_title('Bipolar: Pseudoternary')
    plt.show()
