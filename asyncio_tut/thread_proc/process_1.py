import time
from multiprocessing import Process
import os


def f(a, b):
    print(f'f started from: {os.getpid()}')
    print(a + b)
    print(f'from {os.getpid()}')


if __name__ == '__main__':
    p = Process(target=f, args=(1, 2))
    p_2 = Process(target=f, args=(1, 3))
    p_3 = Process(target=f, args=(1, 4))
    p.start()
    p_2.start()
    p_3.start()
    print('finished')