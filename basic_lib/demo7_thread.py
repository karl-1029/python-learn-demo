# -*- coding: utf-8 -*-
"""
threading模块说明：
threading是Python内置多线程模块，用于创建和管理线程，实现并发任务；
适用场景：IO密集型任务（网络请求、文件读写）；GIL限制导致CPU密集型多线程无法利用多核；
提供线程创建、等待、状态查询，以及线程同步工具：锁、信号量、事件、条件变量等，是面试并发高频模块。

===================== 常用方法清单 =====================
# 一、线程创建与实例方法
# 1. Thread(target, args, name, daemon) 创建线程对象，target为执行函数，args传参，daemon设置守护线程
# 2. start() 启动线程，进入就绪状态，自动调用run()，只能调用一次
# 3. run() 线程执行主体，继承Thread类时重写该方法
# 4. join(timeout) 主线程阻塞等待子线程结束，timeout为超时秒数
# 5. is_alive() 判断线程是否还在运行，返回布尔值
# 6. daemon 属性：设置守护线程，主线程退出时守护线程直接终止，无需等待

# 二、模块全局函数
# 7. current_thread() 获取当前正在执行的线程对象
# 8. active_count() 获取当前存活的线程总数
# 9. enumerate() 返回所有存活线程对象列表

# 三、线程同步工具（面试重点）
# 10. Lock() 互斥锁，保证同一时刻只有一个线程执行临界区代码，acquire()加锁，release()释放锁
# 11. RLock() 可重入锁，同一个线程可以多次获取锁，避免死锁
# 12. Event() 线程事件信号，set()设置信号，wait()阻塞等待信号，clear()清空信号
# 13. Semaphore(value) 信号量，控制最大并发线程数量，value为允许同时执行的线程数
"""

import threading
import time

# 1. Thread创建线程 + start启动 + join等待 + is_alive状态判断
def demo_thread_basic():
    def worker(name):
        print(f"子线程 {name} 开始执行")
        time.sleep(1)
        print(f"子线程 {name} 执行完毕")

    t = threading.Thread(target=worker, args=("T1",), name="工作线程")
    t.start()
    print("线程是否存活：", t.is_alive())
    t.join()
    print("线程是否存活：", t.is_alive())

# 2. 继承Thread类重写run方法创建线程
def demo_thread_inherit():
    class MyThread(threading.Thread):
        def run(self):
            print(f"自定义线程 {self.name} 运行中")
            time.sleep(0.5)
    t = MyThread(name="自定义线程")
    t.start()
    t.join()

# 3. 守护线程daemon演示
def demo_daemon_thread():
    stop_event = threading.Event()

    def daemon_task():
        while not stop_event.is_set():
            print("守护线程正在运行...")
            stop_event.wait(0.3)

    t = threading.Thread(target=daemon_task, name="守护线程", daemon=True)
    t.start()
    time.sleep(0.8)
    stop_event.set()
    t.join()
    print("守护线程已停止")

# 4. 全局函数：current_thread、active_count、enumerate
def demo_thread_global_func():
    def func():
        print("当前线程对象：", threading.current_thread().name)
        time.sleep(0.5)

    t1 = threading.Thread(target=func, name="线程A")
    t2 = threading.Thread(target=func, name="线程B")
    t1.start()
    t2.start()
    print("当前存活线程数量：", threading.active_count())
    print("所有存活线程列表：", [t.name for t in threading.enumerate()])
    t1.join()
    t2.join()

# 5. Lock互斥锁，解决多线程共享变量竞争问题
def demo_lock():
    num = 0
    lock = threading.Lock()

    def add_num():
        nonlocal num
        for _ in range(1000):
            lock.acquire()  # 加锁
            try:
                num += 1
            finally:
                lock.release()  # 释放锁

    t1 = threading.Thread(target=add_num)
    t2 = threading.Thread(target=add_num)
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    print("加锁后最终数值：", num)

# 6. RLock可重入锁，同一线程多次加锁不会死锁
def demo_rlock():
    rlock = threading.RLock()

    def func():
        rlock.acquire()
        print("第一次获取锁")
        rlock.acquire()
        print("第二次获取锁（可重入）")
        rlock.release()
        rlock.release()

    t = threading.Thread(target=func)
    t.start()
    t.join()

# 7. Event事件信号，线程之间收发通知
def demo_event():
    event = threading.Event()

    def wait_task():
        print("子线程等待信号...")
        event.wait()  # 阻塞等待set信号
        print("收到信号，继续执行")

    t = threading.Thread(target=wait_task)
    t.start()
    time.sleep(1)
    print("主线程发出信号")
    event.set()  # 发出信号
    t.join()

# 8. Semaphore信号量，限制并发线程数量
def demo_semaphore():
    sem = threading.Semaphore(2)  # 最多同时2个线程运行

    def limited_task(name):
        with sem:
            print(f"线程{name}进入执行")
            time.sleep(1)
            print(f"线程{name}执行结束")

    for i in range(4):
        t = threading.Thread(target=limited_task, args=(i,))
        t.start()

if __name__ == "__main__":
    print("===== 1.线程基础操作 =====")
    demo_thread_basic()

    print("\n===== 2.继承Thread创建线程 =====")
    demo_thread_inherit()

    print("\n===== 3.守护线程演示 =====")
    demo_daemon_thread()

    print("\n===== 4.全局线程信息函数 =====")
    demo_thread_global_func()

    print("\n===== 5.Lock互斥锁 =====")
    demo_lock()

    print("\n===== 6.RLock可重入锁 =====")
    demo_rlock()

    print("\n===== 7.Event事件信号 =====")
    demo_event()

    print("\n===== 8.Semaphore信号量 =====")
    demo_semaphore()
