import threading
import time

threads = []

def keep_time_worker(value):
    print("I am keep_time_worker value: {}".format(value))
    print("START: {}".format(threading.current_thread().getName()))
    time.sleep(value)
    print("END: {}".format(threading.current_thread().getName()))


def hello():
    print("the usual boring hello world")
# threading.Thread(group=None, 
#                 target=None, 
#                 name=None, 
#                 args=(), 
#                 kwargs={}, 
#                 *,
#                 daemon=None)

desired_break = int(input("Enter break interval in minutes >"))

print("desired_break: {}".format(desired_break))


break_interval = desired_break * 60

for i in range(5):
    t = threading.Thread(target=keep_time_worker, args=(break_interval+i,))
    threads.append(t)
    t.start()



my_timer = threading.Timer(30.0, hello)
my_timer.start()
