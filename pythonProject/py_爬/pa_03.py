import requests
import re

headers = {'keep-live': 'false'}
url = 'https://photos.xtapo.com/'
proxies = {
    'http': 'http://185.179.30.130:8080',
    'https': 'http://185.179.30.130:8080',
}


def get_all_paginal(url, page, pages):  # 返回所有页的url
    all_url = []
    if page == 1 or page == 0:
        all_url.append(url)
        print('下载包含首页！')
        for i in range(page + 1, pages + 1):
            all_url.append(url + f'page{i}/')
    else:
        for i in range(page, pages):
            all_url.append(url + f'page{i}/')  # 生成所有页的url
    print(all_url)
    return all_url


def get_all_photo(all_url):  # 返回所有页面的相册接口
    photo_all_api = []
    for paginal_url in all_url:
        photo_req = requests.get(paginal_url, headers=headers).text  # 获取页面返回的html
        photo_ye_all_api = re.compile('<a href="(.*?)">\n').findall(photo_req)  # 获取页面所有的相册接口
        photo_all_api.extend(photo_ye_all_api)
    print(photo_all_api)
    return photo_all_api


def get_all_img(url, photo_all_api):  # 返回所有图片的url
    img_all_url = []
    for photo_api in photo_all_api:
        photo_url1 = url + photo_api  # 拼接相册链接
        img_req = requests.get(photo_url1, headers=headers).text  # 获取相册页返回的html
        img_ye_all_url = re.compile('<img src="(.*?)" alt="').findall(img_req)  # 拿出所有图片的url
        img_ye_all_url.pop(-1)
        img_all_url += img_ye_all_url
    print(img_all_url)
    return img_all_url



def get_img(img_all_url, path):
    for img_url in img_all_url:
        try:
            img = requests.get(img_url, headers=headers).content  # 循环获取每一张图片的url
        except requests.exceptions.RequestException:
            print(f'{img_url}请求失败，重试')
            continue
        img_name = img_url.replace("/" , "a").split("-")[-1]  # 获取图片名称
        with open(f'{path}{img_name}', 'wb') as w:
            w.write(img)  # 把二进制图片写入本地文件
        print(f'{img_name}下载完成')


all_url = get_all_paginal(url, 13, 15)
photo_all_api = get_all_photo(all_url)
img_all_url = get_all_img(url, photo_all_api)
get_img(img_all_url, 'C:/Users/img/')
