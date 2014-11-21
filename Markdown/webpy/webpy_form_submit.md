#页面表单提交

表单提交主要是运用在评论提交的时候。

使用了 html 中 [<form\> 标签的 action 属性](http://www.w3school.com.cn/tags/att_form_action.asp)

    <form action="comment.html">
        ...
    </form>

在提交后你也许会用到

    web.input()
    和
    raise web.seeother(url)

前者获取表单提交的内容，后者进行跳转。
