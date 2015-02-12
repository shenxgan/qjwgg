#mysql数据库表的进阶操作

注意，本文是围绕着数据库表结构的操作，若你想找的是**mysql数据库的基本操作**，请点击[这里](http://www.qjwgg.com/linux/mysql_basic_op.html)。

###1. 删除字段（一列）

    :::mysql
    ALTER TABLE <table_name> DROP <column_name>;
    
    mysql> alter table test drop name;

###2. 添加字段

    :::mysql
    ALTER TABLE <table_name> ADD <new_column_name> <data_type>;
    
    mysql> alter table test add name varchar(32);

###3. 移动列顺序

    :::mysql
    mysql> alter table test modify id int after name;

###4. 修改default值

    :::mysql
    mysql> alter table test alter name set default 'hello';

###5. 修改null值（需要写出类型）

    :::mysql
    mysql> alter table test modify name varchar(32) not null;

###6. 添加主键

    :::mysql
    mysql> alter table test add primary key(id, name);
    
    # 设置主键自动增长（清空后操作）（不是主键会失败）
    mysql> alter table test modify id integer auto_increment;

###7. 删除主键（此时要设置为主键的列中不能有重复的值）

    :::mysql
    mysql> alter table test drop primary key;
    
    # 若是有自增长的主键，要先删除自增长属性（id为自增长主键）
    mysql> alter table test change id id int;
