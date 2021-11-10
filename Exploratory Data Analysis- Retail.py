#!/usr/bin/env python
# coding: utf-8

# In[9]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# In[20]:


data=pd.read_csv("SampleSuperstore.csv")
data.head()


# In[22]:


data.info()


# In[23]:


data.isnull().sum()


# In[24]:


data.columns


# In[25]:


data.shape


# In[26]:


data.nunique()


# In[27]:


#Exploratory Data Analysis;-
plt.figure(figsize=(7,6))
correlation=data.corr()
sns.heatmap(correlation,annot=True,cmap='OrRd')


# In[28]:


#Pairplot for analyse Whole Data :
sns.pairplot(data)


# In[29]:


#LINEPLOT;-
plt.figure(figsize=(10,5))
sns.lineplot(x='Discount',y='Profit',data=data)
plt.legend('Profit')


# In[31]:


plt.figure(figsize=(30,13))
plt.plot(data['Profit'], color='blue')
plt.grid(alpha=0.2)


# In[32]:


data.corr()


# In[33]:


#Distribution Of Shipment based on states;-
plt.figure(figsize=(30,10))
sns.countplot(data['State'])
plt.xticks(fontsize=16,rotation=90)
plt.ylabel('COUNTS',fontsize=20)
plt.xlabel('STATES',fontsize=20)
plt.title('DISTRIBUTION OF STATES',fontsize=25);
plt.grid(alpha=0.5)
plt.show()


# In[34]:


plt.figure(figsize=(20,10))
plt.subplot(2,1,1)
sns.countplot('Category',data=data);
plt.title('DISTRIBUTION OF CATEGORY')
plt.xlabel('CATEGORY')
plt.ylabel('COUNT')
plt.grid(alpha=0.3)
plt.subplot(2,1,2)
sns.countplot('Sub-Category',data=data);
plt.title('DISTRIBUTION OF SUB-CATEGORY')
plt.xlabel('SUB-CATEGORY')
plt.ylabel('COUNT')
plt.grid(alpha=0.3)
plt.show()


# In[35]:


fig, axs = plt.subplots(ncols=2, nrows = 2, figsize = (10,10))
sns.distplot(data['Sales'], color = 'blue',  ax = axs[0][0])
sns.distplot(data['Profit'], color = 'orange',  ax = axs[0][1])
sns.distplot(data['Quantity'], color = 'green',  ax = axs[1][0])
sns.distplot(data['Discount'], color = 'red',  ax = axs[1][1])
axs[0][0].set_title('Sales Distribution', fontsize = 18)
axs[0][1].set_title('Profit Distribution', fontsize = 18)
axs[1][0].set_title('Quantity distribution', fontsize = 18)
axs[1][1].set_title('Discount Distribution', fontsize = 18)
plt.show()


# In[36]:


#PROFIT DISTRIBUTION BASED ON DIFFERNT REGIONS
C=data[data['Region']=='Central']
E=data[data['Region']=='East']
W=data[data['Region']=='West']
S=data[data['Region']=='South']


# In[37]:


plt.figure(figsize=(20,5))
sns.barplot(x=C['State'].sort_values(ascending=True),y=C['Profit'])
plt.title('DISTRIBUTION OF PROFITS BASED ON CENTRAL REGION', fontsize=20)
plt.xticks(rotation=90, fontsize=15);
plt.xlabel('STATE',fontsize=15)
plt.ylabel('PROFIT',fontsize=15)
plt.grid(alpha=0.3)


# In[38]:


plt.figure(figsize=(20,5))
sns.barplot(x=E['State'].sort_values(ascending=True),y=E['Profit'])
plt.title('DISTRIBUTION OF PROFITS BASED ON EASTERN REGION', fontsize=20)
plt.xticks(rotation=90, fontsize=15);
plt.xlabel('STATE',fontsize=15)
plt.ylabel('PROFIT',fontsize=15)


# In[39]:


plt.figure(figsize=(20,5))
sns.barplot(x=W['State'].sort_values(ascending=True),y=W['Profit'])
plt.title('DISTRIBUTION OF PROFITS BASED ON WESTERN REGION', fontsize=20)
plt.xticks(rotation=90, fontsize=15);
plt.xlabel('STATE',fontsize=15)
plt.ylabel('PROFIT',fontsize=15)
plt.grid(alpha=0.3)


# In[40]:


plt.figure(figsize=(20,5))
sns.barplot(x=S['State'].sort_values(ascending=True),y=S['Profit'])
plt.title('DISTRIBUTION OF PROFITS BASED ON SOUTHERN REGION', fontsize=20)
plt.xticks(rotation=90, fontsize=15);
plt.xlabel('STATE',fontsize=15)
plt.ylabel('PROFIT',fontsize=15)
plt.grid(alpha=0.3)
plt.show()


# In[41]:


#State wise analysis of Profit, Discount, Sale

data['State'].value_counts().head(10)


# In[42]:



data_state= data.groupby(['State'])[['Sales', 'Discount', 'Profit']].mean()
data_state.head(10)


# In[43]:


#[1] State wise Profit analysis
data_state1=data_state.sort_values('Profit')


# In[44]:



data_state1[['Profit']].plot(kind = 'bar', figsize = (20,8), color='black')
plt.title('State wise Profit Analysis', fontsize = 20)
plt.ylabel('Profit per Sate')
plt.xlabel('States')
plt.show()


# In[45]:


#[2] State wise Sale analysis


data_state['Sales'].plot(kind='pie',figsize = (20,20),autopct='%1.1f%%',startangle=90,shadow=True)
plt.title('State wise analysis of Sale',fontsize=20)


# In[46]:


#[3] State wise Discount analysis
data_state1['Discount'].plot(kind='bar',figsize=(18,5),color='green')
plt.title('State wise analysis of Discount', fontsize=20)


# In[47]:


#Category wise sales, Discount, Profit analyse
data_category = data.groupby(['Category'])[['Sales', 'Discount', 'Profit']].mean()
data_category


# In[48]:


data_category.plot.pie(subplots=True, figsize=(18, 20), autopct='%1.1f%%', labels = data_category.index)


# In[49]:


#Ship Mode wise sales, profit, discount
data['Ship Mode'].value_counts()


# In[50]:


data_shipmode = data.groupby(['Ship Mode'])[['Sales', 'Discount', 'Profit']].mean()
data_shipmode.plot.pie(subplots=True,figsize=(18, 20), autopct='%1.1f%%', labels = data_shipmode.index)


# In[ ]:


#Conclusion:
Profit is more than that of sale but there are some areas where profit could be increased.

1. Profit and Discount is high in First Class2. Sales is high for Same day ship3. Maximun sales and Profit obtain in Technology.4. Minimun profit obtain in Furniture5 .State: Vermont: Highest Profit6. State: Ohio: Lowest Profit7. Sub-category: Copier: High Profit & sales8. Sub-category: Binders , Machines and then tables have high Discount.9. Segment: Home-office: High Profit & sales**

Here is top 3 city where deals are Highest.

A) New York City
B) Los Angeles
C) Philadelphia
Wyoming: Lowest Number of deal,Highest amount of sales= Wyoming(11.8%) Lowest amount of sales= South Dakota(0.8%)

