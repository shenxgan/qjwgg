#Python安装MySQLdb库

>系统环境：CentOS6.3, Python2.6.6

1. 缺少MySQLdb库，下载安装MySQL-python，  
   下载地址：[https://pypi.python.org/pypi/MySQL-python](https://pypi.python.org/pypi/MySQL-python)

2. 若缺少setuptools库，  
   下载地址：[https://pypi.python.org/packages/source/s/setuptools/setuptools-5.4.2.zip](https://pypi.python.org/packages/source/s/setuptools/setuptools-5.4.2.zip)

3. 若缺少Python.h文件，下载安装python-devel
    
        # yum install python-devel

4. 可能还需要安装：

        # yum install mysql mysql-devel
        # yum install rpm-build gcc-c++

基本上有以上四步，MySQLdb库就可安装成功了。

**参考：**  
[http://blog.csdn.net/inte_sleeper/article/details/6556103](http://blog.csdn.net/inte_sleeper/article/details/6556103)