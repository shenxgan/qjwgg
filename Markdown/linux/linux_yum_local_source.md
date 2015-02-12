#linux 配置本地 yum 源

    :::bash
    # 前提：需要连接上 ISO 文件
    # 在 CentOS6.3 上测试成功

    #!/bin/bash

    cd /etc/yum.repos.d/

    [ ! -d /media/cdrom ] && mkdir /media/cdrom
    [ ! -f CentOS-Media.repo.org ] && cp CentOS-Media.repo CentOS-Media.repo.org

    sed -i '/        file/d' CentOS-Media.repo
    sed -i 's/^baseurl=.*/baseurl=file:\/\/\/media\/cdrom\//' CentOS-Media.repo
    sed -i 's/^gpgcheck=.*/gpgcheck=0/' CentOS-Media.repo
    sed -i 's/^enabled=.*/enabled=1/' CentOS-Media.repo

    mv CentOS-Base.repo CentOS-Base.repo.org
    mv CentOS-Vault.repo CentOS-Vault.repo.org
    mv CentOS-Debuginfo.repo CentOS-Debuginfo.repo.org

    mount /dev/cdrw /media/cdrom
