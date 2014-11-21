#linux配置samba

下述是我整理出的从安装到配置samba的最简步骤：

    # yum -y install samba
    # cp /etc/samba/smb.conf /etc/samba/smb.conf.bak
    # > /etc/samba/smb.conf
    # vim /etc/samba/smb.conf
    [home]
            comment = Public Stuff
            path = /home/
            public = yes
            writable = yes
            printable = no
            write list = +staff
    
    # service iptables stop
    # setenforce 0
    # smbpasswd -a root
    # service smb restart

至此，你应该可以在Windows端进行使用了。  
我一般习惯使用**Win+R**快捷键打开运行，然后在打开栏中填入”\\ip”，接着按回车即可。
***
下面就详细讲讲上述命令的作用：  
##1. 安装samba，在这里我使用的为yum命令进行安装

    # yum -y install samba

##2. 对samba的配置文件先进行备份

    # cp /etc/samba/smb.conf /etc/samba/smb.conf.bak

##3. 清空配置文件，以备进行编辑

    # > /etc/samba/smb.conf

##4. 编辑配置文件

    # vim /etc/samba/smb.conf
    文件内容为：
    [home]
           comment = Public Stuff
           path = /home/
           public = yes
           writable = yes
           printable = no
           write list = +staff

##5. 关闭防火墙

    # service iptables stop

##6. 临时关闭SELinux

    # setenforce 0

##7. 为samba添加一个root用户

    # smbpasswd -a root
    接着输入密码（自己随意）

##8. 启动samba服务

    # service smb restart