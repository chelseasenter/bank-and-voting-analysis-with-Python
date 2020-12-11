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
    print(vote_count)
    print("----------")

# find the unique values of the list by creating a set of vote_choice_list 
#  -this will create the candidates_names - candidates who received votes)
    candidates_names = list(set(vote_choice_list))

#create a dictionary to store the final_results ("candidate_1":16, "candidate_1":25, "candidate_3":37, ...)
    final_results = {}
    
    for candidate in candidates_names:
        final_tally = vote_choice_list.count(candidate)
        final_results[candidate] = final_tally
    print(final_results) 
    print("------")

    highest_votes = {}


# divide individual candidate list by vote_choice_list, set value to pct_khan, pct_correy, etc - 3
    for candidate, final_tally in final_results.items():
        final_results[candidate] = [final_tally, round((final_tally / vote_count),2)]
        highest_votes["name"] = candidate
        # if this current higher than previous percentage, add to highest dictionary
    print(final_results)
    print("------")

#look for the highest one
#set variable initialize to be highest value

    
    print(final_results["Khan"][1])
    #access same way to acces value, because value is list, use bracket notation 

# create dictionary totals (khan:15, li:23, etc)

# find the highest value in dictionary


      
# #reference this when finding the winner (candidate with the most votes)
# stats = {'a':1000, 'b':3000, 'c': 100}

# winner = max(stats, key=stats.get)

# print(winner)


# for key in mydic:
#   print("the key name is" + key + "and its value is" + mydic[key])



