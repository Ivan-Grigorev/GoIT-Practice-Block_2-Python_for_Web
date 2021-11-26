import threading
import time


class NightClub:
    def __init__(self):
        self.bouncer = threading.Semaphore(3)

    def open_club(self):
        for x in range(1, 51):
            t = threading.Thread(target=self.guest, args=[x])
            t.start()

    def guest(self, guest_id):
        print(f'\nGuest {guest_id} is waiting for entering the club')
        self.bouncer.acquire()

        print(f'\nGuest {guest_id} is doing dancing')
        time.sleep(1)

        print(f'\nGuest {guest_id} is leaving night club')
        self.bouncer.release()


if __name__ == "__main__":
    club = NightClub()
    club.open_club()
