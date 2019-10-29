import re
import requests
import random
import json
from fake_useragent import UserAgent

# 实例化UserAgent对象，用于产生随机UserAgent
ua = UserAgent()


class NeiHanBa(object):

    def __init__(self):
        self.base_url = 'https://www.neihan-8.com/article/list_5_{}.html'
        self.headers = {"User-Agent": ua.random}
        self.fir_regex = re.compile('<div class="f18 mb20">(.*?)</div>', re.S)

        # 清洗掉所有的<>标签, &xxx字符原型, 空格
        self.sec_regex = re.compile('<.*?>|&(.*?);|\s')

    def send_request(self, url):
        # 发送请求
        response = requests.get(url, headers=self.headers)
        data = response.content.decode('GBK')
        # print(data)
        return data

    def parse_data(self, data):
        # 提取数据
        result_list = self.fir_regex.findall(data)

        return result_list

    def save_file(self, data_list, page):
        # 保存数据
        page_num = '==========第 {} 页==========\n\n'.format(page)
        # print(page_num)
        with open('./reptile/neihan8.txt', 'a') as f:
            f.write(page_num)
            for content in data_list:
                # 数据清洗
                new_content = self.sec_regex.sub('', content) + '\n\n'

                f.write(new_content)

    def main(self):
        page = int(random.randint(1,50))
        # 构造每页的url
        url = self.base_url.format(page)
        # 发起请求
        data = self.send_request(url)
        # 提取数据
        data_list = self.parse_data(data)
        # print(data)
        # 数据清洗 并保存
        self.save_file(data_list, page)
        print('爬取的段子已全部写入 neihan8.txt 中, 请查阅...')
        num = int(random.randint(1,5))
        return self.sec_regex.sub('',data_list[num]) + '\n\n'
if __name__ == '__main__':
    NeiHanBa().main()
