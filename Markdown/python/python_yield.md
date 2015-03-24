#Python yield 简述

> * 简单地讲，yield 的作用就是把一个函数变成一个 generator
> * yield 是一个类似 return 的关键字，只是这个函数返回的是个生成器。

###1. 先来了解一些概念：

* 迭代器

    * 从根本上说，迭代器就是有一个 next() 方法的对象。

* 生成器

    * 生成器是迭代器，同时也并不仅仅是迭代器；生成器提供了非常方便的自定义迭代器的途径。
    * 任何使用 yield 的函数都称之为生成器。
    * 生成器就是一个返回迭代器（iterator）的函数。 和普通函数唯一的区别就是这个函数包含 yield 语句。

* 协程

    * 通过协程实现类似并发的任务。
    * 协程不同于线程的是，线程是抢占式的调度，而协程是协同式的调度，也就是说，协程需要自己做调度。
    * 在 Python 的概念中，这里提到的协程就是生成器。

###2. 代码示例

* 费波那契数列

        :::python
        #!/usr/bin/python
        # -*- coding: utf-8 -*-

        '''
        费波那契数列
        费波那契数列由0和1开始，之后的费波那契系数就由之前的两数相加。
        '''

        def fibonacci(n):
            x,y = 0,1
            while n > 0:
                yield x
                x,y,n = y,x+y,n-1


        for fib in fibonacci(13):
            print fib,

    输出结果为：

        :::text
        0 1 1 2 3 5 8 13 21 34 55 89 144

* 生产者 - 消费者

        :::python
        #!/usr/bin/python
        # -*- coding: utf-8 -*-

        import time

        def consumer():
            r = ''
            while True:
                n = yield r
                if not n:
                    return
                print('[CONSUMER] Consuming %s...' % n)
                time.sleep(1)
                r = '200 OK'

        def produce(c):
            c.next()
            n = 0
            while n < 5:
                n = n + 1
                print('[PRODUCER] Producing %s...' % n)
                r = c.send(n)
                print('[PRODUCER] Consumer return: %s' % r)
            c.close()

        if __name__=='__main__':
            c = consumer()
            produce(c)

    输出结果为：

        :::text
        [PRODUCER] Producing 1...
        [CONSUMER] Consuming 1...
        [PRODUCER] Consumer return: 200 OK
        [PRODUCER] Producing 2...
        [CONSUMER] Consuming 2...
        [PRODUCER] Consumer return: 200 OK
        [PRODUCER] Producing 3...
        [CONSUMER] Consuming 3...
        [PRODUCER] Consumer return: 200 OK
        [PRODUCER] Producing 4...
        [CONSUMER] Consuming 4...
        [PRODUCER] Consumer return: 200 OK
        [PRODUCER] Producing 5...
        [CONSUMER] Consuming 5...
        [PRODUCER] Consumer return: 200 OK

###3. 自然界中的费波那契数列

<video controls="controls" autoplay="autoplay">
  <source src="http://www.qjwgg.com/static/src/fibonacci.mp4" type="video/mp4">
Your browser does not support the video tag.
</video>

###参考：

* [Python yield 使用浅析 - IBM](http://www.ibm.com/developerworks/cn/opensource/os-cn-python-yield/)
* [提高你的 Python: 解释 yield 和 Generators（生成器）](http://www.oschina.net/translate/improve-your-python-yield-and-generators-explained)
* [协程 - 廖雪峰的官方网站](http://www.liaoxuefeng.com/wiki/001374738125095c955c1e6d8bb493182103fac9270762a000/0013868328689835ecd883d910145dfa8227b539725e5ed000)