from multiprocessing import Process, Pool
import time


def show(name):
    print("Process name is " + name)


class MyProcess(Process):
    def __init__(self, name):
        super(MyProcess, self).__init__()
        self.name = str(name)

    def run(self):
        print('process name :' + self.name)
        print self.pid
        time.sleep(1)


if __name__ == '__main__':
    proc = Process(target=show, args=('subprocess',))
    proc.start()
    proc.join()
    for i in range(3):
        p = MyProcess(i)
        p.start()
        p.join()
    pool = Pool(processes=3)
    for i in xrange(6):
        pool.apply_async(show, args=(str(i),))
    print('======  apply_async  ======')
    pool.close()
    pool.join()
