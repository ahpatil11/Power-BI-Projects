#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# In[2]:


train = pd.read_excel('Data_Train.xlsx')
train.head()


# In[3]:


combined = train.copy()


# In[4]:


combined.head()


# In[5]:


combined.Delivery_Time.value_counts()


# In[6]:


combined.Delivery_Time.value_counts().plot(kind = 'bar')


# In[7]:


combined.columns


# In[8]:


combined.Reviews.unique()


# In[9]:


combined.Votes.value_counts()


# In[10]:


combined.Rating.unique()


# In[11]:


combined.Average_Cost.unique()


# In[12]:


combined.Minimum_Order.unique()


# In[13]:


int(combined.Minimum_Order[0].split('₹')[1])


# In[14]:


mylist = []
for i in combined.Minimum_Order:
    mylist.append(int(i.split('₹')[1]))


# In[15]:


mylist


# In[16]:


combined['MinOrder_Cleansed'] = pd.Series(mylist)
combined.head()


# In[17]:


a = '₹2,050'.split('₹')[1]
a


# In[18]:


a.replace(',',"")


# In[19]:


combined.loc[combined.Average_Cost == 'for']


# In[20]:


combined.loc[combined.Average_Cost == 'for', 'Average_Cost'] = '0'


# In[21]:


combined.loc[combined.Average_Cost == 'for']


# In[22]:


cost = []
for i in combined.Average_Cost:
    cost.append(int(i.replace('₹', '').replace(',', '')))


# In[23]:


cost


# In[24]:


combined['AvgCost_Cleaned'] = pd.Series(cost)
combined.head()


# In[25]:


combined.AvgCost_Cleaned.unique()


# In[26]:


combined.Location.unique()


# In[27]:


combined.Location[0].split(', ')[-1]


# In[28]:


locs = []
for i in combined.Location:
    locs.append(i.split(', ')[-1])


# In[29]:


combined['Location_cleansed'] = pd.Series(locs)


# In[30]:


combined.Location_cleansed.unique()


# In[31]:


combined[combined.Location_cleansed == 'Electronic City']['Location'].unique()


# In[32]:


combined.Location_cleansed.replace(to_replace = ['Marathalli', 'Whitefield', 'Majestic', 'BTM Layout,Bangalore',
                                                 'Electronic City'], value = ['Bangalore']*5, inplace = True)


# In[33]:


combined.Location_cleansed.replace(to_replace = ['Maharashtra', 'Pune University'], value = ['Pune']*2, inplace = True)


# In[34]:


combined.Location_cleansed.replace(to_replace = ['Delhi University-GTB Nagar', 'Timarpur',
                                                'Delhi Cantt.', 'India Gate'], value = ['Delhi']*4, inplace = True)


# In[35]:


combined.loc[combined.Location_cleansed == 'Gurgoan', 'Location_cleansed'] = 'Gurgaon'


# In[36]:


combined.Location_cleansed.replace('Sector 63A,Gurgaon', 'Gurgaon', inplace = True)


# In[37]:


combined.Location_cleansed.replace(to_replace = ['Mumbai Central', 'Mumbai CST Area'], value = ['Mumbai']*2, inplace = True)


# In[38]:


combined.Location_cleansed.replace(to_replace = ['Begumpet', 'Hyderabad'], value = ['Hyderabad']*2, inplace = True)


# In[39]:


combined.Location_cleansed.unique()


# In[40]:


combined.head()


# In[41]:


combined.Location_cleansed.value_counts().plot(kind = 'bar')


# In[42]:


combined.Cuisines.unique()


# In[43]:


combined.Cuisines[0].split(", ")


# In[44]:


food = []
for i in combined.Cuisines:
    food.append(i.split(", "))


# In[45]:


df = pd.DataFrame(food)


# In[46]:


df.head()


# In[47]:


df[0].unique()


# In[48]:


fastfood = ['Fast Food','Cafe','Burger','Street Food', 'Pizza', 'Rolls','Momos','Finger Food', 'Sandwich',
            'Bar Food', 'Wraps','Hot dogs']

bevrages = ['Coffee','Bubble Tea','Juices','Tea','Beverages']

deserts = ['Ice Cream','Desserts','Mithai','Bakery', 'Mishti' ,'Paan','Frozen Yogurt']

maincourse = ['Italian', 'Mughlai', 'South Indian', 'Chinese',  'North Indian','Biryani', 'Kerala','Asian', 'Bengali'
             , 'European',  'Continental', 'Andhra', 'German', 'Chettinad', 'Parsi','Japanese','Salad', 'Tamil',
             'North Eastern', 'Maharashtrian','Tibetan', 'Arabian','Konkan', 'Odia','Lebanese',
             'American', 'Mediterranean', 'Bohri','Mangalorean', 'Thai', 'Healthy Food', 'Raw Meats', 'Gujarati',
              'Seafood', 'Rajasthani', 'BBQ', 'Coffee', 'Mexican', 'Goan','Korean', 'Kebab', 'Kashmiri',
             'Bihari', 'Portuguese','Afghan', 'Awadhi', 'Malwani', 'Malaysian','Hyderabadi', 'French',
             'Modern Indian', 'Sushi', 'Hot dogs','Iranian', 'Brazilian', 'Indian', 'African', 'Turkish',
             'Assamese', 'Naga', 'Middle Eastern', 'Vietnamese',
             'Steak','Cantonese','Belgian','Charcoal Chicken','Tex-Mex']


# In[49]:


#Function to convert the food into cat

def makefoodcat(x):
   if (x in fastfood):
       return('Fast Food')
   elif(x in bevrages):
       return('Bevrages')
   elif(x in deserts):
       return('Deserts')
   else:
       return('Main Course')


# In[50]:


combined['Cuisines_Cleansed'] = pd.Series(df[0].apply(makefoodcat))


# In[51]:


#Imputing the values
combined.loc[combined.Average_Cost=='0','AvgCost_Cleaned'] = 150


# In[52]:


combined[(combined.Location_cleansed == 'Pune') & (combined.Cuisines_Cleansed == 'Fast Food')]['AvgCost_Cleaned'].describe()


# In[53]:


combined.head()


# In[54]:


combined.Rating.unique()


# In[55]:


combined[combined.Rating == 'NEW'].shape


# In[56]:


combined.loc[combined.Restaurant == 'ID_6472']


# In[57]:


combined.Rating = pd.to_numeric(combined.Rating, errors= 'coerce')


# In[58]:


combined.Rating.describe()


# In[59]:


combined.Rating.fillna(value = 3.6, inplace = True)


# In[60]:


combined.Reviews.unique()


# In[61]:


combined.Reviews = pd.to_numeric(combined.Reviews, errors= 'coerce')


# In[62]:


combined.Reviews.describe()


# In[63]:


combined.Reviews.fillna(value = 26, inplace = True)


# In[64]:


combined.Votes = pd.to_numeric(combined.Votes, errors= 'coerce')


# In[65]:


combined.Votes.describe()


# In[66]:


combined.Votes.fillna(value = 63, inplace = True)


# In[67]:


combined.Rating.unique()


# In[68]:


combined.head()


# In[69]:


combined['Delivery'] = combined['Delivery_Time'].apply(lambda x:x.split(' ')[0])

combined['Delivery_Time']= combined['Delivery_Time'].apply(lambda x:x.split(' ')[0])
# In[70]:


combined['Delivery'] = combined['Delivery'].astype(int)


# In[71]:


combined['Delivery'].unique()


# In[72]:


combined.columns


# In[76]:


combined.head()


# In[74]:


combined = combined.rename({'Location' : 'Area'}, axis = 1)


# In[75]:


combined = combined.drop(['Average_Cost', 'Minimum_Order'], axis = 1)
combined.head()


# In[77]:


combined = combined.rename({'MinOrder_Cleansed' : 'Minimum_Order', 'AvgCost_Cleaned' : 'Average_Cost', 
                            'Location_cleansed' : 'Location', 'Cuisines_Cleansed' : 'Cuisines_Type'}, axis = 1)
combined.head()


# In[78]:


combined.to_excel('New Train.xlsx', index= False)


# In[79]:


combined.info()


# In[ ]:




