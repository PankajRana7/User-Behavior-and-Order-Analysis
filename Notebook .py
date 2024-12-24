#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


# In[5]:


UserDetails =df= pd.read_csv("UserDetails.csv")


# In[6]:


df.head()


# In[7]:


CookingSessions =df= pd.read_csv("CookingSessions.csv")


# In[8]:


df.head()


# In[9]:


OrderDetails =df= pd.read_csv("OrderDetails.csv")


# In[10]:


df.head()


# In[17]:


revenue_by_dish = OrderDetails.groupby('Dish Name')['Amount (USD)'].sum().reset_index()


# In[18]:


highest_revenue_dish = revenue_by_dish.sort_values(by='Amount (USD)', ascending=False).head(1)


# In[19]:


print("Dish with the highest revenue generation:")
print(highest_revenue_dish)


# In[20]:


highly_rated_sessions = CookingSessions[CookingSessions['Session Rating'] >= 4]


# In[21]:


average_duration_highly_rated = highly_rated_sessions['Duration (mins)'].mean()


# In[22]:


print(f"Average session duration for highly-rated cooking sessions: {average_duration_highly_rated:.2f} minutes")


# In[30]:


average_ratings = CookingSessions.groupby('Dish Name')['Session Rating'].mean().reset_index()


# In[31]:


sorted_ratings = average_ratings.sort_values(by='Session Rating', ascending=False)


# In[32]:


print(sorted_ratings)


# In[33]:


user_revenue = OrderDetails.groupby('User ID')['Amount (USD)'].sum().reset_index()


# In[34]:


merged_data = pd.merge(UserDetails, user_revenue, on='User ID', how='left')


# In[35]:


max_revenue_user = merged_data[merged_data['Amount (USD)'] == merged_data['Amount (USD)'].max()]


# In[36]:


print(max_revenue_user[['User Name', 'Age', 'Location', 'Amount (USD)']])


# In[39]:


average_rating_by_meal_type = OrderDetails.groupby('Meal Type')['Rating'].mean().reset_index()


# In[40]:


highest_rated_meal_type = average_rating_by_meal_type.loc[average_rating_by_meal_type['Rating'].idxmax()]


# In[41]:


print("Average rating of dishes by meal type:")
print(average_rating_by_meal_type)
print(f"\nMeal Type with highest user satisfaction: {highest_rated_meal_type['Meal Type']} with an average rating of {highest_rated_meal_type['Rating']}")


# In[46]:


merged_data = pd.merge(CookingSessions, OrderDetails, on=['Session ID', 'Dish Name'], how='inner')


# In[47]:


merged_data['Rating Category'] = merged_data['Session Rating'].apply(lambda x: 'Positive' if x >= 4 else 'Negative')


# In[48]:


sales_by_dish_rating = merged_data.groupby(['Dish Name', 'Rating Category'])['Amount (USD)'].sum().reset_index()


# In[49]:


plt.figure(figsize=(10, 6))
sns.barplot(data=sales_by_dish_rating, x='Dish Name', y='Amount (USD)', hue='Rating Category')
plt.title('Sales of Dishes Based on Session Ratings')
plt.xlabel('Dish Name')
plt.ylabel('Total Sales (USD)')
plt.xticks(rotation=45)
plt.show()


# In[55]:


merged_data = pd.merge(OrderDetails, UserDetails, on='User ID')


# In[56]:


revenue_by_location_age = merged_data.groupby(['Location', 'Age'])['Amount (USD)'].sum().reset_index()


# In[57]:


revenue_by_location_age.rename(columns={'Amount (USD)': 'Total Revenue'}, inplace=True)


# In[58]:


print(revenue_by_location_age)


# In[59]:


plt.figure(figsize=(10, 6))
sns.barplot(x='Age', y='Total Revenue', hue='Location', data=revenue_by_location_age)
plt.title('Total Revenue by Age and Location')
plt.xlabel('Age')
plt.ylabel('Total Revenue (USD)')
plt.legend(title='Location', loc='upper right')
plt.show()


# In[64]:


merged_data = pd.merge(OrderDetails,UserDetails, on='User ID')


# In[65]:


revenue_and_orders_by_age = merged_data.groupby('Age').agg(
    Total_Revenue=('Amount (USD)', 'sum'),
    Total_Orders=('Order ID', 'count')
).reset_index()


# In[66]:


print(revenue_and_orders_by_age)


# In[69]:


dish_revenue = OrderDetails.groupby('Dish Name')['Amount (USD)'].sum().reset_index()


# In[70]:


dish_revenue = dish_revenue.sort_values(by='Amount (USD)', ascending=False)


# In[71]:


print(dish_revenue)


# In[72]:


plt.figure(figsize=(8, 6))
plt.bar(dish_revenue['Dish Name'], dish_revenue['Amount (USD)'], color='skyblue')

plt.xlabel('Dish Name')
plt.ylabel('Total Revenue (USD)')
plt.title('Total Revenue by Dish')
plt.xticks(rotation=45)
plt.show()


# In[80]:


dish_popularity = OrderDetails_merged.groupby('Dish Name').agg(
    total_orders=('Order ID', 'count')
).reset_index().sort_values(by='total_orders', ascending=False)

print(dish_popularity)


# In[ ]:




