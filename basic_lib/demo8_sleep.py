# -*- coding: utf-8 -*-
"""
await 和 sleep 的区别演示
await：语法，暂停当前协程、让出线程；
asyncio.sleep：  异步休眠（非阻塞线程）
time.sleep：     同步休眠，阻塞整个线程
"""
import asyncio
import time

async def a():
    print("任务A开始")
    await asyncio.sleep(2)
    print("任务A结束")

async def b():
    print("任务B开始")
    await asyncio.sleep(2)
    print("任务B结束")

async def main_async():
    t1 = asyncio.create_task(a())
    t2 = asyncio.create_task(b())
    await t1
    await t2
    print("异步总耗时：约2秒\n")

def c():
    print("任务C开始")
    time.sleep(2)
    print("任务C结束")

def d():
    print("任务D开始")
    time.sleep(2)
    print("任务D结束")

def main_sync():
    c()
    d()
    print("同步总耗时：约4秒")

if __name__ == "__main__":
    print("===== 异步 await + asyncio.sleep =====")
    asyncio.run(main_async())

    print("===== 同步 time.sleep =====")
    main_sync()
