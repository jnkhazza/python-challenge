import os
import csv

#Import Data
csvpath = os.path.join('Resources', 'election_data.csv')

with open(csvpath) as csvfile:

    election_data = csv.reader(csvfile, delimiter=',')

    # print(election_data)

    csv_header = next(election_data)
    #print(f"{csv_header}")

    #Storing the data into lists
    voter_id = []
    county = []
    candidate = []

    for row in election_data:
        voter_id.append(int(row[0]))
        county.append(row[1])
        candidate.append(row[2])
    
    #Calculating the Total Votes
    votes_cast = len(voter_id)
    # print(votes_cast)

    #Pulling in the candidate names
    candidate_list = set(candidate)
    # print(candidate_list)

    #For Loop to get the number of votes per candidate
    khan = 0
    correy = 0
    li = 0
    tooley = 0

    for name in candidate:
        if name == 'Khan':
            khan = khan + 1
        if name == 'Correy':
            correy = correy + 1
        if name == 'Li':
            li = li + 1
        if name == "O'Tooley":
            tooley = tooley + 1
    
    #Calculating the percent of votes per candidate
    percent_khan = round(((khan/votes_cast) * 100), 3)
    percent_correy = round(((correy/votes_cast) * 100), 3)
    percent_li = round(((li/votes_cast) * 100), 3)
    percent_tooley = round(((tooley/votes_cast) * 100), 3)

    #Finding the winner
    candidate_votes = {"Khan": khan, "Li": li,"O'Tooley": tooley, "Correy": correy}
    winner = max(candidate_votes, key=candidate_votes.get)

    #Printing the analysis
    print("Election Results")
    print("---------------------------") 
    print(f"Total Votes: {votes_cast}")
    print("---------------------------")
    print(f"Khan: {percent_khan}00% ({khan})")
    print(f"Correy: {percent_correy}00% ({correy})")
    print(f"Li: {percent_li}00% ({li})")
    print(f"O'Tooley: {percent_tooley}00% ({tooley})")
    print("---------------------------")
    print(f"Winner: {winner}")
    print("---------------------------")

#Text File Analysis
file = open('Analysis/PypollAnalysis.txt', 'w')
file.write("Election Results")
file.write("\n---------------------------")
file.write(f"\nTotal Votes: {votes_cast}")
file.write("\n---------------------------")
file.write(f"\nKhan: {percent_khan}00% ({khan})")
file.write(f"\nCorrey: {percent_correy}00% ({correy})")
file.write(f"\nLi: {percent_li}00% ({li})")
file.write(f"\nO'Tooley: {percent_tooley}00% ({tooley})")
file.write("\n---------------------------")
file.write(f"\nWinner: {winner}")
file.write("\n---------------------------")
file.close


   