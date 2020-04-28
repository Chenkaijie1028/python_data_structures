import threading


class MyThread(threading.Thread):
    def __init__(self, n):
        super(MyThread, self).__init__()
        self.n = n

    def run(self):
        print "current task:", self.n, threading.current_thread()


def run(n):
    print "current task:", n, threading.current_thread()


if __name__ == "__main__":
    t1 = threading.Thread(target=run, args=("thread 1",))
    t2 = threading.Thread(target=run, args=("thread 2",))
    t3 = MyThread("thread 3")
    t4 = MyThread("thread 4")

    print threading.current_thread()
    print threading.active_count()

    t1.start()
    t2.start()
    t3.start()
    t4.start()
