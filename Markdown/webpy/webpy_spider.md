#小小爬虫

先贴代码：

    :::python
    #!/usr/bin/python
    # -*- coding: utf-8 -*-

    import urllib2
    import re


    def get_url_from_html(url, urllist):
        try:
            response = urllib2.urlopen(url, timeout=2)
            html = response.read()

            relink = '<a href=(.*?)>.*?</a>'
            url_list = re.findall(relink,html)
            for url in url_list:
                url = url.split(' ',1)[0].strip('"')
                if url[0:21] == urllist[0]:
                    if url not in urllist:
                        print url, '---'
                        urllist.append(url)
                        get_url_from_html(url, urllist)

        except Exception, e:
            print 'catch a exception:', e


    if __name__ == '__main__':

        urllist = []
        initial_url = 'http://www.qjwgg.com/'
        urllist.append(initial_url)

        get_url_from_html(initial_url, urllist)

        print '-'*50
        urllist.sort()
        for url in urllist:
            print url


写这个呢，是因为最近想在网站上添加 sitemap 和 rss 功能。Google 后，明白两者都需要知道站点的所有文章链接。

后来又想到，知道了所有的文章链接，那不是可以根据链接，获取文章内容，我就可以改进**[搜索](http://www.qjwgg.com/search)**功能了。

然后，就有了前面的代码实现，原理比较简单：

1. 首先抓取出首页中的所有链接；
2. 再依次遍历首页中的链接，抓取出链接中的链接...

选择了递归实现，就是文章开头贴出的代码。


其中一次（2014/12/02）的运行结果如下：

    :::bash
    http://www.qjwgg.com/search ---
    http://www.qjwgg.com/qrcode ---
    http://www.qjwgg.com/publish ---
    http://www.qjwgg.com/webpy ---
    http://www.qjwgg.com/webpy/index.html ---
    http://www.qjwgg.com/webpy/webpy_article_structure.html ---
    http://www.qjwgg.com/webpy/webpy_get_title.html ---
    http://www.qjwgg.com/webpy/webpy_get_comment.html ---
    http://www.qjwgg.com/webpy/webpy_download_file.html ---
    http://www.qjwgg.com/webpy/webpy_404_not_found.html ---
    http://www.qjwgg.com/webpy/webpy_highlight.html ---
    http://www.qjwgg.com/webpy/webpy_md2html.html ---
    http://www.qjwgg.com/webpy/webpy_markdown_syntax.html ---
    http://www.qjwgg.com/webpy/webpy_markdown_extra.html ---
    http://www.qjwgg.com/webpy/webpy_comment.html ---
    http://www.qjwgg.com/webpy/webpy_ip_locate.html ---
    http://www.qjwgg.com/webpy/webpy_form_submit.html ---
    http://www.qjwgg.com/webpy/webpy_search.html ---
    http://www.qjwgg.com/webpy/webpy_python_traverse_dir.html ---
    http://www.qjwgg.com/webpy/webpy_python_search_string.html ---
    http://www.qjwgg.com/webpy/webpy_highlight_str.html ---
    http://www.qjwgg.com/python/python_mysqldb.html ---
    http://www.qjwgg.com/linux/linux_svn.html ---
    http://www.qjwgg.com/python ---
    http://www.qjwgg.com/python/python_del_pyc.html ---
    http://www.qjwgg.com/python/python_smtp.html ---
    http://www.qjwgg.com/python/python_logging.html ---
    http://www.qjwgg.com/linux/linux_logrotate.html ---
    http://www.qjwgg.com/python/python_qrcode.html ---
    http://www.qjwgg.com/linux ---
    http://www.qjwgg.com/linux/linux_ip.html ---
    http://www.qjwgg.com/linux/linux_ntp.html ---
    http://www.qjwgg.com/linux/linux_samba.html ---
    http://www.qjwgg.com/linux/mysql_basic_op.html ---
    http://www.qjwgg.com/linux/mysql_advanced_op.html ---
    http://www.qjwgg.com/linux/nmap_tool.html ---
    http://www.qjwgg.com/linux/linux_rsyslog.html ---
    http://www.qjwgg.com/linux/mysql_regularly_delete.html ---
    --------------------------------------------------
    http://www.qjwgg.com/
    http://www.qjwgg.com/linux
    http://www.qjwgg.com/linux/linux_ip.html
    http://www.qjwgg.com/linux/linux_logrotate.html
    http://www.qjwgg.com/linux/linux_ntp.html
    http://www.qjwgg.com/linux/linux_rsyslog.html
    http://www.qjwgg.com/linux/linux_samba.html
    http://www.qjwgg.com/linux/linux_svn.html
    http://www.qjwgg.com/linux/mysql_advanced_op.html
    http://www.qjwgg.com/linux/mysql_basic_op.html
    http://www.qjwgg.com/linux/mysql_regularly_delete.html
    http://www.qjwgg.com/linux/nmap_tool.html
    http://www.qjwgg.com/publish
    http://www.qjwgg.com/python
    http://www.qjwgg.com/python/python_del_pyc.html
    http://www.qjwgg.com/python/python_logging.html
    http://www.qjwgg.com/python/python_mysqldb.html
    http://www.qjwgg.com/python/python_qrcode.html
    http://www.qjwgg.com/python/python_smtp.html
    http://www.qjwgg.com/qrcode
    http://www.qjwgg.com/search
    http://www.qjwgg.com/webpy
    http://www.qjwgg.com/webpy/index.html
    http://www.qjwgg.com/webpy/webpy_404_not_found.html
    http://www.qjwgg.com/webpy/webpy_article_structure.html
    http://www.qjwgg.com/webpy/webpy_comment.html
    http://www.qjwgg.com/webpy/webpy_download_file.html
    http://www.qjwgg.com/webpy/webpy_form_submit.html
    http://www.qjwgg.com/webpy/webpy_get_comment.html
    http://www.qjwgg.com/webpy/webpy_get_title.html
    http://www.qjwgg.com/webpy/webpy_highlight.html
    http://www.qjwgg.com/webpy/webpy_highlight_str.html
    http://www.qjwgg.com/webpy/webpy_ip_locate.html
    http://www.qjwgg.com/webpy/webpy_markdown_extra.html
    http://www.qjwgg.com/webpy/webpy_markdown_syntax.html
    http://www.qjwgg.com/webpy/webpy_md2html.html
    http://www.qjwgg.com/webpy/webpy_python_search_string.html
    http://www.qjwgg.com/webpy/webpy_python_traverse_dir.html
    http://www.qjwgg.com/webpy/webpy_search.html
