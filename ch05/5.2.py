#coding:utf-8

import urllib
from lxml import etree
import requests
def Schedule(blocknum,blocksize,totalsize):
    '''''
    blocknum:已经下载的数据块
    blocksize:数据块的大小
    totalsize:远程文件的大小
    '''
    per = 100.0 * blocknum * blocksize / totalsize
    if per > 100 :
        per = 100
    print '当前下载进度：%d'%per
user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
headers={'User-Agent':user_agent}
r = requests.get('http://www.ivsky.com/tupian/ziranfengguang/',headers=headers)
#使用lxml解析网页
html = etree.HTML(r.text)
img_urls = html.xpath('.//img/@src')#先找到所有的img
i=0
for img_url in img_urls:
    urllib.request.urlretrieve('http:'+img_url,'img'+str(i)+'.jpg',Schedule)
    #2019.11.09在查询该网站时已经将图片地址进行修饰隐藏，缺少"http:"字符串;而且python3中将urlretrieve已经移到urllib.request下面. --Carey          
    i+=1
