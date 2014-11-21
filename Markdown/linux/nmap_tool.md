#nmap — 网络探测工具和安全/端口扫描器

官网地址：[http://nmap.org/](http://nmap.org/)  
Nmap参考指南(Man Page)：[http://nmap.org/man/zh/](http://nmap.org/man/zh/)  
下载地址：[http://nmap.org/dist/nmap-6.46-1.x86_64.rpm](http://nmap.org/dist/nmap-6.46-1.x86_64.rpm)  

##1. 扫描指定网段在线ip

    # nmap -sn -n 172.10.2.1/24

    -sn ping是否在线  
    -n 不进行DNS的解析，节约时间  
    /24 子网掩码，（ipv4地址32位，3*8=24，表明前三位为子网掩码。可参考C类网络地址） 
 
##2. 结果保存到文件

    # nmap -sn -n -oG iplist 172.10.3.1/24

##3. 指定ip范围

[http://nmap.org/man/zh/man-target-specification.html](http://nmap.org/man/zh/man-target-specification.html)

    # nmap -sn -n 172.10.2.1-254
    1-254主机

    # nmap -sn -n 172.10.2-4.1-254
    2-4网段，1-254主机

##4. 指定ip

[http://nmap.org/man/zh/man-performance.html](http://nmap.org/man/zh/man-performance.html)


    # nmap -sn -n -T5 172.10.2.2

    T5可显著提升速度