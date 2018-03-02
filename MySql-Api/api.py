#pip安装对应插件

import tornado.ioloop
import tornado.web
import json
import pymysql  # 导入 pymysql
jsonData = []

class MainHandler(tornado.web.RequestHandler):
  db = pymysql.connect(host="localhost", user="root", password="ty111111", db="world", port=3306)

  # 使用cursor()方法获取操作游标
  cur = db.cursor()

  # 1.查询操作
  # 编写sql 查询语句  user 对应我的表名
  sql = "select * from city"
  try:
    cur.execute(sql)  # 执行sql语句

    results = cur.fetchall()  # 获取查询的所有记录

    # 遍历结果
    for row in results:
      id = row[0]
      name = row[1]
      CountryCode = row[2]
      District = row[3]
      Population = row[4]
      jsonData.append({"id": id, "name": name, "CountryCode": CountryCode, "District": District, "Population": Population})
  finally:
    db.close()  # 关闭连接
    def set_default_headers(self):  #设置可以获取数据的host地址，防止需要跨域；
        print("德玛西亚！！！")
        self.set_header("Access-Control-Allow-Origin", "*")  #指定域名才可以调出数据
        self.set_header("Access-Control-Allow-Headers", "x-requested-with")
        self.set_header('Access-Control-Allow-Methods', 'POST, GET, OPTIONS')
    def get(self):
        # self.write(json.dumps(jsonData))
        self.finish(json.dumps(jsonData))
def make_app():
    return tornado.web.Application([
        (r"/", MainHandler),
    ])

if __name__ == "__main__":
    app = make_app()
    app.listen(7788)
    tornado.ioloop.IOLoop.current().start()