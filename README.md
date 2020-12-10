# python-challenge
Python Homework Week 3 - PyPoll &amp; PyBank

**Table of Content**<p>
Overview of Project Objectives<p>
Brainstorming & Pseudocode
<p><p>
 
## Overview of Project Objectives

This folder contains 2 projects. Below is a summary of each project. Enjoy!

### PyBank 
This project contains a __python__ file that will run a script to analyze my Company's financial records from a **csv** file. 

1. The script will analyze the data and calculate the following metrics: 
   * Total number of months in the provided data set
   * Net Profits and Losses over the entire period
   * Changes in Profits and Losses over the entire period
    * as well as the average of those changes
   * Greatest increase and decrease in profits and losses over the entire period, represented by date and amount
  
2. The final script prints the analysis to the terminal and exports a text file with the results

### PyPoll
In this project, I was tasked with helping a town modernize their vote counting process by creating a python script to process their votes.

1. First, the script calculates the following from the dataset:
   * total number of votes cast
    * a list of candidates who received votes
   * percentage of votes each candidate won
   * total number of votes each candidate won
   * the winner of the election

2. The script will then print out the calculations in the previous step to the terminal and export a text file with the results.

## Brainstorming and Pseudocode
-- in this section I will show (1) my initial brainstorming and (2) my pseudocode, so you can follow my thoughts in how I decided to complete these projects. Please forgive me, this section might be a little messy.

1. PyBank
  * Brainstorming:
#### Header/Before we can begin writing code for our script:
  import classes (csv and os)<p>
  locate csv file<p>
  open it <p>
  set the csv class's function reader to read the csv file<p>
  
#### Notes/things to keep in mind
  GET RID OF HEADER BEFORE PROCEEDING!
  dates and profits(+)/losses(-), amounts are formatted as 00000 or -00000
    
#### Total # months
  dates formatted as DDD-YYYY (NOV-2015)<p>
  total months means ALL months (i.e. jan 2015 and jan 2017 are two separate months)<p>
  there are no multiples of month/years, one for each<p>
  [x] so count all rows except header = total months in data set<p>
    
#### Net
  get the sum of all rows<p>
  [x] add all rows to a variable set to 0 (except the header)<p>
    
#### Calc changes, find max and min change
  for every row, find the difference (designate + or - for profit or loss) between that row and row + 1, then put it in a new list (diff_list)<p>
  [x] this will create a list of differences ("change") between adjacent months, starting with the first month.<p>
  [x] find the average of changes: add all items in list (set sum_diff_list to 0, for items in list add to sum_diff_list)<p> 
    then divide by length (or count) of items in list<p>
    
#### Greatest increase in profits (date and amount) over period
   [x] from diff_list, find the greatest_profit in the list (maximum number), then search for that number in the list (checks for multiples)<p>
    if number of greatest_profit value is less than 1, pull the date (correlate the position of the max# in the diff_list with the csv rows) amd set as greatest_profit<p>
    else number of greatest_profit is greater than 1 for loop anything that matches greatest_profit and set to print with commas between<p>
   [x] from diff_list, find the greatest_loss in the list (minimum number), then search for that number in the list (checks for multiples)<p>
    if number of greatest_loss is less than 1, pull the date (correlate the position of the min# in the diff_list with the csv rows) and set as greatest_loss<p>
    else number of greatest_loss is greater than 1, for loop anything that matches greatest_loss and set to print with commas between
    
#### Print results
 print( Financial Analysis<p>
 ------------<p>
 Total Months: total_months<p>
 Total: net_total<p>
 Average Change: average_change<p>
 Greatest Increase in Profits: max_num
 Greatest Decrease in Losses: min_num
 <p>
-----------------------------------------------------------
  * Pseudocode: 
#### Header/Before we can begin writing code for our script:
import os <p>
import csv <p>
finance_csv = os.path.join("PATH") <p>
with open(finance_csv, encoding='utf-8') as bankfile:
csvreader = csv.reader(bankfile, delimiter=",")

#### Notes/things to keep in mind
 nix_header = next(csvreader)
 lists
  
#### Total # months
 month_count = len(list(csvreader))
 [x] so count all rows except header = total months in data set<p>
 
 print(month_count) -- to test it works
    
#### Net
net_total = 0
for month in csvreader:
  net_total += month[1]
[x] add all rows to a variable set to 0 (except the header)<p>

print(net_total) --to make sure it works

#### Calc changes, find max and min change
--------try list comprehension, maybe?---------diff_list = [diff for diff in csvreader]

counter = 0
diff_list = []
row = 0
while counter < month_count:
 difference = csvreader[row] + csvraeder[row + 1]
 counter += 1

--------using for loop, maybe?-----------------------------
for row in csvreader:
  difference = row[
  diff_list.append(difference)
  for every row, find the difference (designate + or - for profit or loss) between that row and row + 1, then put it in a new list (diff_list)<p>
  [] this will create a list of differences ("change") between adjacent months, starting with the first month.<p>
  [] find the average of changes: add all items in list (set sum_diff_list to 0, for items in list add to sum_diff_list)<p> 
    then divide by length (or count) of items in list<p>
    
#### Greatest increase in profits (date and amount) over period
   [] from diff_list, find the maximum number in the list, then search for that number in the list (checks for multiples)<p>
    if number of max# is less than 1, pull the date (correlate the position of the max# in the diff_list with the csv rows) amd set as greatest_profit<p>
    else nubmer of max# if greater<p>
   [] from diff_list, find the minimum number in the list, then search for that number in the list (checks for multiples)<p>
    if number of min# is less than 1, pull the date (correlate the position of the min# in the diff_list with the csv rows) and set as greatest_loss<p>
    
#### Print results
 print( Financial Analysis<p>
 ------------<p>
 Total Months: total_months<p>
 Total: net_total<p>
 Average Change: average_change<p>
 <p>

2. PyPoll
-- in this section I will show (1) my initial brainstorming and (2) my pseudocode, so you can follow my thoughts in how I decided to complete these projects. Please forgive me, this section might be a little messy.

  * Brainstorming:
 three columns = Voter ID, County, and Candidate
 *note: voter ID is an 8 character string, NOT integer
 1. total votes cast (len of list minus header)
 2. total list of all candidates who received votes (unique value finder, make list of those)
 3. percentage of the votes won by each candidate (tally total votes for each candidate, put them in lists, maybe a dictionary of lists if you have time)
 4. total number of votes for each candidate
 5. winner of the election based on popular vote
 
 summary:
 need a list of vote choices (vote_choice_list)
 (next header) then len(vote_choice_list) for total votes number - 1
 find unique values of vote_choice_list - 2
 sum items in vote_choice_list by name (correy_list, khan_list, li_list, etc) - 4
 divide individual candidate list by vote_choice_list, set value to pct_khan, pct_correy, etc - 3
 create dictionary totals (khan:15, li:23, etc)
 find the highest value in dictionary (I found a stack overflow solution for this problem that can be found [here](https://stackoverflow.com/questions/268272/getting-key-with-maximum-value-in-dictionary)
 
  * Pseudocode:
