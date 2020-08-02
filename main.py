#!/usr/bin/env python3
from threading import Timer
from time import sleep
import getch
import sys
import datetime
from datetime import timedelta

# def timeout(foo, bar=None):
#     print('The arguments were: foo: {}, bar: {}'.format(foo, bar))


def timeout(arg):
    print("arg: {}".format(arg))
    print(type(arg))
    print("Wake up!! Stand up!!! Go!! Walk! Breath! Take a break!")
    #raw_input("Che vuoi fare?")
    arg = True

def main():
    break_timeout_min = 10
    t = Timer(break_timeout_min * 1, timeout, ["string1"])
    start = datetime.datetime.now()

    while 1:
        # using fixed values
        t.start()

        print("now after the t.start")

        sleep(20)
        # here it needs to wait indefinetly or until something/someone quits
        # while 1:
        #     now = datetime.datetime.now()
        #     sleep(10)
        #     elapsed = now - start
        #     print("inside the main loop {} {} {}".format(start,now, elapsed))
        #     # if shared_area[0]:
        #     #     print("Going for reset")
        #     #     shared_area[0] = False
        #     #     t = Timer(break_timeout_min * 1, timeout, shared_area)
        #     #     t.start()
        #     # nb = getch.getch()
        #     # if nb == 'q' or nb == 'Q':
        #     #     t.cancel()
        #     #     sys.exit()

    # t = Timer(break_timeout_min * 60, args=['something'], kwargs=dict(bar=['else']))  
if __name__ == "__main__":
  main()



