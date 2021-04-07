import requests,json
headers={
	'cookie':'EDUWEBDEVICE=4d013b64fe9c47a28b49573907a0e533; __yadk_uid=6xPcjQitHxInvBRLDBeVB8VybPmEItun; WM_NI=s%2BHwyaTOK8bP1sU0v8DonTpHb2P0WJYQK2YfhZ5Fljt9lFXeynO4iWIIoOvAOoypUEddv53aYumID1l6SrEuqJEJsDXCe1FW%2FuGCMmY%2BFZ%2FP6C0EG9Q4rqee1tfD6VvAdzU%3D; WM_NIKE=9ca17ae2e6ffcda170e2e6eeaef93a8c8c84bbb66a81ef8fa7d45b869a9faeb574918bbda7c560f3beb6b2d12af0fea7c3b92ab1f58898fc6b989185d9e15cf3ad9bd1f53488b1a2b5f344a2eea0d1d6429b8f85d3dc6eac86fba7ef62b8e7a4a7db6fbbb281d5ec5d8b97a1b0f54b8db1b791d84fa8bcbad6b26b9baba3aac73bb0ea9d93c87fb3968babf2509c9dabd2c55dedab89a4d0679bf58abbae5cf69d00a6c63393ecbe92e86ff3acaaa5b55eb69fac9bd837e2a3; WM_TID=OHWK2q%2F7StNBRAQRBQYqgWE5UESwPiQE; hb_MA-A976-948FFA05E931_source=www.icourse163.org; NTES_YD_PASSPORT=gvzmk_gn3Y5nm0yYIa8aail94edxzbmeeE0yYtjQpoEzGTk4G2l_fIkuFm6cKArWyr_oon9rxJR5bAjfOHYJTiVRe4yL6jj_VjUWkyZVIQL_12kS1klOjUOCm308Kq30kMz5f6rn7_3z8dl2m1LhFomfwCAniiSTsE0q_bPFIghJOMUgB98ufIVtyTxMjWySE_b48byutBXDbTtl3OI4ylNm8; P_INFO=13233131808|1616127003|1|imooc|00&99|null&null&null#anh&340100#10#0|&0||13233131808; NTESSTUDYSI=5cc7618f17e049c9887e2c325d1083cd; STUDY_INFO="yd.5309dac09e784dbdb@163.com|8|1463681283|1616144644067"; STUDY_SESS="X3QzO950h2S+mTSozjch8qb1cUBbHXmdIo9slsz8IuAVT0+B0jIfaCu/K/p0YDk06dEH52Kkfkp7+W9r1ORgOyTGeeUpNGMuUE0T6IlhusIPjQpfVPe7S3SXaM+AS1fyHQULjidffenx22LxrFF5VdKYjESEIdChBYyAWNPqP98Lhur2Nm2wEb9HcEikV+3FTI8+lZKyHhiycNQo+g+/oA=="; STUDY_PERSIST="h5/xaUGlvrUWuliCchwlOGyYm220tAv5nD8GF3EXuwMW6QWBGnLhvoP29UIPao0MthTT2yKzeE6dhMaSn3KrvvWouFZinxcyGVxHSTHI3aKx62+k6q5JI8srgXh7IhQtjoDivovzn2T5OpGY4L5/l4EuOWvD0VvTKARFqax7Kd6STX2J7ZNZuHSrQdu8JPZSpxiX0r0KM3PpcjCvkBrknCmx9AiI9wKNhjQOLdKWoZXZgpjCC7Iso4RP9U87vJE8LtaQzUT1ovP2MqtW5+L3Hw+PvH8+tZRDonbf7gEH7JU="; NETEASE_WDA_UID=1463681283#|#1616127006202; Hm_lvt_77dc9a9d49448cf5e629e5bebaa5500b=1616082115,1616125861,1616144645; Hm_lpvt_77dc9a9d49448cf5e629e5bebaa5500b=1616148190',
	'Referer':'https://www.icourse163.org/channel/3002.htm',
            'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36 Edg/89.0.774.54'
	}
data={
	'mocCourseQueryVo':'{"categoryId":-1,"categoryChannelId":3002,"orderBy":0,"stats":30,"pageIndex":1,"pageSize":280}'}

r=requests.post('https://www.icourse163.org/web/j/mocSearchBean.searchCourseCardByChannelAndCategoryId.rpc?csrfKey=5cc7618f17e049c9887e2c325d1083cd',headers=headers,data=data)
class_list=[]
cnt=0
for i in range(0,280):
    tmp={}   #tmp必须放到for循环里边，否则会导致class_list所有元素均为最后一次append的元素
    try:
        schoolSN=r.json()['result']['list'][i]['mocCourseBaseCardVo']['schoolSN']
        id=r.json()['result']['list'][i]['id']
        tmp['url']='https://www.icourse163.org/course/'+schoolSN+'-'+str(id)
        tmp['name']=r.json()['result']['list'][i]['mocCourseBaseCardVo']['name']
        tmp['teacherName']=r.json()['result']['list'][i]['mocCourseBaseCardVo']['teacherName']
        tmp['enrollCount']=r.json()['result']['list'][i]['mocCourseBaseCardVo']['enrollCount']
        tmp['schoolName']=r.json()['result']['list'][i]['mocCourseBaseCardVo']['schoolName']
        cnt+=1
    except:
        continue
    class_list.append(tmp)
data={
	'mocCourseQueryVo':'{"categoryId":-1,"categoryChannelId":2002,"orderBy":0,"stats":30,"pageIndex":1,"pageSize":383}'}
r=requests.post('https://www.icourse163.org/web/j/mocSearchBean.searchCourseCardByChannelAndCategoryId.rpc?csrfKey=5cc7618f17e049c9887e2c325d1083cd',headers=headers,data=data)
for i in range(0,383):
    tmp={}
    try:
        schoolSN=r.json()['result']['list'][i]['mocCourseBaseCardVo']['schoolSN']
        id=r.json()['result']['list'][i]['id']
        tmp['url']='https://www.icourse163.org/course/'+schoolSN+'-'+str(id)
        tmp['name']=r.json()['result']['list'][i]['mocCourseBaseCardVo']['name']
        tmp['teacherName']=r.json()['result']['list'][i]['mocCourseBaseCardVo']['teacherName']
        tmp['enrollCount']=r.json()['result']['list'][i]['mocCourseBaseCardVo']['enrollCount']
        tmp['schoolName']=r.json()['result']['list'][i]['mocCourseBaseCardVo']['schoolName']
        cnt+=1
    except:
        continue
    class_list.append(tmp)
print(str(cnt)+' items in total.') #本次试验中，共有590个课程信息
with open('data.json','w',encoding='utf-8') as file:
	file.write(json.dumps(class_list,indent=2,ensure_ascii=False))
	
