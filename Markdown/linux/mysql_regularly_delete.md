#mysql定期删除表中数据

>问题具体描述：删除mysql数据库event表中7天前的数据  
>技术知识点1：mysql事件  
>技术知识点2：sql获取7天前的事件

##1. mysql事件开启

###a. 检查你的MYSQL是否开了这个功能

    SHOW VARIABLES LIKE 'event_scheduler';

###b. 打开你的MYSQL的计划任务功能

    SET GLOBAL event_scheduler = 1;
    或
    SET GLOBAL event_scheduler = ON;

##2. 事件创建

    mysql> CREATE EVENT e_event_delete
        -> ON SCHEDULE EVERY 1 DAY
        -> DO delete from event where timestamp > DATE_SUB(CURDATE(),INTERVAL 7 DAY) order by timestamp;

##3. sql获取7天前的事件

    DATE_SUB(CURDATE(),INTERVAL 7 DAY)
    或
    DATE_SUB(CURDATE(),INTERVAL 1 WEEK)

##4. 参考
* [事件创建](http://www.oschina.net/question/4873_20927)  
* [sql获取7天前的事件](http://blog.csdn.net/amber_room/article/details/7024896)