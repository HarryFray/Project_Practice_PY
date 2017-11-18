from bs4 import BeautifulSoup
import requests


# APIkey = 2a016a417daf4448aca7554281008a52
url = 'https://en.wikipedia.org/wiki/Gu%C3%A9ridon'
''' gets content'''
x = requests.get(url)


'''beatifulsoup makes the content pulled usable '''
soup = BeautifulSoup(x.content,'html.parser')


''' study documentation of requests '''
links = soup.find_all("a")
for link in links:
    print link.get('href')

'''returns all text'''


















