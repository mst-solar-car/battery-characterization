import constants as const

#import colors


# Constants
# Get us some fancy colors
GREEN = '\033[92m'
YELLOW = '\033[93m'
RED = '\033[91m'
WHITE = '\033[37m'
END_COLOR = '\033[30m'



# Function declarations

# NOTE: All color altering functions are not used at the moment - they break the program
'''
# printErr(...) prints the given message to the screen in red
def printErr(msg):
    print(RED + msg + END_COLOR)

# printGreen(...) prints the given message to the screen in green
def printGreen(msg):
    print(GREEN + msg + END_COLOR)

# printYella(...) prints the given message to the screen in yellow
def printYella(msg):
    print(YELLOW + msg + END_COLOR)

def output(str):
    print(WHITE + str + END_COLOR)
    output_file.write(str)
    output_file.write("\n")
'''

# sortByCap_Res(...) (bubblesort) sorts the given list first on capacity then on resistance
def sortByCap_Res(list):
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

# sortByModule(...) (bubblesort) sorts the given list based on module number
def sortByModule(list):
    n = len(list)
    swapped = True
    while swapped:
        swapped = False
        for i in range(1, n):
            # if the pair is out of order
            if list[i-1].module > list[i].module:
                # swap
                tmp = list[i-1]
                list[i-1] = list[i]
                list[i] = tmp
                swapped = True

# getMaxModule(...) finds the largest module in the given list of batteries
def getMaxModule(list):
    maxModule = const.DAMN_SMALL_NUMBER
    for batt in list:
        if batt.module > maxModule:
            maxModule = batt.module
    return maxModule
