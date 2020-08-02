#!/usr/bin/env python3
from threading import Timer
from time import sleep
import getch
import sys
import datetime
from datetime import timedelta


def timeout(arg):
    print("arg: {}".format(arg))
    print(type(arg))
    print("Wake up!! Stand up!!! Go!! Walk! Breath! Take a break!")
    arg = True
# def timeout(foo, bar=None):
#     print('The arguments were: foo: {}, bar: {}'.format(foo, bar))

def main():
    shared_area = { 'reset': False, }
    start = datetime.datetime.now()
    # using fixed values
    break_timeout_min = 1
    t = Timer(break_timeout_min * 1, timeout, ["string1"])
    t.start()

    # here it needs to wait indefinetly or until something/someone quits
    while True:
        now = datetime.datetime.now()
        sleep(1)
        elapsed = now - start
        print("inside the main loop {} {} {}".format(start,now, elapsed))
        # if shared_area[0]:
        #     print("Going for reset")
        #     shared_area[0] = False
        #     t = Timer(break_timeout_min * 1, timeout, shared_area)
        #     t.start()
        # nb = getch.getch()
        # if nb == 'q' or nb == 'Q':
        #     t.cancel()
        #     sys.exit()

    # t = Timer(break_timeout_min * 60, args=['something'], kwargs=dict(bar=['else']))  
if __name__ == "__main__":
  main()



