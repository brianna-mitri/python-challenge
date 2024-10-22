# Python Challenge
Only use Python's os and csv modules to separately analyze financial and voter datasets, and generate outputs through both exported text files and the terminal.

Also includes error handling to help figure out what went wrong and whether it was during the input or output process.

## Python Scripts
**PyBank.py:** analyze financial dataset to generate the following:
```
-------------------------------------------------------
                   Financial Analysis                  
-------------------------------------------------------
Total Months: 86
Total Profit/Loss: $22,564,198.00
Average Change: $-8,311.11
Greatest Increase in Profits: Aug-16 ($1,862,002.00)
Greatest Decrease in Profits: Feb-14 ($-1,825,558.00)
-------------------------------------------------------
```

**PyPoll.py:** analyze voter count dataset to generate the following:
```
-------------------------------------------------------
                    Election Results                   
-------------------------------------------------------
Total Votes: 369,711


Charles Casper Stockham: 23.049% (85,213)
Diana DeGette: 73.812% (272,892)
Raymon Anthony Doane: 3.139% (11,606)


Winner: Diana DeGette
-------------------------------------------------------
```

## Error Handling
These error messages are printed depending on the following issues:
- **FileNotFoundError:** shows if input file isn't found so double check file path.
- **ValueError:** shows with unexpected input data formats.
    - ***PyBank:*** profit/loss column values aren't all numbers.
    - ***PyPoll:*** duplicate voter ID column values found.
- **Input/Analysis Error:** something went wrong during input/analysis process.
- **Output Error:** something when during the output process (outputting analysis into the text file and terminal).

To prevent a FileNotFoundError for the output file, the following code has been added so that if the Analysis folder isn't found then it will be created for the outputted text file to go into:
```os.makedirs("Analysis", exist_ok=True)```

## Expected Data Format
The input csv files are expected to have a header row and the following columns:
- **PyBank's input file:** *Date column* (monthly dates in chronological order), *Profit/Loss column* (only digit values with - for negatives).
- **PyPoll's input file:** *Voter ID column* (first column with unique values), *Candidate's Name column* (third column).

## Files
For the Python scripts to work the files are expected to be in the following format within their respective *PyBank* and *PyPoll* folders:
- **Analysis**[^1]
    - **output_file.txt**
- **Resources**
    - **input_file.csv**
- **main.py**

[^1]: Analysis folder and output_file.txt don't need to be created before running the script. The script should generate them both.