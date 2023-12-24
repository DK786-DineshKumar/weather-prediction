#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd 
import numpy as np
data=pd.read_csv(r"C:\DATA SIENCES\CSV FILE AND FILES\weather data.csv")

data

data.head()

data.shape

data.index


data.columns

data.dtypes

data.head(2)

data.Weather.unique()

data.nunique
data

data.Weather.nunique

data.count()

data.Weather.count()

data.value_counts

data.Weather.value_counts()

data.head(2)
data["Wind Speed_km/h"].value_counts()


data.info()

#find the unique value in the wind speed  from the data set into
data.head(2)
data.nunique
data['Wind Speed_km/h'].unique()


data["Wind Speed_km/h"].nunique()

#find the number of time when the weather is  excatly Clear
data.head(2)

#data.Weather.value_counts()

data[data['Weather']==("Clear")]

data.groupby("Weather").get_group("Clear")



# In[5]:


data.head(2)


# In[14]:


#find the number of time when the wind speed was exactly 4kmph
data[data['Wind Speed_km/h']==4]


# In[17]:


data["Wind Speed_km/h"]==4


# In[22]:


#find out the null values in the data
data.isnull
data.isnull().sum()
data.notnull().sum()


# In[24]:


#rename the column name Weather of the dataframe to Weather condition
data.head(2)
data.rename(columns={"Weather":"Weather condition"})


# In[40]:


#data.head(2)
data.rename(columns={"Weather":"Weather condition"},inplace=True)
data


# In[41]:


#What is the mean in Visibility_km
data.head(2)


# In[45]:


data.Visibility_km.mean()


# In[48]:


#what is the standard deviation of the pressure in the data
data.head(2)
data.Press_kPa.std()


# In[50]:


#what is the variance of relative humidity  in the dataset
data["Rel Hum_%"].var()


# In[56]:


#find the instances when wind speed is above 24 (and&) visibility  is 25
data.head()
data[(data["Wind Speed_km/h"]>24) & (data.Visibility_km==25)]


# In[58]:


#find the instances Dew Point Temp_C when  is above 2 (and&) Temp_C is 2
data.head(2)


# In[76]:


#find the all instances when the snow was recoreder
data["Weather condition"].value_counts()
data[data["Weather condition"]=="Snow"]
data


# In[78]:


data.head()
data[data["Weather condition"].str.contains("Snow")]


# In[79]:


data[data["Weather condition"].str.contains ("Snow ")]


# In[88]:


#what is the mean value of the each column againts each weather conditions 
data.head(2)


# In[93]:


#data.groupby('Weather condition').mean()


# In[94]:


#what is minimum & maximum value of each column againt each Weather condition
data.head(2)


# In[96]:


data.groupby("Weather condition").max()


# In[102]:


data.groupby("Weather condition").min()


# In[106]:


#show the all recorder in weather condition is fog
data[data["Weather condition"]=='fog']
data


# In[113]:


#find the instanes when weather is clear or(|) visibility is above 40
#data["Weather condition"]=="Clear" | data["Visibility_km"]>40
data[(data["Weather condition"] == "Clear") | (data["Visibility_km"]>40)].head()


# In[114]:


#find all instances when(A =weather is clear and &   relative humidity is greater then 50 or |    b.. visibility is above 40)
data[(data["Weather condition"] == "Clear")  &  (data["Rel Hum_%"]>50) | (data["Visibility_km"]>40)]


# In[ ]:




