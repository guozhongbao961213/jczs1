import requests
import re

url = 'https://pic.netbian.com/'
req = requests.get(url).text
img_url_all = re.compile('img src="/(.*?)" alt=').findall(req)
print(img_url_all)
f = 1
for img_url in img_url_all:
    req = requests.get(url + img_url).content
    with open(f'C:/Users/Administrator/Desktop/img/img{f}.jpg', 'wb') as w:
        w.write(req)
        print(f'第{f}张完成')
        f += 1