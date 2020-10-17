#!/usr/bin/env python
# coding: utf-8

# In[8]:


import pandas as pd
import os


# In[9]:


pwd


# In[11]:


mydata = pd.read_csv (r"C:\Users\begum.tanriverdi\Documents\00_CPS-GIS Courses\GIS6345 GIS Programming\Week 5\food_truck_schedule.csv")
mydata.head()


# In[12]:


print (mydata[1:3])


# In[14]:


print (mydata[:3])


# In[19]:


mydata [3:4]


# In[20]:


mydata [2:8]


# In[18]:


import matplotlib.pyplot as plt


# In[27]:


mydata = pd.read_csv (r"C:\Users\begum.tanriverdi\Documents\00_CPS-GIS Courses\GIS6345 GIS Programming\Week 5\food_truck_schedule.csv", index_col=
                     "Day")


# In[24]:


mydata [1:12].plot()
plt.show()


# In[26]:


mydata.plot.bar()


# In[ ]:




