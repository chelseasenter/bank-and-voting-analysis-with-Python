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
    full_csv = zip(month_list, amount_list)

    for row in csvreader:
        month_list.append(row[0])
        amount_list.append(int(row[1]))

    # for row in full_csv:
    #     print(row)

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
    average_diff = round(int(sum_diff / diff_count),2)

# ## GREATEST PROFIT MONTH, AMOUNT
# # using the list of differences between each month, find the highest number, but check for multiples
    greatest_profit = max(diff_list)
    gp_index = diff_list.index(greatest_profit)
    # maxi_count = 0
    # multi_maxi = []
    # for maxi in amount_list:
    #     maxi_count += 1
    # if max_count < 1:
    #     print(f"The greatest loss occured during the month of {reference the month_list item here}: {greatest_profit}")
    # else:
    #     print(f"There were multiple months that had the greatest profit. These months are:")
    #     print(f"{multi_maxi}")

# ## GREATEST LOSS MONTH, AMOUNT
# # using the list of differences between each month, find the lowest number, but check for multiples
    greatest_loss = min(diff_list)
    gl_index = diff_list.index(greatest_loss)
    # mini_count = 0
    # multi_mini = []
    # for mini in amount_list:
    #     mini_count += 1
    # if mini_count < 1: 
    #     print(f"The greatest loss occured during the month of {reference the month_list item here}: {greatest_loss}")
    # else:
    #     for minis in amount_list:
    #         if minis == greatest_loss:
    #             multi_mini.append(minis)
    #     print(f"There were multiple months that had the greatest loss. These months are:")
    #     for minis in multi_mini:
    #         print(f"{multi_mini}")



# ##PRINT RESULTS
# # print title, -----, Total Months, Total Net, Average Change, 
print("Financial Analysis")
print("----------------------------")
print(f"Total Months: {month_count}")
print(f"Total: ${sum_net}")
print(f"Average  Change: ${average_diff}")
print(f"Greatest Increase in Profits: {month_list[gp_index+1]} (${greatest_profit})")
print(f"Greatest Decrease in Profits: {month_list[gl_index+1]} (${greatest_loss})")

text_path = os.path.join("Analysis", "results.txt")

with open(text_path, 'w', newline='', encoding='utf-8') as textfile:
    
    textwriter = textfile.write("Financial Analysis\n")
    textwriter = textfile.write(f"----------------------------\n")
    textwriter = textfile.write(f"Total Months: {month_count}\n")
    textwriter = textfile.write(f"Total: ${sum_net}\n")
    textwriter = textfile.write(f"Average  Change: ${average_diff}\n")
    textwriter = textfile.write(f"Greatest Increase in Profits: {month_list[gp_index]} (${greatest_profit})\n")
    textwriter = textfile.write(f"Greatest Decrease in Profits: {month_list[gl_index]} (${greatest_loss})\n")
    textwriter = textfile.close()

    #can store variable, tuple with all f strings
    #google writing text output, tuples?