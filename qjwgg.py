#!/usr/bin/python
# -*- coding: utf-8 -*-

import web
import os
import cgi
import random
import time

import util
from database import dbhandler


web.config.debug = False

LINUX_URL = '/linux'
PYTHON_URL = '/python'
WEBPY_URL = '/webpy'


dbhandler.connect()
cgi.maxlen = 1 * 1024 * 1024 # 1MB

urls = (
    '/?', 'index',
    LINUX_URL + '(.*)', 'linux',
    PYTHON_URL + '(.*)', 'python',
    WEBPY_URL + '(.*)', 'webpy',
    '/search' + '(.*)', 'search',
    '/about' + '(.*)', 'about',
    '/publish' + '(.*)', 'publish',
    '/qrcode' + '(.*)', 'qrcode',
    '(.+)', 'other',
)

render = web.template.render('templates', cache=False)
web.template.Template.globals['render'] = render

class index:
    def GET(self):
        html = util.md2html('./README.md')
        return render.index(html)

class linux:
    def GET(self, url):
        if url == '' or url == '/':
            url = '/index.html'
        url = LINUX_URL + url

        article = util.url2article(url)

        if article['download'] is True:
            return article['stream']
        elif article['notfound'] is True:
            return render.error(article)
        else:
            return render.article(article)

class python:
    def GET(self, url):
        if url == '' or url == '/':
            url = '/index.html'
        url = PYTHON_URL + url

        article = util.url2article(url)

        if article['download'] is True:
            return article['stream']
        elif article['notfound'] is True:
            return render.error(article)
        else:
            return render.article(article)

class webpy:
    def GET(self, url):

        if url == '' or url == '/':
            url = '/index.html'
        url = WEBPY_URL + url

        article = util.url2article(url)

        if article['download'] is True:
            return article['stream']
        elif article['notfound'] is True:
            return render.error(article)
        else:
            article['catalog'] = util.md2html('Markdown/webpy/catalog.md')
            return render.article_webpy(article)

class search:
    def GET(self, url):
        article = {}
        article['title'] = 'search'
        html = ''
        key = ''
        x = web.input()
        key = x.get('key', '')
        if key != '':
            key = key.encode('utf-8')
            html = util.traversal_path('./Markdown', key)

        article['content'] = html
        return render.search(article)

class about:
    def GET(self, url):
        article = {}
        article['url'] = '/about/'
        article['title'] = 'about'

        sql = "select * from comment where url='%s' order by date" %(article['url'])
        comment_list = dbhandler.select(sql)
        article['comment_list'] = comment_list
        article['md_name'] = './Markdown/about.md'
        html = util.md2html(article['md_name'])
        article['content'] = html
        return render.about(article)

class publish:
    def GET(self, url):
        file = open('./Markdown/markdown_online.md', 'rb')
        md = file.read()
        file.close()
        return render.publish(md)

class qrcode:
    def GET(self, url):
        article = {}
        article['img'] = ''
        article['text'] = ''
        article['img_name'] = 0
        return render.qrcode(article)

    def POST(self, url):
        article = {}
        isicon = False
        article['img_name'] = time.time()
        try:
            x = web.input(myfile={})
        except ValueError:
            return "File too large!"

        text = x.get('text', '')
        myfile = x.get('myfile', '')

        if text == '':
            raise web.seeother('')
        else:
            if myfile != '' and myfile.filename != '':

                filename = myfile.filename
                if filename.endswith('.ico') or filename.endswith('.jpg') or filename.endswith('.png') or filename.endswith('.bmp'):
                    fout = open('./static/img/qrcode.ico','w')
                    fout.write(myfile.file.read())
                    fout.close()
                    isicon = True
                else:
                    return 'Unsupported image formats!'
            img_name = article['img_name']
            util.text2qrcode(text, isicon, img_name)
            article['text'] = text
            article['img'] = '<img src="/static/img/qrcode/%s.png"/>'%(img_name)

            return render.qrcode(article)

class other:
    def GET(self, url):
        article = {}
        article['title'] = '404 Not Found'
        article['content'] = '404 Not Found'
        return render.error(article)

if __name__ == "__main__":
    app = web.application(urls, globals())
    app.run()

