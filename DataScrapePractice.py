from bs4 import BeautifulSoup
import requests



x = requests.get('url')
''' .content gives all info pulled from web
beatifulsoup makes that content pulled useable '''
soup = BeautifulSoup(x.content)





