## SETTING UP BEFORE WRITING CODE FOR SCRIPT'S PURPOSE
# import the classes we'll need:

import os
import csv


# locate csv file

finance_csv = os.path.join("Resources","budget_data.csv")

#open the csv file and set the csv.reader function to read it:

with open(finance_csv) as bankfile:
    csvreader = csv.reader(bankfile, delimiter=",")


# # get rid of the header!
    csv_header = next(csvreader)


# create lists for processing, analyzing, and displaying data
    month_list = []
    amount_list = []

    for row in csvreader:
        month_list.append(row[0])
        amount_list.append(int(row[1]))

##----DONE---- COUNT TOTAL MONTHS IN DATA
# get length of rows to get the total months included in the data:
    month_count = len(month_list)

    
# ----DONE---- NET CHANGE OF ALL MONTHS OVER THE PERIOD:
# this will add all profits/losses together for a net
    sum_net= 0
    for row in amount_list:
        sum_net = int(sum_net) + int(row)


# ## CALCULATE CHANGES OVER THE PERIOD, THEN GET AVERAGE CHANGE
### this take the previous row and gets the difference (current month - previous month profit/loss)
#working
    prev_month = 0
    diff_list = []
    for row in amount_list:
        diff_list.append(int(row) - prev_month)
        prev_month = int(row)
# remember: "header" of diff_list is the first month - 0 (not the "first" difference value we want)
    diff_header = diff_list.pop(0)
    diff_count = len(diff_list)
    
# # find the average of all changes over the period:
    #create for loop to add up all changes (NOT PROFIT/LOSSES)
    sum_diff = 0
    for item in diff_list:
        sum_diff = sum_diff + int(item)
    average_diff = round(int(sum_diff / diff_count),4)

# ## GREATEST PROFIT MONTH, AMOUNT
# # using the list of differences between each month, find the highest number, but check for multiples
    greatest_profit = max(diff_list)
    gp_index = diff_list.index(greatest_profit)


# ## GREATEST LOSS MONTH, AMOUNT
# # using the list of differences between each month, find the lowest number, but check for multiples
    greatest_loss = min(diff_list)
    gl_index = diff_list.index(greatest_loss)




# ##PRINT RESULTS
# # print title, -----, Total Months, Total Net, Average Change, 
final_results = [f"Financial Analysis\n", 
f"----------------------------\n", 
f"Total Months: {month_count}\n", 
f"Total: ${sum_net}\n", 
f"Average  Change: ${average_diff}\n", 
f"Greatest Increase in Profits: {month_list[gp_index+1]} (${greatest_profit})\n", 
f"Greatest Decrease in Profits: {month_list[gl_index+1]} (${greatest_loss})\n"
]

text_path = os.path.join("Analysis", "results.txt")

with open(text_path, 'w', newline='', encoding='utf-8') as textfile:
    
    for line in final_results:
        textwriter = textfile.write(line)
        print(line)
    textwriter = textfile.close()
