import re
import requests
from bs4 import BeautifulSoup
import json
def get_news(s):
    url='https://www.zhihu.com/billboard'
    response=requests.get(url)
    soup = BeautifulSoup(response.text, 'lxml')
    l=soup.select('div[class=HotList-itemTitle]')
    return l[0].get_text()