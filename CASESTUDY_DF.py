#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd


# In[3]:


pip install xmltodict


# In[4]:


import xmltodict
with open('regions.xml') as xml_file:
    df=xmltodict.parse(xml_file.read())

df


# In[5]:


region=df['data']['region']
region


# In[58]:


for employee in region:
    print(f"id:{employee['id']},name:{employee['name']},manager:{employee['manager']}")


# READING TEXT FILE

# In[8]:


df1 = pd.read_csv("customers.csv")
print(df1)


# In[9]:


df1.describe()


# In[10]:


df1.nunique()


# In[11]:


df1['city']


# In[12]:


df1.columns


# In[13]:


df1.head()


# In[14]:


df1.tail()


# In[15]:


df1.sort_values(by ="age")


# In[16]:


df1.sort_values(by ="age" ,ascending=False)


# READING JSON FILE

# In[6]:


df2 = pd.read_json("products.json")
print(df2)


# In[47]:


df2.describe()


# In[48]:


df2.columns


# In[49]:


df2.size


# In[50]:


df2.head()


# In[51]:


df2.tail()


# In[52]:


df2.sort_values(by ="price")


# In[7]:


df3 = pd.read_csv("sales.txt")
print(df3)


# In[54]:


df3 = pd.read_csv("sales.txt",delimiter='\t')
print(df3)


# In[55]:


df4 = pd.read_csv("task.txt")
print(df4)


# In[4]:


url="https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv"
df4 = pd.read_csv(url)
df4.head()


# COMBINE DATAFRAMES

# In[17]:


import pandas as pd

# Reading the data
df1 = pd.read_csv('customers.csv')
df2 = pd.read_json('products.json')
df3 = pd.read_csv('sales.txt', sep='\t')

# Combining the DataFrames
final_df = df3.merge(df2, on='product_id').merge(df1, on='customer_id')

# Display the final DataFrame
print(final_df)


# In[ ]:




