## SETTING UP MY IMPORTS, LOCATING AND READING FILES (pre-purpose set-up)
import csv
import os

#locate csv file
election_csv = os.path.join("Resources","election_data.csv")

#open csv file and read it:

with open(election_csv) as pollfile:
    csvreader = csv.reader(pollfile, delimiter=",")

#remove the first line from the csvreader variable!
    csv_header = next(csvreader)

#create vote_choice_list
    vote_choice_list = []
    for row in csvreader:
        vote_choice_list.append(row[2])
    
#find the length of the list for the total votes cast
    vote_count = len(vote_choice_list)


# find the unique values of the list by creating a set of vote_choice_list 
#  -this will create the candidates_names - candidates who received votes)
    candidates_names = list(set(vote_choice_list))

#create a dictionary to store the final_results ("candidate_1":16, "candidate_1":25, "candidate_3":37, ...)
    final_results = {}
        
    for candidate in candidates_names:
        final_tally = vote_choice_list.count(candidate)
        final_results[candidate] = final_tally


    winner_value = 0

# divide individual candidate list by vote_choice_list, set value to pct_khan, pct_correy, etc - 3
    for candidate, final_tally in final_results.items():
        final_results[candidate] = [final_tally, round((final_tally / vote_count)*100,3)]
        if final_tally > winner_value:
            winner_value = final_tally
            winner_name = candidate
            winner_pct = final_results[candidate][1]


        # if this current higher than previous percentage, add to highest dictionary

final_header = [f"Election Results", 
f"-------------------------",
f"Total Votes: {vote_count}", 
f"-------------------------"
]
final_candidates = [f"{name}: {final_results[name][1]}% ({final_results[name][0]})" for name in final_results]

txt_path = os.path.join("Analysis","results.txt")

with open(txt_path, "w", newline="", encoding="utf-8") as textfile:
    for header in final_header:
        textwriter = textfile.write(header)
        print(header)
        for candidates in final_candidates:
            print(candidates)
        print("-------------------------")
        print(f"Winner: {winner_name}")






    # for name in final_results:
    #     print(f"{name}: {final_results[name][0]}% ({final_results[name][1]})")





