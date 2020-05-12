import requests


class HeFeng():
    def __init__(self):
        self.url = "https://cdn.heweather.com/china-city-list.txt"
        self.encoding='utf8'
        self.pre_request="https://free-api.heweather.net/s6/weather/now?=location="
        self.sub_request="&key=fe25a971118e422ebe08446900d10b04"
    def get_weather(self,city_code):
        url=self.pre_request+city_code+self.sub_request
        info=requests.get(url)
        info.encoding=self.encoding
        print(info.text)
    def get_city_code(self):
        cities = self.get_citys()
        for each in cities:
            yield each[2:13]


    def get_citys(self):
        html=requests.get(self.url)
        html.encoding=self.encoding
        cities=html.text.split('\n')
        return cities[6:]



if __name__ == '__main__':
    hefeng = HeFeng()
    codes=hefeng.get_city_code()
    for i in range(10):
        print(hefeng.get_weather(codes.__next__()))

