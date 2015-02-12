#mysql数据库的基本操作

最近弄了弄mysql数据库，现找了点时间整理整理，录为笔记如下：

###1. 查看所有数据库

    :::mysql
    mysql> show databases;

###2. 删除数据库

    :::mysql
    mysql> drop database testdb;

###3. 创建数据库

    :::mysql
    mysql> create database testdb;

###4. 进入数据库

    :::mysql
    mysql> use testdb;

###5. 查看所有表

    :::mysql
    mysql> show tables;

###6. 创建表

    :::mysql
    mysql> create table test(id int not null, name varchar(32) not null);

###7. 删除表

    :::mysql
    mysql> drop table test;

    # 删除时进行判断：
    mysql> drop table if exists test;

###8. 查看表的结构

    :::mysql
    mysql> desc test;

###9. 清空表

    :::mysql
    mysql> truncate table test;

什么，还不够，那你可以看看[mysql数据库表的进阶操作](http://www.qjwgg.com/linux/mysql_advanced_op.html)。
