# S&T Solar Car Battery Grouping


## Where do I start?
Several resistance values are averaged from each channel's reading on our battery testers. So if you are filling in the battery `CSV`, you can run `avg_res.py` for easy average resistance calculations.

If you are assembling battery modules, run `main.py` on the battery `CSV` to spit out which cell belongs in which module.

# avg_res.py

## Functionality overview
1. Reads some resistance values from the user (one resistance per channel in our battery testers).
2. Displays the average of the resistances.

## Running the script
Open the command prompt in the same directory that `avg_res.py` is in. Type the following command:

    > py avg_res.py


# main.py

## Functionality overview
1. Reads data from a `CSV file` containing a cell ID, capacity, and internal resistance for any number of cells. That data is stored into a list for easy manipulation.
2. The batteries are sorted in ascending order first by resistance then by capacity.
3. The battery cell numbers along with information about each cell is then
outputted to the screen by module as assembly instructions.


## Input file layout
The input `CSV file` should look like this:

| Cell Number   | Capacity   | Internal Resistance  | Module |
| :------------:|:----------:| --------------------:|--------|
| 1             | 3000       | 75                   | 1      |
| 2             | 3380       | 80                   | 1      |

etc.

With commas ( , ) as the delimiters.


## Running the script
Open the command prompt in the same directory where `main.py` and the `CSV file` containing the data are located. Run the following command:

    > py main.py <filename>

Where `<filename>` is the `CSV file`.

If you omit `<filename>` the program will use the **first** csv it finds in the directory the script is running in.

## What if the battery pack structure changes?

It is highly possible that in the future, the structure of the battery pack will change and therefore the batteries will need to be characterized differently.
The code present in this project is generic enough to be used on future packs with only *minor* tweaks such as the alteration of the following constants:

    PACK_CELLS = 420
    MODULE_CELLS = 12

These variables govern the number of cells in the pack as a whole and the number of cells per parallel grouping (module) respectively.
