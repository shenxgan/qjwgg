#Python 守护线程示例

    :::python
    #!/usr/bin/python
    # -*- coding: utf-8 -*-

    import thread
    import threading
    import time


    class DaemonThread(threading.Thread):
        def __init__(self):
            threading.Thread.__init__(self)
            self._dismissed = threading.Event()
            self.setDaemon(True)

        def run(self):
            while True:
                if self._dismissed.is_set():
                    break
                try:
                    print time.time()
                    time.sleep(1)
                except Exception, e:
                    print 'catch a exception:', e
                    # thread.interrupt_main()
                    # thread.exit()

        def stop(self):
            self._dismissed.set()
