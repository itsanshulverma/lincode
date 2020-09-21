###########################################
#   Author: Anshul Verma
#   github.com/itsanshulverma
###########################################

import matplotlib.pyplot as plt
from . import line_coding_schemes as lcs

def plot_UNRZ(bits):
    fig, axs = plt.subplots()
    x, y = lcs.uni_NRZ(bits)
    axs.plot(x, y, linewidth=3)
    axs.set(xlabel='Time', ylabel='Amplitude', title='Unipolar: NRZ')
    axs.grid()
    plt.show()

def plot_PNRZ(bits):
    fig, axs = plt.subplots(2, sharex=True)
    x, y = lcs.pol_NRZL(bits)
    axs[0].plot(x, y, linewidth=3)
    axs[0].set_title('Polar: NRZ-L')
    axs[0].set(ylabel='Amplitude', title='Polar: NRZ-L')
    axs[0].grid()
    x, y = lcs.pol_NRZI(bits)
    axs[1].plot(x, y, linewidth=3)
    axs[1].set_title('Polar: NRZ-I')
    axs[1].set(xlabel='Time', ylabel='Amplitude', title='Polar: NRZ-I')
    axs[1].grid()
    plt.show()

def plot_PRZ(bits):
    fig, axs = plt.subplots()
    x, y = lcs.pol_RZ(bits)
    axs.plot(x, y, linewidth=3)
    axs.set_title('Polar RZ')
    axs.set(xlabel='Time', ylabel='Amplitude', title='Polar RZ')
    axs.grid()
    plt.show()

def plot_Biphase(bits):
    fig, axs = plt.subplots(2, sharex=True)
    x, y = lcs.MANCHESTER(bits)
    axs[0].plot(x, y, linewidth=3)
    axs[0].set(ylabel='Amplitude', title='Biphase: Manchester')
    axs[0].grid()
    x, y = lcs.diff_MANCHESTER(bits)
    axs[1].plot(x, y, linewidth=3)
    axs[1].set(xlabel='Time', ylabel='Amplitude', title='Differential Manchester')
    axs[1].grid()
    plt.show()

def plot_Bipolar(bits):
    fig, axs = plt.subplots(2, sharex=True)
    x, y = lcs.AMI(bits)
    axs[0].plot(x, y, linewidth=3)
    axs[0].set(ylabel='Amplitude', title='Bipolar: AMI(Alternate Mark Inversion)')
    axs[0].grid()
    x, y = lcs.Pseudoternary(bits)
    axs[1].plot(x, y, linewidth=3)
    axs[1].set(xlabel='Time', ylabel='Amplitude', title='Bipolar: Pseudoternary')
    axs[1].grid()
    plt.show()
