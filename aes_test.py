from bak.aes_demo import *
import requests
import json
body={
    "action":"add_case",
    "data":{
    	"title": "test12345",
        "summary": "test",
        "tag": "test",
        "protocol": "HTTP",
        "method": "GET",
        "path": "/",
        "params": "test"
     }
}
body=encrpt_zhCN(json.dumps(body))
print(body)
#构造请求体
payload={'code':body}
resp=requests.post('http://localhost:9090/api/aes',data=payload)

#获取服务器返回密文
code=resp.json()['code']

data=decrpt_zhCN(code)

print(data)