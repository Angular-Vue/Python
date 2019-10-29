import json
import urllib
import urllib.request
from bs4 import BeautifulSoup

def weather(name):
    file_path = './weather/city.json'
    with open(file_path) as f:
        js = json.load(f)  # js是转换后的字典
        for key in js:
            if key == name:
                url = "http://www.weather.com.cn/weather/" + js[key] + ".shtml"
                info = urllib.request.urlopen(url).read()
                soup = BeautifulSoup(info, "html.parser")
                print(soup.title.get_text())
                info = ""
                name = soup.find_all(attrs={"class": "sky skyid lv3 on"})
                for u in name:
                    wea = u.find(attrs={"class": "wea"}).get_text()
                    tem = u.find(attrs={"class": "tem"}).get_text()
                    info = "天气:" + wea + " 温度:" + tem
                    info = info.replace("\n", "")
                return info
def isHaveCity(name):
    file_path = './weather/city.json'
    with open(file_path) as f:
        js = json.load(f)  # js是转换后的字典
        return name in js