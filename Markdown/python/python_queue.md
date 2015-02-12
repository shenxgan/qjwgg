#Queue 模块

    :::python
    >>> import Queue

> Queue 模块一般用于多线程环境，多用于线程之间的通信

###其中定义的类和异常：

三种类型的队列：

1. **class Queue.Queue(maxsize=0)**

    先进先出队列（FIFO queue）。与以前数据结构中的队列一样。maxsize 用于指定队列的长度大小；maxsize 若小于或等于零，表示队列大小不限。

2. **class Queue.LifoQueue(maxsize=0)**

    后进先出队列（LIFO queue）。可理解为数据结构中的栈。maxsize 含义与上述一样。

3. **class Queue.PriorityQueue(maxsize=0)**

    优先级队列。优先级越低越先出队列。

两种异常：

1. **exception Queue.Empty**

    当对空队列进行无阻塞的 get 操作（get(False) 或 get_nowait()）时，将抛出此异常。

2. **exception Queue.Full**

    当对满队列进行无阻塞的 put 操作（put(item, False) 或 put_nowait(item)）时，将抛出此异常。

###此包中的常用方法(q = Queue.Queue()):

    :::python
    q.qsize()           # 返回队列的大小
    q.empty()           # 如果队列为空，返回 True, 反之 False
    q.full()            # 如果队列满了，返回 True, 反之 False
    q.put(item)         # 入队列
    q.put_nowait(item)  # 相当 q.put(item, False)
    q.get()             # 出队列
    q.get_nowait()      # 相当 q.get(False)
    q.task_done()       # 在完成一项工作之后，q.task_done() 函数向任务已经完成的队列发送一个信号
    q.join()            # 等到队列为空，再执行别的操作

###代码示例

    :::python
    >>> import Queue
    >>> q = Queue.Queue()
    >>> q.qsize()
    0
    >>> q.empty()
    True
    >>> q.put(1)
    >>> q.put(2)
    >>> q.get()
    1
    >>> q.get()
    2

###参考
[https://docs.python.org/2/library/queue.html](https://docs.python.org/2/library/queue.html)
