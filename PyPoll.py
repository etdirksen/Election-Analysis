'''
This file will read the election_results.csv file, format it without the commas, and print it out line by line.

We will also display these stats:

-Total number of votes cast
-A complete list of candidates who received votes
-Total number of votes each candidate received
-Percentage of votes each candidate won
-The winner of the election based on popular vote 
'''
# We need to import the os module to interact with our OS, to tell our program to navigate to the folder where the 'election_results.csv' file is located.
# We need to import the csv module to more easily handle a csv file. This gives us access to variables and functions that were already written to read and parse the data from the file.

from asyncore import write
from cgitb import text
import os
import csv

# We create a variable to hold the location of our csv file.
# We use the join() function from the os module to join together the near-full path location with the name of the file.
dir_path = os.path.dirname(__file__)
file_to_load = os.path.join(dir_path,"Resources\election_results.csv")

#with open(file_to_load) as election_data:
#    print(election_data)

# Now we are going to write to a text file.
file_to_save = os.path.join(dir_path,"analysis\election_analysis.txt")

total_votes = 0
candidate_options = []
candidate_votes = {}

winning_candidate = ""
winning_count = 0
winning_percentage = 0

# We use 'with' to open the file stored in the variable as a new variable, election_data, so that we do not have to worry about closing the file at the end of the program.
with open(file_to_load, "r") as election_data:
    file_reader = csv.reader(election_data)
    headers = next(file_reader)
    print(headers)

    for row in file_reader:
        candidate_name = row[2]
        
        
        if candidate_name not in candidate_options:
            candidate_options.append(candidate_name)
            candidate_votes[candidate_name] = 0
        
        candidate_votes[candidate_name] += 1
        total_votes += 1
    
for candidate_name in candidate_votes:
    votes = candidate_votes[candidate_name]
    vote_percentage = float(votes) / float(total_votes) * 100
    if (votes > winning_count) and (vote_percentage > winning_percentage):
        winning_count = votes
        winning_percentage = vote_percentage
        winning_candidate = candidate_name

header_election_results = (
    f"Election Results\n"
    "-------------------------------------------------\n"
    f"Total votes: {total_votes:,}\n"
    "-------------------------------------------------"
)
print(header_election_results)

for item in candidate_options:
    print(
        f"{item}: {(candidate_votes[item] / total_votes) * 100:.1f}% ({candidate_votes[item]:,})"
    )
print("-------------------------------------------------")

winning_election_results = (
    f"Winning candidate: {winning_candidate}\n"
    f"Winning vote Count: {winning_count:,}\n"
    f"Winning percentage: {winning_percentage:.1f}%"
)
print(winning_election_results)
    
with open(file_to_save,"w") as text_file:
    text_file.write(header_election_results + "\n")
    text_file.write(winning_election_results)