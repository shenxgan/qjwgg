#webpy 对查找的关键字进行高亮处理

在前两节的基础上，就可以将字段从目录中的文件里搜索出来了。

当搜索的字段从目录中查找到之后，想着是否应该对其做一个高亮处理。因为每每用 Crtl+F 在网页上进行搜索时，都会对搜索的结果进行一个高亮处理。

想到 MD 语法中支持书写 HTML 语法，并且最终在网页上呈现时都是要转换为 HTML 的，所以方法有了：

将查找到的字段放到一个[ <strong\> 标签](http://www.w3school.com.cn/tags/tag_strong.asp)中，并设置其颜色为红色 `style="color: red"`

    match = match.replace(key,'<strong style="color: red">%s</strong>' %(key))
    
很简单的操作，可点击右上角的搜索图标进行搜索查看效果。

**不足：**

感觉最大的不足就是当[ <code\> 标签](http://www.w3school.com.cn/tags/tag_code.asp)中存在搜索的字段时，高亮效果就会失效，并且 <strong\> 标签也会被显现出来。

还未找到好的方法去解决这个问题。