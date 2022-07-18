# Module 3, Deliverable 3: 03-election-analysis

## Project Overview
Initially we were helping our friends Seth and Tom to do an analysis on the election results, based on the data source provided under "Resources". After we completed our initial analysis, the Colorado Board of Elections commission gave me some additional tasks to complete the election audit of a recent local congressional election. 

1. Find the total number of votes cast
2. Make a complete list of candidates who received votes
3. Calculate the total number of votes each candidate received
4. Calculate the percentage of votes each candidate won
5. Determine the winner of the election based on popular vote
6. Make a total list of counties where votes were cast from.
7. Calculate the total number of votes from each county.
8. Calculate the percentage of votes from each county.
9. Determine the county with the largest voter turnout.

## Resources
- Data Source: election_results.csv
- Software: Python 3.10.5, Visual Studio Code 1.69.1

## Results
An analysis of the election results show that:
- There were 369,711 total votes cast in the election.
- The results of each candidate were:
    - Charles Casper Stockham: 23.0% of the total vote (85,213 votes)
    - Diana DeGette: 73.8% of the total vote (272,892 votes)
    - Raymon Anthony Doane: 3.1% of the total vote (11,606 votes)
- The results for the winner are:
    - Winning candidate: Diana DeGette
    - Winning vote Count: 272892
    - Winning percentage: 73.8%
- The number of votes cast from each county:
    - Jefferson: 10.5% of the total vote (38,855 votes)
    - Denver: 82.8% of the total vote (306,055 votes)
    - Arapahoe: 6.7% of the total vote (24,801 votes)
- The results for the county with the largest voter turnout:
    - County with the largest voter turnout: Denver
    - Percentage of total votes: 82.8%
    - Total votes from this county: 306,055

The results will print to the terminal as follows:

![Election Results: Terminal Print](https://github.com/etdirksen/03-election-analysis/blob/main/Resources/election_terminal_print.png)

## Summary
This would make a great tool for future elections! It can handle large amounts of data and provide a quick summary of the results. It also outputs to a file that can be shared with others. The script is flexible, and is already built to keep tally of votes cast from non-predetermined counties, voter IDs, and for running candidates.

As it stands, the data that we analyzed had limited information about our candidates. So far we are only keeping track of their names. We could modify the code to include biographies and output this information to the text file. We could also include information about the policies that each candidate wants to focus on in the same way, and put this in the text file to see at a glance. This way we can keep track of how the area is evolving after implementing these policies as well as what kind of candidate the area has favored over the next several years.
