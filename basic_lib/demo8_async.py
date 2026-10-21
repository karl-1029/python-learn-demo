# -*- coding: utf-8 -*-
"""
async/await说明：
async 和 await 是 Python 3.5+ 引入的异步语法，用来编写协程代码；
协程是用户态轻量级任务，适合IO密集场景（网络请求、数据库、文件IO），单线程内切换，开销远小于线程；
单纯的 async/await 只是语法标记，本身不自带事件循环，事件循环由 asyncio 提供。

===================== 常用知识点清单 =====================
# 1. async def  定义协程函数，函数内部可以写await，调用后返回coroutine协程对象，不会自动执行
# 2. await      等待一个可等待对象（协程、Task、Future），让出控制权；只能写在async def内部
# 3. coroutine 对象 协程函数调用之后得到的对象，原生无法直接运行，必须交给事件循环调度
# 4. asyncio.run() 事件循环入口，驱动协程运行
"""
import asyncio


async def foo():
    print("foo 开始执行")
    print("foo 结束执行")
    return 100

async def foo_await():
    print("进入demo")
    ret = await foo()
    print("拿到返回值：", ret)

if __name__ == "__main__":
    # 直接调用，不跑内部代码
    print("仅仅生成协程对象，内部代码不会执行！想要运行它，必须依赖事件循环（asyncio），单独async/await语法无法调度")
    print("foo() 的返回：", foo())

    # 方式1：直接用 asyncio.run 运行协程
    asyncio.run(foo())

    # 方式1：直接用 asyncio.run 运行协程
    coroutine = foo_await()
    print("协程对象 foo_await() : ", coroutine)
    asyncio.run(coroutine)
