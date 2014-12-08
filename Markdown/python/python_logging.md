#Python中使用logging

在Python中使用logging模块真的很方便，废话不多说。

下述是我记录的在Python代码中添加输出到**终端**和**文件**的logging用法。

###1. 源码示例：

    #!/usr/bin/python
    # -*- coding: utf-8 -*-

    import logging

    def log_test():

        FORMAT = '%(asctime)s %(filename)s[line:%(lineno)d][func:%(funcName)s] [%(levelname)s] %(message)s'

        ch = logging.StreamHandler()
        # fh = logging.FileHandler('test.log')
        fh = logging.handlers.RotatingFileHandler('test.log', maxBytes=10*1024*1024, backupCount=5)
        
        formatter = logging.Formatter(FORMAT)

        ch.setFormatter(formatter)
        fh.setFormatter(formatter)

        logging.getLogger('').addHandler(ch)
        logging.getLogger('').addHandler(fh)
        
        logging.getLogger('').setLevel(logging.INFO)  # 默认为WARNING等级

        logging.warning('python logging.')
        logging.error('hello, %s'%('logging.'))

    if __name__ == '__main__':
        log_test()

###2. 终端/文件输出如下：

    2014-10-28 11:43:23,986 py_log.py[line:21][func:log_test] [WARNING] python logging.
    2014-10-28 11:43:23,987 py_log.py[line:22][func:log_test] [ERROR] hello, logging.
    
###3. logging.Formatter的格式：
![](/static/img/py_logging_format.png)

[https://docs.python.org/2/library/logging.html#logrecord-attributes](https://docs.python.org/2/library/logging.html#logrecord-attributes)

###4. log文件大小限制：

当将log记录到文件时，若是服务程序，则必须要考虑log文件大小的问题。还好，Python中logging模块已经考虑到此问题了，直接就可支持使用。

我在上述代码示例中使用的是**RotatingFileHandler**类，它可指定文件大小与保存的份数。在上述代码示例中为保存5份，每份10M大小。

> 这个功能很像Linux系统中的logrotate服务，logrotate服务介绍请参考[《logrotate服务》](http://www.qjwgg.com/linux/linux_logrotate.html)

当然，除了上面以大小进行轮转的**RotatingFileHandler**类外，还有以时间进行轮转的**TimedRotatingFileHandler**类。

详细请参考[https://docs.python.org/2/library/logging.handlers.html](https://docs.python.org/2/library/logging.handlers.html)

###5. logging模块官网文档：
[https://docs.python.org/2/library/logging.html](https://docs.python.org/2/library/logging.html)
