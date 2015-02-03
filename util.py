#!/usr/bin/python
# -*- coding: utf-8 -*-

import web
import markdown
import codecs
import os
import urllib2
import json
import threading
import sys
import re
import qrcode
import time
import Image

from database import dbhandler


class ip2address(threading.Thread):
    def __init__(self, ip):
        threading.Thread.__init__(self)
        self.ip = ip
        self.count = 0
        self.setDaemon(True)
        self.start()

    def run(self):
        while True:
            self.count += 1
            usrip = self.ip
            '''
            首先可尝试从数据库进行读取

            sql = "select usraddr from comment where usrip='%s' limit 1" %(usrip)
            addr = dbhandler.select(sql)
            if addr[0] != '':
                usraddr = addr[0]
            '''
            addr = ip2addr(self.ip)
            if addr['country'] != '': ##查询到了结果
                usraddr = addr['country'] + addr['region'] + addr['city']
                sql = "update comment set usraddr='%s' where usrip='%s'" %(usraddr, usrip)
                dbhandler.execute(sql)
                break
            if self.count >= 5: ##限制最多去查询5次
                break

    def stop(self):
        pass


def ip2addr(ip):
    addr = {}
    addr['country'] = ''
    addr['region'] = ''
    addr['city'] = ''
    try:
        url = 'http://ip.taobao.com/service/getIpInfo.php?ip=%s' %(ip)
        print url
        data = urllib2.urlopen(url)
        addr_json = data.read()
        addr_dict = json.loads(addr_json)
        if addr_dict['code'] == 0:
            addr['country'] = addr_dict['data']['country']
            addr['region'] = addr_dict['data']['region']
            addr['city'] = addr_dict['data']['city']
    except Exception, e:
        print e
    finally:
        return addr


def md2html(md_file):

    input_file = codecs.open(md_file, mode='r', encoding='utf8')
    md = input_file.read()
    html = markdown.markdown(md, extensions=['markdown.extensions.extra'])
    input_file.close()

    return html


def url2article(url):

    article = {}
    article['download'] = False
    article['notfound'] = False
    article['usrip'] = web.ctx.ip

    if url.split('/')[2] == 'comment.html':
        urldata = web.input()
        url = urldata.url

        usrname = urldata.usrname
        comment = urldata.comment

        if usrname != '' and comment != '':
            usrip = article['usrip']
            usraddr = u'火星'

            comment = markdown.markdown(comment, extensions=['markdown.extensions.extra'], safe_mode='escape')  ##将md转化为html
            sql = "insert into comment values ('%s','%s',NOW(),'%s','%s','%s','%s')" %(0, url, usrname, usrip, usraddr, comment)
            sql = sql.encode('utf-8')
            print sql
            dbhandler.execute(sql)
            upaddr = ip2address(usrip)

        raise web.seeother(url)

    name = url.split('/')[2].replace('.html', '')
    md_path = 'Markdown'+url.replace('.html', '.md')

    if url == '/about/':
        md_path = 'Markdown/about.md'

    article['url'] = url  # '/linux/linux_ntp.html'
    article['name'] = name
    article['md_path'] = md_path

    if os.path.isfile(md_path) is True:
        if url != '/about/' and url.split('.')[1] == 'md':  #下载md文件
            fh = open(md_path)
            web.header("Content-Type","text;charset=utf-8")
            web.header("Content-Disposition", "attachment;filename=%s" %(article['name']))
            article['download'] = True
            article['stream'] = fh.read()
            fh.close()
        else:
            html = md2html(md_path)
            html_info = html.split('<h1>', 1)
            html_info = html_info[1].split('</h1>', 1)
            title = html_info[0]
            #category = 'linux'
            content = html
            article['title'] = title
            article['content'] = content
            article['md_name'] = name+'.md'

            ## 从数据库读取评论列表
            sql = "select * from comment where url='%s' order by id" %(article['url'])
            comment_list = dbhandler.select(sql)
            article['comment_list'] = []

            for comment_info in comment_list:
                dict = {}
                dict['id']       = comment_info[0]
                dict['url']      = comment_info[1]
                dict['date']     = comment_info[2]
                dict['usrname']  = comment_info[3]
                dict['usrip']    = comment_info[4]
                dict['usraddr']  = comment_info[5]
                dict['comment']  = comment_info[6]
                article['comment_list'].append(dict)
    else:
        article['notfound'] = True
        article['title'] = '404 Not Found'
        article['content'] = '404 Not Found'

    return article


def findstr(filepath, key):
    file = open(filepath, 'rb')
    title = ''
    while True:
        line = file.readline()
        if line.find('#') != -1:
            title = line.replace('\n','').replace('#','')
            break
    text = ''
    buffer = file.read()

    for match in re.findall('\n.*'+key+'.*\n',buffer):
        html = filepath.split('/',2)[2].replace('md','html')
        if html.find('index.html') == -1:
            match = match.replace(key,'<strong style="color: red">%s</strong>' %(key))
            text += match
    if text != '':
        text = '#[%s](%s)\n%s' %(title, html, text)
        #text += '\n<br><br>\n***\n'
    file.close()
    return text


def traversal_path(path, key):
    alltext = ''
    for root, dirs, files in os.walk(path):
        if root.find('.svn') == -1:
            for file in files:
                file = os.path.join(root, file)
                if file != './Markdown/webpy/catalog.md':
                    text = findstr(file, key)
                    if text != '':
                        alltext += text

    alltext = alltext.decode('utf-8')
    html = markdown.markdown(alltext, extensions=['markdown.extensions.extra'])
    return html


def text2qrcode(text, isicon, img_name):
    qr = qrcode.QRCode(
        version=4,
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=5,
        border=1,
    )
    qr.add_data(text)
    qr.make(fit=True)

    img = qr.make_image()

    if isicon is True:
        img = img.convert("RGBA")
        icon = Image.open("./static/img/qrcode.ico")

        img_w, img_h = img.size
        factor = 4
        size_w = int(img_w / factor)
        size_h = int(img_h / factor)

        icon_w, icon_h = icon.size
        if icon_w > size_w:
            icon_w = size_w
        if icon_h > size_h:
            icon_h = size_h
        icon = icon.resize((icon_w, icon_h), Image.ANTIALIAS)

        w = int((img_w - icon_w) / 2)
        h = int((img_h - icon_h) / 2)
        img.paste(icon, (w, h))

    imgname = './static/img/qrcode/%s.png'%(img_name)
    img.save(imgname)

    # 1. 保留最近2小时之内的；2. 保留最近的100张；（可根据文件名算出时间间隔）

if __name__ == '__main__':
    md2html('test/syntax.md')
