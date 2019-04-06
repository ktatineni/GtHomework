# Dependencies and Setup
import pandas as pd
import numpy as np

# File to Load (Remember to Change These)
file_to_load = "/Users/krishna/Documents/School/GeorgiaTech/HW/HW4/Instructions/HeroesOfPymoli/Resources/purchase_data.csv"

# Read Purchasing File and store into Pandas data frame
purchase_data = pd.read_csv(file_to_load)
print(purchase_data.head())
print(purchase_data.columns)
#print(purchase_data.info())

#############################################
# ## Player Count
player_count = purchase_data['Purchase ID'].count()
print('Total number of players:',player_count)


# ## Purchasing Analysis (Total)

# * Run basic calculations to obtain number of unique items, average price, etc.
unique_items = purchase_data['Item Name'].value_counts().count()
avg_price = purchase_data['Price'].mean()
num_of_purchase = purchase_data['Price'].count()
total_revenue = purchase_data['Price'].sum()


# * Create a summary data frame to hold the results
summary_puchasing_analytics = pd.DataFrame(data = [['uniqe item',unique_items],['avg price' ,avg_price], ['number of purchases' ,num_of_purchase], ['total revenue',total_revenue]])
print(summary_puchasing_analytics.head())

#############################################

# ## Gender Demographics

total_players = purchase_data["Gender"].count()

# * Percentage and Count of Male Players
number_of_male_players = purchase_data['Gender'][purchase_data['Gender']=='Male'].count()
percentage_of_male_players = (number_of_male_players/total_players)*100
#print(percentage_of_male_players)

# * Percentage and Count of Female Players
number_of_femaleplayers = purchase_data['Gender'][purchase_data['Gender']=='Female'].count()
percentage_of_femaleplayers = (number_of_femaleplayers/total_players)*100
#print(percentage_of_femaleplayers)

# * Percentage and Count of Other / Non-Disclosed

number_of_other = purchase_data['Gender'][purchase_data['Gender']=='Other / Non-Disclosed'].count()
percentage_of_other = (number_of_other/total_players)*100
#print(percentage_of_other)

#Summary DataFrame
summary_gender_demographics = pd.DataFrame(data = [['Total Players', total_players], ['Number of Male Players', number_of_male_players],
['Number of Female Players', number_of_femaleplayers], ["Number of Other Players", number_of_other],["Percentage of Male Players", percentage_of_male_players],
['Percentage of Female Players', percentage_of_femaleplayers], ['Percentage of Other', percentage_of_other]])
print(summary_gender_demographics, '\n\n')


#############################################

# ## Purchasing Analysis (Gender)

#Purchase Count
purchase_count_male = purchase_data['Price'][purchase_data['Gender']=='Male'].count()
#print(purchase_count_male)
purchase_count_female = purchase_data['Price'][purchase_data['Gender']=='Female'].count()
#print(purchase_count_female)
purchase_count_other = purchase_data['Price'][purchase_data['Gender']=='Other / Non-Disclosed'].count()
#print(purchase_count_other)



#Average Puchase Price
avg_purchase_price_male = purchase_data['Price'][purchase_data['Gender']=='Male'].mean()
avg_purchase_price_female  = purchase_data['Price'][purchase_data['Gender']=='Female'].mean()
avg_purchase_price_other = purchase_data['Price'][purchase_data['Gender']=='Other / Non-Disclosed'].mean()
#print(avg_purchase_price_male, avg_purchase_price_female, avg_purchase_price_other)

#Total Purchase Value
total_purchase_value_male = purchase_data['Price'][purchase_data['Gender']=='Male'].sum()
total_purchase_value_female = purchase_data['Price'][purchase_data['Gender']=='Female'].sum()
total_purchase_value_other = purchase_data['Price'][purchase_data['Gender']=='Other / Non-Disclosed'].sum()
#print(total_purchase_value_male, total_purchase_value_female, total_purchase_value_other)


#Average Purchase Total per Person by Gender

total_purchase_perperson_male = purchase_data[["Price", 'SN']][purchase_data['Gender']=='Male'].groupby('SN').mean()
#print(total_purchase_perperson_male)

total_purchase_perperson_female = purchase_data.groupby('SN')
total_purchase_perperson_female = purchase_data[["Price", 'SN']][purchase_data['Gender']=='Female'].mean()
#print(total_purchase_perperson_female)

total_purchase_perperson_other = purchase_data.groupby('SN')
total_purchase_perperson_other = purchase_data[["Price", 'SN']][purchase_data['Gender']=='Other / Non-Disclosed'].mean()
#print(total_purchase_perperson_other)

summary_purchasing_analytics_gender = pd.DataFrame(data = [['Purchase Count Male' , purchase_count_male], ['Purchase Count Female', purchase_count_female], ["Purchase Count Non-Disclosed", purchase_count_other],
["Average Purchase Price Male", avg_purchase_price_male], ["Average Purchase Price Female", avg_purchase_price_female], ["Average Purchase Price Other", avg_purchase_price_other],
['Total Purchase Male', total_purchase_value_male], ['TotalPurchase Female', total_purchase_value_female], ['Total Purchase Other', total_purchase_value_other],
['Average Purchase Total per Person Male', total_purchase_perperson_male], ['Average Purchase Total per Person Female', total_purchase_perperson_female], ['Average Purchase Total per Person', total_purchase_perperson_other]])

print(summary_purchasing_analytics_gender, '\n')

#############################################
# Age Demographics


bins = [0,13,21,100]
group_name = ['0-13','14-21','above 21']
demographic_column = pd.cut(purchase_data['Age'], bins, labels = group_name)
purchase_data['demographics'] = demographic_column

#age group purchase count
kid_purchase_count = purchase_data['demographics'][purchase_data['demographics']=='0-13'].count()

teenage_purchase_count = purchase_data['demographics'][purchase_data['demographics']=='14-21'].count()

adult_purchase_count = purchase_data['demographics'][purchase_data['demographics']=='above 21'].count()

#Total Purchase price
kid_average_purchase_price = purchase_data["Price"][purchase_data['demographics']=='0-13'].mean()
teen_average_purchase_price = purchase_data['Price'][purchase_data['demographics']=='14-21'].mean()
adult_average_purchase_price = purchase_data['Price'][purchase_data['demographics']=='above 21'].mean()

#Total Purchase value
kid_purchase_value = purchase_data['Price'][purchase_data['demographics']=='0-13'].sum()
teen_purchase_value = purchase_data['Price'][purchase_data['demographics']=='14-21'].sum()
adult_purchase_value = purchase_data['Price'][purchase_data['demographics']=='above 21'].sum()

#Average Purchase Toatl per Person by Age Group
kid_average_purchase_total_perperson = purchase_data[['Price', 'SN']][purchase_data['demographics']=='0-13'].groupby('SN').mean()
teen_average_purchase_total_perperson = purchase_data[['Price', 'SN']][purchase_data['demographics']=='14-21'].groupby('SN').mean()
adult_average_purchase_total_perperson = purchase_data[['Price', 'SN']][purchase_data['demographics']=='above 21'].groupby('SN').mean()

summary_agedemographics = pd.DataFrame(data = [['Number of kids', kid_purchase_count], ['Number of teenagers', teenage_purchase_count], ['Number of adults', adult_purchase_count],
['The avg. purchase of a kid', kid_average_purchase_price], ['The avg. purchase of a teenager', teen_average_purchase_price], ['The avg. purchase of an adult', adult_average_purchase_price],
['Total purchase of kids', kid_purchase_value], ['Total purchase of teenager', teen_purchase_value], ['Total purchase of adults', adult_purchase_value],
['Kid average purchase total per person', kid_average_purchase_total_perperson], ['Teen average purchase total per person', teen_average_purchase_total_perperson], ['Adult average purchase total per person', adult_average_purchase_total_perperson]])

print(summary_agedemographics)

# ## Top Spenders
#print(purchase_data)
top_spenders = purchase_data.groupby('SN').sum()
print(top_spenders.sort_values(by = ['Price'], ascending = False))
#.sort_values(by = 'Price', axis = 1, ascending = False)




# * Create a summary data frame to hold the results
#
#
# * Sort the total purchase value column in descending order
#
#
# * Optional: give the displayed data cleaner formatting
#
#
# * Display a preview of the summary data frame
#
#

# In[8]:





# ## Most Popular Items

# * Retrieve the Item ID, Item Name, and Item Price columns
#
#
# * Group by Item ID and Item Name. Perform calculations to obtain purchase count, item price, and total purchase value
#
#
# * Create a summary data frame to hold the results
#
#
# * Sort the purchase count column in descending order
#
#
# * Optional: give the displayed data cleaner formatting
#
#
# * Display a preview of the summary data frame
#
#

# In[9]:





# ## Most Profitable Items

# * Sort the above table by total purchase value in descending order
#
#
# * Optional: give the displayed data cleaner formatting
#
#
# * Display a preview of the data frame
#
#

# In[10]:
