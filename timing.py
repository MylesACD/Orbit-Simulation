import time

def runtime(func):
    start = time.perf_counter()
    rtn = func
    finish = time.perf_counter()
    print("run time: " , int(finish-start))
    return rtn

