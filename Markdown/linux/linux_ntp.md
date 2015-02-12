#linux搭建NTP

    :::bash
    yum -y install ntp
    vim /etc/ntp.conf
        restrict 172.10.2.0 mask 255.255.255.0 nomodify notrap
        server 127.127.1.0
        fudge 127.127.1.0 stratum 10


**客户端同步时间：**

    :::text
    ntpdate 172.10.2.24

**注意**系统时区，上述仅同步时间，并未更改时区。
