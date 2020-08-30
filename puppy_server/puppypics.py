from bs4 import BeautifulSoup
import requests
import urllib

query = 'puppies'

base = 'https://www.google.com/search?q='
url = base + urllib.parse.quote_plus(query) + '&tbm=isch'
# print(url) 

response = requests.get(url)
soup = BeautifulSoup(response.text, 'lxml')
link_list = soup.find_all('a')

for link in link_list:
    l = link['href']
    if '/url?' in link:
        img = link.split('=')[1]
        print(img)



# https://dogtime.com/assets/uploads/2018/10/puppies-cover-1280x720.jpg



