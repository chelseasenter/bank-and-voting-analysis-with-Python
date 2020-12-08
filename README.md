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
   dates and profits(+)/losses(-)
    Total # months
    dates formatted as DDD-YYYY (NOV-2015), total months means ALL months (jan 2015 and jan 2017 are two separate months)
    there are no multiples of month/years, one for each
    [x] so count all rows except header = total months in data set
    
    Net
    get the sum of all rows
    [x] add all rows to a variable set to 0 (except the header)
    
    Calc changes
    
    
    amounts are formatted as 00000 or -00000
  * Pseudocode: 


2. PyPoll
  * Brainstorming:
 
  * Pseudocode:
