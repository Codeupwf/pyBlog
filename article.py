# -*- coding: utf-8 -*-
'''文章的处理模块，所有操作都是围绕着文章对象进行处理。

目前本模块实现功能有：
sortArticleListByTime 根据文章中的时间戳来对文章列表进行排序。
getArticleTime 获取文章时间戳。
getArticleContent 获取文章内容。

文章文件开头必须有如下标签，用来说明文章的通用属性。
---
layout: post
title: "头文件是如何参与编译的"
date: 2014-08-03 00:00:00
comments: true
categories: Unix CLI
---
'''

import os
import codecs
# import datetime
import markdown
import time
from flask import Markup

STR_MORE_BEGIN = '[***More...***]('
STR_MORE_END = ')       '

def sortArticleListByTime(fileList, reverse = False):
    '''根据文章中的时间戳来对文章列表进行排序。

    读取文件列表中所有文章的时间戳并按时间戳进行排序，返回排序后的文章列表。
    fileList: 文章列表，内容需要为markdown文章的绝对路径，需要能够直接打开
    reverse: 升降序规则，True表示降序，时间戳较新的在前，反之时间戳较旧的在前
    return: 排序后的fileList，注意此返回值不包含无效输入'''
    articles = []
    sortedFileList = []
    for file in fileList:
        if file.find('.markdown') == -1:
            continue
        articles.append({"Time":getArticleTime(file), "filePath":file})
    articles = sorted(articles, key = lambda x:x["Time"], reverse = reverse)
    for a in articles:
        sortedFileList.append(a["filePath"])
    return sortedFileList

def getArticleTime(filePath):
    '''获取文章时间戳。

    获取指定路径文章的时间戳，并换算成标准时间。
    filePath: 绝对路径，用于打开文件（e.g. /Users/Codeup/Documents/Coding/Projects/pyBlog/posts/2014-08-03-include-file-in-compile.markdown）'''
    f = codecs.open(filePath, mode='r', encoding='utf-8')
    lines = []
    try:
        lines = f.readlines()
    except :
        pass
    f.close()
    date = ''
    for line in lines[1:]:
        if line.find('date: ') == 0:
            date = line.replace('date: ', '')[0:-1]
            break
    if date != '':
        date_tup = time.strptime(date, "%Y-%m-%d %H:%M:%S")
        date_secds = time.mktime(date_tup)
        return date_secds
    else:
        return date
    # return date


def getArticleContent(filePath, urlPrefix, showMore):
    '''获取文章内容。

    获取指定路径下单篇文章的全部内容。
    filePath: 绝对路径，用于打开文件和构造文件名称（e.g. /Users/Codeup/Documents/Coding/Projects/pyBlog/posts/2014-08-03-include-file-in-compile.markdown）
    urlPrefix: URL前缀，用来构造more超链接。(e.g. http://blog.wangfu.info/article/)
    showMore: 是否显示‘--more--’后的内容。'''
    f = codecs.open(filePath, mode='r', encoding='utf-8')
    link = urlPrefix + filePath.split(os.sep)[-1].split('.')[0]     #链接地址，用于构造more超链接
    lines = []
    try:
        lines = f.readlines()
    except:
        pass
    f.close()
    ret = {}
    title = ''
    date = ''
    index = 1
    for line in lines[1:]:
        index += 1
        if line.find('title: ') == 0:
            title = line.replace('title: "', '')[0:-2]      #解析标题
        if line.find('date: ') == 0:
            date = line.replace('date: ', '')[0:-1]     #解析时间戳
        if line.find('---') == 0:
            break       #解析到 --- 认为通用标签结束，进入正文解析流程
    content = u''
    for line in lines[index:]:
        if line.find('--more--') == 0:      #解析到 --more--
            if showMore:
                continue     #如果showMore为真，则跳过 --more-- ，继续将后面的正文返回
            else:
                content += STR_MORE_BEGIN + link +STR_MORE_END  #如果showMore为假，则停止解析正文，并将 --more-- 替换为文章超链接Markdown文本
                break
        content += line    
    if title:
        ret['title'] = title
        ret['date'] = date
        ret['content'] = Markup(markdown.markdown(content,extensions=['codehilite(guess_lang=False)','fenced_code']))   #代码高亮
        ret['name'] = filePath.split(os.sep)[-1].split('.')[0]
    return ret