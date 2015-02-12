#linux 一键配置安装 samba 脚本

    :::bash
    # 需要先可使用 yum 进行软件的安装
    # 在 CentOS6.3 上测试成功

    #!/bin/bash

    SMB_CONF='/etc/samba/smb.conf'
    ROOT_PASSWD='123'

    yum -y install samba
    [ $? -ne 0 ] && exit

    [ ! -f $SMB_CONF.org ] && cp $SMB_CONF $SMB_CONF.org
    > $SMB_CONF
    cat > $SMB_CONF << EOF
    [home]
        comment = Public Stuff
        path = /home/
        public = yes
        writable = yes
        printable = no
        write list = +staff
    EOF

    service iptables stop
    setenforce 0
    echo -e $ROOT_PASSWD\\n$ROOT_PASSWD | smbpasswd -as root
    service smb restart
