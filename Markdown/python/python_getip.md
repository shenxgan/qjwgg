#Python 获取本机 ip

    :::python
    #!/usr/bin/python
    # -*- coding: utf-8 -*-

    import socket


    def get_ip():
        try:
            csock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            csock.connect(('8.8.8.8', 80))
            (addr, port) = csock.getsockname()
            csock.close()
            return addr
        except socket.error:
            return "127.0.0.1"


    if __name__ == '__main__':
        print get_ip()
