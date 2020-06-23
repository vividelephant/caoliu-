import requests
from pyquery import PyQuery as pq
from time import sleep
import re
import os
shaixuan = re.compile('ess-data="(.*?)"')
headers = {'user-agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Safari/537.36'}
name = input('请输入你要创建的文件夹名称：')
if not os.path.exists(name):
    os.mkdir(name)
page = int(input('请输入你要爬取几页：'))
if page >= 1:
        urls = ['http://t66y.com/thread0806.php?fid=16&search=&page={}'.format(a) for a in range(1,page+1)]


def get_title(url):
    response = requests.get(url, headers =headers)
    response = response.text
    doc = pq(response)
    # print(doc)
    html = doc('h3 a').items()
    for urls in html:
        urls = urls.attr('href')
        urls = 'http://t66y.com/{}'.format(urls)
        ge_html(urls)
        

def ge_html(url):
    response = requests.get(url, headers =headers)
    response = response.text
    doc = pq(response)
    # print(doc)
    html = doc('img').items()
    for urls in html:
        try:
            urls = str(urls)
            urls = shaixuan.findall(urls)
            url = ''.join(urls)
            # print(url)

            get_url(url)
        except:
            continue
        # urls = str(urls)
        # urls = shaixuan.findall(urls)
        # url = ''.join(urls)
        # # print(url)

        # get_url(url)

def get_url(url):
    global i
    get_html = requests.get(url,headers = headers)
    sleep(2)
    with open(name+'/'+'{}.jpg'.format(i),'wb')as f:
        f.write(get_html.content)

    print('正在打印第{}张图片'.format(i))
    
    i = i+1






if __name__ == "__main__":
    i = 1
    for url in urls:
        get_title(url)

# https://www.yuoimg.com/u/20200614/11330311.jpg
# https://www.yuoimg.com/u/20200614/11321871.jpg