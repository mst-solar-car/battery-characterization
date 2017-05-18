# S&T Solar Car Battery Grouping

## Functionality overview
1. Reads data from a `CSV file` containing a cell ID, capacity, and internal resistance for any number of cells. That data is stored into a list for easy manipulation.
2. The batteries are sorted in ascending order first by resistance then by capacity.

## Input file layout
The input `CSV file` should look like this:

| Cell Number   | Capacity   | Internal Resistance  | Module |
| :------------:|:----------:| --------------------:|--------|
| 1             | 3000       | 75                   | 1      |
| 2             | 3380       | 80                   | 1      |

etc.

With commas ( , ) as the delimiters.

## Install Dependencies
This program uses the `colorama` module for python.

Install on Windows using

    > py -m pip install colorama

or

    > python -m pip install colorama

## Run the program
Open the command prompt in the same directory where `main.py` and the `CSV file` containing the data are located. Run the following command:
    > py main.py (filename)

Where (filename) is the `CSV file`.

## What if the battery pack structure changes?

It is highly possible that in the future, the structure of the battery pack will change and therefore the batteries will need to be characterized differently.
The code present in this project is generic enough to be used on future packs with only *minor* tweaks such as the alteration of the following constants:

    PACK_CELLS = 420;
    MODULE_CELLS = 12;

These variables govern the number of cells in the pack as a whole and the number of cells per parallel grouping (module) respectively.
