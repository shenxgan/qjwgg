#time 模块常用函数整理

    :::python
    >>> import time

###time.localtime()
接收时间辍（1970纪元后经过的浮点秒数）并返回当地时间下的时间元组

    :::python
    >>> time.localtime()
    time.struct_time(tm_year=2015, tm_mon=1, tm_mday=7, tm_hour=17, tm_min=13, tm_sec=26, tm_wday=2, tm_yday=7, tm_isdst=0)

### time.asctime()
将时间元祖转换为字符串时间格式

    :::python
    >>> time.asctime(time.localtime())
    'Wed Jan  7 17:17:55 2015'

###time.time()
返回当前时间的时间戳（1970纪元后经过的浮点秒数）

    :::python
    >>> time.time()
    1420623303.820671

###time.sleep()
推迟调用线程的运行

    :::python
    >>> time.time(); time.sleep(2); time.time()
    1420623396.385442
    1420623398.387518

###time.strftime()
格式化时间

    :::python
    >>> time.strftime('%Y-%m-%d %X', time.localtime())
    '2015-01-07 17:53:52'
    >>> time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())
    '2015-01-07 17:54:19'

```text
%y 两位数的年份表示（00-99）
%Y 四位数的年份表示（000-9999）
%m 月份（01-12）
%d 月内中的一天（0-31）
%H 24小时制小时数（0-23）
%I 12小时制小时数（01-12）
%M 分钟数（00=59）
%S 秒（00-59）
%a 本地简化星期名称
%A 本地完整星期名称
%b 本地简化的月份名称
%B 本地完整的月份名称
%c 本地相应的日期表示和时间表示
%j 年内的一天（001-366）
%p 本地A.M.或P.M.的等价符
%U 一年中的星期数（00-53）星期天为星期的开始
%w 星期（0-6），星期天为星期的开始
%W 一年中的星期数（00-53）星期一为星期的开始
%x 本地相应的日期表示
%X 本地相应的时间表示
%Z 当前时区的名称
%% %号本身
```

###time.strptime
根据指定的格式把一个时间字符串解析为时间元组。（格式化符号与 time.strftime() 中的一样）

    :::python
    >>> time.strptime('2015-01-07 05:18:33', '%Y-%m-%d %X')
    time.struct_time(tm_year=2015, tm_mon=1, tm_mday=7, tm_hour=5, tm_min=18, tm_sec=33, tm_wday=2, tm_yday=7, tm_isdst=-1)

###time.ctime()
把时间戳转化为字符串时间格式

    :::python
    >>> time.ctime()
    'Wed Jan  7 05:13:32 2015'
    >>> time.ctime(time.time())
    'Wed Jan  7 05:14:22 2015'


###参考
* [https://docs.python.org/2/library/time.html](https://docs.python.org/2/library/time.html)
* [http://www.w3cschool.cc/python/python-date-time.html](http://www.w3cschool.cc/python/python-date-time.html)
