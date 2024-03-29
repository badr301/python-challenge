# First we'll import the os module
# This will allow us to create file paths across operating systems
import os

# Module for reading CSV files
import csv

csvpath = os.path.join('..', 'Resources', 'election_data.csv')



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
    Khans = []
    Correys = []
    Lis = []
    Tooleys = []

    letter_counts = []
    # Read each row of data after the header
    for row in csvreader:
        lnt.append(row[2])
        if row[2] == 'Khan' :
            Khans.append(row[2])
        elif  row[2] == 'Correy':
            Correys.append(row[2])        
        elif row[2] == 'Li':
            Lis.append(row[2])
        elif row[2] == "O'Tooley":
            Tooleys.append(row[2])

x = len(lnt)
print('Total Votes: ' ,len(lnt)) 
print('Total Votes for khan: ' , len(Khans)*100/x, "%  (",len(Khans),")") 
print('Total Votes for Correy: ' , len(Correys)*100/x,"%  (",len(Correys),")") 
print('Total Votes for Li: ' , len(Lis)*100/x  ,"%  (",len(Lis),")")
print("Total Votes for O'Tooley : ", len(Tooleys)*100/x ,"%  (",len(Tooleys),")")



print('-------------------------')
#Winner: Khan
print("Winner : Khan" ,max([len(Khans)*100/x, len(Correys)*100/x,len(Lis)*100/x,len(Tooleys)*100/x ]))
print('-------------------------')

