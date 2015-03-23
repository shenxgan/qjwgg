#Python with 简述

>with 语句适用于对资源进行访问的场合，确保不管使用过程中是否发生异常都会执行必要的“清理”操作，释放资源，比如文件使用后自动关闭、线程中锁的自动获取和释放等。

先看看代码示例：
```python
#!/usr/bin/python
# -*- coding: utf-8 -*-


class context_expression:
    def __enter__(self):
        print "i'm in __enter__"
        return 100

    def __exit__(self, type, value, traceback):
        print "i'm in __exit__"


with context_expression():
    print "i'm in with"

with context_expression() as value:
    print "i'm in with as"
    print value
```

输出为：
```text
i'm in __enter__
i'm in with
i'm in __exit__
i'm in __enter__
i'm in with as
100
i'm in __exit__
```

![](http://www.qjwgg.com/static/img/python/python_with.png)

###参考

* [http://www.ibm.com/developerworks/cn/opensource/os-cn-pythonwith/](http://www.ibm.com/developerworks/cn/opensource/os-cn-pythonwith/)
* [http://zhoutall.com/archives/325](http://zhoutall.com/archives/325)