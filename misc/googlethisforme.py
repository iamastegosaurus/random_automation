from bs4 import BeautifulSoup
import requests
import urllib
from gtts import gTTS
from playsound import playsound

base = 'https://www.google.com/search?q='
query = 'coffee'
out = 'useful_information.mp3'

url = base + urllib.parse.quote_plus(query) # + '&btnI' - gives im feeling lucky but usually has annoying redirect
print(url)
response = requests.get(url)
soup = BeautifulSoup(response.text, 'lxml')

accepted_tags = ['style', 'script', '[document]', 'head', 'title']
[s.extract() for s in soup(accepted_tags)]
visible_text = soup.getText()

print(visible_text)

# voice = gTTS(text=visible_text, lang='en')
# voice.save(out)

# playsound(out)
