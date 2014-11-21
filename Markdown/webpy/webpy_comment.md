#webpy实现留言板功能

>系统环境：CentOS6.3, python2.6.6  
>数据库：MySQL

在网站基本文章的框架具备之后，想着是否应该加上一个评论/留言的功能。遂上网查之，资料基本上没有（或许是我没有找到），但明白了一点，肯定需要数据库的支持，我选择了 MySQL 数据库。

依照着我个人的理解，最终实现了它。我的思路如下：

1. 在用户提交表单（点击提交评论）的时候，程序获取用户提交内容并插入数据库
2. 在用户进入留言页面时，从数据库中读取该页面的评论内容并进行呈现

下述就对上述两点进行详细的解说：

##1. 在 python 中使用 MySQL，需要安装 MySQLdb 库

可参照我的另一篇文章： [《python中安装MySQLdb》](/python/python_mysqldb.html)

##2. 界面上的评论框

刚开始确实不知道评论框是用的什么标签，然后就随便去了一个有评论的网站，看了看页面源代码，原来是需要一个[HTML <textarea\> 标签](http://www.w3school.com.cn/tags/tag_textarea.asp)。后在我的代码中新建了一个评论模板，将<textarea\>标签加进去了。

##3. 表单的提交

在评论模板中可添加[HTML <form\> 标签](http://www.w3school.com.cn/tags/tag_form.asp)，后在python代码中可使用webpy的[web.input](http://webpy.org/cookbook/input.zh-cn)来接收用户数据。

##4. 支持 Markdown 语法

在通过 web.input 获取用户数据之后，对用户评论内容进行解析，以达到支持 Markdown 语法的目的。

    comment = markdown.markdown(comment, extensions=['markdown.extensions.extra'], safe_mode='escape')  ##将md转化为html

本来想着 Markdown 是支持 HTML 语法的，留言板支持了 Markdown 语法，不就是支持了 HTML 语法吗？

在刚开始我也是这么做的，同时支持解析 Markdown 语法和 HTML 语法；但就在今天（2014/11/20）我在网上看到这样一个评论：

>随随便便支持 HTML 的评论框不是好评论框

后来知道了原因： [XSS 漏洞](http://www.guokr.com/blog/442544/ "XSS 漏洞")

搜索了一下解决方法，发现 Python 中 Markdown 自带类似功能 [safe_mode](https://pythonhosted.org/Markdown/reference.html#safe_mode)。我选用的是`safe_mode='escape'`，将所有的 HTML 语法直接呈现，而不进行解析。

##5. 将用户评论内容存入数据库

在通过 web.input 获取用户数据之后，可直接将获取到的数据插入数据库了。以下我列出我存入数据库的内容，仅供参考：

    url，    记录此篇文章的url地址
    date，   记录评论的时间
    usrname，记录用户输入的昵称（这是页面上的一个<text>标签）
    usraddr，记录用户的地址（通过获取用户的ip地址，进而获取用户物理地址，方法请接着往下看）
    comment，用户评论的内容

ip 地址获取物理地址： [《ip定位》](/webpy/webpy_ip_locate.html)

##6. 读取数据库获取评论

在用户通过 url 打开此篇文章时，立即从数据库读取此 url 对应的评论，进行呈现即可。

##7. 在线 demo

webpy 留言板在线 demo，可直接访问我的[留言板](/about)，哈哈~

##8. 遗留问题

评论/留言暂不支持回复等功能，还未找到好的方法解决这个问题~
