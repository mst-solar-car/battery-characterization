import os
import csv
import sys
import math
import time
import battery
import functions as funcs
import constants as const

# Clear the console screen
os.system('cls')

fileName = ""

# Read command line arguments
if len(sys.argv) > 1:
    fileName = sys.argv[1]
else:
    # Find the first CSV (alphabetically) in the current directory
    for subfile in os.listdir(os.getcwd()):
        if subfile.endswith(".csv"):
            fileName = subfile
            break


# Open and prepare the file
# Check to see if the file exists
if fileName and os.path.exists(fileName):
    file = open(fileName, 'r+')
    csv_file = csv.reader(file, delimiter=',')
else:
    print("The provided filename can't be found. Exiting program.")
    exit()


# Get data from the csv and store it in the battery list
batteries = []
characterizedBatts = []
battIndex = 0   # Current index for batteries list
charBattIndex = 0   # Current index for the characterizedBatts list

count = 0   # Start recording batteries once the count is 2
            # Actual data starts on the 3rd line of the CSV
for row in csv_file:
    if count >= 2:
        id = row[0]
        capacity = row[1]
        resistance = row[2]
        module = row[4]

        # Check to make sure we have data and make sure the cell module cell is
        # empty so we don't double dip when making modules
        if id != "" and capacity != "" and resistance != "":
            # Convert each id, capacity, and module from strings to their proper datatype
            id = int(id)
            capacity = int(capacity)
            resistance = float(resistance)

            if module == "":
                # This battery still needs to be placed in a module
                # Put it in the batteries list to be sorted
                newBat = battery.BatteryCell(id, capacity, resistance, -1) # Cells without modules have a module value of -1
                batteries.insert(battIndex, newBat)
                battIndex = battIndex + 1
            else:
                # This battery has already been sorted
                # Cast the value to an integer
                module = int(module)

                # Put it in the characterizedBatts list so they aren't resorted
                newBat = battery.BatteryCell(id, capacity, resistance, module)
                characterizedBatts.insert(charBattIndex, newBat)


                '''if capacity != 0 and resistance != 0:
                    newBat = battery.BatteryCell(int(id), int(capacity), float(resistance))
                    batteries.insert(battIndex, newBat)
                    battIndex = battIndex + 1'''

    count = count + 1
file.close()


# Sort the batteries list by resistances
sortedBatts = batteries
funcs.sortByCap_Res(sortedBatts)

# Sort the characterizedBatts list by module for easy display
funcs.sortByModule(characterizedBatts)


# TODO: Calculate std. deviation and actually do more intense statistical analysis


''' Group Cells '''

# Create list of used module #'s
usedModules = []
for batt in characterizedBatts:
    if not (batt.module in usedModules):
        usedModules.append(batt.module)

#  Get the current module we are assembling so we don't double up on module names
cellLabels = []
for i in range(0, const.PACK_CELLS):
    if not (i in usedModules):
        cellLabels.append(i)

# dummy cell to populate the module array
batt = battery.BatteryCell(0,0,0,-1)

# Modules array - 2D list of size MODULE_CELLS x CURRENT_NUM_MODULES
# floor(total num cells / num cells per module) gives us the number of modules
CURRENT_NUM_MODULES = math.floor(len(sortedBatts)/const.MODULE_CELLS)
modules = [[batt for x in range(const.MODULE_CELLS)] for y in range(CURRENT_NUM_MODULES)]

# Counting variables
moduleCount = 0
battCount = 0

# Populate the module array
for batt in sortedBatts:
    # Fill up each row in the array - rows have MODULE_CELLS open spaces
    if battCount < const.MODULE_CELLS:
        modules[moduleCount][battCount] = batt
        battCount = battCount + 1
    else:
        # Reset the counter
        moduleCount = moduleCount + 1
        battCount = 0
        modules[moduleCount][battCount] = batt


# Calculate the worst capacity for each module, store that into an a array
index = 0
worstCapacities = []
for row in modules:
    worstCapacity = const.DAMN_BIG_NUMBER
    for elem in row:
        if elem.capacity < worstCapacity:
            worstCapacity = elem.capacity
    worstCapacities.insert(index, worstCapacity)
    index = index + 1

# Get the total resistance for each module
index = 0
totalResistances = []
for row in modules:
    denominator = 0
    for elem in row:
        if elem.resistance != 0:
            denominator = denominator + (1 / elem.resistance)

    if denominator != 0:
        totalResistances.insert(index, 1 / denominator)
    index = index + 1



# Create file for saving the output of the modules
file_name = "output_" + str(time.time()) + ".txt"
output_file = open(file_name, 'w')



# Print the final modules along with the worst capacity of each module
index = 0
for row in modules:
    print("Module " + str(cellLabels[index]))
    print("Capacity: " + str(worstCapacities[index-1]))
    print("Resistance: " + str(totalResistances[index-1]))
    print("ID\t\tResistance\tCapacity")
    for elem in row:
        if elem.resistance != 0: # Are there still valid batteries in the list
            # Adjust the tabbing accordingly
            if elem.resistance < 100:
                print(str(elem.id)+ "\t\t" + str(elem.resistance)+ "\t\t"+ str(elem.capacity))
            else:
                print(str(elem.id)+ "\t\t", str(elem.resistance)+ "\t"+ str(elem.capacity))
    print("\n")
    index = index + 1
    moduleCount = moduleCount + 1
    input("Press Enter to show the next module")
    os.system('cls')

output_file.close()
