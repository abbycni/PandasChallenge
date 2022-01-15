#!/usr/bin/env python
# coding: utf-8

# ### Note
# * Instructions have been included for each segment. You do not have to follow them exactly, but they are included to help you think through the steps.

# In[16]:


# Dependencies and Setup
import pandas as pd
import numpy

# File to Load (Remember to Change These)
file_to_load = "Resources/purchase_data.csv"

# Read Purchasing File and store into Pandas data frame
purchase_data = pd.read_csv(file_to_load)

df=purchase_data 
print(df.head())
df.columns


# ## Player Count

# * Display the total number of players
# 

# In[17]:



#total_players- Not unique 
total_players=len(purchase_data["SN"])
print(total_players)
#total_playersunique- The unique number of players 
total_playersunique=len(purchase_data["SN"].unique())
print(total_playersunique)


# ## Purchasing Analysis (Total)

# * Run basic calculations to obtain number of unique items, average price, etc.
# 
# 
# * Create a summary data frame to hold the results
# 
# 
# * Optional: give the displayed data cleaner formatting
# 
# 
# * Display the summary data frame
# 

# In[18]:


unique_items=len(purchase_data["Item ID"].unique())
unique_items
average_price=(purchase_data["Price"]).mean()
average_price 
Total_Item_count=(purchase_data["Purchase ID"]).count()
Total_revenue=(purchase_data)["Price"].sum()

Purchase_analysis_df=pd.DataFrame({"Number of unique Items":unique_items,"Average Price":[average_price], "Number of purchases":[Total_Item_count], "Total Revenue":[Total_revenue]})

Purchase_analysis_df                  
              
   


# ## Gender Demographics

# * Percentage and Count of Male Players
# 
# 
# * Percentage and Count of Female Players
# 
# 
# * Percentage and Count of Other / Non-Disclosed
# 
# 
# 

# In[19]:


Gender_Group=(purchase_data).groupby("Gender")
print(Gender_Group)

Gender_Group["SN"].nunique()


pd.DataFrame({"Total_count":Gender_Group["SN"].nunique(),"Percentage":Gender_Group["SN"].nunique()/total_playersunique *100})


# # ## Purchasing Analysis (Gender)

# * Run basic calculations to obtain purchase count, avg. purchase price, avg. purchase total per person etc. by gender
# 
# 
# 
# 
# * Create a summary data frame to hold the results
# 
# 
# * Optional: give the displayed data cleaner formatting
# 
# 
# * Display the summary data frame

# In[20]:


purchase_count=Gender_Group.count()

average_purchase_price=Gender_Group["Price"].mean()

purchase_total=Gender_Group["Price"].sum()

#AverageTotalpurchaseperperson= Gender_Group["Price"].sum()/"Total_count":Gender_Group["SN"].nunique()
#Purchase_analysis_gender_df=pd.DataFrame({"Purchase Count":Gender_Group.[purchase_count],"Average Purchase Price":Gender_Group.[average_purchase_price], "Total Purchase Value":Gender_Group.[purchase_total]})
pd.DataFrame({"Purchase_Count":Gender_Group["SN"].count(),"Average_Purchase_Price":Gender_Group["Price"].mean(), "Total Purchase Value":Gender_Group["Price"].sum(), "Average Total Purchase per Person":Gender_Group["Price"].sum()/Gender_Group["SN"].nunique()})

#Purchase_analysis_gender_df                      
    
#Average_price_per_person=({GenderGroup(Gender_Group["SN"].uninque().mean()}["Price"].mean()


# ## Age Demographics

# * Establish bins for ages
# 
# 
# * Categorize the existing players using the age bins. Hint: use pd.cut()
# 
# 
# * Calculate the numbers and percentages by age group
# 
# 
# * Create a summary data frame to hold the results
# 
# 
# * Optional: round the percentage column to two decimal points
# 
# 
# * Display Age Demographics Table
# 

# In[6]:


# Create bins in which to place values based upon TED Talk views
bins = [0 , 9, 14, 19, 24, 29, 34, 39, 45]

# Create labels for these bins
group_labels = ["less than 10", "10 to 14", "15 to 19", "20 to 24", "25 to 29", "30 to 34",
                "35 to 39", "40+"]
# Slice the data and place it into bins
pd.cut(purchase_data["Age"], bins, labels=group_labels).head()

# Place the data series into a new column inside of the DataFrame
purchase_data["Purchase Data by age"] = pd.cut(purchase_data["Age"], bins, labels=group_labels)
purchase_data.head()


Age_Group=(purchase_data).groupby("Purchase Data by age")

UniqueTotals=Age_Group["SN"].nunique()
Percentage=UniqueTotals/total_playersunique *100

Age_demograohics_df=pd.DataFrame({"Total Count":UniqueTotals,"Percentage of Players":Percentage})
#df.sort_values(by='Purchase Data by age', ascending=False).head()

Age_demograohics_df


# ## Purchasing Analysis (Age)

# * Bin the purchase_data data frame by age
# 
# 
# * Run basic calculations to obtain purchase count, avg. purchase price, avg. purchase total per person etc. in the table below
# 
# 
# * Create a summary data frame to hold the results
# 
# 
# * Optional: give the displayed data cleaner formatting
# 
# 
# * Display the summary data frame

# In[7]:


# Create bins in which to place values based upon TED Talk views
bins = [0 , 9, 14, 19, 24, 29, 34, 39, 45]

# Create labels for these bins
group_labels = ["less than 10", "10 to 14", "15 to 19", "20 to 24", "25 to 29", "30 to 34",
                "35 to 39", "40+"]
# Slice the data and place it into bins
pd.cut(purchase_data["Age"], bins, labels=group_labels).head()

# Place the data series into a new column inside of the DataFrame
purchase_data["Purchase Data by age"] = pd.cut(purchase_data["Age"], bins, labels=group_labels)
purchase_data.head()

Age_Group=(purchase_data).groupby("Purchase Data by age")

UniqueTotals=Age_Group["SN"].nunique()

Totals=purchase_data["Purchase Data by age"].value_counts()

#df.groupby([df.Price])
#Average_Purchase_Price=(purchase_data)["Price"].mean()
Average_Purchase_Price=Age_Group["Price"].mean()


Age_demograohics_df=pd.DataFrame({"Total Count":Totals,"Average Purchase Price":Average_Purchase_Price, "Total Purchaase Value":Totals*Average_Purchase_Price, "Avg Purchase per Person":Totals*Average_Purchase_Price/UniqueTotals})

Age_demograohics_df


# ## Top Spenders

# ## Age Demographics

# * Run basic calculations to obtain the results in the table below
# 
# 
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


Players_Group=(purchase_data).groupby("SN")


df=pd.DataFrame({"Purchase Count by Player":Players_Group["SN"].count(),"Average Purchase Price":Players_Group["Price"].sum()/Players_Group["SN"].count(), "Total Purchase Value":Players_Group["Price"].sum()})

df.sort_values(by=["Total Purchase Value"], ascending=False).head()

## Most Popular Items
# * Retrieve the Item ID, Item Name, and Item Price columns
# 
# 
# * Group by Item ID and Item Name. Perform calculations to obtain purchase count, average item price, and total purchase value
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

# In[15]:


Item_Group=(purchase_data).groupby("Item ID")

df=pd.DataFrame({"Item name":Item_Group["Item Name"],"Purchase Count":Item_Group["Item ID"].count(),"Item Price":Item_Group["Price"].sum()/Item_Group["SN"].nunique(), "Total Purchase Value":Item_Group["Price"].sum()})
df.sort_values(by='Purchase Count', ascending=False).head()

#print(df)


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


Item_Group=(purchase_data).groupby("Item ID")

pd.DataFrame({"Item Name":Item_Group["Item Name"],"Purchase Count":Item_Group["Item ID"].count(),"Item Price":Item_Group["Price"].sum()/Item_Group["SN"].nunique(), "Total Purchase Value":Item_Group["Price"].sum()})

df.sort_values(by='Purchase Count', ascending=False).head()


# In[ ]:




