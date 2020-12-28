#!/usr/bin/env python
# coding: utf-8

# In[2]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
get_ipython().run_line_magic('matplotlib', 'inline')


# In[ ]:


#http://archive.ics.uci.edu/ml/datasets/Forest+Fires


# In[14]:


data=pd.read_csv(r'C:\Users\Aylin Yilmaz\Desktop\forestfires.csv') 
data


# In[ ]:


# 1. X and Y - x-axis and y-axis0 spatial coordinate within the Montesinho park map: 1 to 9
# FFMC - FFMC index from the FWI system: 18.7 to 96.20
# DMC - DMC index from the FWI system: 1.1 to 291.3
# DC - DC index from the FWI system: 7.9 to 860.6
# ISI - ISI index from the FWI system: 0.0 to 56.10
# temp - temperature in Celsius degrees: 2.2 to 33.30
# RH - relative humidity in %: 15.0 to 100
# wind - wind speed in km/h: 0.40 to 9.40
# rain - outside rain in mm/m2 : 0.0 to 6.4
# area - the burned area of the forest (in ha): 0.00 to 1090.84


# In[15]:


data.drop(['FFMC','DMC','DC'], axis=1) #simplify data 
new_data=data.drop(['FFMC','DMC','DC'], axis=1)
new_data


# In[5]:


new_data.info


# In[22]:


mean=sum(new_data.temp)/517
print("mean {}".format(mean))


# In[23]:


n_fire = new_data.shape[0] 

temp_below18=new_data.loc[(new_data['temp']<=18)]
n_below18 = temp_below18.shape[0]
print("temparature rating 18 and below: {}".format(n_below18))
print("lowest temperature")


# In[25]:


n_fire = new_data.shape[0] #temp sinir belirleme

temp_18_25=new_data.loc[(new_data['temp']>=18) & (new_data['temp']<=25 )]
n_18_25= temp_18_25.shape[0]
print("temparature rating 18 and  25: {}".format(n_18_25))
print("warm temperature")


# In[26]:


n_fire = new_data.shape[0] #temp sinir belirleme

temp_above25=new_data.loc[(new_data['temp']>=25)]
n_above25 = temp_above25.shape[0]
print("temparature rating 25 and above: {}".format(n_above25))
print("highest temperature")


# In[27]:


np.round(new_data.describe())


# In[28]:


plt.hist(new_data.temp,bins=12,
         color='#008080',label="temparature") 

plt.xlabel("temp")
plt.ylabel("Total Number")
plt.legend()
plt.title("temperature in Celsius degrees")

plt.show()


# In[13]:


correlation = new_data.corr()
display(correlation)
plt.figure(figsize=(14, 12))
heatmap = sns.heatmap(correlation, annot=True, linewidths=0, vmin=-1, cmap="RdBu_r")


# In[13]:


#Visualize the co-relation between
#Create a new dataframe containing only selected  columns to visualize their co-relations
wind_temp = new_data[['wind', 'temp']]

#Initialize a joint-grid with the dataframe, using seaborn library
gridA = sns.JointGrid(x="temp", y="wind", data=new_data, size=6)

#Draws a regression plot in the grid 
gridA = gridA.plot_joint(sns.regplot, scatter_kws={"s": 10})

#Draws a distribution plot in the same grid
gridA = gridA.plot_marginals(sns.distplot)


#this correlation is negative. when temp is increasing, wind is decreasing. r=-0.23


# In[29]:


wind_rain = new_data[['wind', 'rain']]
gridA = sns.JointGrid(x="rain", y="wind", data=new_data, size=6)
gridA = gridA.plot_joint(sns.regplot, scatter_kws={"s": 10})
gridA = gridA.plot_marginals(sns.distplot)

#this correlation is positive.wind variable increases while the other increases. r= 0.0061


# In[ ]:




