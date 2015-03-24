#Python lambda 表达式简述

> 1. 在 python 中使用 lambda 来创建匿名函数  
> 2. lambda 是为了减少单行函数的定义而存在的


###一. 先看代码示例

1. 求解 1+2+3+ ··· +99+100

        :::python
        >>> reduce(lambda x,y:x+y, xrange(101))
        5050
        >>> 

2. 求解阶乘，比如 5!

        :::python
        >>> reduce(lambda x,y:x*y, xrange(1,6))
        120
        >>> 

3. 求解阶乘和，比如 1!+2!+3!+4!+5!

        :::python
        >>> reduce(lambda m,n:m+n,map(lambda z:reduce(lambda x,y:x*y, xrange(1,z)), xrange(2,7)))
        153
        >>> 

###二. 匿名函数 lambda

lambda 作为一个表达式，定义了一个匿名函数

    :::python
    >>> f = lambda x,y,z:(x+y)*z
    >>> f(1,2,3)
    9
    >>> 

###三. 内置函数 map, reduce, filter

1. map

        :::python
        map(...)
            map(function, sequence[, sequence, ...]) -> list

    说明：对 sequence 中的 item 依次执行 function(item)，执行结果**输出为 list**。

    示例：

        :::python
        >>> map(lambda x:x*x, xrange(5))
        [0, 1, 4, 9, 16]
        >>> 

2. reduce

        :::python
        reduce(...)
            reduce(function, sequence[, initial]) -> value

    说明：对 sequence 中的 item 顺序迭代调用 function，函数必须要有2个参数。要是有第3个参数，则表示初始值，可以继续调用初始值，**返回一个值**。

    示例：

        :::python
        >>> reduce(lambda x,y:x+y, xrange(5))
        10
        >>> 

3. filter

        :::python
        filter(...)
            filter(function or None, sequence) -> list, tuple, or string

    说明：对 sequence 中的 item 依次执行 function(item)，将执行结果为 True(!=0) 的 item **组成一个 List/String/Tuple（取决于 sequence 的类型）返回**，False(0) 则退出，进行过滤。

    示例：

        :::python
        >>> filter(lambda x:x%2, xrange(10))
        [1, 3, 5, 7, 9]
        >>> 

###参考

* [http://www.cnblogs.com/zhoujinyi/archive/2013/06/07/3121976.html](http://www.cnblogs.com/zhoujinyi/archive/2013/06/07/3121976.html)