import threading
import time
from etl.data_gather.settings import SAVE_MONGO_CONFIG, RESOURCE_DIR

class MultipleThreading(threading.Thread):

    def __init__(self, func, args=(), kwargs=None):
        threading.Thread.__init__(self)
        self.func = func
        self.args = args
        if kwargs is None:
            kwargs = {}
        self.kwargs = kwargs

    def run(self):  ##重写run()方法
        print('func_name is: {}'.format(self.func.__name__))
        return self.func(*self.args, **self.kwargs)


class ListDetailSpider(object):
    def __init__(self, config, proj=None):
        config["db"] = 'lz_data_yewu'
        self.proj = proj
        # self.host = "gpscenter.whu.edu.cn"  # 网站域名
        # self.host_name = ""  # 网站中文名
    def music(self, data):
        print("bengin listen music: {}".format(time.ctime()))
        time.sleep(2)
        print(str(data))
        print("music end: {}".format(time.ctime()))
        yy = '好听'
        return yy
    def movie(self, data):
        print("bengin look movie: {}".format(time.ctime()))
        time.sleep(5)
        print(str(data))
        print("movie end: {}".format(time.ctime()))

a = ListDetailSpider(SAVE_MONGO_CONFIG)
b = ListDetailSpider(SAVE_MONGO_CONFIG)
th1 = MultipleThreading(a.music, ("love.mp3",))
th2 = MultipleThreading(b.movie, ("Anit.avi",))
th1.start()
th2.start()
print(th1.isAlive())
print(th2.isAlive())
print(time.ctime())
time.sleep(9)
print(th1.is_alive())
print(th2.is_alive())
print(time.ctime())