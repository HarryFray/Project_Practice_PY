''' study
json
url structure
dictionarys
'''

import urllib2
import json



''' expand knowledge of urls here what does & or ? do'''
url = ('https://newsapi.org/v2/everything?'
        'sources=abc-news&'
      # 'q=Kitten&'
       #'from=2017-11-20&'
     #  'sortBy=popularity&'
       'apiKey=2a016a417daf4448aca7554281008a52')


''' opens specified url from api so in json format '''
json_obj = urllib2.urlopen(url)

''' loads jason object'''
data = json.load(json_obj)


for item in data['articles']:
   # print data
    #if 'Rancho' in item['title']:
    print item['title']








