import csv
import os

finance_csv = os.path.join("Resources","election_data.csv")

stats = {'a':1000, 'b':3000, 'c': 100}

winner = max(stats, key=stats.get)

print(winner)