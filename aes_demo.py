#AES-demo
#pip install pycryptodome
import base64
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad

'''
采用AES对称加密算法
'''
# str不是16的倍数那就补足为16的倍数-此填充模式填充数据块儿不支持中文
def add_to_16(value):
    while len(value) % 16 != 0:
        value += '\0'
    return str.encode(value)  # 返回bytes

def pad_zero(value,length=16):
    if length not in [16,24,32]:
        raise ValueError('填充长度必须为16、24或32！')
    while len(value)% length !=0:
        value += '\0'
    return value.encode()

#加密方法
def encrypt_aes(pt, key='20200501'):
    # 初始化加密器
    aes = AES.new(add_to_16(key), AES.MODE_ECB)
    #先进行aes加密
    encrypt_aes = aes.encrypt(add_to_16(pt))
    #用base64转成字符串形式
    encrypted_text = str(base64.encodebytes(encrypt_aes), encoding='utf-8')  # 执行加密并转码返回bytes
    return encrypted_text
#解密方法
def decrypt_aes(ct, key='20200501'):
    # 秘钥
    # 密文
    # 初始化加密器
    aes = AES.new(add_to_16(key), AES.MODE_ECB)
    #优先逆向解密base64成bytes
    base64_decrypted = base64.decodebytes(ct.encode(encoding='utf-8'))
    #执行解密密并转码返回str
    decrypted_text = str(aes.decrypt(base64_decrypted),encoding='utf-8').replace('\0','')
    return decrypted_text

#支持中文
def encrpt_zhCN(pt,key='hello123321olleh'):
    #确定区块大小
    BLOCK_SIZE = 16  # Bytes长度
    #初始化加密器
    #AES算法允许128,192,256位长度的密钥，对应的字节应该是16,24,32, 所以填写长度的时候应该填16,24,32
    cipher = AES.new(add_to_16(key), AES.MODE_ECB)
    # 填充算法-默认pkcs7模式-支持中文加解密
    block = pad(pt.encode(), BLOCK_SIZE)
    #加密填充后的数据块
    encrypt_aes = cipher.encrypt(block)
    #base64转字符串形式
    encrypted_text=base64.encodebytes(encrypt_aes).decode()
    return encrypted_text

def decrpt_zhCN(ct,key='hello123321olleh'):
    BLOCK_SIZE = 16
    #生成加密器-与加密方法里相同的密钥和加密模式
    decipher = AES.new(add_to_16(key), AES.MODE_ECB)
    # 先解码base64成bytes
    base64_decrypted = base64.decodebytes(ct.encode(encoding='utf-8'))
    #再解密出原始的数据块
    msg_dec = decipher.decrypt(base64_decrypted)
    #将数据块还原，并转成str
    decrypted_text=unpad(msg_dec, BLOCK_SIZE).decode()
    # decrypted_text = msg_dec.decode()
    return decrypted_text

if __name__ == '__main__':
    encrypted_text=encrypt_aes('hello')
    print(encrypted_text)
    decrypted_text= decrypt_aes(encrypted_text)
    print(decrypted_text)

    ct=encrpt_zhCN('''{
    "ret": 0,
    "id" : 677
    }''')
    print('密文是: '+ct)
    pt=decrpt_zhCN(ct)
    print('明文是: '+pt)

    print(pad_zero('123456789ABCDEF',16))

