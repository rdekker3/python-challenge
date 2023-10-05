import os
import csv #relevant packages

# Collect data 
election_csv = os.path.join('..', 'Resources', 'election_data.csv')

votes = [] # create a list for the total votes
with open(election_csv, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    for row in csvreader:
        votes.append(row[2]) #populate votes with third column

CCS = [] # create a list for the candidate
with open(election_csv, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    for row in csvreader:
        if row[2] == "Charles Casper Stockham": CCS.append(row[2]) #match candidate name to populate list
DDG = [] # create a list for the candidate
with open(election_csv, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    for row in csvreader:
        if row[2] == "Diana DeGette": DDG.append(row[2]) #match candidate name to populate list
RAD = [] # create a list for the candidate
with open(election_csv, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    for row in csvreader:
        if row[2] == "Raymon Anthony Doane": RAD.append(row[2]) #match candidate name to populate list

a = len(CCS) #create variables to be printed; calculate total votes for each candidate
b = len(DDG)
c = len(RAD)

x = (round((a / len(votes)), 5) * 100) #formula for vote percentage
y = (round((b / len(votes)), 5) * 100)
z = (round((c / len(votes)), 3) * 100)


with open("analysis/PyPoll.txt", "a") as f: #write to a txt file, set to print each line
    print("Election Results",file=f)
    print("----------------------------",file=f)
    print("Total Votes: ", len(votes),file=f) #include both text and formulae 
    print("----------------------------",file=f)
    print("Charles Casper Stockham: ", x,"%" , "(",a,")",file=f) #include both percentage and total votes
    print("Diana DeGette: ", y,"%" , "(",b,")", file=f)
    print("Raymon Anthony Doane: ", z,"%" ,"(",c,")",file=f)
    print("----------------------------",file=f)
    print("Winner: Diana DeGette",max(a,b,c), file=f) #show winner with most votes
    print("----------------------------",file=f)