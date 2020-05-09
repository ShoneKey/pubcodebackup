import requests

payload={
    'username':'auto',
    'password':'sdfsdfsdf'
}
#模拟登录
res=requests.post('http://localhost/api/mgr/loginReq',data=payload)
#获取响应头-set-cookies
# print(res.headers)
# cookies=res.headers['Set-Cookie']

#获取cookies方式2
cookies=res.cookies
print(cookies)
header={
    'Cookie':cookies
}
# #查看课程
# resp=requests.get('http://localhost/api/mgr/sq_mgr/?action=list_course&pagenum=1&pagesize=20',headers=header)

#使用Cookies2
resp=requests.get('http://localhost/api/mgr/sq_mgr/?action=list_course&pagenum=1&pagesize=20',cookies=cookies)
print(resp.json())