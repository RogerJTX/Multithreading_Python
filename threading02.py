import threading
import time

class ListDetailSpider(object):
    def __init__(self):
        self.a = 1

    def dance(self):
        # 跳舞5s中
        for x in range(1,6):
            print('我正在跳舞，%s秒' %x)
            time.sleep(1)

    def sing(self):
        # 唱歌5s中
        for x in range(1,6):
            print('我正在唱歌，%s秒' %x)
            time.sleep(1)
def main():
    bp = ListDetailSpider()
    t1 = threading.Thread(target=bp.dance())
    t2 = threading.Thread(target=bp.sing())
    t3 = threading.Thread(target=bp.dance())

    t1.start()
    t2.start()
    t3.start()

if __name__ == '__main__':
    main()