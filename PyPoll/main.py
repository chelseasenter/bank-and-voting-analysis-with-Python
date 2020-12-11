## SETTING UP MY IMPORTS, LOCATING AND READING FILES, REMOVING HEADER (pre-purpose set-up)
#imports
import csv
import os

#locate csv file
election_csv = os.path.join("Resources","election_data.csv")

#open csv file and read it:

with open(election_csv) as pollfile:
    csvreader = csv.reader(pollfile, delimiter=",")

#remove the first line from the csvreader variable!
    csv_header = next(csvreader)

## PURPOSE OF SCRIPT: Analyze votes to find winner
#create a list of all voters' choices: 
    vote_choice_list = []
    for row in csvreader:
        vote_choice_list.append(row[2])
    
#find the length of the list for the total votes cast
    vote_count = len(vote_choice_list)


# find the unique values of the list by creating a list of a set of vote_choice_list 
#  first, the set will return only unique values. 
#  second, the list will change the set back into a list for further use
    candidates_names = list(set(vote_choice_list))

#create a dictionary to store the final_results (i.e. "candidate_1": 16 votes, "candidate_1": 25 votes, ...)
    final_results = {}

# set a for loop to add to the list the candidate name as the key and the total votes they received as the value        
    for candidate in candidates_names:
        final_tally = vote_choice_list.count(candidate)
        final_results[candidate] = final_tally


#initialize a winner_value variable to find the candidate with the most votes
#create a for loop to edit the final_results dictionary to include percentage of votes received as a list with total number of votes
    winner_value = 0
    for candidate, final_tally in final_results.items():
        final_results[candidate] = [final_tally, round((final_tally / vote_count)*100,3)]
        # if final_tally of current candidate is greater than previous percentage, change winner_value and winner_name to current candidate
        if final_tally > winner_value:
            winner_value = final_tally
            winner_name = candidate

## PRINT RESULTS IN TERMINAL & EXPORT RESULTS TO A TEXT FILE
# create a header list for initial information (before all candidate results are listed)
results_header = [f"Election Results\n", 
f"-------------------------\n",
f"Total Votes: {vote_count}\n", 
f"-------------------------\n"
]

# using list comprehension, create a list of candidates' final results to print out)
results_candidates = [
    f"{name}: {final_results[name][1]}% ({final_results[name][0]})\n" for name in final_results]

# create a footer list for conclusion of election (announce the winner)
results_footer = ["-------------------------\n", f"Winner: {winner_name}\n"]

# locate text file that results will be exported to:
txt_path = os.path.join("Analysis","results.txt")

#open text file and run for loops to write results of the election into the file:
with open(txt_path, "w", newline="", encoding="utf-8") as textfile:
    for header in results_header:
        textwriter = textfile.write(header)
        print(header)
    for candidates in results_candidates:
        textwriter = textfile.write(candidates)
        print(candidates)
    for footer in results_footer:
        textwriter = textfile.write(footer)
        print(footer)        

