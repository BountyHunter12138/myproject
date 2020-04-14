import random
import requests
import time
import hashlib
import json

from requests import Response

class Youdao():
    def __init__(self,content):
        self.content=content
        self.url='http://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule'
        self.ts=self.get_ts()
        self.salt=self.get_salt()
        self.sign=self.get_sign()

    def get_salt(self):
        return self.ts + str(random.randint(0, 10))

    def get_md5(self,value):
        m=hashlib.md5()
        m.update(value.encode("utf-8"))
        return m.hexdigest()

    def get_sign(self):
        s="fanyideskweb"+self.content+self.salt+"Nw(nmmbP%A-r6U3EUn]Aj"
        return self.get_md5(s)


    def get_ts(self):
        t = time.time()
        return str(int(round(t * 1000)))



    def yield_form_data(self):
        return {
            'i': self.content,
            'from': 'AUTO',
            'to': 'AUTO',
            'smartresult': 'dict',
            'client': 'fanyideskweb',
            'sign': self.sign,
            'salt': self.salt,
            'ts': self.ts,
            'bv': '70244e0061db49a9ee62d341c5fed82a',
            'doctype': 'json',
            'version': '2.1',
            'keyfrom': 'fanyi.web',
            'action': 'FY_BY_REALTlME',
        }

    def yield_headers(self):
        return{
            'Cookie': 'OUTFOX_SEARCH_USER_ID=518732761@10.108.160.18; OUTFOX_SEARCH_USER_ID_NCOO=168453912.11179173; JSESSIONID=aaafKk0ImFZPOcqIWd0fx; ___rl__test__cookies=1586790084730',
            'Referer': 'http: // fanyi.youdao.com /',
            'User-Agent': 'User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36',
        }



    def fanyi(self):
        response = requests.post(self.url, data=self.yield_form_data(), headers=self.yield_headers())
        content=json.loads(response.text)
        return content['translateResult'][0][0]['tgt']

if __name__ =="__main__":
    while(True):
        a = input('input:')
        youdao=Youdao(a)
        print("fanyi_result :",youdao.fanyi())
