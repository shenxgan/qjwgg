#Markdown转换为html

Markdown下载地址：[https://pypi.python.org/pypi/Markdown](https://pypi.python.org/pypi/Markdown)

下述是**MD文件**转化为html的源码示例：

    :::python
    #!/usr/bin/python
    # -*- coding: utf-8 -*-

    import markdown
    import codecs

    def md2html(md_file):

        '''从文件读取出md格式文件流'''
        input_file = codecs.open(md_file, mode='r', encoding='utf8')
        md = input_file.read()

        #html = markdown.markdown(md) #对应普通语法解析
        html = markdown.markdown(md, extensions=['markdown.extensions.extra']) #对应扩展语法解析

        return html

    if __name__ == '__main__':
        md2html('test/syntax.md')

若是Markdown格式的字符串/文件流转化为html字符串的话，仅使用这一句即可：

    :::python
    html = markdown.markdown(md, extensions=['markdown.extensions.extra'])
