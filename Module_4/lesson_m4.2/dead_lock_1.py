import threading

lock_obj = threading.Lock()  # change to Rlock

print("Acquired first time")
lock_obj.acquire()
print("Acquired 2 time")
lock_obj.acquire()

print("Releasing")
lock_obj.release()

# def re entrance():
#     print("start")
#     lock_obj.acquire()
#     print("Aquired")
#     re entrance()
#
# re entrance()
