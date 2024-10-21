# import modules
import os
import csv

# ---------------------------
# setup file paths & analysis
# ---------------------------

# define existing input file and desired output file 
infile_pybank = "budget_data.csv"
outfile_pybank = "pybank_output.txt"

# specify file paths for input and output files
infile_path_pybank = os.path.join("Resources", infile_pybank)
outfile_path_pybank = os.path.join("Analysis", outfile_pybank)

# initialize variables for analysis
total_months = 0
total_profit = 0
previous_profit = None
profit_changes = []


# ---------------------------
# read and analyze input file
# ---------------------------

try:
    # if input file doesn't exist then raise error
    if not os.path.exists(infile_path_pybank):
        raise FileNotFoundError
    
    # check if analysis folder exists and create one if it doesn't
    os.makedirs("Analysis", exist_ok = True)

    # open input file using "read" mode
    with open(infile_path_pybank, 'r', newline='') as infile:

        # read input file
        reader = csv.reader(infile)

        # capture the header row and skip it
        csv_header = next(reader)

        # read through each row of data
        for row in reader:
            
            # capture month and profit values
            month = row[0]
            profit_str = row[1]

            # if profit value is not a number then raise error
            if not profit_str.lstrip('-').isdigit():
                raise TypeError
            else:
                profit = float(profit_str)

            # increment values
            total_months += 1
            total_profit += profit

            # capture profit changes along with corresponding month
            if previous_profit != None:
                profit_changes.append((month, profit - previous_profit))

            # update previous profit value
            previous_profit = profit

        # profit change calculations
        avg_change = sum(map(lambda x: x[1], profit_changes))/len(profit_changes)
        max_change_month, max_change = max(profit_changes, key=lambda x: x[1])
        min_change_month, min_change = min(profit_changes, key=lambda x: x[1])

        # print financial analysis
        output_width = 55
        print("-------------------------------------------------------")
        print("Financial Analysis".center(output_width))
        print("-------------------------------------------------------")
        print(f"Total Months: {total_months}")
        print(f"Total Profit/Loss: ${total_profit:,.2f}")
        print(f"Average Change: ${avg_change:,.2f}")
        print(f"Greatest Increase in Profits: {max_change_month} (${max_change:,.2f})")
        print(f"Greatest Decrease in Profits: {min_change_month} (${min_change:,.2f})")
        print("-------------------------------------------------------")

# error messages when trying to read/analyze input file
except FileNotFoundError:
    # if input file isn't found show error
    print(f"FileNotFoundError: Input CSV file, {infile_pybank}, not found.")
except TypeError:
    # if a profit value isn't a number
    print("TypeError: Make sure profit values are numerical.")
except:
    # something else went wrong
    print("Error: Something went wrong during input file process. Try checking input file.")


# -----------------------------
# write analysis to output file
# -----------------------------

try:
    # check if analysis folder exists and create one if it doesn't
    os.makedirs("Analysis", exist_ok = True)

    # open output file using "write" mode
    with open(outfile_path_pybank, 'w', newline='') as outfile:

        # write fincial analysis onto output file
        outfile.write("-------------------------------------------------------\n")
        outfile.write(f"{"Financial Analysis".center(output_width)}\n")
        outfile.write("-------------------------------------------------------\n")
        outfile.write(f"Total Months: {total_months}\n")
        outfile.write(f"Total Profit/Loss: ${total_profit:,.2f}\n")
        outfile.write(f"Average Change: ${avg_change:,.2f}\n")
        outfile.write(f"Greatest Increase in Profits: {max_change_month} (${max_change:,.2f})\n")
        outfile.write(f"Greatest Decrease in Profits: {min_change_month} (${min_change:,.2f})\n")
        outfile.write("-------------------------------------------------------\n")

except:
    # error occured
    print("Something went wrong during output process. Please check accordingly.")