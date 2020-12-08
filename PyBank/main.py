## SETTING UP BEFORE WRITING CODE FOR SCRIPT'S PURPOSE
# import the classes we'll need:

import os
import csv


# locate csv file

finance_csv = os.path.join("Resources","budget_data.csv")


#open the csv file and set the csv.reader function to read it:

with open(finance_csv) as bankfile:
    csvreader = csv.reader(bankfile, delimiter=",")

    print(csvreader)
    print("---- csv is pulling up----")
# # get rid of the header!
#     print({csvreader[3][0]})
    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")

# DONE---------
#this take the previous row and gets the difference (current month - previous month profit/loss)
#     next = 0
#     for row in csvreader:
#         print(f"MONTH AMOUNT: {row[1]}")
#         print(f"month amount is {int(row[1])} minus {next} = {int(row[1]) - next}")
#         next = int(row[1])
#         print(int(next))
# DONE^^^^^^^^^


# ## COUNT TOTAL MONTHS IN DATA
# # get length of rows to get the total months included in the data:
#     month_count = len(list(csvreader))

#     print(month_count)
#     print("----month count ^ ----")

# ## NET CHANGE OF ALL MONTHS OVER THE PERIOD:
#this will add all profits/losses together for a net
    sum = 0
    for row in csvreader:
        sum += int(row[1])
    print(f"The net profits for this period is: {sum}")

# ## CALCULATE CHANGES OVER THE PERIOD, THEN GET AVERAGE CHANGE
# # find the difference between each month and add that number in a new list:
#     diff_list = []

#     for row in csvreader:
#         print(row)
#     #set previous month to 0
#     #     prev_month = 0
#     # # #add the change from the previous month and the current row (this month) to the diff_list
#     # # diff_list.append(prev_month + row[1])
#     #     print(f"{prev_month}")
#     #     prev_month = row[1]
#     print("----diff list? ^ ----")

# # find the average of all changes over the period:

# ## GREATEST PROFIT MONTH, AMOUNT
# # using the list of differences between each month, find the highest number, but check for multiples

# ## GREATEST LOSS MONTH, AMOUNT
# # using the list of differences between each month, find the lowest number, but check for multiples

# ##PRINT RESULTS
# # print title, -----, Total Months, Total Net, Average Change, 