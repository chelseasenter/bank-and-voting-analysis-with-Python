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

# divide individual candidate list by vote_choice_list, set value to pct_khan, pct_correy, etc - 3
    for candidate in final_results:
        
# create dictionary totals (khan:15, li:23, etc)

# find the highest value in dictionary

# key = ["apple", "banana", "cherry", "pear"]         #equivalent to candidates_names
# fruits = ["apple", "banana", "cherry", "apple",     #equivalent to vote_choice_list
# "banana", "cherry", "apple", "banana", "apple"
# ]
# fruit_dict = dict()                                 #equivalent to final_results

# for x in key:                                       #for _ in candidates_names
#     occurrences = fruits.count(x)                   #occurences = vote_choice_list.count(_)
#     fruit_dict[x] = occurrences                     #final_results[_] = occurences
# print(fruit_dict)                                   #print(final_results)
      
# #reference this when finding the winner (candidate with the most votes)
# stats = {'a':1000, 'b':3000, 'c': 100}

# winner = max(stats, key=stats.get)

# print(winner)





