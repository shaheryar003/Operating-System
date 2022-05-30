from multiprocessing import Process
import os

def info(title):
    print(title)
    print('module name:', _name_)
    print('parent process:', os.getppid())
    print('process id:', os.getpid())

def f(name):
    info('function f')
    print('hello', name)

if _name_ == '_main_':
    info('main line')
    p1 = Process(target=f, args=('bob1',))
    p2 = Process(target=f, args=('bob2',))
    p3 = Process(target=f, args=('bob',))
    p1.start()
    p2.start()
    p3.start()
    p1.join()
    p2.join()
    p3.join()
    