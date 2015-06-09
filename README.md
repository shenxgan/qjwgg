#[qjwgg](http://www.qjwgg.com/ "请叫我古怪") -- web.py 搭建的轻量级博客

*注意：*

> *http://www.qjwgg.com*域名已经不再使用了。

##简要介绍

web.py 实现的简易 blog，webpy 用来搭建框架，Markdown 用来书写内容。

在 webpy + Markdown 的基础上也做了一些有趣的东西：

1. 在线生成二维码 [**demo**](http://www.qjwgg.com/qrcode)
2. Markdown 在线解析 [**demo**](http://www.qjwgg.com/publish)

##安装必要环境

下述安装步骤是在 CentOS6.3 Python2.6.6 中进行的，供参考

    :::bash
    wget https://bootstrap.pypa.io/get-pip.py --no-check-certificate
    python get-pip.py

    pip install web.py
    pip install Markdown==2.4  # 注意版本
    pip install qrcode
    pip install Pygments  # 使用 Pygments 进行代码高亮

    yum install gcc gcc-c++
    yum install python-devel
    yum install libjpeg libjpeg-devel  # 使得 PIL 支持 jpeg 格式
    pip install PIL --allow-external PIL --allow-unverified PIL

    yum install mysql mysql-server
    yum install mysql-devel
    pip install MySQL-python

    service mysqld start
    mysqladmin -uroot password "password"  # 设置 mysql 密码
    mysql -uroot -ppassword < doc/qjwgg.sql  # 导入 sql 文件，创建数据库和相关表格

##运行

在得到[源码](https://github.com/qjwgg/qjwgg "GitHub 项目主页")后直接运行 qjwgg.py 即可：

    :::bash
    ./qjwgg.py 80

后台运行可使用

    :::bash
    nohup ./qjwgg.py 80 &

##代码结构

以下仅仅列出了代码的两级结构，相信已足够说明此博客的结构了。

    :::bash
    tree -L 2 -C
    .
    ├── database.py                 #数据库操作接口，若使用 web.py 自带的数据库操作则可不用这个
    ├── doc                         #数据库创建的 sql 语句
    │   └── qjwgg.sql
    ├── Makefile                    #用来清除 .pyc 文件
    ├── Markdown                    #MD 文件存放目录
    │   ├── about.md                #About 页面
    │   ├── linux                   #Linux 类文章
    │   ├── markdown_online.md      #Markdown 在线解析中的语法介绍
    │   ├── python                  #Python 类文章
    │   ├── tools                   #Tools 类文章
    │   └── webpy                   #web.py + Markdown 教程
    ├── qjwgg.py                    #程序入口，进行 URL 分发并启动博客系统
    ├── README.md                   #Home 页面
    ├── robots.txt                  #robots.txt 文件
    ├── sitemap.xml                 #站点地图
    ├── static                      #存放静态文件目录，web.py 框架的要求
    │   ├── css
    │   ├── fonts
    │   ├── highlight               #用于代码高亮
    │   ├── img
    │   └── js
    ├── templates                   #模板库
    │   ├── about.html              #About 页面
    │   ├── article.html            #普通的文章模板
    │   ├── article_webpy.html      #web.py + Markdown 教程模板
    │   ├── comment.html            #评论系统模板
    │   ├── error.html              #404 not found 模板
    │   ├── index.html              #首页模板
    │   ├── layout                  #布局模板
    │   ├── post_comment.html       #评论框模板
    │   ├── publish.html            #在线 Markdown 解析模板
    │   ├── qrcode.html             #在线生成二维码模板
    │   ├── search.html             #搜索模板
    │   ├── tools.html              #Tools 页面模板
    │   └── tools_index.html        #Tools 首页模板
    └── util.py                     #用于博客后台逻辑实现

    14 directories, 22 files

截图如下：

![](http://www.qjwgg.com/static/img/qjwgg_tree.png "qjwgg 代码结构图")


##流程

从输入 URL 到文章的呈现，最基本的流程如下：

1. url 分发到相对应的类执行 GET 或 POST 操作
2. 根据 url 获取其 MD 文件地址
3. 调用相应模板进行呈现 MD 文件内容

在后段时间，我添加了简易留言板和文章搜索的功能


##发布一篇新文章

在此博客系统中，发布一篇新的文章，要改动的地方有两处：

1. 添加新 MD 文件
2. 在 MD 文件所属文章类型中（相对应类型目录中的 index.md 文件）添加其链接

当然，也曾经见到过使用 pyinotify 监控文件/文件夹变化来实现文章的自动发布

##教程

可参考本站教程：[《webpy+Markdown 教程》](http://www.qjwgg.com/webpy)
