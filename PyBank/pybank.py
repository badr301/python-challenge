# First we'll import the os module
# This will allow us to create file paths across operating systems
import os

# Module for reading CSV files
import csv

csvpath = os.path.join('..', 'Resources', 'budget_data.csv')


# i am making an update here

with open(csvpath, newline='') as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    #print(csvreader)

    # Read the header row first (skip this step if there is now header)
    csv_header = next(csvreader)
    #print(f"CSV Header: {csv_header}")

    #print(" ```text ")
    print(' Financial Analysis ')
    print(" ---------------------------- " )

    lnt = []
    total1 = 0
    # Read each row of data after the header
    for row in csvreader:
        lnt.append(row[1])
        total1 = total1 + int(row[1])
    print(f'Total:  ${total1:,.0f}')
    print('Total Months: ' ,len(lnt))
    print('Greatest Increase in Profits: $' ,max(lnt))
    print('Greatest Decrease in Profits: $' ,min(lnt))
    print("Average = $", total1/len(lnt) )
    print(" ``` ")

 