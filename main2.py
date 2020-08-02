from Timer import Timer

def countdown(n):
    while n > 0:
        n -= 1

def timeout(arg):
  print("timeout!")

if __name__ == "__main__":
    # Use 1: Explicit start/stop
    t = Timer(break_time=10)

    t.start()

    while 1:
      print(t.get_elapsed)

    # # Use 2: As a context manager
    # with t:
    #     countdown(1000000)
    # print(t.elapsed)

    # with Timer() as t2:
    #     countdown(1000000)
    # print(t2.elapsed)
