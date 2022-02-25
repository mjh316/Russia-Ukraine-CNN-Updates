import requests
import json
from pprint import pprint as pp
from bs4 import BeautifulSoup

url = 'https://www.cnn.com/europe/live-news/ukraine-russia-news-02-25-22/index.html'


text = requests.get(url).text
soup = BeautifulSoup(text, features='lxml')

headers = soup.select("h2.sc-dfVpRl.kvaBeP")
#'<h2 class="sc-dfVpRl kvaBeP">'
headers = list(map(lambda x: x.text, headers[1:]))

with open('data.data', 'w') as f:
    f.write('\n'.join(headers))

