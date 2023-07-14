#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import matplotlib.pylab as plt
import seaborn as sns


# # Dataset

# https://www.kaggle.com/datasets/robikscube/rollercoaster-database

# In[ ]:


# Set path ==> coaster_db.csv 


# In[2]:


df = pd.read_csv('C:/Users/USER/Desktop/PYTHON/Mainboot/Notebook Jupyter/coaster_db.csv')


# # Step 1: Data Understanding

# In[ ]:


### Dataframe Shape
### head and tail
### dtypes
### describe


# In[3]:


df.shape


# In[4]:


df.head()


# In[5]:


df.tail()


# In[6]:


df.columns


# In[7]:


df.dtypes


# In[8]:


df.describe()


# # Step 2: Data Preperation
# 

# In[18]:


#Dropping irrelevant columns and rows
#Identifying duplicated columns
#Renaming Columns
#Feature Creation


# In[9]:


df.head()


# In[ ]:


# observe what are in columns(column names)


# In[10]:


df.columns


# In[11]:


df[['coaster_name', 'Length', 'Speed', 'Location', 'Status', 'Opening date',
       'Type', 'Manufacturer', 'Height restriction', 'Model', 'Height',
       'Inversions', 'Lift/launch system', 'Cost', 'Trains', 'Park section',
       'Duration', 'Capacity', 'G-force', 'Designer', 'Max vertical angle',
       'Drop', 'Soft opening date', 'Fast Lane available', 'Replaced',
       'Track layout', 'Fastrack available', 'Soft opening date.1',
       'Closing date', 'Opened', 'Replaced by', 'Website',
       'Flash Pass Available', 'Must transfer from wheelchair', 'Theme',
       'Single rider line available', 'Restraint Style',
       'Flash Pass available', 'Acceleration', 'Restraints', 'Name',
       'year_introduced', 'latitude', 'longitude', 'Type_Main',
       'opening_date_clean', 'speed1', 'speed2', 'speed1_value', 'speed1_unit',
       'speed_mph', 'height_value', 'height_unit', 'height_ft',
       'Inversions_clean', 'Gforce_clean']]


# In[13]:


# Decide what we want to keep and don't want(columns)   
# analysis objectives, and domain knowledge


# In[12]:


df[['coaster_name', 
    #'Length', 'Speed', 
    'Location', 'Status', #'Opening date',
      # 'Type',
    'Manufacturer', #'Height restriction', 'Model', 'Height',
       #'Inversions', 'Lift/launch system', 'Cost', 'Trains', 'Park section',
       #'Duration', 'Capacity', 
    #'G-force', 'Designer', 'Max vertical angle',
       #'Drop', 'Soft opening date', 'Fast Lane available', 'Replaced',
       #'Track layout', 'Fastrack available', 'Soft opening date.1',
       #'Closing date', 'Opened', 
    #'Replaced by', 'Website',
       #'Flash Pass Available', 'Must transfer from wheelchair', 'Theme',
       #'Single rider line available', 'Restraint Style',
       #'Flash Pass available', 'Acceleration', 'Restraints', 'Name',
       'year_introduced', 'latitude', 'longitude', 'Type_Main',
       'opening_date_clean',# 'speed1', 'speed2', 'speed1_value', 'speed1_unit',
       'speed_mph', 
    #'height_value', 'height_unit', 
    'height_ft',
       'Inversions_clean', 'Gforce_clean']]


# In[ ]:


#can delete column by drop 


# In[23]:


#Example for dropping single column

#df.drop(['Opening date'],axis=1) # axis 1 denoted column here


# #### Renaming dataframe (df) into df1

# In[13]:


df1=df[['coaster_name', 
    #'Length', 'Speed', 
    'Location', 'Status', #'Opening date',
      # 'Type',
    'Manufacturer', #'Height restriction', 'Model', 'Height',
       #'Inversions', 'Lift/launch system', 'Cost', 'Trains', 'Park section',
       #'Duration', 'Capacity', 
    #'G-force', 'Designer', 'Max vertical angle',
       #'Drop', 'Soft opening date', 'Fast Lane available', 'Replaced',
       #'Track layout', 'Fastrack available', 'Soft opening date.1',
       #'Closing date', 'Opened', 
    #'Replaced by', 'Website',
       #'Flash Pass Available', 'Must transfer from wheelchair', 'Theme',
       #'Single rider line available', 'Restraint Style',
       #'Flash Pass available', 'Acceleration', 'Restraints', 'Name',
       'year_introduced', 'latitude', 'longitude', 'Type_Main',
       'opening_date_clean',# 'speed1', 'speed2', 'speed1_value', 'speed1_unit',
       'speed_mph', 
    #'height_value', 'height_unit', 
    'height_ft',
       'Inversions_clean', 'Gforce_clean']].copy()


# In[14]:


df1.shape


# In[15]:


df1.dtypes


# In[16]:


pd.to_datetime(df1['opening_date_clean'])


# In[17]:


df1['opening_date_clean']=pd.to_datetime(df1['opening_date_clean'])


# In[18]:


df1['opening_date_clean']


# In[19]:


df1.dtypes


# In[20]:


#Rename columns
df1.columns


# In[ ]:


# Renaming column names as you want as {"old name":"New name"}


# In[21]:


df1=df1.rename(columns={'coaster_name':'CoasterName',
                   'year_introduced':'YearIntroduced',
                   'latitude':'Latitude','longitude':'Longitude',
                  'Type_Main':'TypeMain','opening_date_clean':'OpeningDateClean',
                   'speed_mph':'Speedmph','height_ft':'Height_ft',
                   'Inversions_clean':'Inversions',
                   'Gforce_clean':'Gforce'})


# In[22]:


df1


# In[23]:


df1.head()


# In[ ]:


# To find missing values


# In[24]:


df1.isna().sum()


# In[ ]:


# To find duplicate in rows


# In[25]:


df1.duplicated()


# In[26]:


df1.loc[df1.duplicated()]


# In[27]:


df1.duplicated(subset=['CoasterName'])


# In[ ]:


#To find with column


# In[28]:


df1.loc[df1.duplicated(subset=['CoasterName'])] #97 rows are duplicated with coastername


# In[29]:


df1.loc[df1.duplicated(subset=['CoasterName'])].head()


# In[32]:


#checking an example in duplicated using query
df1.query('CoasterName =="Crystal Beach Cyclone"') #to differentiate use singe quotes and double quotes' " " '


# In[33]:


df1.columns


# In[34]:


df1.duplicated(subset=['CoasterName','Location','OpeningDateClean']).sum()


# In[35]:


df1.duplicated(subset=['CoasterName','Location','OpeningDateClean'])


# In[ ]:


# to select inverse of columns which are not duplicated


# In[36]:


~df1.duplicated(subset=['CoasterName','Location','OpeningDateClean'])


# In[39]:


#These are not duplicated rows but having unordered index so we are resetting the index by using reset index

df1.loc[~df1.duplicated(subset=['CoasterName','Location','OpeningDateClean'])].reset_index(drop=True)

#now we can see sequence of numbers in index


# In[ ]:


# copy and assign as new dataframe


# In[40]:


df = df1.loc[~df1.duplicated(subset=['CoasterName','Location','OpeningDateClean'])].reset_index(drop=True).copy()


# In[42]:


df.shape


# # Step 3: Feature Understanding 

# ## (Univeriate analysis)
# #### Plotting feature Distribution
#     Histogram
#     KDE
#     boxplot

# In[44]:


df


# In[45]:


# single columns in a dataframe is a series


# In[46]:


df['YearIntroduced']


# In[47]:


#Here value_counts shows how many unique value occurs
df['YearIntroduced'].value_counts()


# In[ ]:


# using plots


# In[53]:


ax=df['YearIntroduced'].value_counts().head(15)\
.plot(kind='bar',title='Top 15 Year Coater Introduced')
ax.set_xlabel("Year Introduced")
ax.set_ylabel("No.of Coaster")


# In[61]:


#to find a distribution how speedmph is 
ax=df['Speedmph'].plot(kind='hist',bins=20,title='Coaster Speed(mph)')
ax.set_xlabel("Speed(mph)")


# In[62]:


#Kernal density plot
ax=df['Speedmph'].plot(kind='kde',title='Coaster Speed(mph)')
ax.set_xlabel("Speed(mph)")


# # Step 4: Feature Relationships
#     
#     Scatterplot
#     Heatmap Correlation
#     Pairplot
#     Groupby Comparisons

# In[63]:


# two features in scatterplot
df


# In[68]:


df.plot(kind='scatter',x='Speedmph',y='Height_ft',grid=True,title='Coaster Speed vs. Height')
plt.show()


# In[69]:


# Seaborn for better visulization


# In[70]:


sns.scatterplot(x='Speedmph',y='Height_ft',data=df)


# In[71]:


# To add hue
sns.scatterplot(x='Speedmph',y='Height_ft',hue='YearIntroduced',data=df)


# In[ ]:


# three features in seaborn(Compairs multiple features)


# In[72]:


df.head()


# In[75]:


sns.pairplot(df,vars=['YearIntroduced','Speedmph','Height_ft','Inversions','Gforce'],hue='TypeMain')
plt.show()


# In[ ]:


#drop na


# In[76]:


df[['YearIntroduced','Speedmph','Height_ft','Inversions','Gforce']]


# In[77]:


df[['YearIntroduced','Speedmph','Height_ft','Inversions','Gforce']].dropna()


# In[ ]:


#correlation


# In[79]:


df_corr=df[['YearIntroduced','Speedmph','Height_ft','Inversions','Gforce']].dropna().corr()


# In[80]:


df_corr


# In[81]:


#heatmap


# In[82]:


sns.heatmap(df_corr)


# In[ ]:


#to see values inside heatmap use annot=True


# In[83]:


sns.heatmap(df_corr,annot=True)


# ### Questions about data

# In[ ]:


# What are the Location with fastest roller coasters(minimum of 10)?


# In[94]:


ax=df.query('Location !="Other"')\
    .groupby('Location')['Speedmph']\
    .agg(['mean','count'])\
    .query('count>=10')\
    .sort_values('mean')['mean']\
    .plot(kind='barh',figsize=(12,5),title='Average Coaster Speed by location')
ax.set_xlabel("Average Coaster Speed")
plt.show()


# In[ ]:





# In[ ]:





# In[ ]:




