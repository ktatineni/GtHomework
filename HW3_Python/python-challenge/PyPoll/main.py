import pandas as pd

poll_data = pd.read_csv('/Users/krishna/Documents/School/GeorgiaTech/HW/HW3/python-challenge/PyPoll/Resources/election_data.csv')
print(poll_data.head())

total_votes = poll_data['Voter ID'].count()
print(total_votes)

#candidate_list & total number of votes each candidate won
candidate_list = poll_data['Candidate'].value_counts()
print(candidate_list)


#Percentage
percentage_of_votes = candidate_list/total_votes
print(percentage_of_votes)

winner = percentage_of_votes.max()
print('\n\nKhan:',winner)
winner = 'Khan' + str(winner)


with open('/Users/krishna/Documents/School/GeorgiaTech/HW/HW3/python-challenge/PyPoll/output.txt','w') as file:

    file.write(str(total_votes))
    file.write('\n')
    file.write('\n')
    file.write(str(candidate_list))
    file.write('\n')
    file.write('\n')
    file.write(str(percentage_of_votes))
    file.write('\n')
    file.write('\n')
    file.write(str(winner))
