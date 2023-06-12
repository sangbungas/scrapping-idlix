#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().system('pip install bs4')


# In[2]:


from bs4 import BeautifulSoup


# In[3]:


import requests
import pandas as pd


# In[4]:


page = requests.get('https://77.105.142.75/genre/drama-korea/')


# In[5]:


page.content


# In[6]:


soup = BeautifulSoup(page.content, 'html.parser')


# In[7]:


soup


# In[25]:


NARD = soup.find_all('div', class_='data')


# In[26]:


for each_nard in NARD:
    print(each_nard.text)


# In[27]:


rating = soup.find_all('div', class_='rating')


# In[28]:


for each_rating in rating:
    print(each_rating.text)


# In[29]:


data_nard = []
for each_nard in NARD:
    data_nard.append(each_nard.text)


# In[30]:


data_nard


# In[32]:


data_ratings = []
for each_rating in rating:
    data_ratings.append(each_rating.text)


# In[34]:


data_ratings


# # MULTI PAGE DATA SCRAPING

# In[35]:


data_nard = [] 
data_ratings = [] 

for index in range (1,15):
    page = requests.get(f'https://77.105.142.75/genre/drama-korea/page/{index}')
    soup = BeautifulSoup(page.content,'html.parser')

#mencari judul dan tanggal tayang
    NARD = soup.find_all('div', class_='data') 
    for each_nard in NARD: 
        data_nard.append(each_nard.text) 

#mencari rating
    R = soup.find_all('div', class_='rating') 
    for each_r in R: 
        data_ratings.append(each_r.text) 

data = {
    'Judul dan Tanggal Tayang': data_nard,
    'Rating': data_ratings
}
pd.DataFrame(data)


# In[36]:


pd.DataFrame(data).to_excel('scraping idlix.xlsx')


# In[ ]:




