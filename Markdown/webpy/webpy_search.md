#webpy实现查找功能

本节讲述web.py+Markdown的轻量小博客实现文章查找功能

先来说一说我这个博客的基础，文章内容是一个个的MD文件，在python端解析成html后供webpy进行调用呈现

所以，我的查找就会相对简单，思路如下：

1. 首先需要python实现从文件目录中进行查找字符串的功能（我是想直接从MD文件中进行查找关键字）
2. 查找到之后根据文章路径获取其对应唯一的url路径
3. 对查找到的关键字要进行高亮处理

最难的也是上述的第一步，但网上资料还是有的，可参考我随后整理的两篇文章：《python遍历目录》和《python在目录中查找字符串》

可点击网页右上角的这个图标![](http://www.qjwgg.com/static/img/menu_search.png)进入搜索页面：

![](/static/img/search_demo.png)
