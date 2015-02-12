#webpy 下载文件

需求：在文章中可点击链接进行下载服务器上的文件

若是 http 服务器的话，可以直接链接文件的路径即可进行下载；但发现在 webpy 上却行不通。  
虽然 webpy 有一个指定的 static 目录可以直接进行下载，但是若是其它目录呢？

网上搜索了一下，查到一种方法：

    :::python
    web.header("Content-Type","text;charset=utf-8")
    web.header("Content-Disposition", "attachment;filename=%s" %(filename))

每篇文章正文末尾处的**“本文MD文件下载”**即为此种方法实现的。

注：此方法仅适用于小文件（估摸着要小于 200M ？具体没有进行测试）。要下载超大的文件请自行上网搜索。
