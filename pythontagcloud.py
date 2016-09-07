#!/usr/bin/python3.4
# -*- coding: utf-8 -*-

# http://www.lfd.uci.edu/~gohlke/pythonlibs/#cx_freeze
# 万能仓库下载pygame
# pip3下载simplejson
# C:\Python34\Lib\site-packages

from pytagcloud import create_tag_image, make_tags
import re
import time
from collections import Counter
import datetime

# 去除内容中的非法字符 (Windows)
def validatecontent(content):
    # '/\:*?"<>|'
    rstr = r"[\/\\\:\*\?\"\<\>\|\.\*\+\-\(\)\"\'\（\）\！\？\“\”\,\。\；\：\{\}\{\}\=\%\*\~\·]"
    new_content = re.sub(rstr, "", content)
    return new_content

if __name__ == '__main__':

    # 打印的语言
    languages = input("选择打印英文按0，打印中文请按1，打印中英结合请按2（默认打印中英结合）：")
    language = 'MicrosoftYaHei'
    try:
        if languages == "0":
            language = 'Lobster'
        elif languages == "1":
            language = 'MicrosoftYaHei'
        elif languages == "2":
            language = 'MicrosoftYaHei'
    except:
        language = 'MicrosoftYaHei'

    # 打印的字体大小
    fontszs = input("选择特大字体请按0，大字体请按1，中字体请按2，小字体请按3（默认大字体）：")
    fontsz = 90
    try:
        if fontszs == "0":
            fontsz = 180
        elif fontszs == "1":
            fontsz = 120
        elif fontszs == "2":
            fontsz = 90
        elif fontszs == "3":
            fontsz = 60
    except:
        fontsz = 120

    # 图片长宽
    imglength = 1000
    imgwidth = 800
    try:
        imglengths = int(input("请输入图片长（默认1000）："))
        if isinstance(imglengths, int) == True:
            imglength = imglengths
    except:
        imglength = 1000
    try:
        imgwidths = int(input("请输入图片宽（默认800）："))
        if isinstance(imgwidths, int) == True:
            imgwidth = imgwidths
    except:
        imgwidth = 800

    # 背景颜色
    rcolor = 255
    gcolor = 255
    bcolor = 255
    print("RGB颜色对照值可以参考博客：http://www.cnblogs.com/TTyb/p/5849249.html")
    try:
        rcolors = int(input("请输入背景颜色RGB格式的R（0-255默认白色）："))
        if isinstance(rcolors, int) == True:
            rcolor = rcolors
    except:
        rcolor = 255
    try:
        gcolors = int(input("请输入背景颜色RGB格式的G（0-255默认白色）："))
        if isinstance(gcolors, int) == True:
            gcolor = gcolors
    except:
        gcolor = 255
    try:
        bcolors = int(input("请输入背景颜色RGB格式的B（0-255默认白色）："))
        if isinstance(bcolors, int) == True:
            bcolor = bcolors
    except:
        bcolor = 255
    # 构造
    # counts =[('cloud', 3),
    # ('words', 2),
    # ('code', 1),
    # ('word', 1),
    # ('appear', 1)]
    arr = []
    file = open('../tagcloud/tag_file.txt', 'r')
    data = file.read().split('\r\n')
    for content in data:
        contents = validatecontent(content).split()
        for word in contents:
            arr.append(word)
    counts = Counter(arr).items()

    # 用一个时间来命名
    nowtime=time.strftime('%Y%H%M%S', time.localtime())
    # 设置字体大小
    tags = make_tags(counts, maxsize=int(fontsz))
    # 生成图片
    create_tag_image(tags, '../tagcloud/' + str(nowtime) + '.png', size=(imglength, imgwidth), fontname=language,background=(int(rcolor), int(gcolor), int(bcolor)))
    print(('已经储存至../tagcloud/' + str(nowtime) + '.png'))
