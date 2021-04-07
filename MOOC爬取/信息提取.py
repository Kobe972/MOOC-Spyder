import json,requests,re
from selenium import webdriver
browser=webdriver.Chrome()
js=[]
cnt=0
with open('data.json','r',encoding='utf-8') as file:
    s=file.read()
    data=json.loads(s)
for i in range(0,len(data)):
    try:
        tmp={}
        tmp['课程url']=data[i]['url']
        tmp['课程名称']=data[i]['name']
        tmp['开课学校']=data[i]['schoolName']
        tmp['授课老师']=data[i]['teacherName']
        browser.get(data[i]['url'])
        html=browser.page_source
        result=re.search('<span>(\d*年\d*月\d*日)',html)
        tmp['开课时间']=result.group(1)
        result=re.search('第(.*)次开课',html)
        tmp['开课次数']=result.group(1)
        tmp['参加人数']=data[i]['enrollCount']
        js.append(tmp)
        cnt+=1
        if(cnt%10==0):
            with open('out.json','w',encoding='utf-8') as file:
                file.write(json.dumps(js,indent=2,ensure_ascii=False))
    except:
        None
    if i%10==0:
        print('爬取'+str(i+1)+'次,成功'+str(cnt)+'次') #运行结果：共失败3次
browser.close()
with open('out.json','w',encoding='utf-8') as file:
    file.write(json.dumps(js,indent=2,ensure_ascii=False))
    
