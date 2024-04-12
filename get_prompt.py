from typing import Any, Mapping, Optional
import random
import urllib.parse
from bs4 import BeautifulSoup
import requests
import json
from typing import Callable
import re
from typing import List, Union
import re
from typing import List, Union

def get_output(tool,tool_name,question,nowstep):
    template = """现在有以下工具供你使用，你需要尽可能好的回答问题，请你在无法使用自身能力解决当前问题的情况下使用工具解决问题。
如果当前信息已经可以解决问题了，请输出 [最终答案：]，而不需要进行思考。

可调用的工具列表和描述:
%s

请使用如下的输出格式进行输出：

问题：你必须回答的问题
思考：思考在当前情况下应该做什么
工具：你需要调用的工具名称[%s]
工具输入：动作的输入，应该严格符合要工具的输入，格式为json{"参数1":,"参数2":,....}
工具输出：调用工具的输出，这并不需要你生成，由工具自动生成
... ( 思考/工具/工具输入/工具输出可以重复N次)
最终答案：如果可以从工具输出中提取出答案，那么请直接输出。


问题：%s
%s
思考：
"""%(tool,tool_name,question,nowstep)
    return template

def get_tool_name(tool_list):
    ans=''
    for i  in tool_list:
        ans=ans+'，'+i['tool_name']
    return ans

def get_tool(tool_list):
    ans=''
    for i in tool_list:
        ans=ans+'[ 工具名称：'+i['tool_name']+' 工具描述：'+i['discription']+' 工具参数：'+str(i['input'])+' 调用实例：'+str(i['example'])+']\n'
    return ans

def get_prompt(tool_list,question,nowstep):
    tool_name=get_tool_name(tool_list)
    tool=get_tool(tool_list)
    prompt =get_output(tool,tool_name,question,nowstep)
    return prompt