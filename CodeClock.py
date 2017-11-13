'''CodeClock'''
import time

def CodeClock(code):
    start_time = time.clock()
    eval(code)
    return time.clock() - start_time

def looper(x):
    count = 0
    for ii in range(x):
        count += 1
        print count
    return

print CodeClock('looper(1000000)')