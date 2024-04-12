from flask import Flask,render_template,request,jsonify
import json
from flask import Flask,Response
import urllib.parse
import requests
import json
import time
from flask import request
import os
from model import LLM
from inference import inference
from process_paper import get_paper_ans
app = Flask(__name__)
num=1
@app.route('/main')
def index():  
    return render_template("1.html")
    
now_model=LLM()
@app.route('/testGet',methods=['GET','POST'])
def get_ans():
    data = json.loads(request.form.get('data'))
    query=data['name']
    history=data['history']
    code=data['option']
    #print(data)
    if code=='2':
        ans=inference(now_model,query)
    if code=='3':
        ans=get_paper_ans(query,now_model)
    
    return jsonify({'status':ans})
if __name__ == '__main__':
    app.run(host='127.0.0.1',port=1666) 