from threading import Thread
from time import sleep

print "Hi"

c = 0


def foo():
    global c
    while True:
        print(c)
        c += 1
        sleep(0.3)

t = Thread(target=foo)
t.daemon = True
t.start()

while True:
    print("Running..")
    sleep(1)
