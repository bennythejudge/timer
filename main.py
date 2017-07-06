#!/usr/bin/env python3
from threading import Timer
from time import sleep
import getch
import sys

def timeout():
    print("Wake up!! Stand up!!! Go!! Walk! Breath! Take a break!")

# def timeout(foo, bar=None):
#     print('The arguments were: foo: {}, bar: {}'.format(foo, bar))

def main():
    # using fixed values
    break_timeout_min = 1
    t = Timer(break_timeout_min * 1, timeout)
    t.start()

    # here it needs to wait indefinetly or until something/someone quits
    while True:
        print("inside the main loop")
        sleep(1)
        # nb = getch.getch()
        # if nb == 'q' or nb == 'Q':
        #     t.cancel()
        #     sys.exit()

    # t = Timer(break_timeout_min * 60, args=['something'], kwargs=dict(bar=['else']))  
if __name__ == "__main__":
  main()



