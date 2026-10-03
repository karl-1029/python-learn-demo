"""
try
    xxx
except  异常
    xxx
finally
    xxx
"""
try:
    print("=============================================================================")
    # print(name)
    # 1 / 0
    "ABC"[10]
    print("=============================================================================")
except NameError as e:
    print("NameError: ", e)
except ZeroDivisionError as e:
    print("ZeroDivisionError: ", e)
except IndexError as e:
    print("IndexError: ", e)
except Exception as e:
    print("Exception: ", e)
finally:
    print("this is finally.............")


print("====================================test=========================================")


def fun1():
    print("this is fun1")
    fun2()


def fun2():
    print("this is fun2")
    fun3()


def fun3():
    1 / 0
    print("this is fun3")


if __name__ == "__main__":
    try:
        fun1()
    except Exception as e:
        print("Exception: ", e)
    finally:
        print("this is finally.............")