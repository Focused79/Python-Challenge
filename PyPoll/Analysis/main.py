
# Import os and csv modules:

import os
import csv

# Set path with os module:

csvpath = os.path.join("c:/Users/Albrecht/Desktop/BC Class Repo/SMU-VIRT-DATA-PT-12-2023-U-LOLC/Python-Challenge/PyPoll/Resources/election_data.csv")

# Output file path:

output_text_path = "output.txt"

# Open csv file and assign it to csv variable 'csvfile':

with open(csvpath) as csvfile:

    # Initialize CSV reader, interpreting first row of column headers:

    csvreader = csv.DictReader(csvfile)
    
    # Start count at 0:

    total = 0
    
    # Loop through to count each value in row:

    for row in csvreader:
        total += 1

# Open the output file in write mode:

with open(output_text_path, 'w') as output_file:

    # Print/Write output to file and terminal, respectively:

    print("Election Results", file=output_file)
    print("--------------------------", file=output_file)
    print(f"Total Votes Cast: {total}", file=output_file)
    print("---------------------------", file=output_file)
    print("Election Results")
    print("--------------------------")
    print(f"Total Votes Cast: {total}")
    print("---------------------------")

# Path and csvreader function copied below to carry out new tasks:

with open(csvpath) as csvfile:
    csvreader = csv.DictReader(csvfile)

    # Variable utilization to start count at 0 and a dictionary to store the number of votes each candidate received, respectively:

    total_votes = 0
    candidate_votes = {}

    # Loop through rows in csv:

    for row in csvreader:
        
        #Count total votes and votes for each candidate:
        
        total_votes += 1
        candidate = row['Candidate']

        # Incrementing votes by candidate:

        candidate_votes[candidate] = candidate_votes.get(candidate, 0) + 1

# Loop through three candidates to calculate and print percentages to output file:

with open(output_text_path, 'a') as output_file:
        
    for candidate, votes in candidate_votes.items():
        percentage = (votes/total_votes) * 100
        print(f"{candidate}: {percentage: .3f}% ({votes})", file=output_file)

        # Also print calculations to terminal:

        print(f"{candidate}: {percentage: .3f}% ({votes})")


    # Print seperating line to output file and terminal:

    print("--------------------------", file=output_file)
    print("--------------------------")
    
    # Find winner and print to file and terminal:

    winner = max(candidate_votes, key=candidate_votes.get)
    print(f"Winner: {winner}", file=output_file)
    print(f"Winner: {winner}")

    # Print seperating line to file and terminal:

    print("--------------------------", file=output_file)
    print("--------------------------")
          
# Verify in terminal that the output has been written in output file:

print(f"Results written to: {output_text_path}")









