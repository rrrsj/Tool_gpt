import requests
import pdfplumber
def download_pdf(url):
    response = requests.get(url)
    with open('./pdf/now.pdf', "wb") as file:
        file.write(response.content)
    return '下载完成'
def get_paper_ans(question,llm):
    try:
        content=''
        with pdfplumber.open('./pdf/now.pdf') as pdf:
            for i in range(0,min(len(pdf.pages),10),2):
                now=llm(
'''Please extract the part from article information that related to the question, article information located in [], just extract the knowledge, do not need to answer the question. 
Article Information:
[%s]
Question:%s
'''%(pdf.pages[i].extract_text()+pdf.pages[i+1].extract_text(),question)
                    )
                content=content+now
        ans=llm(
            '''Please answer the question based on the relevant information, relevant information located in [].
Relevant Information
[%s]
Question:%s
Ans:
'''%(content,question)
        )
        return ans
    except:
        return "文献未下载或者gpt接口不可用"