#ReviewBoard 系统的搭建

> 搭建平台: CentOS6.3  
> 官网：[https://www.reviewboard.org/](https://www.reviewboard.org/)


###1. 搭建步骤：

    # yum -y install mysql mysql-server
    # yum -y install httpd
    # yum -y install sendmail
    # yum -y install ReviewBoard

    # service mysqld start
    # service httpd start
    # service sendmail start

    # mysqladmin -u root password "password"
    # mysql -u root -p
        > create database reviewboard default charset utf8 collate utf8_general_ci;

    # rb-site install /var/www/reviews.example.com
        Domain Name: 172.10.3.25
        Root Path [/]: （回车）
        Shipped Media URL [static/]: （回车）
        Uploaded Media URL [media/]: （回车）
        Database Type: 1/mysql（输入1或者 mysql，下同）
        Database Name [reviewboard]: （回车）
        Database Server [localhost]: （回车）
        Database Username: root
        Database Password: *****（mysql 数据库 root 用户密码）
        Confirm Database Password [*****]: （回车）
        Cache Type: 1/memcached
        Memcache Server [localhost:11211]: （回车）
        Web Server: 1/apache
        Python Loader: 1/wsgi
        Username [admin]: （回车）
        Password: *****（此密码为 reviewboard 的管理员登陆密码）
        Confirm Password [*****]: （回车）
        E-Mail Address: ***@***.com

    # 更改文件拥有者为apache（web 服务器）（在 site 创建完成时，会提示做如下更改）
    # chown -R apache /var/www/reviews.example.com/htdocs/media/uploaded
    # chown -R apache /var/www/reviews.example.com/htdocs/media/ext/
    # chown -R apache /var/www/reviews.example.com/data/
    # cp /var/www/reviews.example.com/conf/apache-wsgi.conf /etc/httpd/conf.d

    # vim /etc/httpd/conf/httpd.conf
        ...
        <Directory />
            Options FollowSymLinks
            AllowOverride None
            Allow from all（添加部分）
        </Directory>
        ...
    # setenforce 0
    # 开启80端口，以便其他主机能够访问reviewboard
    # /sbin/iptables -I INPUT -p tcp --dport 80 -j ACCEPT
    # service httpd restart


###2. 设置开机自启动

    # chkconfig httpd on
    # chkconfig mysqld on
    # chkconfig sendmail on
    # vim /etc/rc.d/rc.local（加入以下部分）
        ...
        setenforce 0
        /sbin/iptables -I INPUT -p tcp --dport 80 -j ACCEPT
        ...


###3. 登录 reviewboard

输入在创建 rb-site 时设置的用户名（默认为 admin）、密码，即可登录 reviewboard. 效果图如下：

![](/static/img/reviewboard_login.png)
