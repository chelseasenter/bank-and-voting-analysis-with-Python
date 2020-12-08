## SETTING UP BEFORE WRITING CODE FOR SCRIPT'S PURPOSE
# import the classes we'll need:

import os
import csv


# locate csv file

finance_csv = os.path.join("Resources","budget_data.csv")


#open the csv file and set the csv.reader function to read it:

with open(finance_csv, encoding='utf-8') as bankfile:
    csvreader = csv.reader(bankfile, delimiter=",")


# get rid of the header!
nix_header = next(csvreader)


## COUNT TOTAL MONTHS IN DATA
# get length of rows to get the total months included in the data:


## NET CHANGE OF ALL MONTHS OVER THE PERIOD:
# get the sum of all profit/losses over the period:

## CALCULATE CHANGES OVER THE PERIOD, THEN GET AVERAGE CHANGE
# find the difference between each month and add that number in a new list:

# find the average of all changes over the period:

## GREATEST PROFIT MONTH, AMOUNT
# using the list of differences between each month, find the highest number, but check for multiples

## GREATEST LOSS MONTH, AMOUNT
# using the list of differences between each month, find the lowest number, but check for multiples

##PRINT RESULTS
# print title, -----, Total Months, Total Net, Average Change, 