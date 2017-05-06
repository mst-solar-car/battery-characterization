# S&T Solar Car Battery Grouping

## Install Dependencies
This program uses the colorama module for python.

Install on Windows using

    > py -m pip install colorama
or

    > python -m pip install colorama

## Running the program

    > py main.py (filename)
or

    > python main.py (filename)
Where (filename) is a `CSV file` in the same directory as `main.py` and you have `Python 3` installed.

## Functionality overview

1. Reads data from a `CSV file` containing capacity and internal resistance for any number of cells. That data is stored into a list for easy manipulation.
2. The battery statistics are analyzed and groupings of 12 cells each are made using metrics yet to be determined.

## What if the battery pack structure changes?

It is highly possible that in the future, the structure of the battery pack will change and therefore the batteries will need to be characterized differently.
The code present in this project is generic enough to be used on future packs with only *minor* tweaks such as the alteration of the following constants:

    PACK_CELLS = 420;
    MODULE_CELLS = 12;

These variables govern the number of cells in the pack as a whole and the number of cells per parallel grouping (module) respectively.
