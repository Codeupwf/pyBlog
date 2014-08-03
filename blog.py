import os
import codecs
import datetime
import PyRSS2Gen
import markdown
from flask import Flask, request, g, redirect, url_for, abort, \
    render_template, flash, Markup

# configuration
DEBUG = True
TITLE = 'Wang Fu'
URL = 'http://blog.wangfu.info'
POST_DIR = os.path.dirname(os.path.abspath(__file__)) + os.sep + 'posts'
RSS_PATH = os.path.dirname(os.path.abspath(__file__)) + os.sep + 'rss.xml'

# create app
app = Flask(__name__)
app.config.from_object(__name__)
app.config.from_envvar('SETTINGS', silent=True)

def articleFileRender(filePath):
    f = codecs.open(filePath, mode='r', encoding='utf-8')
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
            title = line.replace('title: "', '')[0:-2]
        if line.find('date: ') == 0:
            date = line.replace('date: ', '')[0:-1]
        if line.find('---') == 0:
            break
    content = u''
    for line in lines[index:]:
        content += line
    if title:
        ret['title'] = title
        ret['date'] = date
        ret['content'] = Markup(markdown.markdown(content,extensions=['codehilite(guess_lang=False)','fenced_code']))
        ret['name'] = filePath.split(os.sep)[-1].split('.')[0]
    return ret


def RSSMaker():
    articles = []
    postDir = app.config["POST_DIR"]
    fileList = []
    files = os.listdir(postDir)
    for f in files:
        fileList.append(postDir + os.sep + f)
    fileList.sort(reverse=True)
    for singleFile in fileList:
        article = articleFileRender(singleFile)
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


@app.route(r'/', methods=['GET'])
def index():
    articles = []
    postDir = app.config["POST_DIR"]
    fileList = []
    files = os.listdir(postDir)
    p = int(request.args.get('p', '0'))
    for f in files:
        fileList.append(postDir + os.sep + f)
    fileList.sort(reverse=True)
    for singleFile in fileList[p:p + 3]:
        article = articleFileRender(singleFile)
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
    return render_template("index.html", title=app.config['TITLE'], url=app.config['URL'], articles=articles, prev=prev, pnext=pnext, prevnum=p - 3, nextnum=p + 3)


@app.route(r'/article/<articleID>')
def article(articleID):
    postPath = app.config["POST_DIR"] + os.sep + \
        articleID.replace('.', '') + '.markdown'
    article = articleFileRender(postPath)
    return render_template("article.html", title=app.config['TITLE'], url=app.config['URL'], article=article)


@app.errorhandler(404)
def notFound(e):
        # set 404 status
    return render_template("404.html"), 404


@app.route(r'/rss')
def RSSRender():
    f = open(app.config['RSS_PATH'], "r")
    return f.read()

if __name__ == '__main__':
    RSSMaker()
    #app.run()
