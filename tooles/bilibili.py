import requests
import json
def get_bilibili_hot():
    url='https://api.bilibili.com/x/web-interface/popular?ps=10&pn=1'
    response=requests.get(url)
    js=json.loads(response.text)
    ans=''
    for i in js['data']['list']:
        ans=ans+'Title:'+i['title']+'  '+'Name:'+i['desc'].replace('\n', '')+'\n'
    return ans