#Import Modules
import os
import csv

#Set path for file
PyPoll_csv = os.path.join('Resources','election_data.csv')

#Define function
def Poll_Analysis():

    #Set up dictionary for candidates and their vote count
    Candidate_Votes = {}

    #Set counter to zero for total votes
    numrow = 0

    #First loop for counting rows (votes) and pulling keys/values for dictionary
    for row in csvreader:
        numrow += 1
        if row[2] not in Candidate_Votes:
            Candidate_Votes[row[2]] = 0
        Candidate_Votes[row[2]] = Candidate_Votes[row[2]] + 1

    #Print results using variables
    print("Election Results")
    print("-------------------------")
    print("Total Votes: " + str(numrow))
    print("-------------------------")
    for Candidate in Candidate_Votes:
        print(Candidate + ": " + ("{:.0%}".format(round((Candidate_Votes[Candidate] / numrow), 2))) + " (" + str(Candidate_Votes[Candidate]) + ")")
    
    #Pull values from dictionary
    Candidates = list(Candidate_Votes.keys())
    Votes = list(Candidate_Votes.values())

    #Find highest vote count to find winner using indexes
    maxvote = max(Votes)
    VoteIndex = Votes.index(maxvote)
    Winner = Candidates[VoteIndex]

    #Print winner
    print('-------------------------')
    print("Winner: " + Winner)
    print('-------------------------')

    #Create text file for output
    Text_Output = open("Analysis/Poll Analysis.txt", 'w')
    Text_Output.write('Election Results' + "\n" + "-------------------------" + "\n")
    Text_Output.write("Total Votes: " + str(numrow) + "\n" + "-------------------------" + '\n')
    for Candidate in Candidate_Votes:
        Text_Output.write(Candidate + ": " + ("{:.0%}".format(round((Candidate_Votes[Candidate] / numrow), 2))) + " (" + str(Candidate_Votes[Candidate]) + ")" + '\n')
    Text_Output.write("\n" + '-------------------------' + '\n')
    Text_Output.write("Winner: " + Winner + '\n' + '-------------------------')
    Text_Output.close()

#Read file and run function
with open(PyPoll_csv, 'r') as csvfile:

    csvreader = csv.reader(csvfile, delimiter=',')

    header = next(csvreader)

    Poll_Analysis()