import os

NUM_RESISTANCES = 4

while(True):
    os.system('cls')
    print("Enter 4 resistances")
    a = int(input("First: "))
    b = int(input("Second: "))
    c = int(input("Third: "))
    d = int(input("Fourth: "))

    avg = (a + b + c + d) / NUM_RESISTANCES
    print("Average:", avg)
    input("press enter to continue")
