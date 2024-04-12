import re
import json
def normail_thought(input):
    ans=re.findall(r"思考：([^\n]*)",input, re.S)
    if len(ans)!=0:
        return ans[0],0
    ans=re.findall(r"最终答案：([\s|\S]*)",input, re.S)
    return ans[0],1

def normail_tool_name(input):
    ans=re.findall(r"工具：([^\n]*)",input, re.S)
    if len(ans)!=0:
        return ans[0],0
    ans=re.findall(r"最终答案：([\s|\S]*)",input, re.S)
    return ans[0],1

def normail_tool_input(input):
    ans=re.findall(r"工具输入：([^\n]*)",input, re.S)
    return ans[0]

def use_tools(input,all_tools,LLM):
    try:
        tool_name=''
        tool_input=''
        ok=''
        ans=''
        thought,flag=normail_thought(input)
        if flag==1:
            return thought,'',0
        try:
            tool_name,ok=normail_tool_name(input)
            if ok==1:
                return tool_name,'',0
            tool_input=normail_tool_input(input)
            tool_input=json.loads(tool_input.replace('\'','"'))
        except:
                tool_input=LLM('将下面的内容转化为json格式，请直接给出结果，不要添加任何信息：\n'+str(tool_input))
                tool_input=json.loads(tool_input.replace('\'','"'))
        print(tool_name,tool_input)
        if '知乎热搜' in tool_name:
            ans=all_tools['知乎热搜'](tool_input['参数1'])
        elif '获取文章' in tool_name:
            ans=all_tools['获取文章'](tool_input['参数1'])
        elif '下载文章' in tool_name:
            ans=all_tools['下载文章'](tool_input['参数1'])
        return ans,'思考：'+thought+'\n'+'工具：'+tool_name+'\n'+'工具输入：'+str(tool_input)+'\n',1
    except:
        return 0,0,99

