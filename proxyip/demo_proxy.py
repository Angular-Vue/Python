# -*- coding: utf-8 -*-
import requests
import json
import time
import random
import re
from fake_useragent import UserAgent

# 实例化UserAgent对象，用于产生随机UserAgent
ua = UserAgent()


def click_proxy():
    proxy_list = []
    with open("proxyip.json") as f:
        proxy_list = json.loads(f.read())
    # print(proxy_list)
    # print(type(proxy_list))

    while True:
        for proxy in proxy_list:
            header = {'User_Agent': ua.random}
            temp_proxy = {}
            temp_proxy[proxy["ip_type"]] = proxy["ip"]
            # print(type(temp_proxy))
            try:
                response = requests.get(verify_url, headers=header, proxies=temp_proxy, timeout=3)
                if response.status_code == 200:
                    temp_url = random.choice(url_list)
                    num = re.findall(r"/(\d+)", temp_url)
                    requests.get(temp_url, headers=header, proxies=temp_proxy)
                else:
                    print("IP: {} 不能使用，正常尝试下一个...".format(proxy.get("ip")))
                    time.sleep(0.1)
                    continue
            except Exception as e:
                print('=========wrong: {}========='.format(e))
                time.sleep(0.1)
            time.sleep(5)


if __name__ == "__main__":
    click_proxy()
