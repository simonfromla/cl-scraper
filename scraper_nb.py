
# coding: utf-8

# In[3]:


import requests
from bs4 import BeautifulSoup as BS
# import pandas as pd
# import numpy as np

# url = 'https://geo.craigslist.org/iso/us' # Only USA
url = 'https://www.craigslist.org/about/sites' # All Locations
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) '
           'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/'
           '537.36'}
response = requests.get(url, headers=headers)

# print(response.content)
# print(response.status_code)
# print(response.headers)

soup = BS(response.content, 'html.parser')
soup.prettify
# print(soup)
# ul_lists = soup.find_all('a')
# print(ul_lists)
# print(ul_lists[8:728])
# ul_list = soup.
city_dict = {}
section = soup.find('section', class_='body')
for li in section.find_all('li'):
    city_name = li.text
    for link in li.find_all('a'):
        city_dict[city_name] = link['href']
# print(city_dict)
        
# for list_item in ul_lists:
#     city_dict[list_item.text] = list_item['href']



# In[4]:


# Techniques in navigating the DOM elements you want, narrowing down
# print(len(ul_lists))
# print(ul_lists[-1])
# print(ul_lists)


# In[5]:


gz_url = city_dict["seoul"]
gz_url


# In[6]:


search_url = gz_url + 'search/sss'


# In[7]:


search_params = {'sort':'rel',
                'min_price':'50',
                'mobile_os':'2',
                'query':'iphone 5s -cracked -replacement -broken -case -charger',
                'srchType': 'T'}


# In[8]:


r = requests.get(search_url, params=search_params, headers=headers)


# In[9]:


soup_object = BS(r.content, 'html.parser')


# In[10]:


# soup_object.prettify


# In[11]:


price_list = []
for i, a in enumerate(soup_object.find_all('a', {'class': 'result-image gallery'})):
    price = a.find('span', {'class': 'result-price'}).text
    if i < 20: # Top 20, as {'sort': 'rel[evence]'} pushes chargers n shit to the back
        price_list.append(int(price[1:]))


# In[12]:


price_list


# In[ ]:




