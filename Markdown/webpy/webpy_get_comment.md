#webpy获取评论内容

##1. 原理

因为webpy在实现留言板的时候呢，是将用户的评论内容存入了数据库中，所以当需要呈现用户评论的时候就需要从数据库进行读取了。

在存入数据库的时候是使用文章的url作为表关键字的，所以从MD文件加载文章完成后（解析MD文件），紧接着就应该去加载用户评论了（读取数据库）。


##2. 实现方法

1. 读取数据库，获取评论内容
2. 创建了一个coment.html的模板（模板源码见下），用于呈现评论内容
3. 在article.html模板（普通文章的模板）中调用coment.html模板

comment.html模板的源码如下：

    $def with (article)

    <div class="blog-post">
        <div class="blog-comment">
            <p class="p1">评论列表</p>
            <hr></hr>
            $for comment_info in article['comment_list']:
                <div>
                    <p class="p2">$comment_info[2]（来自$comment_info[4]的网友）</p>
                    <p class="p3">$:comment_info[5]</p>
                    <p class="p2">$comment_info[1]</p>
                    <hr></hr>
                </div>
        </div>
    </div>

其中，article['comment_list']是从数据库中获取的此篇文章的所有的评论内容，在此模板中使用for循环来进行呈现。
    
    
##相关文章：
* [webpy实现留言板功能](/webpy/webpy_comment.html)
