#Python 制作 sitemap

在获取到站点的所有链接后（获取方法可参照[《小小爬虫》](http://www.qjwgg.com/webpy/webpy_spider.html)），想着应该可以用来制作站点的 [sitemap.xml](http://www.qjwgg.com/sitemap.xml "点击访问本站的 sitemap.xml") 了。

* 关于 sitemap 的介绍与相关规范，可访问其官网：[http://www.sitemaps.org/](http://www.sitemaps.org/)

搜索找到 [ApeSmit](https://pypi.python.org/pypi/apesmit/0.01) 可用。它的介绍为：

>simple Python module to create XML sitemaps

用法还是很简单的，代码示例如下：

    :::python
    #!/usr/bin/python
    # -*- coding: utf-8 -*-

    import urllib2
    import re
    import apesmit


    def create_sitemap(urllist):
        sm = apesmit.Sitemap(changefreq='weekly', lastmod='today')
        for url in urllist:
            sm.add(url)
        out = open('sitemap.xml', 'w')
        sm.write(out)
        out.close()


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

        print '-'*100
        urllist.sort()
        for url in urllist:
            print url

        create_sitemap(urllist)

效果可查看本站的 sitemap.xml: [http://www.qjwgg.com/sitemap.xml](http://www.qjwgg.com/sitemap.xml)
