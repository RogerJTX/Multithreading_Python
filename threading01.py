import time
def dance():
    # 跳舞5s中
    for x in range(1,6):
        print('我正在跳舞，%s秒' %x)
        time.sleep(1)

def sing():
    # 唱歌5s中
    for x in range(1,6):
        print('我正在唱歌，%s秒' %x)
        time.sleep(1)
def main():
    dance()
    sing()

if __name__ == '__main__':
    main()