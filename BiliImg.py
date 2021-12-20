import requests
import time
import urllib.request

# 图片下载
def download_img(imgurl, img_name):
    request = urllib.request.Request(imgurl)
    print(request)
    try:
        response = urllib.request.urlopen(request)
        filename = "./images/xsq/" + img_name
        if (response.getcode() == 200):
            with open(filename, "wb") as f:
                f.write(response.read())  # 将内容写入图片
            return filename
    except:
        return "failed"

def getimglist():
    r = requests.get('https://api.bilibili.com/x/dynamic/feed/draw/doc_list?uid=8138650')
    imglist = r.json()['data']['items']

    for item in imglist:
        otherStyleTime = time.strftime("%Y-%m-%d %H%M%S ", time.localtime(int(item['ctime'])))
        print(otherStyleTime)
        i = 1
        for img in item['pictures']:
            filename = otherStyleTime + item['description'] + ' ' + str(i) + '.jpg'
            print(filename)
            download_img(img['img_src'], filename)
            i = i+1

getimglist()
