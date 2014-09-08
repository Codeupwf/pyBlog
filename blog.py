# -*- coding: utf-8 -*-
import os
import codecs
import datetime
import PyRSS2Gen
import markdown
from article import getArticleContent, sortArticleListByTime, getMarkdownArticleContent, \
    createTmpTxtFile
from flask import Flask, request, g, \
    render_template, flash, Markup, send_from_directory,send_file, redirect, url_for, jsonify
from flask.ext.cache import Cache
from users import valid_password

# configuration
TITLE = 'Wang Fu'
URL = 'http://blog.wangfu.info'
POST_DIR = os.path.dirname(os.path.abspath(__file__)) + os.sep + 'posts'
RSS_PATH = os.path.dirname(os.path.abspath(__file__)) + os.sep + 'rss.xml'
LOG_FORMAT = '%(asctime)-15s [%(pathname)s:%(lineno)d]: %(message)s'

# create app
app = Flask(__name__)
app.config.from_object(__name__)
app.config.from_envvar('SETTINGS', silent=True)
app.debug_log_format = LOG_FORMAT
app.secret_key = 'some_secret'

# create cache instance
cache = Cache(app, config={"CACHE_TYPE": "simple"})


def articleFileRender(filePath, showMore):
    '''渲染单篇文章

    filePath: 文章绝对路径
    showMore: 是否显示--More--标签之后的内容'''
    return getArticleContent(filePath, app.config["URL"] + "/article/", showMore)

 
def RSSMaker():
    articles = []
    postDir = app.config["POST_DIR"]
    fileList = []
    files = os.listdir(postDir)
    for f in files:
        fileList.append(postDir + os.sep + f)
    fileList = sortArticleListByTime(fileList, reverse = True)
    for singleFile in fileList:
        article = articleFileRender(singleFile, True)
        if article:
            articles.append(article)
    rssItems = []
    for article in articles:
        link = app.config["URL"] + "/article/" + article["name"]
        rssItem = PyRSS2Gen.RSSItem(
            title=article["title"],
            link=link,
            description=article["content"],
            guid=PyRSS2Gen.Guid(link),
            pubDate=datetime.datetime(int(article["date"][0:4]),
                                      int(article["date"][5:7]),
                                      int(article["date"][8:10]),
                                      int(article["date"][11:13]),
                                      int(article["date"][14:16])))
        rssItems.append(rssItem)
    rss = PyRSS2Gen.RSS2(
        title=app.config["TITLE"],
        link=app.config["URL"],
        description="",
        lastBuildDate=datetime.datetime.utcnow(),
        items=rssItems)
    rss.write_xml(open(app.config['RSS_PATH'], "w"))

@cache.cached()
def getPageByIndex(Index):
    '''根据文章索引号获取显示页，每页显示3篇文章，所以0、1、2其实返回数据是一样的。
    使用@cache.cached()装饰器装饰，根据索引进行缓存，提高显示效率。
    flask-cache扩展依据【request.path】作为缓存Key，所以调用本函数前要对request.path进行key值处理，必须包含Index信息'''
    app.logger.debug("index begin")
    articles = []
    postDir = app.config["POST_DIR"]
    fileList = []
    files = os.listdir(postDir)
    p = int(Index)
    for f in files:
        fileList.append(postDir + os.sep + f)
    fileList = sortArticleListByTime(fileList, reverse = True)
    for singleFile in fileList[p:p + 3]:
        article = articleFileRender(singleFile, False)
        if article:
            articles.append(article)
    if p > 2:
        prev = True
    else:
        prev = False
    if p + 4 <= len(fileList):
        pnext = True
    else:
        pnext = False
    tmprender = render_template("index.html", title=app.config['TITLE'], url=app.config['URL'], articles=articles, prev=prev, pnext=pnext, prevnum=p - 3, nextnum=p + 3)
    app.logger.debug("index end")
    return tmprender

@app.route(r'/', methods=['GET'])
def index():
    '''显示主页'''
    app.logger.debug(request.path)
    p = int(request.args.get('p', '0'))
    request.path = request.path + str(p)
    app.logger.debug(request.path)
    return getPageByIndex(p)


@app.route(r'/article/<articleID>')
# @cache.cached()
def article(articleID):
    '''显示单页文章'''
    postPath = app.config["POST_DIR"] + os.sep + \
        articleID.replace('.', '') + '.markdown'
    article = articleFileRender(postPath, True)
    return render_template("singleArticle.html", title=app.config['TITLE'], url=app.config['URL'], article=article)

@app.route(r'/users/<articleID>', methods=['POST'])
def showPrivateArticle(articleID):
    '''显示私密单页的文章'''
    app.logger.debug("showPrivateArticle begin")
    if not valid_password(request.form["password"]):
        error = 'Invalid password'
        app.logger.debug(error)
        return jsonify(result = error, isSuccess = 0)
    postPath = app.config["POST_DIR"] + os.sep + \
        articleID.replace('.', '') + '.markdown'
    article = articleFileRender(postPath, True)
    article['isPrivate'] = False
    return jsonify(content = article["content"], isSuccess = 1)

@app.route(r'/posts/<articleID>.txt')
@app.route(r'/posts/<articleID>')
def sourceArticle(articleID):
    '''显示单页文章Markdown原文'''
    postPath = app.config["POST_DIR"] + os.sep + \
        articleID.replace('.', '') + '.markdown'
    return send_file(createTmpTxtFile(postPath))


@app.errorhandler(404)
def notFound(e):
        # set 404 status
    return render_template("404.html"), 404


@app.route(r'/rss')
@cache.cached()
def RSSRender():
    f = open(app.config['RSS_PATH'], "r")
    return f.read()

if __name__ == '__main__':
    RSSMaker()
    app.run(debug = True)
