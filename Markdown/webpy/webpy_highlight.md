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
