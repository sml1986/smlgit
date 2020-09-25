import requests
import os
from bs4 import BeautifulSoup
import urllib.request

# 请求头
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.116 Safari/537.36'}


# 让python创建文件，保存我们抓取的数据
if not os.path.exists("网易云歌单"):
    os.mkdir("网易云歌单")


#输入想要抓取的歌单
play_url = input('请输入需要的歌单信息：')


#使用requests请求访问网站，返回数据
s = requests.session()
res = s.get(play_url, headers=headers).content
# print(res)

# https://music.163.com/#/playlist?id=3214189237
# 筛选歌曲  网页选择器
'''
BeautifulSoup(参数，参数)
参数一：指定你要筛选的网页
参数二：html解析库：lxml
'''
soup = BeautifulSoup(res, 'lxml')
music_data = soup.find('ul', class_='f-hide')
# print(music_data)


# 将抓取的信息进行处理，只保留歌曲名称信息和歌曲url
# 全局变量，临时保存歌曲名称和歌曲url
lists = []

for music in music_data.find_all('a'):
    # print('{}:{}'.format(music.text, music['href']))
    list = []
    music_url = 'http://music.163.com/song/media/outer/url' + music['href'][5:] + '.mp3'
    music_name = music.text
    list.append(music_name)
    list.append(music_url)

    # 局部变量添加到全局变量当中
    lists.append(list)
# print(lists)

# 下载
for i in lists:
    url = i[1]
    name = i[0]

    try:
        print('正在下载：', name)
        urllib.request.urlretrieve(url, '网易云歌单/%s.mp3' % name)
        print('下载成功')
    except:
        pass