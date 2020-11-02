from bs4 import BeautifulSoup
import requests
import urllib
import os
import shutil

path = os.path.dirname(os.path.abspath(__file__))

query = 'puppies'

url = 'https://www.google.com/search?q=' + urllib.parse.quote(query) + '&tbm=isch'

# https://www.google.com/search?q=puppies&tbm=isch


response = requests.get(url)

soup = BeautifulSoup(response.content, 'html.parser')

images = soup.find_all('img') # , attrs = {'alt': 'Post image'}

n = 0

for image in images:
    src = image['src']
    if 'https://' in src:

        urllib.request.urlretrieve(src, path + '//image_downloads//' + str(n))

    n += 1 
    # if n > 15:
    #     break