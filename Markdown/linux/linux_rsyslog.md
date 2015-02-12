#rsyslog配置讲解

**rsyslog负责写入日志，[logrotate](http://www.qjwgg.com/linux/linux_logrotate.html)负责备份和删除旧日志，以及更新日志文件。**

>系统环境：CentOS6.3  
>对于我来说，仅修改其配置文件，用于屏蔽不需要的日志信息。

##rsyslog配置文件/etc/rsyslog.conf

语义讲解：

    :::bash
    # rsyslog v5 configuration file
    
    # For more information see /usr/share/doc/rsyslog-*/rsyslog_conf.html
    # If you experience problems, see http://www.rsyslog.com/doc/troubleshoot.html
    
    #### MODULES ####
    # 加载模块
    $ModLoad imuxsock # provides support for local system logging (e.g. via logger command)
    $ModLoad imklog   # provides kernel logging support (previously done by rklogd)
    #$ModLoad immark  # provides --MARK-- message capability
    
    # Provides UDP syslog reception
    # 允许514端口接收使用UDP协议转发过来的日志
    #$ModLoad imudp
    #$UDPServerRun 514
    
    # Provides TCP syslog reception
    # 允许514端口接收使用TCP协议转发过来的日志
    #$ModLoad imtcp
    #$InputTCPServerRun 514
    
    
    #### GLOBAL DIRECTIVES ####
    # 定义日志格式默认模板
    # Use default timestamp format
    $ActionFileDefaultTemplate RSYSLOG_TraditionalFileFormat
    
    # File syncing capability is disabled by default. This feature is usually not required,
    # not useful and an extreme performance hit
    #$ActionFileEnableSync on
    
    # Include all config files in /etc/rsyslog.d/
    # 加入/etc/rsyslog.d下配置文件
    $IncludeConfig /etc/rsyslog.d/*.conf
    
    
    #### RULES ####
    
    # Log all kernel messages to the console.
    # Logging much else clutters up the screen.
    # 关于内核的所有日志都放到/dev/console(控制台)
    #kern.*                                                 /dev/console
    
    # Log anything (except mail) of level info or higher.
    # Don't log private authentication messages!
    # 记录所有日志类型的info级别以及大于info级别的信息到/var/log/messages，但是mail邮件信息，authpriv验证方面的信息和cron时间任务相关的信息除外
    *.info;mail.none;authpriv.none;cron.none                /var/log/messages
    
    # The authpriv file has restricted access.
    # authpriv验证相关的所有信息存放在/var/log/secure
    authpriv.*                                              /var/log/secure
    
    # Log all the mail messages in one place.
    # 邮件的所有信息存放在/var/log/maillog; 这里有一个-符号,表示是使用异步的方式记录, 因为日志一般会比较大
    mail.*                                                  -/var/log/maillog
    
    
    # Log cron stuff
    # 计划任务有关的信息存放在/var/log/cron
    cron.*                                                  /var/log/cron
    
    # Everybody gets emergency messages
    # 记录所有的大于等于emerg级别信息, 以wall方式发送给每个登录到系统的人, *代表所有在线用户
    *.emerg                                                 *
    
    # Save news errors of level crit and higher in a special file.
    # 记录uucp,news.crit等存放在/var/log/spooler
    uucp,news.crit                                          /var/log/spooler
    
    # Save boot messages also to boot.log
    # 启动的相关信息
    local7.*                                                /var/log/boot.log
    
    
    # ### begin forwarding rule ###
    # 转发规则
    # The statement between the begin ... end define a SINGLE forwarding
    # rule. They belong together, do NOT split them. If you create multiple
    # forwarding rules, duplicate the whole block!
    # Remote Logging (we use TCP for reliable delivery)
    #
    # An on-disk queue is created for this action. If the remote host is
    # down, messages are spooled to disk and sent when it is up again.
    #$WorkDirectory /var/lib/rsyslog # where to place spool files
    #$ActionQueueFileName fwdRule1 # unique name prefix for spool files
    #$ActionQueueMaxDiskSpace 1g   # 1gb space limit (use as much as possible)
    #$ActionQueueSaveOnShutdown on # save messages to disk on shutdown
    #$ActionQueueType LinkedList   # run asynchronously
    #$ActionResumeRetryCount -1    # infinite retries if host is down
    # remote host is: name/ip:port, e.g. 192.168.0.1:514, port optional
    # @@表示通过tcp协议发送  @表示通过udp进行转发
    #*.* @@remote-host:514
    # ### end of the forwarding rule ###

###1. 服务名称

    :::text
    服务类别                        说明
    auth (authpriv)                 主要与认证有关的机制，例如 login, ssh, su 等需要账号/密码的咚咚；
    cron                            就是例行性工作排程 cron/at 等产生讯息记录的地方；
    daemon                          与各个 daemon 有关的讯息；
    kern                            就是核心 (kernel) 产生讯息的地方；
    lpr                             亦即是打印相关的讯息啊！
    mail                            只要与邮件收发有关的讯息纪录都属于这个；
    news                            与新闻组服务器有关的东西；
    syslog                          就是 syslogd 这支程序本身产生的信息啊！
    user, uucp, local0 ~ local7     与 Unix like 机器本身有关的一些讯息。

###2. 讯息等级
从上到下，级别从低到高，记录的信息越来越少 详细的可以查看手册: man 3 syslog

    :::text
    等级 等级名称        说明
    1    info            仅是一些基本的讯息说明而已；
    2    notice          比 info 还需要被注意到的一些信息内容；
    3    warning(warn)   警示的讯息，可能有问题，但是还不至于影响到某个 daemon 运作的信息；
                         基本上，info, notice, warn 这三个讯息都是在告知一些基本信息而已，
                         应该还不至于造成一些系统运作困扰；
    4    err(error)      一些重大的错误讯息，例如配置文件的某些设定值造成该服务服法启动的信息说明，
                         通常藉由 err 的错误告知，应该可以了解到该服务无法启动的问题呢！
    5    crit            比 error 还要严重的错误信息，这个 crit 是临界点 (critical) 的缩写，
                         这个错误已经很严重了喔！
    6    alert           警告警告，已经很有问题的等级，比 crit 还要严重！
    7    emerg(panic)    疼痛等级，意指系统已经几乎要当机的状态！ 很严重的错误信息了。
                         通常大概只有硬件出问题，导致整个核心无法顺利运作，就会出现这样的等级的讯息吧！

除了这些有等级的讯息外，还有两个特殊的等级，那就是 **debug**(错误侦测等级) 与 **none** (不需登录等级) 两个，当我们想要作一些**错误侦测**，或者是**忽略掉某些服务的信息**时， 就用这两个咚咚吧！

###3. 连接符号

    :::text
    连接符号    说明
    .xxx        表示大于等于xxx级别的信息
    .=xxx       表示等于xxx级别的信息
    .!xxx       表示在xxx之外的等级的信息

##参考
[rsyslog和logrotate服务](http://w.gdu.me/wiki/Linux/rsyslog_logrotate.html)  
[第十九章、認識與分析登錄檔](http://linux.vbird.org/linux_basic/0570syslog.php)
