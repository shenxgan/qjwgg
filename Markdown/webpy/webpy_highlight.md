#代码高亮

在网上搜索了一下，发现 highlight.js 进行代码高亮最为方便。官网：[https://highlightjs.org/](https://highlightjs.org/)

下载可直接去官网进行下载，可选择需要高亮的语言进行下载。

使用方法：
将 CSS 文件添加到 &lt;head&gt; 中，将 js 文件添加到页面底部 &lt;body&gt; 标签前面。

* 在 &lt;head&gt; 标签中添加
```html
    <link href="/static/highlight/styles/googlecode.css" rel="stylesheet">
```
* 在 &lt;body&gt; 标签前面添加
```html
    <script src="/static/highlight/highlight.pack.js"></script>
    <script >hljs.initHighlightingOnLoad();</script>
```
至此，已经实现了代码高亮，并看到了效果。现在就开始挑选一个你喜欢的 CSS 来对你的代码进行高亮吧！


***

###后续修改

个人认为 highlight.js 进行代码高亮效果不佳，遂改用了 [Pygments](http://pygments.org/) 

####使用方法：
1. 去 [github](https://github.com/richleland/pygments-css) 下载 css 文件（我使用的是 `emacs.css`）
2. 安装 Pygments

        :::bash
        pip install Pygments

3. 修改 Markdown 解析语句（添加了 `'markdown.extensions.codehilite'`）

        :::python
        html = markdown.markdown(md, extensions=['markdown.extensions.extra', 'markdown.extensions.codehilite'])

以上三步完成后即可看到代码高亮的效果了（有可能你还需要稍微修改一下你的 `blog.css`）

***

使用 highlight.js 和 Pygments 进行代码高亮的效果对比：（左边为 Pygments 代码高亮效果）

![](/static/img/highlight_pygments.png)

