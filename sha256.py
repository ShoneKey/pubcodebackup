import hashlib
from pprint import pprint

import requests

#1-1 待加密的字符串
key='111111'

#1-2 实例化一个sha256对象
sha256=hashlib.sha256()

#1-3 调用update 加密
sha256.update(key.encode())

#1-4 调用hexdigest 方法即加密结果
print('sha256加密后为：',sha256.hexdigest())
payload={"userName":"sqqdcl" ,"password":sha256.hexdigest()}

#1-5 请求头
header={"Content-Type":"application/x-www-form-urlencoded","X-Requested-With":"XMLHttpRequest"}

#1-6 发送请求
r=requests.post('http://47.96.181.17:8098/login',data=payload,headers=header)

pprint(r.json())
