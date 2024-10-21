# import modules
import os
import csv

# ---------------------------
# setup file paths & analysis
# ---------------------------

# needed files
infile_pypoll = "election_data.csv"
outfile_pypoll = "pypoll_output.txt"

# define file paths
infile_path_pypoll = os.path.join("Resources", infile_pypoll)
outfile_path_pypoll = os.path.join("Analysis", outfile_pypoll)

# define variables for analysis
total_votes = 0
name_counts = {}
id_values = []

# ---------------------------
# read and analyze input file
# ---------------------------

try:
    # check if input file exists
    if not os.path.exists(infile_path_pypoll):
        raise FileNotFoundError

    # open input file using "read" mode
    with open(infile_path_pypoll, 'r', newline='') as infile:
    
        # read input file
        reader = csv.reader(infile)

        # save and skip header row
        csv_header = next(reader)
        
        # read through each row of data
        for row in reader:

            # capture voter ID and candidate name
            #voter_id = row[0]
            id_values.append(row[0])
            name = row[2]

            # increment total votes value
            total_votes += 1

            # count each candidate's name's occurence
            if name in name_counts:
                # increment count for existing name
                name_counts[name] += 1
            else:
                # initilialize value for new name
                name_counts[name] = 1
    
    # check for duplicate voter id values
    if total_votes > len(set(id_values)):
        # raise error if duplicate ids found
        raise ValueError
    
    # --------------------------
    # print analysis to terminal
    # --------------------------

    # set title
    output_width = 55
    print("-------------------------------------------------------")
    print("Election Results".center(output_width))
    print("-------------------------------------------------------")

    # display total votes
    print(f"Total Votes: {total_votes:,}\n\n")

    # calculate voting results per candidate
    for name, count in name_counts.items():

        # calculate percentage of votes
        vote_percent = (count/total_votes)*100

        # print candidate's voting result
        print(f"{name}: {vote_percent:.3f}% ({count:,})")

    # show candidate with highest vote count
    winner = max(name_counts, key=name_counts.get)
    print(f"\n\nWinner: {winner}")
    print("-------------------------------------------------------")

# error messages when trying to read/analyze input file
except FileNotFoundError:
    print(f"FileNotFoundError: Input CSV file, {infile_pypoll}, not found.")
except ValueError:
    print("ValueError: Duplicate voter IDs found.")
except:
    print("Error: Something went wrong during input file process. Try checking input file.")


# write output file