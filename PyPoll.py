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

# We use 'with' to open the file stored in the variable as a new variable, election_data, so that we do not have to worry about closing the file at the end of the program.
with open(file_to_load, "r") as election_data:
    file_reader = csv.reader(election_data)
    headers = next(file_reader)
    print(headers)

    '''
    for row in file_reader:
        print(row)
=======
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

# We use 'with' to open the file stored in the variable as a new variable, election_data, so that we do not have to worry about closing the file at the end of the program.
with open(file_to_load, "r") as election_data:
    file_reader = csv.reader(election_data)
    headers = next(file_reader)
    print(headers)

    '''
    for row in file_reader:
        print(row)