#mysql 1153, "Got a packet bigger than 'max_allowed_packet' bytes"

在[ mysql 官网](http://dev.mysql.com/doc/refman/5.1/en/server-system-variables.html#sysvar_max_allowed_packet)对 max_allowed_packet 的描述为：

> The maximum size of one packet or any generated/intermediate string.

####查看其大小：

    :::mysql
    mysql> show VARIABLES like '%max_allowed_packet%';
    +--------------------------+------------+
    | Variable_name            | Value      |
    +--------------------------+------------+
    | max_allowed_packet       | 1048576    |
    | slave_max_allowed_packet | 1073741824 |
    +--------------------------+------------+
    2 rows in set (0.02 sec)

    mysql> 

默认大小为 1048576 字节，即 1M 大小。

####修改其值：

可通过修改 /etc/my.cnf 文件来设置 max_allowed_packet 大小，重启 mysql 服务后生效：

    :::bash
    vim /etc/my.cnf
        [mysqld]
        datadir=/var/lib/mysql
        socket=/var/lib/mysql/mysql.sock
        user=mysql
        # Disabling symbolic-links is recommended to prevent assorted security risks
        symbolic-links=0
        max_allowed_packet=10M  # 在 [mysqld] 下添加 max_allowed_packet=10M

        [mysqld_safe]
        log-error=/var/log/mysqld.log
        pid-file=/var/run/mysqld/mysqld.pid
