import threading
from time import sleep

cond = threading.Condition()


def f1():
    c = 0
    while True:
        with cond:
            cond.wait()
            c += 1
            print(f"Получили событие с остатком! {c} раз(-а)")
            if c == 5:
                break


def f2():
    for i in range(1, 11):
        if i % 2 == 0:
            with cond:
                cond.notify()
        else:
            print(f"f1: {i}")
        sleep(0.1)


t1 = threading.Thread(target=f1)
t1.start()
t2 = threading.Thread(target=f2)
t2.start()

t1.join()
t2.join()

print("\nКонец!")

