import requests

#模拟新增客户
payloadd='''
{
"aac003": "张三",
"aac004": "1",
"aac011": "21",
"aac030": "13575722021",
"aac01u": "88002255",
"crm003": "1",
"crm004": "1",
"crm00a": "2018-11-11",
"crm00b": "aaaaaa",
"crm00c": "2019-02-28",
"crm00d": "bbbbbb"
}
'''
#获取token
user={"userName":"fancl","password":"sq000000"}
res=requests.post('http://47.96.181.17:9090/rest/toController',json=user)
token=res.json()["token"]
print(token)

header={
    'Content-Type':'application/json',
    'X-AUTH-TOKEN':token
}
#添加客户
resp=requests.post('http://47.96.181.17:9090/rest/ac01CrmController',data=payloadd.encode('utf-8'),headers=header)
print(resp.text)


#清除测试数据
id=resp.json()['obj']['id']
resp2=requests.delete(f'http://47.96.181.17:9090/rest/ac01CrmController/{id}',headers=header)
print(resp2.json())

