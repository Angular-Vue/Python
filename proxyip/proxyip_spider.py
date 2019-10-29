# -*- coding: utf-8 -*-
# @Author: Nick
# @Date:   2019-10-11 15:40:58
# @Last Modified by:   Nick
# @Last Modified time: 2019-10-12 16:54:31


import requests
import json
import time
from lxml import etree


class proxyip_spider(object):
    """docstring for proxyip_spider"""

    def __init__(self):
        # self.base_url = "https://www.kuaidaili.com/free/"
        self.headers = {'User-Agent': 'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1)'}
        self.url = "https://www.kuaidaili.com/free/inha/{}"

    def send_request(self, page):
        data = requests.get(self.url.format(page)).content.decode()

        return data

    def parse_data(self, page):
        html_str = self.send_request(page)
        # print(html_str)
        element_obj = etree.HTML(html_str)
        ip_type = element_obj.xpath('//*[@id="list"]/table/tbody/tr/td[4]/text()')
        ip = element_obj.xpath('//*[@id="list"]/table/tbody/tr/td[1]/text()')
        port = element_obj.xpath('//*[@id="list"]/table/tbody/tr/td[2]/text()')
        data_li = list(zip(ip_type, ip, port))
        # print(data_li)
        return data_li

    def save_data(self, data):
        with open("proxyip.json", "a+") as f:
            f.write(json.dumps(data))

    def main(self):
        proxy_data = list()
        for p in range(10):
            print("正在抓取{}页。。。".format(p + 1))
            data_li = self.parse_data(p + 1)
            for per_data in data_li:
                ip_type, ip, port = per_data
                proxy_data.append(dict(ip_type=ip_type, ip=ip + ":" + port))
            # print(proxy_data)
            time.sleep(1)
        self.save_data(proxy_data)
        print(proxy_data)


if __name__ == '__main__':
    proxyip_spider().main()
