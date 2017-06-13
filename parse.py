#coding=utf-8
import requests
import os

def getManyPages(keyword,pages):
    params=[]
    for i in range(30,30*pages+30,30):
        params.append({
                      'tn': 'resultjson_com',
                      'ipn': 'rj',
                      'ct': 201326592,
                      'is': '',
                      'fp': 'result',
                      'queryWord': keyword,
                      'cl': 2,
                      'lm': -1,
                      'ie': 'utf-8',
                      'oe': 'utf-8',
                      'adpicid': '',
                      'st': -1,
                      'z': '',
                      'ic': 0,
                      'word': keyword,
                      's': '',
                      'se': '',
                      'tab': '',
                      'width': '',
                      'height': '',
                      'face': 0,
                      'istype': 2,
                      'qc': '',
                      'nc': 1,
                      'fr': '',
                      'pn': i,
                      'rn': 30,
                      'gsm': '1e',
                      '1488942260214': ''
                  })
    url = 'https://image.baidu.com/search/acjson'
    urls = []
    for i in params:
        urls.append(requests.get(url,params=i).json().get('data'))

    return urls


def getImg(dataList, localPath):

    if not os.path.exists(localPath):  # 新建文件夹
        os.mkdir(localPath)

    x = 1
    for list in dataList:
        for i in list:
            if i.get('thumbURL') != None:
                print'Downloading：', i.get('thumbURL')
                ir = requests.get(i.get('thumbURL'))
                fileName=localPath + '/%d.jpg' % x
                pic = open(fileName, 'wb')
                pic.write(ir.content)
                pic.close()
                x += 1
            else:
                print('图片链接不存在')

#if __name__ == '__main__':
inp = raw_input('请输入关键词: ')
name = inp;

while (True):
    inp = raw_input('请输入想要下载的页数，每页30张图，自动创造并存储到image的文件中： ')
    num = int(inp)  
    try:
        num = int(inp)
        break
    except:
        print ('请输入一个正整数')


dataList = getManyPages(name,num)  # 参数1:关键字，参数2:要下载的页数
getImg(dataList,'image') # 参数2:指定保存的路径
    
