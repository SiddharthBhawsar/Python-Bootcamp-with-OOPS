# #
import time
from functools import lru_cache



@lru_cache(maxsize=34)
def some_work(n):
#     #Some task taking n second
    time.sleep(n)
    return n
#
if __name__ == '__main__':
    print("Now running some work")
    # some_work(3)
    # print("done")
    some_work(3)
    some_work(1)
    some_work(6)
    some_work(9)
    print("Done Calling again....")
    # input()
    some_work(9)
    print("Called again")
