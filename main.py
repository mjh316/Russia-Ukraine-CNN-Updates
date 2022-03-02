import requests
import json
import pytz
from datetime import datetime
from pprint import pprint as pp
from bs4 import BeautifulSoup

base_url = 'https://www.cnn.com/europe/live-news/ukraine-russia-news-{}-{}-{}{}/index.html'

tz_WA = pytz.timezone('US/Pacific')
datetime_WA = datetime.now(tz_WA)

url1 = base_url.format(
    str(datetime_WA.month).rjust(2, '0'),
    str(datetime_WA.day).rjust(2, '0'),
    str(datetime_WA.year)[-2:],
    '-intl'
)

url2 = base_url.format(
    str(datetime_WA.month).rjust(2, '0'),
    str(datetime_WA.day).rjust(2, '0'),
    str(datetime_WA.year)[-2:],
    ''
)
print(url1 + '\n' + url2)

text = requests.get(url1).text
soup = BeautifulSoup(text, features='lxml')

headers = soup.select("h2.sc-dfVpRl.kvaBeP")
if headers == []:
    text = requests.get(url2).text
    soup = BeautifulSoup(text, features='lxml')
    headers = soup.select("h2.sc-dfVpRl.kvaBeP")
#'<h2 class="sc-dfVpRl kvaBeP">'
headers = list(map(lambda x: x.text, headers[1:]))

#print(headers)

with open('data.data', 'w') as f:
    f.write('\n'.join(headers))

