#Python Markdown扩展

我使用Markdown扩展语法的情况有两个：

1. 绘制表格
2. 指定代码所使用的语言，用于代码高亮

比如指定代码语言为Python时可这样使用：

\```python  
  
  【代码】  
  
\```

在Python中进行解析Markdown扩展语法，需要进行指定。

    markdown.markdown(md, extensions=['markdown.extensions.extra'])

详细可参考我的另一篇文章：[《Markdown转换为html》](/webpy/webpy_md2html.html)

下图是在官网教程截取的有关扩展的表格。  
我想要两个（表格和指定代码语言）都支持，所以使用的是**markdown.extensions.extra**，对应下图中的第一行。

![](/static/img/py_md_extra.png)


###参考

Python Markdown 提供的扩展：  
[https://pythonhosted.org/Markdown/extensions/index.html](https://pythonhosted.org/Markdown/extensions/index.html)


