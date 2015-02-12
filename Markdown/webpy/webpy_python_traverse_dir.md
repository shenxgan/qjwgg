#Python 遍历目录

需求：使用 Python 遍历指定目录内的所有文件

先来看看代码示例：

    :::python
    #!/usr/bin/python
    # -*- coding: utf-8 -*-

    import os

    def traversal_path(path):
        for root, dirs, files in os.walk(path):
            for file in files:
                file = os.path.join(root, file)
                print file

    if __name__ == '__main__':
        traversal_path('./')

官网参考：[https://docs.python.org/2/library/os.html#os.walk](https://docs.python.org/2/library/os.html#os.walk)
