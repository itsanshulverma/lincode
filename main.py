###########################################
#   Line Coding Schemes Plotter
#   Author: Anshul Verma
#   github.com/itsanshulverma
###########################################

from line_code import plot_schemes as pl

def main():
    print("\n===================== Menu ======================")
    print("1. Unipolar NRZ")
    print("2. Polar NRZ-L & NRZ-I")
    print("3. Polar RZ")
    print("4. Biphase Manchester & Differential Manchester")
    print("5. Bipolar AMI & Pseudoternary")
    print("6. Exit")
    print("=================================================")
    ch = int(input("Choice: "))
    if ch == 6:
        quit()
    elif ch>=1 and ch<=5:
        bits = input("Input Bits: ")
        print("Plotting figure...Done!\nOpening figure window...")
        if ch == 1:
            pl.plot_UNRZ(bits)
        elif ch == 2:
            pl.plot_PNRZ(bits)
        elif ch == 3:
            pl.plot_PRZ(bits)
        elif ch == 4:
            pl.plot_Biphase(bits)
        elif ch == 5:
            pl.plot_Bipolar(bits)
        print("Closing figure window...Done!")
    else:
        print("Invalid choice!")

if __name__ == "__main__":
    ch = 'Y'
    while(ch=='y' or ch=='Y'):
        main()
        ch = input("\nContinue? [Y/N] : ")