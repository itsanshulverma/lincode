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
        if ch == 1:
            print("Plotting figure...Done!\nOpening figure window...")
            pl.plot_UNRZ(bits)
        elif ch == 2:
            startbit = int(input("Start Bit: "))
            print("Plotting figure...Done!\nOpening figure window...")
            pl.plot_PNRZ(bits, startbit)
        elif ch == 3:
            print("Plotting figure...Done!\nOpening figure window...")
            pl.plot_PRZ(bits)
        elif ch == 4:
            startbit = int(input("Start Bit: "))
            print("Plotting figure...Done!\nOpening figure window...")
            pl.plot_Biphase(bits, startbit)
        elif ch == 5:
            print("Plotting figure...Done!\nOpening figure window...")
            pl.plot_Bipolar(bits)
        print("Closing figure window...Done!")
    else:
        print("Invalid choice!")

if __name__ == "__main__":
    ch = 'Y'
    while(ch.lower() =='y'):
        main()
        ch = input("\nPress Y to continue? : ")