import time
import threading


def countdown(n):
    while n > 0:
        print("T-minus", n)
        n -= 1
        time.sleep(1)


t1 = threading.Thread(target=countdown, args=(10,))
print("Is t1 alive:", t1.is_alive())


t1.start()
print("\nIs t1 alive:", t1.is_alive())
t1.join()

print("Is t1 alive:", t1.is_alive())
