import os
import csv
print("Election Results")
csv_file = os.path.join("resources", "election_data.csv") 
csvreader = csv.reader('election_data', delimiter =",")
Ballot_ID = 
print("Total Votes :", len(Ballot_ID))





candidates = ["Charles_Casper_Stockham", "Diana DeGette", "Raymon Anthony Doane"]
votetotal = candidates.count("Charles_Casper_Stockham")
print(votetotal)