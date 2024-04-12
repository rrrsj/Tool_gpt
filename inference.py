from get_tooles import get_tools,all_tools
from get_prompt import get_prompt
from use_tool import use_tools

def inference(model,question):
    tools_dis=get_tools()
    tools=all_tools()
    now_step=''
    ok=1
    while ok:
        prompt=get_prompt(tools_dis,question,now_step)
        output=model(prompt)
        #print(output)
        ans,tem,ok=use_tools(output,tools,model)
        if ok==0:
            now_step=now_step+tem+'最终答案：\n'+ans+'\n'
            break
        elif ok==1:
            now_step=now_step+tem+'工具输出：'+ans+'\n'
        elif ok==99:
            return "error"
    return now_step



    



    