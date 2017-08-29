import requests
from bs4 import BeautifulSoup as BS


# url = 'https://geo.craigslist.org/iso/us'
url = 'https://www.craigslist.org/about/sites'
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
city_dict = {}
for li in soup.find_all('li'):
    city_name = li.find_next_sibling('a').text
    print(city_name)
    for link in li.find_all('a'):
        print(link['href'])
