#import modules
import os
import csv

#create path for csv
py_poll = os.path.join('election_data.csv')

#set variables
total_votes = 0
candidate = ""
candidate_votes = {}
candidate_percentages ={}
win_votes = 0
winner = ""

#display header columns
print(f'{csvheader}')

with open(py_poll) as csvfile:
    csvreader = csv.reader(csvfile,delimiter=',')
    next(csvreader)
    for row in csvreader:
        total_votes = total_votes + 1
        candidate = row[2]
        if candidate in candidate_votes:
            candidate_votes[candidate] = candidate_votes[candidate] + 1
        else:
            candidate_votes[candidate] = 1

#total number of votes
total_votes       

#winning candidate
candidate



