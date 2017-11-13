from bs4 import BeautifulSoup
import requests



x = requests.get('https://www.wikipedia.org/')


''' .content gives all info pulled from web
beatifulsoup makes that content pulled useable '''
soup = BeautifulSoup(x.content)





