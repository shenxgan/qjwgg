#linux配置svn

>本文记载svn的搭建与使用  
>环境：CentOS6.3

**总的步骤：**

    # yum -y install svn
    # mkdir repository
    # svnadmin create repository/
    # vim authz
    # vim passwd
    # vim svnserve.conf
    # svnserve -d -r /home/guguai/repository/ ##当前目录为/home/guguai
    # service iptables stop
    # svn co svn:172.10.2.24  ##172.10.2.24为本机（CentOS6.3）ip

**详细流程：**

##1. 安装svn

    # yum -y install svn

##2. 创建仓库
	
    # mkdir repository
    # svnadmin create repository/

##3. 在repository/conf目录下：

    # vim authz
        [/]
        guguai = rw  ##表示guguai用户对整个仓库具有读写权限


    # vim passwd
        guguai = 123456  ##表示添加一个用户名为guguai，密码为123456的用户
    
    	
    # vim svnserve.conf
        将文件中的这几行前面的#号去掉（注意不要留空格）
        anon-access = none
        auth-access = write
        password-db = passwd
        authz-db = authz
        realm = repository  ##仓库，repository为自定义字串
    

##4. 启动svn
	
    # svnserve -d -r /home/guguai/repository/

##5. 关闭防火墙
	
    # service iptables stop

##6. 使用：
	
    # svn co svn:172.10.2.24

在windows端推荐使用[TortoiseSVN](http://pan.baidu.com/s/1jG5NlMA)软件。
