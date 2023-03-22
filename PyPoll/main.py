'''
Tasks for this script
-1 Calculate the total number of votes cast
-2 A complete list of candidates who received votes
-3 The percentage of votes each candidate won
-4 The total number of votes each candidate won
-5 The winner of the election based on popular vote
''' 

import os
import csv

poll_csv = os.path.join("Resources", "election_data.csv")

#lists to store voting information

header = []
ballot_ID = []
county = []
candidates = []
short_list = []
uniq_candidates = []

#declare variables
total_votes = 0
percent_votes = 0
stockham_total = 0
stockham_percent = 0
degette_total = 0
degette_percent = 0
doane_total = 0
doane_percent = 0
pop_winner = 0

with open(poll_csv) as csvreader:
    csvreader = csv.reader(csvreader, delimiter=",")

    header = next(csvreader)
    #print(header) #test for header output

    #populate lists with data from 'election_data.csv'
    for row in csvreader:
        ballot_ID.append(row[0])
        county.append(row[1])
        candidates.append(row[2])

    #task 1, total number of votes cast
    total_votes = len(ballot_ID)

    #task 2, list of unique candidates who received votes    
    for candidate in candidates:
        if candidate not in short_list:
            short_list.append(candidate)

    uniq_candidates = tuple(short_list) 


    #task 4, total number of votes for each candidate
    for row in candidates:
        if row == 'Charles Casper Stockham':
            stockham_total += 1
        elif row == 'Diana DeGette':
            degette_total += 1
        else:
            doane_total += 1

    #task 5, determine winner by popular vote
    if stockham_total > degette_total and stockham_total > doane_total:
        pop_winner = str('Charles Casper Stockham')
    elif degette_total > stockham_total and degette_total > doane_total:
        pop_winner = str('Diana DeGette')
    elif doane_total > stockham_total and doane_total > degette_total:
        pop_winner = str('Raymon Anthony Doane') 
    else:
        print("Hold the press! We're going to a run off!") 

    #task 3, calculate the percentage of the total for each candidate
    stockham_percent = (stockham_total / total_votes) * 100
    degette_percent = (degette_total / total_votes) * 100
    doane_percent = (doane_total / total_votes) * 100

    print("Election Results")
    print("-------------------------------------------------------------")
    print(f'Total Votes: {total_votes}')
    print("-------------------------------------------------------------")
    print(f'{uniq_candidates[0]}: {stockham_percent:.3f}% ({stockham_total})')
    print(f'{uniq_candidates[1]}: {degette_percent:.3f}% ({degette_total})')
    print(f'{uniq_candidates[2]}: {doane_percent:.3f}% ({doane_total})')
    print("-------------------------------------------------------------")
    print(f'Winner: {pop_winner}')
    print("-------------------------------------------------------------")


#output results to a text file
output_file = os.path.join("Analysis", "election_data_analysis.txt")

with open(output_file, "w") as textfile:
    writer = csv.writer(textfile)   

    #write the results into the text file, []'s are needed to print the line as a string instead of making it comma delimited...that was fun to trouble shoot
    writer.writerow(["Election Results"])
    writer.writerow(["-------------------------------------------------------------"])
    writer.writerow([f'Total Votes: {total_votes}'])
    writer.writerow(["-------------------------------------------------------------"])
    writer.writerow([f'{uniq_candidates[0]}: {stockham_percent:.3f}% ({stockham_total})'])
    writer.writerow([f'{uniq_candidates[1]}: {degette_percent:.3f}% ({degette_total})'])
    writer.writerow([f'{uniq_candidates[2]}: {doane_percent:.3f}% ({doane_total})'])
    writer.writerow(["-------------------------------------------------------------"])
    writer.writerow([f'Winner: {pop_winner}'])
    writer.writerow(["-------------------------------------------------------------"])