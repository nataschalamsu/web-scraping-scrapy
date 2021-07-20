#!/usr/bin/env python
# coding: utf-8

# In[24]:


import numpy as np
import pandas as pd

df = pd.read_csv('https://raw.githubusercontent.com/nataschalamsu/web-scraping-scrapy/master/scrapingscraper/scraped_data.csv')


# In[17]:


df.info()


# In[25]:


sorted_by_price = df.sort_values(by=['price'])
print(sorted_by_price)


# In[31]:


filtered_by_price = df[df.price.eq(259.9)]
print(filtered_by_price)


# In[40]:


filter_by_name = df[df['name'].str.contains('Aster')]
print(filter_by_name)


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




