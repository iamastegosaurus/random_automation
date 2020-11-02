from bs4 import BeautifulSoup
import requests


query = 'puppies'

url = 'https://www.google.com/search?q=' + query + '&tbm=isch'
print(url)
response = requests.get(url)

soup = BeautifulSoup(response.content, 'html.parser')
# items = soup.find_all('a') # , attrs = {'alt': 'Post image'}

# for i in items:
#     try:
#         print(i['href'])
#     except:
#         pass



# https://www.google.com/search?q=puppies&sxsrf=ALeKk03ttGs1GWkIax9cTCYn4KRbqqS4dg:1598832660518&source=lnms&tbm=isch&sa=X&ved=2ahUKEwiM6KPmk8TrAhUhAp0JHaZiBCgQ_AUoAXoECCEQAw&biw=1920&bih=947

# https://www.google.com/imgres?imgurl=https%3A%2F%2Fd17fnq9dkz9hgj.cloudfront.net%2Fuploads%2F2020%2F04%2Fshelter-dog-cropped-1.jpg&imgrefurl=https%3A%2F%2Fwww.petfinder.com%2Fpet-adoption%2Fdog-adoption%2Fpuppies-for-adoption%2F&tbnid=q5rF8jIe_0GiNM&vet=12ahUKEwi_7Y_ok8TrAhVR0KwKHYwhBXAQMygAegUIARDQAQ..i&docid=YQegNZyd9aOpDM&w=970&h=505&q=puppies&ved=2ahUKEwi_7Y_ok8TrAhVR0KwKHYwhBXAQMygAegUIARDQAQ

# <img alt="Puppies for Adoption | Petfinder" class="n3VNCb" src="https://d17fnq9dkz9hgj.cloudfront.net/uploads/2020/04/shelter-dog-cropped-1.jpg" data-deferred="1" id="imi" data-w="970" data-h="505" jsname="HiaYvf" jsaction="load:XAeZkd,gvK6lb;" style="height: 399.835px; width: 768px; margin: 0px;" data-atf="true" data-iml="524.8200000496581">

imghp?hl=EN

https://www.google.com/search?hl=EN&tbm=isch&sxsrf=ALeKk03yYJX-EXvCduLQWNnO7_m_kLiVFw%3A1598838751695&source=hp&biw=2560&bih=1307&ei=31dMX-HBJ8WUtAbO0K-YCw&q=puppies&oq=&gs_lcp=CgNpbWcQARgAMgcIIxDqAhAnMgcIIxDqAhAnMgcIIxDqAhAnMgcIIxDqAhAnMgcIIxDqAhAnMgcIIxDqAhAnMgcIIxDqAhAnMgcIIxDqAhAnMgcIIxDqAhAnMgcIIxDqAhAnUABYAGDGNmgBcAB4AIABAIgBAJIBAJgBAKoBC2d3cy13aXotaW1nsAEK&sclient=img

https://www.google.com/search?q=puppies&sxsrf=ALeKk03ttGs1GWkIax9cTCYn4KRbqqS4dg:1598832660518&source=lnms&tbm=isch&sa=X&ved=2ahUKEwiM6KPmk8TrAhUhAp0JHaZiBCgQ_AUoAXoECCEQAw&biw=1920&bih=947

https://www.google.com/search?q=puppies&sxsrf=ALeKk03ttGs1GWkIax9cTCYn4KRbqqS4dg:1598832660518&source=lnms&tbm=isch&sa=X&ved=2ahUKEwiM6KPmk8TrAhUhAp0JHaZiBCgQ_AUoAXoECCEQAw&biw=1920&bih=947

https://www.google.com/search?q=puppies&sxsrf=ALeKk03ttGs1GWkIax9cTCYn4KRbqqS4dg:1598832660518&source=lnms&tbm=isch&sa=X&ved=2ahUKEwiM6KPmk8TrAhUhAp0JHaZiBCgQ_AUoAXoECCEQAw&biw=1920&bih=947