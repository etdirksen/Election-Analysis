""" counties = ["Arapahoe","Denver","Jefferson"]
if "El Paso" in counties:
    print("El Paso is in the list of counties.")
else:
    print("El Paso is not in the list of counties.") """

""" my_votes = int(input("How many votes did you get in the election? "))
total_votes = int(input("What is the total votes in the election? "))
print(f"I received {my_votes / total_votes * 100}% of the total votes.") """

'F-String skill drill'
""" counties_dict = {"Arapahoe": 369237, "Denver":413229, "Jefferson": 390222}
for county, voters in counties_dict.items():
    print(f"{county} has {voters} registered voters.") """

""" candidate_votes = int(input("How many votes did the candidate get in the election? "))
total_votes = int(input("What is the total number of votes in the election? "))
message_to_candidate = (
    f"You received {candidate_votes:,} votes. "
    f"The total number of votes in the election was {total_votes:,}. "
    f"You received {candidate_votes / total_votes * 100:.3f}% of the total votes.")

print(message_to_candidate) """

""" counties_dict = {"Arapahoe": 422829, "Denver": 463353, "Jefferson": 432438}
for county, voters in counties_dict.items():
    print(f"{county} has {voters} voters.") """

"""
This is a list of dictionaries. I want to get every item in the list (every dictionary) and then I want to print each (key, value) pair from each dictionary. There are two keys to
each dictionary 'county' and 'registered_voters', so when I am iterating through the list, I want to specify each key that I want the value from.
"""
"""voting_data = [{"county":"Arapahoe", "registered_voters": 422829}, {"county":"Denver", "registered_voters": 463353}, {"county":"Jefferson", "registered_voters": 432438}]
for voter_dict in voting_data:
    print(f"{voter_dict['county']} has {voter_dict['registered_voters']:,} registered voters.")

voting_data[0]['county'] = "Nothing"
for voter_dict in voting_data:"""
""" 
counties = ["Arapahoe","Denver","Jefferson"]
if "El Paso" in counties:
    print("El Paso is in the list of counties.")
else:
    print("El Paso is not in the list of counties.") 
"""

""" my_votes = int(input("How many votes did you get in the election? "))
total_votes = int(input("What is the total votes in the election? "))
print(f"I received {my_votes / total_votes * 100}% of the total votes.") """

'F-String skill drill'
""" counties_dict = {"Arapahoe": 369237, "Denver":413229, "Jefferson": 390222}
for county, voters in counties_dict.items():
    print(f"{county} has {voters} registered voters.") """

""" candidate_votes = int(input("How many votes did the candidate get in the election? "))
total_votes = int(input("What is the total number of votes in the election? "))
message_to_candidate = (
    f"You received {candidate_votes:,} votes. "
    f"The total number of votes in the election was {total_votes:,}. "
    f"You received {candidate_votes / total_votes * 100:.3f}% of the total votes.")

print(message_to_candidate) """

""" counties_dict = {"Arapahoe": 422829, "Denver": 463353, "Jefferson": 432438}
for county, voters in counties_dict.items():
    print(f"{county} has {voters} voters.") """

"""
This is a list of dictionaries. I want to get every item in the list (every dictionary) and then I want to print each (key, value) pair from each dictionary. There are two keys to
each dictionary 'county' and 'registered_voters', so when I am iterating through the list, I want to specify each key that I want the value from.
"""
voting_data = [{"county":"Arapahoe", "registered_voters": 422829}, {"county":"Denver", "registered_voters": 463353}, {"county":"Jefferson", "registered_voters": 432438}]
for voter_dict in voting_data:
    print(f"{voter_dict['county']} has {voter_dict['registered_voters']:,} registered voters.")