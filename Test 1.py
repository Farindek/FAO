#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd
# Import plotting library
import matplotlib.pyplot as plt
food_df = pd.read_csv('/Users/oluwakemifarinde/Downloads/FoodBalanceSheets_E_Africa_NOFLAG.csv', encoding='latin-1')
food_df


# In[2]:


#4
food_df.shape


# In[3]:


len(food_df)


# In[7]:


#6
my_tuppy = (1,2,5,8)
my_tuppy[2] = 6


# In[6]:


#5
S = [['him', 'sell'], [90, 28, 43]]
S[0][1][1]


# In[10]:


#7
y = [(2, 4), (7, 8), (1, 5, 9)]
y[1][1]


# In[15]:


#11
food_df.groupby('Item')['Y2014'].count()


# In[13]:


food_df.groupby('Item')['Item'].count()


# In[16]:


#11
food_df.groupby('Item')['Y2017'].count()


# In[17]:


food_df.groupby('Item')['Y2017'].sum()


# In[18]:


food_df.groupby('Item')['Y2014'].sum()


# In[20]:


#12
food_df.describe()


# In[21]:


#13
food_df.isnull().sum()


# In[24]:


#15
food_df.groupby('Element')['Y2015'].sum()


# In[25]:


#15
food_df.groupby('Element')['Y2016'].sum()


# In[26]:


#15, 16
food_df.groupby('Element')['Y2014'].sum()


# In[27]:


#15
food_df.groupby('Element')['Y2017'].sum()


# In[28]:


#15, 17, 18
food_df.groupby('Element')['Y2018'].sum()


# In[31]:


#19
food_df.groupby('Area')['Y2018'].sum()


# In[32]:


#20
food_df.groupby('Area')['Area'].count()


# In[34]:


corr=food_df.corr()


# In[35]:


#14
corr


# In[ ]:




