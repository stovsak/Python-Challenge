import os
import csv

#create the variables for the Polling Project

total_votes = 0
khan_votes = 0
correy_votes = 0
li_votes = 0
otooley_votes = 0

#create the path for the file

userhome = os.path.expanduser('~')
csvpath = userhome + '/Desktop/Python_PyPoll_Resources_election_data.csv'

with open(csvpath, 'rU') as f:
    csvreader = csv.reader(f, delimiter = ',')

#create loop for candidates

    for row in csvreader:
        total_votes += 1

        if(row[2] == "Khan"):
            khan_votes += 1
        elif(row[2] == "Correy"):
            correy_votes +=1
        elif(row[2] == "Li"):
            li_votes += 1
        else:
            otooley_votes += 1
    
#candidate percentage calculations

    kahn_percent = khan_votes / total_votes
    correy_percent = correy_votes / total_votes
    li_percent = li_votes / total_votes
    otooley_percent = otooley_votes / total_votes

#loop for the election winner

winner = max(khan_votes, correy_votes,li_votes, otooley_votes)
if winner == khan_votes:
    winner_name = "Khan"
elif winner == correy_votes:
    winner_name = "Correy"
elif winner == li_votes:
    winner_name = "Li"
else:
    winner_name = "O'tooley"

#print the election results

print(f"Election Results")
print(f"---------------------")
print(f"Total Votes: {total_votes}")
print(f"---------------------")
print(f"Khan: {kahn_percent: .3%}{(khan_votes)}")
print(f"Correy: {correy_percent: .3%}{(correy_votes)}")
print(f"Li: {li_percent: .3%}{(li_votes)}")
print(f"O'tooley: {otooley_percent: .3%}{(otooley_votes)}")
print(f"---------------------")
print(f"Winner: {winner_name}")
print(f"---------------------")