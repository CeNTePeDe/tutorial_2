import time
from random import randint
import os
from datetime import datetime
from multiprocessing import Process, Pool


# with open("file.txt", 'w') as f_o:
#     for _ in range(100_000_00):
#         f_o.write(f'{randint(0,9)}\n')

def lab(*args, **kwargs):
    result = 0
    with open('file.txt', 'r') as f_o:
        for s in f_o:
            result += randint(0, int(s))
    print(os.getpid(), result)


# if __name__ == '__main__':
#    start = datetime.now()
#    p = Process(target=lab)
#    p_1 = Process(target=lab)
#    p.start()
#    p_1.start()
#    p.join()
#    p_1.join()
#    print(datetime.now() - start)


# if __name__ == '__main__':
#    start = datetime.now()
#    p_list = [Process(target=lab) for _ in range(2)]
#    for p in p_list:
#        p.start()
#    for p in p_list:
#        p.join()
#    print(datetime.now() - start)
#


if __name__ == '__main__':
    start = datetime.now()
    with Pool(2) as pool:
        pool.map(lab, (1, 2))
    print(datetime.now() - start)
