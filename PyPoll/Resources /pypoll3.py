import os
import csv


csvpath = os.path.join ('PyPoll_election_data.csv')
total_votes = 0
voter_id = 0
unique_candidates = []
candidate = []
candidate_list = []


with open(csvpath, "r") as csvfile:
    reader = csv.reader(csvfile, delimiter = ',')
    header_row = next(reader)



#number of votes
    for row in reader:
        total_votes += 1
        voter_id = voter_id + int(row[0])

        #counting number of times each candidates name appears
        candidate_list.append(row[2])
    count = candidate_list.count("Khan")
    count2 = candidate_list.count("Correy")
    count3 = candidate_list.count("Li")
    count4 = candidate_list.count("O'Tooley")


    for candidate in candidate_list:
        if candidate not in unique_candidates:
            unique_candidates.append(candidate)
    
#percentage of votes 
khan_vote_percentage = count/total_votes*100
correy_vote_percentage = count2/total_votes*100
li_vote_percentage = count3/total_votes*100
otooley_vote_percentage = count4/total_votes*100


print("Election Results")
print("--------------------------------")
print('Total Votes: ' + str(total_votes))
print("Candidates Running" + str(unique_candidates))
print("--------------------------------")
print("Khan :", count ,  (round(khan_vote_percentage, 3)), "%" )
print("Correy :", count2 ,  (round(correy_vote_percentage, 3)), "%" )
print("Li :", count3 ,  (round(li_vote_percentage, 3)), "%" )
print("O'Tooley :", count4 ,  (round(otooley_vote_percentage, 3)) , "%" )
print("--------------------------------")
print("Winner: Khan ")


with open('Election_Results.txt', 'w') as text:
    text.write("Election Results" + '\n')
    text.write('--------------------------------' + '\n')
    text.write('Total Votes: ' + str(total_votes) + '\n')
    text.write("Candidates Running" + str(unique_candidates) + '\n')
    text.write('--------------------------------' + '\n')
    text.write("Khan :" + str(count) +  str(round(khan_vote_percentage, 3)) + "%"  + '\n')
    text.write("Correy :" + str(count2) +  str(round(correy_vote_percentage, 3)) + "%"  + '\n')
    text.write("Li :" + str(count3) +  str(round(li_vote_percentage, 3)) + "%"  + '\n')
    text.write("O'Tooley :" + str(count4) + str(round(otooley_vote_percentage, 3)) + "%"  + '\n')
    text.write("--------------------------------" + '\n')
    text.write("Winner: Khan " + '\n')
    
    
    