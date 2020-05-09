import time

import paramiko

# 创建SSHClient 实例对象
ssh = paramiko.SSHClient()

# 调用方法，表示没有存储远程机器的公钥，允许访问
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

# 连接远程机器  地址、端口、用户名密码
ssh.connect("192.168.21.138",22,"root", "devops")


# # 创建目录
cmd = 'mkdir testdir;cd testdir;touch test.data;echo songqin >test.data;cat test.data'

cmd1='mkdir testdir'
cmd2='cd testdir'
cmd3='touch test.data'
cmds=[cmd1,cmd2,cmd3]
total_cmd=';'.join(cmds)
ssh.exec_command(total_cmd)
monitor_cmd='date +%Y%m%d_%H%M%S;free'
for i in range(10):
    stdin, stdout, stderr=ssh.exec_command(monitor_cmd)
    print(stdout.read().decode())
    print(stderr.read().decode())
    time.sleep(3)


# 如果命令跨行
cmd = '''echo '1234
5678
90abc' > myfile
'''
ssh.exec_command(cmd)


# 获取命令的执行结果
cmd = 'free'
stdin, stdout, stderr = ssh.exec_command(cmd)
res = stdout.read()
error_msg=stderr.read()

print(res.splitlines()[2])

ssh.close()