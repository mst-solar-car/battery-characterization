import os
import csv
import sys
import math
from colorama import init

# Constants
PACK_CELLS = 420
MODULE_CELLS = 12
DAMN_BIG_NUMBER = 10000000000000000

# Get us some fancy colors
init()  # Initialize colorama
YELLOW = '\033[93m'
RED = '\033[91m'
END_COLOR = '\033[30m'

# Class definitions
class BatteryCell:
    capacity = reistance = id = 0

# Function declarations

# printErr(...) prints the given message to the screen in red
def printErr(msg):
    print(RED + msg + END_COLOR)

# sort(...) (bubblesort) sorts the given list first on capacity then on resistance
def sort(list):
    n = len(list)
    swapped = True
    while swapped:
        swapped = False
        for i in range(1, n):
            # if the pair is out of order
            if list[i-1].capacity > list[i].capacity:
                # swap
                tmp = list[i-1]
                list[i-1] = list[i]
                list[i] = tmp
                swapped = True
            elif list[i-1].capacity == list[i].capacity:
                if list[i-1].resistance > list[i].resistance:
                    # swap
                    tmp = list[i-1]
                    list[i-1] = list[i]
                    list[i] = tmp
                    swapped = True


# Read command line arguments
if len(sys.argv) > 1:
    fileName = sys.argv[1]
else:
    printErr("Include the file name as a commandline parameter.")
    sys.exit();


# Open and prepare the file
file = open(fileName, 'r+')
csv1 = csv.reader(file, delimiter=',')


# Get data from the csv and store it in the battery array
batteries = []
battIndex = 0   # Current index for batts array
count = 0   # Start recording batteries once the count is 2
for row in csv1:
    if count >= 1:
        newBat = BatteryCell()
        newBat.id = int(row[0])
        newBat.capacity = int(row[1])
        newBat.resistance = float(row[2])
        batteries.insert(battIndex, newBat)
        battIndex = battIndex + 1
    else:
        count = count + 1


# Sort the battery array by resistances
sortedBats_resistance = batteries
sort(sortedBats_resistance)


# TODO: Calculate std. deviation and do more intense statistical analysis


# Group Cells

# dummy cell to populate the module array
batt = BatteryCell()
batt.id = batt.resistance = batt.capacity = 0

# Modules array
modules = [[batt for x in range(MODULE_CELLS)] for y in range(math.floor(len(sortedBats_resistance)/MODULE_CELLS))]

# Counting variables
moduleCount = 0
battCount = 0

# Populate the module array
for batt in sortedBats_resistance:
    # Fill up each row in the array - rows have MODULE_CELLS open spaces
    if battCount < MODULE_CELLS:
        modules[moduleCount][battCount] = batt
        battCount = battCount + 1
    else:
        # Reset the counter
        moduleCount = moduleCount + 1
        battCount = 0
        modules[moduleCount][battCount] = batt


# Calculate the worst capacity for each module, store that into an a array
count = 0
worstCapacities = []
for row in modules:
    worstCapacity = DAMN_BIG_NUMBER
    for elem in row:
        if elem.capacity < worstCapacity:
            worstCapacity = elem.capacity
    worstCapacities.insert(count, worstCapacity)
    count = count + 1

# Get the total resistance for each module
index = 0
totalResistances = []
for row in modules:
    denominator = 1
    for elem in row:
        if elem.resistance != 0:
            denominator = denominator + (1 / elem.resistance)

    totalResistances.insert(index, 1 / denominator)
    index = index + 1


# Print the final modules along with the worst capacity of each module
count = 1
print("ID\t\tResistance\tCapacity")
for row in modules:
    print("Module", count)
    print("  Capacity: ", worstCapacities[count-1])
    print("  Resistance: ", totalResistances[count-1])
    for elem in row:
        if elem.resistance != 0: # Are there still valid batteries in the list
            # Adjust the tabbing accordingly
            if elem.resistance < 100:
                print(elem.id, "\t\t", elem.resistance, "\t\t", elem.capacity)
            else:
                print(elem.id, "\t\t", elem.resistance, "\t", elem.capacity)
    print("\n")
    count = count + 1
