#Python 从文件中查找字符串

需求：使用 Python 从文件中查找指定的字符串

    :::python
    #!/usr/bin/python
    # -*- coding: utf-8 -*-

    import re

    def findstr(filepath, key):
        file = open(filepath, 'rb')
        buffer = file.read()

        for match in re.findall('\n.*'+key+'.*\n',buffer):
            print match
        file.close()

    if __name__ == '__main__':
        findstr('/root/test.md', 'key')
