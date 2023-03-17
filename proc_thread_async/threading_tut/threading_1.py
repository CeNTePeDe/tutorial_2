import time
import threading
import os
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime
from threading import Thread

CNT = 0


def func_calc():
    """Func with heavy calculations"""
    cnt = 0
    for _ in range(50_000_000):
        cnt += 1

    print(f'thread from {threading.get_ident()} from process {os.getpid()}')


def func_sleep():
    """Func with I/O bound operations"""
    print(f'this thread {threading.get_ident()} from process {os.getpid()}')
    time.sleep(1)


def func_cnt_printer_and_increment():
    global CNT
    CNT += 1
    print(f'this thread {threading.get_ident()} from process{os.getpid()}: {CNT}')


if __name__ == '__main__':
    start_time = datetime.now()
    #th1 = Thread(target=func_calc)
    #th2 = Thread(target=func_calc)
    #th3 = Thread(target=func_calc)
    #th = [th1, th2, th3]
    #for i in th:
    #    i.start()
    #for i in th:
    #    i.join()

    with ThreadPoolExecutor(max_workers=3) as t:
        [t.submit(func_cnt_printer_and_increment) for _ in range(3)]

    print(f'Total time for execution of function is {datetime.now() - start_time}')
