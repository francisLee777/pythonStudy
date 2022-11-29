import urllib.request
import webbrowser as web

import requests as req

url = "http://www.hao123.com"
payload = str({"id": 123, "name": "haoyu"})  # req body 字符串
headers = {"Content-Type": "application/json",
           "Cookie": "sss;aaa"}    # headers 字典

resp = req.request("post", url, headers=headers, data=payload)
print(resp.status_code, resp.text)


content = urllib.request.urlopen("http://www.baidu.com")
print(content.info())
print(content.geturl())
print(content.getcode())

open("baidu.html", "wb").write(content.read())
web.open_new_tab("baidu.html")


def Download(a, b, c):
    per = 100.0 * a * b / c
    if per > 100:
        per = 100
    print('%.2f' % per)


# url = 'http://www.sina.com.cn'
# local = './sina.html'
# urllib.request.urlretrieve(url, local, Download)
