#Subversion

**类别：**常用软件  
**用途：**代码管理  
**官网：**[http://subversion.apache.org/](http://subversion.apache.org/)

![](http://subversion.apache.org/images/svn-square.jpg)
![](http://subversion.apache.org/images/svn-name-banner.jpg)

###官网介绍

> Subversion is an open source version control system.

###使用

* Windows 上一般使用 [TortoiseSVN](http://tortoisesvn.net/index.zh.html)

    > TortoiseSVN 无需使用 Subversion 命令行，是目前最方便的 Subversion 版本控制系统，其操作和使用非常直观和简洁。
    
    `TortoiseSVN` 用着确实很方便。

* Linux 上就需要使用一些命令（仅列出简单且常用的命令）了：

        svn co svn://192.168.0.100/qjwgg    # co=checkout 检出代码
        svn update                          # 更新代码
        svn add file                        # 添加新文件
        svn commit -m "commint info"        # 提交代码并书写日志
        
        
###类似软件

* [Git](http://git-scm.com/)
