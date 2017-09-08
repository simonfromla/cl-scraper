
# coding: utf-8

# In[25]:


import requests
from bs4 import BeautifulSoup as bs

url = 'https://geo.craigslist.org/iso/us' # Only USA
# url = 'https://www.craigslist.org/about/sites' # All Locations

headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) '
           'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/'
           '537.36'}

response = requests.get(url, headers=headers)
# print(response.content)
# print(response.status_code)
# print(response.headers)

soup = bs(response.content, 'html.parser')
# soup.prettify
# print(soup)

city_dict = {}

section = soup.find('div', class_='geo-site-list-container')
# section = soup.find('section', class_='body')

for li in section.find_all('li'):
    city_name = li.text
    for link in li.find_all('a'):
        city_dict[city_name] = link['href']
print(city_dict)
# for list_item in ul_lists:
#     city_dict[list_item.text] = list_item['href']


# In[26]:


# Techniques in navigating the DOM elements you want, narrowing down
# print(len(ul_lists))
# print(ul_lists[-1])
# print(ul_lists)
# ul_lists = soup.find_all('a')
# print(ul_lists[8:728])


# In[27]:


la_url = city_dict["los angeles"]
# guangzhou_url


# In[28]:


search_url = la_url + 'search/sss'


# In[29]:


search_params = {'sort':'rel',
                'min_price':'50',
                'mobile_os':'2',
                'query':'galaxy_s -cracked -replacement -broken -case -charger',
                'srchType': 'T'}


# In[30]:


r = requests.get(search_url, params=search_params, headers=headers)


# In[ ]:


soup_object = bs(r.content, 'html.parser')
# soup_object.prettify


# In[ ]:


price_list = []
for i, a in enumerate(soup_object.find_all('a', {'class': 'result-image gallery'})):
    price = a.find('span', {'class': 'result-price'}).text
    if i < 20: # Top 20, as {'sort': 'rel[evence]'} pushes chargers n shit to the back
        price_list.append(int(price[1:])) # int(price[1:]) to turn $120 into only price integer


# In[ ]:


price_list


# In[ ]:


import pandas as pd
import numpy as np


# In[ ]:


df = pd.DataFrame(columns=('city', 'price'), index=np.arange(0, 20*len(city_dict)))
# index= roughly top 20 results * num of cities. index creates the vertical size of the df


# In[ ]:


index = 0

for city in city_dict:
    # create url, make request, make soup
    url = city_dict[city]
    r = requests.get(url, headers=headers, params=search_params)
    s = bs(r.content, 'html.parser')
    
    # pull prices from that city webpage (20 max)
    for i, a in enumerate(soup_object.find_all('a', {'class': 'result-image gallery'})):
        price = a.find('span', {'class': 'result-price'}).text
        if i < 20: # Top 20, as {'sort': 'rel[evence]'} pushes chargers n shit to the back
            price = int(price[1:])
            
            # push the data into the dataframe directly. Skip list making
            df.loc[index] = [city, price]
            index += 1


# In[ ]:


print(df.head())
df.head()
# display(df.head())


# In[ ]:


df.info()

