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


# In[28]:


filtered = df['name'].str.find('Navy')
print(filtered)


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




