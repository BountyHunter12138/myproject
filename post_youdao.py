from random import random
import random
import requests
import time

url="http://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule"
content = " 我和你 "

def get_salt():
    s=str(random.randint(0,10))
    t=get_ts()
    #print("random = ",s)
    #print("ts =",t)
    #print("salt =",t+s)
    return t+s
    #return '15846865666505'

def get_md5(value):
    import hashlib
    m = hashlib.md5()
    m.update(value.encode("utf-8"))
    return m.hexdigest()


def get_sign():
    e = get_content()
    i = get_salt()
    s = "fanyideskweb" + e + i + "Nw(nmmbP%A-r6U3EUn]Aj"
    print("s=", get_md5(s))
    return get_md5(s)
    #return 'ebbca201bf1eaa2797175df91e7dc725'
            #ec579abcd509567b8d56407a80835950

def get_ts():
    import time
    t = time.time()
    ts = str(int(round(t * 1000)))
    print(ts)
    return ts
           #1585615766651
def get_content():
    return content

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

def get_headers():
    headers={
        'Cookie: OUTFOX_SEARCH_USER_ID=518732761@10.108.160.18;'
        'Referer: http://fanyi.youdao.com/'
        'User-Agent: Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.25 Safari/537.36 Core/1.70.3741.400 QQBrowser/10.5.3863.400'
    }
    return headers




if __name__ == '__main__':
    print(form_data)
    print(get_headers())
    response = requests.post(url,data=form_data,headers=get_headers())
    print(response.text)

都是狗屁