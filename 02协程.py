'''协程，又称微线程，纤程。英文名Coroutine。

子程序，或者称为函数，在所有语言中都是层级调用，比如A调用B，B在执行过程中又调用了C，C执行完毕返回，B执行完毕返回，最后是A执行完毕。

所以子程序调用是通过栈实现的，一个线程就是执行一个子程序。

子程序调用总是一个入口，一次返回，调用顺序是明确的。而协程的调用和子程序不同。

协程看上去也是子程序，但执行过程中，在子程序内部可中断，然后转而执行别的子程序，在适当的时候再返回来接着执行。

注意，在一个子程序中中断，去执行其他子程序，不是函数调用，有点类似CPU的中断。比如子程序A、B：'''

import asyncio
import time


# def A():
#     print('1')
#     print('2')
#     print('3')
#
# def B():
#     print('a')
#     print('b')
#     print('c')
#
# A()
# B()
#依次返回 1 2 3 a b c


def consumer():
    r = None
    while True:
        n = yield r
        if not n:
            return
        print('[CONSUMER] Consuming %s...' % n)
        r = '200 OK'

def produce(c):
    c.send(None)        #传入 None 启动生成器，使 consumer（）函数在 yield r处停止
    n = 0
    while n < 5:
        n = n + 1
        print('[PRODUCER] Producing %s...' % n)
        r = c.send(n)       #将 n 赋值给 n
        print('[PRODUCER] Consumer return: %s' % r)
    c.close()

c = consumer()      #构建一个生成器
produce(c)          #将生成器传入函数