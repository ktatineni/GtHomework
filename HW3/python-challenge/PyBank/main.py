
import pandas as pd

budget_data = pd.read_csv('/Users/krishna/Documents/School/GeorgiaTech/HW/HW3/python-challenge/PyBank/Resources/budget_data.csv')
print(budget_data.head())

#count the number of months
total_months = budget_data.Date.count()
print("The total number of months included in the dataset:" ,total_months)
total_months = "The total number of months:" + str(total_months)

#output 86 months

#sum of profit and loses
total_amount = budget_data['Profit/Losses'].sum()
print("\nThe net total amount of Profit/Losses over the entire period:",total_amount)
total_amount = 'total profit:' + str(total_amount)
#38382578

# Avg. Profit/Loses
avg_amount = budget_data['Profit/Losses'].mean()
print("\nThe average of the changes in Profit/Losses over the entire period:",avg_amount)
avg_amount = 'average profit/loss:' + str(avg_amount)
#446309.0465116279

#Max Amount
var = ['Date','Profit/Losses']
max_amount = budget_data[var].max()
print("\nThe greatest increase in profits (date and amount) over the entire period:",max_amount)
max_amount = 'the max amount:' + str(max_amount)

#Min Amoount
min_amount = budget_data[var].min()
print("\nThe greatest decrease in losses (date and amount) over the entire period:",min_amount)
min_amount = 'The mim amount: ' + str(min_amount)



with open('/Users/krishna/Documents/School/GeorgiaTech/HW/HW3/python-challenge/PyBank/output.txt','w') as file:
    file.write(str(total_months))
    file.write('\n')
    file.write('\n')
    file.write(str(total_amount))
    file.write('\n')
    file.write('\n')
    file.write(str(avg_amount))
    file.write('\n')
    file.write('\n')
    file.write(str(max_amount))
    file.write('\n')
    file.write('\n')
    file.write(str(min_amount))
