import threading
import time


# 继承类threading.Thread
class MyThread(threading.Thread):
    def __init__(self, n):
        # 这里要继承构造函数
        super(MyThread, self).__init__()
        # 可以定义自己的实例变量
        self.n = n

    def run(self):
        print('running task', self.n)
        time.sleep(2)


t1 = MyThread('t1')
t2 = MyThread('t2')

t1.start()
t2.start()