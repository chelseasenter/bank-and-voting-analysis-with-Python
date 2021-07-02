# python-challenge
Python Homework Week 3 - PyPoll &amp; PyBank<p>
Chelsea Senter <p>

# Table of Contents 
Overview of Project Objectives:
<p>
- PyBank <p>
 - PyPoll<p>

Brainstorming & Pseudocode
<p>
- PyBank: Brainstorming<p>
- PyBank: Pseudocode<p>
- PyPoll: Brainstorming<p>
- PyPoll: Pseudocode<p>

Review of Projects:
<p>
- reflections/notes<p>
- helpful links<p>

<p><p><p>

# Overview of Project Objectives

This folder contains 2 projects. Below is a summary of each project. Enjoy!<p><p>

## PyBank 

This project contains a __python__ file (main.py) that will run a script to analyze my Company's financial records from a **csv** file (Resources > budget_data.csv). <p><p>

 1. The script will analyze the data and calculate the following metrics: <p>
  - Total number of months in the provided data set<p>
  - Net Profits and Losses over the entire period<p>
  - Changes in Profits and Losses over the entire period<p>
  - as well as the average of those changes<p>
  - Greatest increase and decrease in profits and losses over the entire period, represented by date and amount<p><p>
  <p>
 2. The final script prints the analysis to the terminal and exports a text file with the results (Analysis folder > results.txt)<p>

## PyPoll
In this project, I was tasked with helping a town modernize their vote counting process by creating a python script (main.py) to process their votes (Resources > election_data.csv).<p><p>

 1. First, the script calculates the following from the dataset:<p>
 - total number of votes cast<p>
 - a list of candidates who received votes<p>
 - percentage of votes each candidate won<p>
 - total number of votes each candidate won<p>
 - the winner of the election<p><p>
<p>
 2. The script will then print out the calculations in the previous step to the terminal and export a text file with the results (Analysis folder > results.txt).<p>

# Brainstorming and Pseudocode
<p>
 -- in this section I will show <p>
 1. my initial brainstorming (because I'm extra) and <p>
 2. my pseudocode, so you can follow my thoughts in how I decided to complete these projects. <p>
 **Please forgive me, this section might be a little messy.**
<p><p>


## PyBank<p>
 <p>
 <details><summary> Brainstorming: </summary>
- [x] Header/Before we can begin writing code for our script:<p>
  import classes (csv and os)<p>
  locate csv file<p>
  open it <p>
  set the csv class's function reader to read the csv file<p>
  
- [x] Notes/things to keep in mind
  GET RID OF HEADER BEFORE PROCEEDING!
  dates and profits(+)/losses(-), amounts are formatted as 00000 or -00000
    
- [x] Total # months
  dates formatted as DDD-YYYY (NOV-2015)<p>
  total months means ALL months (i.e. jan 2015 and jan 2017 are two separate months)<p>
  there are no multiples of month/years, one for each<p>
  [x] so count all rows except header = total months in data set<p>
    
- [x] Net
  get the sum of all rows<p>
- [x] add all rows to a variable set to 0 (except the header)<p>
    
- [x] Calc changes, find max and min change
  for every row, find the difference (designate + or - for profit or loss) between that row and row + 1, then put it in a new list (diff_list)<p>
-   [x] this will create a list of differences ("change") between adjacent months, starting with the first month.<p>
-   [x] find the average of changes: add all items in list (set sum_diff_list to 0, for items in list add to sum_diff_list)<p> 
    then divide by length (or count) of items in list<p><p>
    
- [x] Greatest increase in profits (date and amount) over period<p>
-   [x] from diff_list, find the greatest_profit in the list (maximum number), then search for that number in the list (checks for multiples)<p>
    if number of greatest_profit value is less than 1, pull the date (correlate the position of the max# in the diff_list with the csv rows) amd set as greatest_profit<p>
    else number of greatest_profit is greater than 1 for loop anything that matches greatest_profit and set to print with commas between<p>
-   [x] from diff_list, find the greatest_loss in the list (minimum number), then search for that number in the list (checks for multiples)<p>
    if number of greatest_loss is less than 1, pull the date (correlate the position of the min# in the diff_list with the csv rows) and set as greatest_loss<p>
    else number of greatest_loss is greater than 1, for loop anything that matches greatest_loss and set to print with commas between<p><p>

- [x] Print results<p>
 print( Financial Analysis<p>
 ------------<p>
 Total Months: total_months<p>
 Total: net_total<p>
 Average Change: average_change<p>
 Greatest Increase in Profits: max_num<p>
 Greatest Decrease in Losses: min_num<p>
 <p><p>
</p>
</details>

 <details><summary> Pseudocode: </summary>
- [x] Header/Before we can begin writing code for our script:<p>
import os <p>
import csv <p>
finance_csv = os.path.join("PATH") <p>
with open(finance_csv, encoding='utf-8') as bankfile:<p>
csvreader = csv.reader(bankfile, delimiter=",")<p><p>

- [x] Notes/things to keep in mind<p>
 nix_header = next(csvreader)<p>
 lists<p><p>
  
- [x] Total # months<p>
 month_count = len(list(csvreader))<p>
- [x] so count all rows except header = total months in data set<p><p>
 
 print(month_count) -- to test it works<p><p>
    
- [x] Net<p>
net_total = 0<p>
for month in csvreader:<p>
  net_total += month[1]<p>
- [x] add all rows to a variable set to 0 (except the header)<p><p>

print(net_total) --to make sure it works<p><p>

- [x] Calc changes, find max and min change<p>
--------try list comprehension, maybe?---------diff_list = [diff for diff in csvreader]<p><p>

counter = 0<p>
diff_list = []<p>
row = 0<p>
while counter < month_count:<p>
 difference = csvreader[row] + csvraeder[row + 1]<p>
 counter += 1<p><p>

- [x] Greatest increase in profits (date and amount) over period<p>
- [x] from diff_list, find the maximum number in the list, then search for that number in the list (checks for multiples)<p>
    if number of max# is less than 1, pull the date (correlate the position of the max# in the diff_list with the csv rows) amd set as greatest_profit<p>
    else nubmer of max# if greater<p>
- [x] from diff_list, find the minimum number in the list, then search for that number in the list (checks for multiples)<p>
    if number of min# is less than 1, pull the date (correlate the position of the min# in the diff_list with the csv rows) and set as greatest_loss<p><p>
    
- [x] Print results<p>
 print( Financial Analysis<p>
 ------------<p>
 Total Months: total_months<p>
 Total: net_total<p>
 Average Change: average_change<p><p>
</p>
</details>

## PyPoll<p>
-- in this section I will show <p>
1. my initial brainstorming and <p>
2. my pseudocode, so you can follow my thoughts in how I decided to complete these projects. <p>
**Please forgive me, this section might be a little messy.**<p><p>

 <details><summary> Brainstorming: </summary>
 three columns = Voter ID, County, and Candidate<p>
 --note to self: voter ID is an 8 character string, NOT integer!<p>
 1. total votes cast (len of list minus header)<p>
 2. total list of all candidates who received votes (unique value finder, make list of those)<p>
   -- to do this, I will use a set then convert to list to pull out unique values<p>
 3. percentage of the votes won by each candidate (tally total votes for each candidate, put them in lists, maybe a dictionary of lists if you have time)<p>
 4. total number of votes for each candidate<p>
   --to do this, I want to create a dictionary with keys of the candidate names and values as the sum of their votes. So...<p>
   --I will need to create a for loop to count each candidate in candidate names in the overall vote_choice_list, then...<p>
   --add the candidate name as key and the number of votes as value<p>
 5. winner of the election based on popular vote<p><p>

Summary:<p>
- [x] set up imports, open and read csv files<p>
- [x] next header - we don't need it!<p>
- [x] need a list of vote choices (vote_choice_list) then...<p>
- [x] len(vote_choice_list) for total votes number - 1<p>
- [x] find unique values (candidate names) of vote_choice_list - 2<p>
- [x] sum items in vote_choice_list by name (correy_list, khan_list, li_list, etc) - 4<p>
- [x] divide individual candidate list by vote_choice_list, set value to pct_khan, pct_correy, etc - 3<p>
- [x] create dictionary totals (khan:15, li:23, etc)<p>
- [x] find the highest value in dictionary<p><p>
</p>
</details>

 <details><summary> Pseudocode: </summary>
- [x] set up imports, open and read csv files<p>
    import csv & os<p>
    with open election_data.csv as pollfile<p>
    call upon csv.reader to read pollfile, using delimiter=","<p><p>

- [x] next header - we don't need it!<p>
    next(csvreader)<p><p>
  
- [x] need a list of vote choices (vote_choice_list) then...<p>
    vote_choice_list = []<p>
    for row in csvreader:<p>
        append() vote_choice_list with index position [2], because lists start at [0] and we need the last "column" in the row)<p><p>
    
- [x] len(vote_choice_list) for total votes number - 1<p>
    vote_count = len(vote_choice_list)<p>
    print(vote_count)<p>
    print("----------")<p><p>

- [x] find unique values (candidate names) of vote_choice_list - 2<p>
      list(set(vote_choice_list))<p><p>

- [x] sum items in vote_choice_list by name (correy_list, khan_list, li_list, etc) - 4<p><p>

    final_results = {}<p><p>
        for candidate in candidates_names:<p>
        final_tally = vote_choice_list.count(candidate)<p>
        final_results[candidate] = final_tally<p>
    print(final_results) <p><p>

- [x] divide individual candidate list (total votes per candidate) by vote_choice_list, set value to dictionary as list with the total votes - 3<p>
         final_results[key] = [final_tally, round((final_tally / vote_count)*100,3)] <p>

- [x] find the highest value in dictionary by setting for loop and initializing "winner_value"<p><p>
         winner_value = 0 <p>
         (inside for loop for each candidate:)
          if final_tally > winner_value: <p>
            winner_value = final_tally <p>
            winner_name = candidate <p>
- [x] create lists to for loop into terminal (print) and write into text file all at once: <p>
             variables needed: <p>
             header <p>
             body with candidate overview <p>
             footer declaring winner <p> <p>
</p>
</details>

# Review of Projects: notes, links, etc.
 <details><summary> Reflections: </summary>
 <p>
After seeing how other READMEs are formatted, I will no longer include the brainstorming section. I will possibly the Pseudocode portion, especially when I'm completing coursework to show my work. This illustrates to me the importance of extracurricular projects, so I have the freedom to exclude "my process" notes and focus fully on the material I'm creating.<p><p>

There was a lot of brainstorming, writing things out, deleting lines, adding lines, scrapping the whole thing, starting over. It was frustrating to feel totally lost in what I had to do when I felt I had exhausted all possible routes on the current "thought road" I was on. However, after looking over my final products, I'm quite pleased with what I created. Although there were moments of frustration, those moments allowed for wonderful eureka! moments when things worked the first time I ran them. I'm looking forward to those moments in the future as I progress my knowledge. Overall, I'm sure I will find quicker ways to get the results I need, but for now this wasn't half bad.<p><p>
</p>
</details>

 <details><summary> Some links that I found helpful during these projects: </summary>
 <p>
[how to round a number in python](https://stackoverflow.com/questions/20457038/how-to-round-to-2-decimals-with-python)<p>
[how to write files to a txt file](https://www.datacamp.com/community/tutorials/reading-writing-files-python)<p>
[finding the index of an item in a list](https://stackoverflow.com/questions/176918/finding-the-index-of-an-item-in-a-list)<p>
[finding the min/max of items in a list](https://medium.com/programminginpython-com/python-program-to-find-the-largest-and-smallest-number-in-a-list-fd8fac8aba08)<p>
[printing lists: 4 ways](https://www.geeksforgeeks.org/print-lists-in-python-4-different-ways/)<p>
[python sets](https://www.w3schools.com/python/python_sets.asp)<p>
[finding unique values in a list by creating a set](https://stackoverflow.com/questions/12897374/get-unique-values-from-a-list-in-python)<p>
[find the highest value in a dictionary](https://stackoverflow.com/questions/268272/getting-key-with-maximum-value-in-dictionary)<p>
[how to count an item in a list](https://www.kite.com/python/answers/how-to-count-the-number-of-occurrences-of-an-element-in-a-list-in-python#:~:text=of%20%22b%22%20.-,Use%20list.,number%20of%20occurrences%20of%20value%20.)<p>
[how to add a key:value to a dictionary](https://www.journaldev.com/23232/python-add-to-dictionary)<p>
[printing values from a dictionary](https://realpython.com/iterate-through-dictionary-python/)<p>
 </p>
 </details>
