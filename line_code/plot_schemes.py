###########################################
#   Author: Anshul Verma
#   github.com/itsanshulverma
###########################################

import matplotlib.pyplot as plt
import numpy as np
from . import line_coding_schemes as lcs

def plot_UNRZ(bits):
    fig, axs = plt.subplots(figsize=(7, 4))
    x, y = lcs.uni_NRZ(bits)
    axs.plot(x, y, linewidth=3)
    axs.set(xlabel='Time', ylabel='Amplitude', title='Unipolar: NRZ')
    axs.set_xticks([x for x in range(len(bits)+1)])
    axs.set_yticks([-1.5, -1, -0.5, 0, 0.5, 1, 1.5])
    axs.set_yticklabels(['', '-1', '', '0', '', '1', ''])
    axs.grid()
    plt.show()

def plot_PNRZ(bits, startbit):
    fig, axs = plt.subplots(2, figsize=(6, 6), sharex=True)
    x, y = lcs.pol_NRZL(bits)
    axs[0].plot(x, y, linewidth=3)
    axs[0].set_title('Polar: NRZ-L')
    axs[0].set(ylabel='Amplitude', title='Polar: NRZ-L')
    axs[0].set_xticks([x for x in range(len(bits)+1)])
    axs[0].set_yticks([-1.5, -1, -0.5, 0, 0.5, 1, 1.5])
    axs[0].set_yticklabels(['', '-1', '', '0', '', '1', ''])
    axs[0].grid()
    x, y, ix0, i0, ix1, i1 = lcs.pol_NRZI(bits, startbit)
    axs[1].plot(x, y, linewidth=3)
    p1, = axs[1].plot(ix0, i0, 'o', markeredgecolor="black", markerfacecolor="white", markersize=7, label="Next bit is 0: No Inversion")
    p2, = axs[1].plot(ix1, i1, 'ok', markersize=7, label="Next bit is 1: Inversion")
    axs[1].legend(loc='lower right', prop={'size': 5.5})
    axs[1].set_title('Polar: NRZ-I')
    axs[1].set(xlabel='Time', ylabel='Amplitude', title='Polar: NRZ-I')
    axs[1].set_xticks([x for x in range(len(bits)+1)])
    axs[1].set_yticks([-1.5, -1, -0.5, 0, 0.5, 1, 1.5])
    axs[1].set_yticklabels(['', '-1', '', '0', '', '1', ''])
    axs[1].grid()
    plt.show()

def plot_PRZ(bits):
    fig, axs = plt.subplots(figsize=(7, 4))
    x, y = lcs.pol_RZ(bits)
    axs.plot(x, y, linewidth=3)
    axs.set_title('Polar RZ')
    axs.set(xlabel='Time', ylabel='Amplitude', title='Polar RZ')
    axs.set_xticks([x for x in range(len(bits)+1)])
    axs.set_yticks([-1.5, -1, -0.5, 0, 0.5, 1, 1.5])
    axs.set_yticklabels(['', '-1', '', '0', '', '1', ''])
    axs.grid()
    plt.show()

def plot_Biphase(bits, startbit):
    fig, axs = plt.subplots(2, figsize=(6, 6), sharex=True)
    x, y = lcs.MANCHESTER(bits)
    axs[0].plot(x, y, linewidth=3)
    axs[0].set(ylabel='Amplitude', title='Biphase: Manchester')
    axs[0].set_xticks([x for x in range(len(bits)+1)])
    axs[0].set_yticks([-1.5, -1, -0.5, 0, 0.5, 1, 1.5])
    axs[0].set_yticklabels(['', '-1', '', '0', '', '1', ''])
    axs[0].grid()
    x, y, ix0, i0, ix1, i1 = lcs.diff_MANCHESTER(bits, startbit)
    axs[1].plot(x, y, linewidth=3)
    axs[1].plot(ix0, i0, 'o', markeredgecolor="black", markerfacecolor="white", markersize=7, label="No Inversion: Next bit is 1")
    axs[1].plot(ix1, i1, 'ok', markersize=7, label="Inversion: Next bit is 0s")
    axs[1].legend(loc='lower right', prop={'size': 5.5})
    axs[1].set(xlabel='Time', ylabel='Amplitude', title='Differential Manchester')
    axs[1].set_xticks([x for x in range(len(bits)+1)])
    axs[1].set_yticks([-1.5, -1, -0.5, 0, 0.5, 1, 1.5])
    axs[1].set_yticklabels(['', '-1', '', '0', '', '1', ''])
    axs[1].grid()
    plt.show()

def plot_Bipolar(bits):
    fig, axs = plt.subplots(2, figsize=(6, 6), sharex=True)
    x, y = lcs.AMI(bits)
    axs[0].plot(x, y, linewidth=3)
    axs[0].set(ylabel='Amplitude', title='Bipolar: AMI(Alternate Mark Inversion)')
    axs[0].set_xticks([x for x in range(len(bits)+1)])
    axs[0].set_yticks([-1.5, -1, -0.5, 0, 0.5, 1, 1.5])
    axs[0].set_yticklabels(['', '-1', '', '0', '', '1', ''])
    axs[0].grid()
    x, y = lcs.Pseudoternary(bits)
    axs[1].plot(x, y, linewidth=3)
    axs[1].set(xlabel='Time', ylabel='Amplitude', title='Bipolar: Pseudoternary')
    axs[1].set_xticks([x for x in range(len(bits)+1)])
    axs[1].set_yticks([-1.5, -1, -0.5, 0, 0.5, 1, 1.5])
    axs[1].set_yticklabels(['', '-1', '', '0', '', '1', ''])
    axs[1].grid()
    plt.show()
