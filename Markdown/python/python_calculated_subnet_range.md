#通过 ip 和子网掩码计算出子网范围

    #!/usr/bin/python
    # -*- coding: utf-8 -*-

    import ctypes


    def nd(ip, nm):
        ip1 = ip.split(".")
        nm1 = nm.split(".")
        begin = [str(int(i) & int(m)) for i, m in map(None, ip1, nm1)]
        end = [str(int(i) | ctypes.c_ubyte(~int(m)).value) for i, m in map(None, ip1, nm1)]
        begin = '.'.join(begin)
        end = '.'.join(end)
        return begin, end


    if __name__ == '__main__':
        ip = '172.10.2.24'
        nm = '255.255.255.0'
        begin, end = nd(ip, nm)
        print begin,end
