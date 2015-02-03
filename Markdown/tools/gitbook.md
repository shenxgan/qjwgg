#GitBook

**类别：**特色工具  
**用途：**电子书制作  
**官网：**[https://www.gitbook.com/](https://www.gitbook.com/)

![](/static/img/tools/gitbook.png)

###先来看看 GitBook 的介绍：

> GitBook is a command line tool (and Node.js library) for building beautiful books using GitHub/Git and Markdown.

![](/static/img/tools/gitbook_webpy.png)

###安装

使用 npm 来安装 gitbook.

* 下载安装 npm, 下载地址：[http://nodejs.org/download/](http://nodejs.org/download/)
* 安装 gitbook

        npm install gitbook -g

###使用

gitbook 需要两个基本文件：README.md 和 SUMMARY.md

* `README.md` 为书的介绍
* `SUMMARY.md` 为书的目录，示例如下（注意格式）

        * [教程简介](webpy/index.md)
        * [文章结构](webpy/webpy_article_structure.md)
            * [获取标题](webpy/webpy_get_title.md)
            * [获取评论](webpy/webpy_get_comment.md)
            * [webpy 下载文件](webpy/webpy_download_file.md)
            * [404 Not Found](webpy/webpy_404_not_found.md)
            * [代码高亮](webpy/webpy_highlight.md)
        * [Markdown解析](webpy/webpy_md2html.md)
            * [普通语法](webpy/webpy_markdown_syntax.md)
            * [Python Markdown扩展](webpy/webpy_markdown_extra.md)
        * [留言板功能](webpy/webpy_comment.md)
            * [ip定位](webpy/webpy_ip_locate.md)
            * [页面表单提交](webpy/webpy_form_submit.md)
        * [搜索功能](webpy/webpy_search.md)
            * [Python 遍历目录](webpy/webpy_python_traverse_dir.md)
            * [Python 从文件中查找字符串](webpy/webpy_python_search_string.md)
            * [对查找的关键字进行高亮处理](webpy/webpy_highlight_str.md)
        * [爬虫]()
            * [小小爬虫](webpy/webpy_spider.md)
            * [Python 制作 sitemap](webpy/webpy_sitemap.md)


* `gitbook serve -p 8000 .`
    
    * gitbook 首先把你的 Markdown 文件编译为 HTML 文件，并根据 SUMMARY.md 生成书的目录。

    * 所有生成的文件都保存在当前目录下的一个名为 _book 的子目录中。

    * 完成这些工作后，gitbook 会作为一个 HTTP Server 运行，并在你指定的端口（8000）监听 HTTP 请求。

接下来，就用浏览器进行访问吧：http://localhost:8000

###参考

* [http://www.ituring.com.cn/article/127645](http://www.ituring.com.cn/article/127645)
* [https://github.com/GitbookIO/gitbook](https://github.com/GitbookIO/gitbook)

