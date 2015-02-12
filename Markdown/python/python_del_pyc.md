#Python删除pyc文件

每次Python程序运行完之后，总会在各个模块中生成对应的.pyc文件，对我查看py文件时造成纷扰，遂想删之，若是在一个目录中，你可以使用`# rm -f *.pyc`来删除此目录下的pyc文件，若是多个目录，你也可以写一个makefile文件，然后执行`# make clean`进行删除。

那我想每次在Python程序**退出时自动删除pyc文件**该怎么办？想到应该可以使用Python代码来实现它，后通过网络资源整理如下：

>文件：rm_pycfile.py

>作用：删除此目录及其子目录中所有的pyc文件

>源码文件下载：[rm_pycfile.py]() （右键目标另存为…进行下载）

>源码：

    :::python
    #!/usr/bin/python
    # -*- coding: utf-8 -*-
    
    import os
    import fnmatch
    
    def FindFile(root, patterns='*',single=False, yield=False):
        """
        root:           需要遍历的目录
        patterns:       需要查找的文件，以；为分割的字符串
        single:         是否只遍历单层目录，默认为否
        yield:          是否包含目录本身，默认为否
        """
        patterns = patterns.split(';')
        for path, subdirs, files in os.walk(root):
            if yield:
                files.extend(subdirs)
            files.sort()
            for file in files:
                for pattern in patterns:
                    if fnmatch.fnmatch(file, pattern.strip()):
                        yield os.path.join(path, file)
            if single:
                break
    
    def RemovePycfile():
        for file in FindFile(os.getcwd(),'*.pyc'):
            print 'rm -f', file
            os.remove(file)
    
    if __name__ == '__main__':
        RemovePycfile()

##在Python程序中使用：

直接在Python程序的主进程中包含**RemovePycfile()**函数即可，如下方法进行包含

    :::python
    from rm_pycfile import RemovePycfile()

然后可直接在“主函数”中使用RemovePycfile()来进行删除所有的pyc文件了。

当然，你也可以使用它来删除其它类型的文件，相信你会很轻易的修改成你想要的。
