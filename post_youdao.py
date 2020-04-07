import requests
import random
import time

url="http://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule"


def get_salt():
    s=str(random.randint(0,10))
    t=get_ts()
    print("random = ",s)
    print("ts =",t)
    print("salt =",t+s)
    return t+s
    #return '15846865666505'
           #15856157666510
           #1586221706637

def get_sign():
    return 'ebbca201bf1eaa2797175df91e7dc725'
            #ec579abcd509567b8d56407a80835950

def get_ts():
    import time
    t = time.time()
    ts = str(int(round(t * 1000)))
    return ts
           #1585615766651

form_data={
    'i': '我爱你',
    'from': 'AUTO',
    'to': 'AUTO',
    'smartresult': 'dict',
    'client': 'fanyideskweb',
    'salt': get_salt(),
    'sign': get_sign(),
    'ts': get_ts(),
    'bv': 'ec579abcd509567b8d56407a80835950',
    'doctype': 'json',
    'version': '2.1',
    'keyfrom': 'fanyi.web',
    'action': 'FY_BY_REALTlME',
}
response=requests.post(url,form_data)
print(response.text)


