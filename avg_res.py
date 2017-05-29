'''
    avg_res.py reads NUM_RESISTANCES resistance values from the reader
    and outputs their average.

    This is done forever or until the user stops the program.

    Used when entering in battery info. into the spreadsheet.
'''
import os

NUM_RESISTANCES = 4

while(True):
    os.system('cls')

    print("Enter " + str(NUM_RESISTANCES) + " resistances\n")

    # Calculate the numerator of our average equation
    numerator = 0
    for i in range(0, NUM_RESISTANCES):
        # Get resistance from the user and add it to the numerator
        res = int(input("Value " + str(i) + ": "))
        numerator = numerator + res

    # Calculate the average and output it
    avg = numerator / NUM_RESISTANCES
    print("\nAverage:", avg)
    input("\nPress enter to continue")
