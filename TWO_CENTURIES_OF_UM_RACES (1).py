#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[2]:


import seaborn as sns


# In[3]:


df = pd.read_csv("TWO_CENTURIES_OF_UM_RACES.csv")


# In[4]:


df.head(10)


# In[5]:


df.shape


# In[6]:


df.dtypes 


# In[7]:


#clean up data
#Only want USA Races, 50k or 50mi, 2020
 


# In[8]:


#step 1 show 50mi or 50k
#50 km
#50 mi


# In[9]:


df[df['Event distance/length'] == '50mi']


# In[10]:


#combine 50k and 50mi


# In[11]:


df[df['Event distance/length'].isin(['50km','5mi'])]


# In[12]:


df[(df['Event distance/length'].isin(['50km','5mi'])) & (df['Year of event']==2020)]


# In[13]:


df[df["Event name"]== 'Everglades 50 Mile Ultra Run (USA)']


# In[14]:


df[df["Event name"]== 'Everglades 50 Mile Ultra Run (USA)']["Event name"].str.split('(').str.get(1).str.split(')').str.get(0)


# In[15]:


df[df["Event name"].str.split('(').str.get(1).str.split(')').str.get(0)=='USA']


# In[16]:


#combine all the filters together


# In[17]:


df[(df['Event distance/length'].isin(['50km','5mi'])) & (df['Year of event']==2020) & (df["Event name"].str.split('(').str.get(1).str.split(')').str.get(0)=='USA')]


# In[18]:


df2 = df[(df['Event distance/length'].isin(['50km','5mi'])) & (df['Year of event']==2020) & (df["Event name"].str.split('(').str.get(1).str.split(')').str.get(0)=='USA')]


# In[19]:


df2.head()


# In[20]:


df2.shape


# In[21]:


#remove (USA) from eveent name


# In[22]:


df2['Event name'].str.split('(').str.get(0)


# In[23]:


df2['Event name'] = df2['Event name'].str.split('(').str.get(0)


# In[24]:


df2.head()


# In[25]:


df2.shape


# In[26]:


df2['Event name'].str.split('(').str.get(0)


# In[27]:


df2['Event name']=df2['Event name'].str.split('(').str.get(0)


# In[28]:


df2.head()


# In[29]:


#cleqn up the athelet age


# In[30]:


df2['athlete_age'] = 2020 - df2['Athlete year of birth']


# In[31]:


# Remove h from athlete performance


# In[32]:


df2['Athlete performance'] = df2['Athlete performance'].str.split(' ').str.get(0)


# In[33]:


df2.head()


# In[34]:


# drop columns : Athlete club,Athlete country , Athlete year of birth, Athlere Age Category 


# In[35]:


df2= df2.drop(['Athlete club','Athlete country','Athlete year of birth','Athlete age category'],axis = 1)


# In[36]:


df2.head()


# In[37]:


df2=df2.drop(['Athlete performance'],axis = 1)


# In[38]:


#clean up null values


# In[39]:


df2.isna().sum()


# In[40]:


df2[df2['athlete_age'].isna()==1]


# In[41]:


df2=df2.dropna()


# In[42]:


df2.shape


# In[43]:


#check for duplicates


# In[44]:


df2[df2.duplicated()== True]


# In[45]:


#reset index


# In[46]:


df2.reset_index(drop= True)


# In[47]:


#fix types


# In[48]:


df2.dtypes


# In[49]:


df2['athlete_age']= df2['athlete_age'].astype(int)


# In[50]:


df2['Athlete average speed ']= df2['Athlete average speed'].astype(float)


# In[51]:


df2.dtypes


# In[52]:


df2.head()


# In[53]:


#rename columns 


# In[54]:


#Year of event                  int64
#Year of event                    object
#Event name                    object
#Event distance/length         object
#Event number of finishers      int64
#Athlete performance           object
#Athlete gender                object
#Athlete average speed         object
#Athlete ID                     int64
#athlete_age                    int32
#Athlete average speed        float64
#dtype: object


# In[55]:


df2= df2.rename(columns={'Year of event ':'year',
                         'Year of event':'race_day',
                         'Event name':'race_name',
                         'Event distance/length':'race_length',
                         'Event number of finishers':'race_number_of_finishers',
                         'Athlete performance':'athlete_performance',
                         'Athlete gender':'athlete_gender',
                         'Athlete average speed':'athlete_average_speed',
                         'Athlete ID':'athlete_id',
                         'athlete_age':'athlete_age',
                         'Athlete average speed':'athlete_average_speed',
                         })


# In[56]:


df2.head()


# In[57]:


#reorder columns


# In[58]:


df3= df2[['race_day','race_name','race_length','race_number_of_finishers','athlete_id','athlete_gender','athlete_age','athlete_average_speed']]


# In[59]:


df3.head()


# In[60]:


#find 2 races that i ran in 2020 - sarastota / Everglades


# In[61]:


df3[df3['race_name'] == 'Yankee Springs Fall Trail Run Festival ']


# In[62]:


#860347


# In[63]:


df3[df3['athlete_id']== 64838]


# In[64]:


#charts and graphs


# In[65]:


sns.histplot(df3['race_length'])


# In[66]:


sns.histplot(df3, x = 'race_length' , hue = 'athlete_gender')


# In[67]:


sns.displot(df3[df3['race_length']== '50km']['athlete_average_speed'])


# In[83]:


import numpy as np


# In[84]:


print(df3['athlete_average_speed'].dtype)
print(df3['race_length'].dtype)


# In[85]:


df3['athlete_average_speed'] = pd.to_numeric(df3['athlete_average_speed'], errors='coerce')
df3['race_length'] = pd.to_numeric(df3['race_length'], errors='coerce')


# In[86]:


print(df3['athlete_average_speed'].isnull().sum())
print(df3['race_length'].isnull().sum())


# In[90]:


sns.lmplot(data=df3,x= 'athlete_age' , y= 'athlete_average_speed',hue = 'athlete_gender')


# In[ ]:


#questions i want to find out from the data


# In[ ]:


#Year of event                  int64
#Year of event                    object
#Event name                    object
#Event distance/length         object
#Event number of finishers      int64
#Athlete gender                object
#Athlete average speed         object
#Athlete ID                     int64
#athlete_age                    int32
#Athlete average speed        float64


# In[ ]:


#Difference in speed for the 50k,50mi male to female


# In[92]:


df3.groupby(['race_length' , 'athlete_gender'])['athlete_average_speed'].mean()


# In[ ]:


#what age groups are the best in the 50m race(20+races min) 


# In[95]:


df3.query('race_length=="50mi"') .groupby ('athlete_age')['athlete_average_speed'].agg(['mean','count']).sort_values('mean' , ascending = False).query('count>19')

