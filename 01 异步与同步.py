import time
import asyncio

# '''实现同步:product()函数生产上架商品，顾客 consumer()买商品。上架和买一种商品耗时 1s'''
#
# def consumer(n,s_t):
#     '''
#     从生产商购买商品
#     :param n: 商品
#     :param t: 耗时
#     :return:
#     '''
#     time.sleep(1)  # 购买一件商品耗时 1 s
#     print('商品5已被购买。')
#     while n != 0:
#         n = n-1
#         time.sleep(1)
#         print('商品{}已被购买。'.format(n))
#     e_t = time.time()
#     print('#' * 50)
#     print('商品已全部购买，耗时{}秒。'.format(e_t - s_t))
#
# def product():
#     n = 0
#     while n < 5:
#         time.sleep(1)
#         n = n+1
#         print('商品{}上架已完成。'.format(n))
#     return n
#
#
# s_t = time.time()
# produce = product()
# consumer(produce,s_t)


'''
实现异步：通过 asycio 定义一个协程，该协程不能直接执行，而是需要通run_until_complete()
将其加入到 event_loop 事件循环中，并启动循环，这就实现了异步。
'''
#定义一个 asyncio 协程

async def hello():
    print('Hello World.')
    await asyncio.sleep(2)
    print('Hello myself.')

#创建一个 asyncio 事件循环
loop = asyncio.get_event_loop()
tasks = [hello() for i in range(10)]
#将 asyncio 协程加入到 asyncio 事件循环中，并执行
loop.run_until_complete(asyncio.wait(tasks))
#关闭事件循环
loop.close()









