#!/usr/bin/env python
# coding: utf-8

# In[28]:


import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


# In[29]:


data=pd.read_csv('SampleSuperstore.csv')


# In[30]:


data.head()


# In[31]:


#First, we plot a heatmap to determine the correlation between the features.
Var_Corr = data.corr()
# plot the heatmap and annotation on it
sns.heatmap(Var_Corr, xticklabels=Var_Corr.columns, yticklabels=Var_Corr.columns, annot=True)


# In[32]:


#We determine the relationship between the overall sales and the profit
plt.scatter(x=data['Sales'], y=data['Profit'])
plt.ylabel('Profit')
plt.xlabel('Sales')
plt.show()


# In[33]:


#We see if there is a relationship between the discount and the profit
plt.scatter(x=data['Discount'], y=data['Profit'])
plt.ylabel('Profit')
plt.xlabel('Sales')
plt.show()


# In[34]:


#Compare the ship mode:
sns.set_style('whitegrid')
sns.countplot(x='Ship Mode',data=data,palette='RdBu_r')


# In[35]:


#Compare the Segment:
sns.set_style('whitegrid')
sns.countplot(x='Segment',data=data,palette='RdBu_r')


# In[ ]:





# In[36]:


#Compare the Region:
sns.set_style('whitegrid')
sns.countplot(x='Region',data=data,palette='RdBu_r')


# In[37]:


#Compare the Category:
sns.set_style('whitegrid')
sns.countplot(x='Category',data=data,palette='RdBu_r')


# In[38]:


#Compare the Sub-Category:
sns.set_style('whitegrid')
sns.countplot(x='Sub-Category',data=data,palette='RdBu_r')


# In[39]:


#We see how segment and region compare with each other
sns.set_style('whitegrid')
sns.countplot(x='Segment',hue='Region',data=data,palette='rainbow')


# In[40]:


#We see how segment and Category compare with each other
sns.set_style('whitegrid')
sns.countplot(x='Segment',hue='Category',data=data,palette='rainbow')


# In[41]:


#We see how region and Category compare with each other
sns.set_style('whitegrid')
sns.countplot(x='Region',hue='Category',data=data,palette='rainbow')


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




