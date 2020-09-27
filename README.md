# python-challenge

import os
import csv

pypoll_csv = os.path.join("..", "Resources", "election_data.csv")

#Data Lists
candidates = []
candidatevote = {}
vote = 0
votepercent = {}
percent = 0
totalvotenumber = 0

with open(pypoll_csv) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    for row in csvreader:
        candidates.append(row[2])
        totalvotenumber += 1
    
    candidatevote = dict.fromkeys(candidates, vote)
    votepercent = dict.fromkeys(candidates, percent)

    for candidate in candidates:
        if candidate == "Khan":
            candidatevote["Khan"] += 1
            votepercent["Khan"] += 1
        elif candidate == "Correy":
            candidatevote["Correy"] += 1
            votepercent["Correy"] += 1
        elif candidate == "Li":
            candidatevote["Li"] += 1
            votepercent["Li"] += 1
        elif candidate == "O'Tooley":
            candidatevote["O'Tooley"] += 1
            votepercent["O'Tooley"] += 1
    
    for key, value in votepercent.items():
        votepercent[key] = round((value * 100 / totalvotenumber), 2) 
        

output_path = os.path.join("..", "Homework 3", "py_poll.txt")

with open(output_path, 'w') as txtfile:
    
        

print(totalvotenumber)
print(candidatevote)
print(votepercent)
        
text_file
