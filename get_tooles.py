from typing import Any, List, Mapping, Optional
import random
import json
from typing import Callable
import re
from typing import List, Union
from tooles import get_zhihu_news,get_arxiv
from process_paper import download_pdf
def get_tools(retiver=None,k=None):
    tooles = [
        {'tool_name':'知乎热搜','discription':'获取知乎热搜','input':{'参数1':'获取热搜'},'example':{'参数1':'获取热搜'}},
        {'tool_name':'获取文章','discription':'获取arxiv最新文章','input':{'参数1':'要查询的文章关键词'},'example':{'参数1':'Tool'}},
        {'tool_name':'下载文章','discription':'下载给定链接的文章','input':{'参数1':'要下载文章的链接url'},'example':{'参数1':'https://www.bilibili.com/'}},
    ]
    if retiver==None:
        return tooles
def all_tools():
    tooles={"知乎热搜":get_zhihu_news.get_news,'获取文章':get_arxiv.get_arxiv_paper,'下载文章':download_pdf}
    return tooles

        
