import os
import csv

input_file = "./election_data.csv"
output_file = "./output_election_data.txt"

 # Dictionary to store the count of votes for each candidate
vote_counts = {}

# Open the CSV file and iterate through each row
with open(input_file) as elec:
    csv_reader = csv.reader(elec)
    next(csv_reader)  # Skip header row
    total_votes = 0  # Total number of votes
    for row in csv_reader:
        candidate = row[2]  # Candidate is the third element in each row
        # Increment the count for the candidate
        #vote_counts[candidate] = vote_counts.get(candidate, 0) + 1
        #total_votes += 1
        #candidate_list = ["Charles Casper Stockham", "Dianna DeGette", "Raymon Anthony Doane"]
        #candidate=candidate_list
        if candidate in vote_counts:
            vote_counts[candidate] += 1
        else:
            vote_counts[candidate] = 1
        total_votes += 1
    # Calculate the percentage of votes for each candidate
    candidate_percentages = {}
    for candidate, count in vote_counts.items():
        percentage = (count / total_votes) * 100
        candidate_percentages[candidate] = (f"{percentage:.3f}%", count)

    # Find the winner of the election
    winner = max(vote_counts, key=vote_counts.get)



# Print results
elec_r = (
    f"Election Results\n"
    f"------------------------\n"
    f"Total Votes : {total_votes}\n"
    f"-------------------------\n"
    f"Results:  {candidate_percentages} \n"
    #for candidate, (percentage, count) in candidate_percentages.items():
        #f"{candidate}, {percentage}, {count}\n"
    
    f"----------------------\n"
    f"Winner {winner}\n"
)
print(elec_r)
with open(output_file, "w") as file:
    file.write(elec_r)


#for cand,results in candidate_percentages.items():
    #print(cand)
    #print(results)