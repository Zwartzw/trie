import random
import threading
import os
import multiprocessing as mp
import time
def target():
    lines = [str(random.randint(10 ** 7, 10 ** 8)) + '\n' for _ in range(100000)]
    with lock:
        with open('data/qq.txt', 'a', encoding='utf8',newline=None) as f:
            f.writelines(lines)
def init(l):
    global lock
    lock =l
if __name__ == '__main__':
    if not os.path.exists('data'):
        os.mkdir('data')
    start = time.time()
    # 多线程
    # ts = []
    # lock = threading.Lock()
    # for _ in range(100):
    #     ts.append(threading.Thread(target=target,args=(lock,)))
    # for t in ts:
    #     t.start()
    # for t in ts:
    #     t.join()

    # 利用Manager管理进程
    # lock = mp.Manager().Lock()
    # p = mp.Pool(16)
    # for _ in range(100):
    #     p.apply_async(target,args=(lock,))
    # p.close()
    # p.join()

    #初始化Pool
    lock = mp.Lock()
    p = mp.Pool(initializer=init,initargs=(lock,))

    for _ in range(10):
        p.apply_async(target,callback=None)  # 可以使用callback来处理target的返回值
    p.close()
    p.join()
    print(time.time()-start)