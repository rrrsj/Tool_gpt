import json
import urllib.request
import requests
import os
from typing import Any, List, Mapping, Optional
import urllib.parse
import requests
import json
import os
from typing import Callable
from typing import List, Union
import re
from key import gpt_key
from random import randint


headers = {
    "authority": "gptpanda.com.cn",
    "accept": "*/*",
    "accept-language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6",
    "content-type": "application/json",
    "origin": "https://gptpanda.com.cn",
    "referer": "https://gptpanda.com.cn/",
    "sec-ch-ua": "\"Not?A_Brand\";v=\"8\", \"Chromium\";v=\"108\", \"Microsoft Edge\";v=\"108\"",
    "token": gpt_key,
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36 Edg/108.0.1462.46"
}
url = "https://gptpanda.com.cn/api/chat/completions"
def get_data(message):
    data = {
        "prompt": message,
        "parentMessageId": randint(1,1000000000000),
        "persona_id": "",
        "options": 
        {
            "model": "gpt-3.5-turbo",
            "temperature": 0,
            "presence_penalty": 0,
            "frequency_penalty": 0,
            "max_tokens": 1888
        }
    }
    return data

def get_output(message):
    data = json.dumps(get_data(message), separators=(',', ':'))
    response = requests.post(url, headers=headers, data=data)
    now=response.text.split('\n')
    ans=''
    for i in now:
        try:
            word=json.loads(i)
            ans=ans+word['content']
        except:
            continue
    return ans

class LLM():
    def __call__(self,prompt: str,) -> str:
        ans=get_output(prompt)
        return ans

