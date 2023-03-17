import os
from multiprocessing import Pool
from time import sleep


def f(x):
    print(os.getpid(), 'sleep')
    sleep(1)
    return x * x


if __name__ == '__main__':
    pool = Pool(2)
    # print(pool.map(f, (1, 2, 3, 4, 5, 6,)))
    # print(pool.apply(f, (2,)))
    res = pool.map_async(f, (2, 3, 4, 5))
    print(res.get())
