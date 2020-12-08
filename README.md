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
    [x] from diff_list, find the maximum number in the list, then search for that number in the list (checks for multiples)<p>
       if number of max# is less than 1, pull the date (correlate the position of the max# in the diff_list with the csv rows) amd set as greatest_profit<p>
       else nubmer of max# if greater<p>
    [x] from diff_list, find the minimum number in the list, then search for that number in the list (checks for multiples)<p>
       if number of min# is less than 1, pull the date (correlate the position of the min# in the diff_list with the csv rows) and set as greatest_loss<p>
    
#### Print results
    print( Financial Analysis<p>
    ------------<p>
    Total Months: total_months<p>
    Total: net_total<p>
    Average Change: average_change<p>

  * Pseudocode: 


2. PyPoll
  * Brainstorming:
 
  * Pseudocode:
