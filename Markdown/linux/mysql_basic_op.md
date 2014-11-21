#mysql数据库的基本操作

最近弄了弄mysql数据库，现找了点时间整理整理，录为笔记如下：

##1. 查看所有数据库

    mysql> show databases;

##2. 删除数据库

    mysql> drop database testdb;

##3. 创建数据库

    mysql> create database testdb;

##4. 进入数据库

    mysql> use testdb;

##5. 查看所有表

    mysql> show tables;

##6. 创建表

    mysql> create table test(id int not null, name varchar(32) not null);

##7. 删除表

    mysql> drop table test;

    删除时进行判断：
    mysql> drop table if exists test;

##8. 查看表的结构

    mysql> desc test;

##9. 清空表
    
    mysql> truncate table test;

什么，还不够，那你可以看看[mysql数据库表的进阶操作](/linux/mysql_advanced_op.html)。