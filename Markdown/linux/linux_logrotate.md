#logrotate服务

logrotate是一个日志管理程序，用来把旧的日志文件删除（备份），并创建新的日志文件，这个过程称为"转储"。我们可以根据日志的大小，或者根据其使用的天数来转储。

>系统环境：CentOS6.3

##1. logrotate启动方式

logrotate 的执行由**crond服务**实现。在/etc/cron.daily目录中，有个文件logrotate，它实际上是个shell script，用来启动logrotate。logrotate程序每天由cron在指定的时间（/etc/crontab）启动。

手动强制执行：

    logrotate -f /etc/logrotate.conf

可用来检测，配置是否生效。


##2. 配置文件/etc/logrotate.conf

    # see "man logrotate" for details
    # rotate log files weekly
    weekly      # 每周轮转一次
    
    # keep 4 weeks worth of backlogs
    rotate 4    # 保留4个
    
    # create new (empty) log files after rotating old ones
    create      # rotate后，允许创建一个空的新文件
    
    # use date as a suffix of the rotated file
    dateext     # 表示转存文件会以日期来结束
    
    # uncomment this if you want your log files compressed
    #compress   # 压缩，默认为不启用压缩
    
    # RPM packages drop log rotation information into this directory
    include /etc/logrotate.d    # 将/etc/logrotate.d/这个目录中的所有档案都读进来执行rotate的工作，比如httpd
    
    # no packages own wtmp and btmp -- we'll rotate them here
    /var/log/wtmp {             # 定义/var/log/wtmp这个日志文件
        monthly                 # 每月轮转一次，取代了上面的全局设定的每周轮转一次
        create 0664 root utmp   # 新的日志文件的权限，属主，属主
    	minsize 1M              # 定义日志必须要大于1M大小才会去轮转
        rotate 1                # 保留1个，取代了上面的全局设定的保留4个
    }
    
    /var/log/btmp {
        missingok               # 如果日志丢失, 不报错
        monthly
        create 0600 root utmp
        rotate 1
    }
    
    # system-specific logs may be also be configured here.


##3. 配置语法

    选项                    用途
    nocompress,compress     不压缩,压缩
    delaycompress           不压缩前一个截断的文件（需要与compress一起用）
    daily,weekly,monthly    每天/周/月轮转一次
    copytruncate            清空原有文件，而不是创建一个新文件
    create 0644 root utmp   新建日志文件，权限、属主、组
    ifempty                 即使用空文件也转储
    notifempty              日志文件为空不进行转储
    olddir <dir>            转储后的日志存放目录，必须和当前日志文件在同一个文件系统
    rotate 5                保留最近的5个日志文件
    minisize 1M             必须大于1MB才会转转
    size 50M                超过50MB后轮转日志
    mail www@my.org         轮换后的把日志发给邮箱
    missingok               如果日志文件不存在，不报错
    prerotate,endscript     在logrotate之前执行的命令，如/usr/bin/charrt -a /var/log/logfile
    postrotate,endscript    在logrotate之后执行的命令，如/usr/bin/charrt +a /var/log/logfile
                            /bin/kill -HUP $(/bin/cat /var/run/rsyslogd.pid 2>/dev/null) &>/dev/null
                            /usr/bin/killall -HUP httpd
                            [ -f /var/run/nginx.pid ] && kill -USR1 $(cat /var/run/nginx.pid)
    sharedscripts           共享脚本，表示切换时只执行一次脚本
    dateext                 增加日期作为后缀，不然会是一串无意义的数字
    dateformat .%s          切换后文件名，必须配合dateext使用

##4. 参考
[rsyslog和logrotate服务](http://w.gdu.me/wiki/Linux/rsyslog_logrotate.html)  
[第十九章、認識與分析登錄檔](http://linux.vbird.org/linux_basic/0570syslog.php)