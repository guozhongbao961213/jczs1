import requests
import re


# 从主页面拿到所有页面上的图片超链接
def get_all_mig_html(url):
    url_list = []
    resp_html = requests.get(url).text
    MFStar = re.compile('<a href="(.*?)">\n').findall(resp_html)  # MFStar 所有超链接地址   </MFStar-108/>

    for i in MFStar:
        url_list.append("https://photos.xtapo.com/" + i)

    return url_list


# 拿到超链接里面的图片地址
def get_url(url):
    resp_html = requests.get(url=url).text
    MFStar = re.compile('<img src="(.*?)" alt="').findall(resp_html)  # MFStar 所有超链接地址   </MFStar-108/> -->图片.jpg
    print(MFStar)

    for i in MFStar:
        print(i)
        # save_img(i)
        print(f"{i}下载完成")
    print("完成")


# 请求图片地址，保存到本地
def save_img(url):
    resp_img = requests.get(url).content  # 请求这个图片
    img_name = url.split("/")[-1]
    print(img_name)
    with open(f'img/{img_name}', 'wb') as f:
        f.write(resp_img)


for i in range(2, 48):
    url = f"https://photos.xtapo.com/page{i}/"  # 每次变更主页面的url
    url_list = get_html(url)
    for i in url_list:
        get_url(i)