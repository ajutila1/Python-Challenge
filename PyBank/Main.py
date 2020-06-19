#Import Modules
import os
import csv

#Set path for file
PyBank_csv = os.path.join('Resources','PyBank.csv')

#Define function, no parameter since it will create lists
def Bank_Analysis():

    #Set counter to zero that will be summing profits through the first loop
    total_profit = 0

    #Create lists for three to calculate difference and then to link calculations to date
    date = []
    data = []
    difference = []
    
    #First loop to count months, sum profits, and collect values for lists
    for row in csvreader:
        date.append(str(row[0]))
        data.append(int(row[1]))
        total_profit += int(row[1])
    
    #Count either date/data list for month total
    total_months = len(data)

    #Calculate differences month to month in profits
    for idx in range(len(data)-1):
        difference.append(data[idx+1] - data[idx])

    #Find max/min change in profits
    maxval = difference.index(max(difference))
    minval = difference.index(min(difference))

    #Calculate average change
    avgchange = sum(difference) / len(difference)

    #Use list indexes to match change in data to date
    maxdate = date[maxval+1]
    mindate = date[minval+1]

    #Print Conclusions
    print('Financial Analysis')
    print('----------------------------')
    print('Total Months: ' + str(total_months))
    print('Total: $' + str(total_profit))
    #Round for average change
    print('Average Change: $' + str(round(avgchange, 2)))
    print('Greatest Increase in Profits: ' + (maxdate) + ' ($' + str(max(difference)) + ')')
    print('Greatest Decrease in Profits: ' + (mindate) + ' ($' + str(min(difference)) + ')')

    #Create text file for output
    Text_Output = open("Analysis/Financial Analysis.txt", 'w')
    Text_Output.write('Financial Analysis' + "\n" + '----------------------------' + '\n' 'Total Months: ' + str(total_months) + '\n')
    Text_Output.write('Total: $' + str(total_profit) + "\n" + 'Average Change: $' + str(round(avgchange, 2)) + "\n")
    Text_Output.write('Greatest Increase in Profits: ' + (maxdate) + ' ($' + str(max(difference)) + ')' + "\n")
    Text_Output.write('Greatest Decrease in Profits: ' + (mindate) + ' ($' + str(min(difference)) + ')')
    Text_Output.close()

#Read csv file
with open(PyBank_csv, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')

    header = next(csvreader)
    
    #Run function
    Bank_Analysis()