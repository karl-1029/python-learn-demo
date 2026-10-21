"""
random模块说明：
random 是Python内置伪随机数模块，用来生成随机整数、随机小数、随机抽取元素、打乱列表；
伪随机：依靠种子seed生成，种子固定，随机结果就固定，适合测试、抽奖、随机取样等场景。

===================== random 全部常用方法清单（注释）=====================
# 【种子控制】
# 1. random.seed(n)        设置随机种子；种子相同，后续随机结果完全一致，用于复现结果

# 【生成随机小数（浮点数）】
# 2. random.random()        生成 [0.0, 1.0) 之间的随机小数，最基础随机函数
# 3. random.uniform(a,b)   生成 [a,b] 区间内的随机浮点数，左右边界都可取

# 【生成随机整数】
# 4. random.randint(a,b)    生成 [a,b] 闭区间随机整数，包含首尾两个数字
# 5. random.randrange(start, stop, step) 按步长取随机整数，等价于 choice(range(...))

# 【序列随机操作（列表/元组/字符串）】
# 6. random.choice(seq)     从序列中随机选取1个元素，有放回抽取
# 7. random.choices(pop, k, weights) 有放回随机选取k个元素，支持权重概率选择
# 8. random.sample(pop, k)  无放回随机选取k个元素，不重复抽取，k不能超过序列长度
# 9. random.shuffle(list)   原地打乱列表顺序，直接修改原列表，无返回值
"""

import random

# 1. seed 设置随机种子，固定随机结果
def demo_seed():
    random.seed(666)
    print("seed固定种子后的随机数：", random.random())

# 2. random() 0~1随机小数
def demo_random():
    res = random.random()
    print("random() 0-1小数：", res)

# 3. uniform() 指定区间随机浮点数
def demo_uniform():
    res = random.uniform(1, 10)
    print("uniform(1,10)区间小数：", res)

# 4. randint() 闭区间随机整数 [a,b]
def demo_randint():
    res = random.randint(1, 100)
    print("randint(1,100)随机整数：", res)

# 5. randrange() 带步长随机整数
def demo_randrange():
    res = random.randrange(0, 100, 2)  # 只取偶数
    print("randrange偶数随机：", res)

# 6. choice() 随机选1个元素
def demo_choice():
    lst = ["苹果", "香蕉", "橙子"]
    res = random.choice(lst)
    print("choice单选：", res)

# 7. choices() 有放回多选，支持权重
def demo_choices():
    lst = ["一等奖", "二等奖", "谢谢参与"]
    # 权重：1:5:94
    res = random.choices(lst, weights=[1, 5, 94], k=3)
    print("choices有放回抽取3个：", res)

# 8. sample() 无放回随机取样，不重复
def demo_sample():
    lst = [1,2,3,4,5,6]
    res = random.sample(lst, k=3)
    print("sample无放回取3个：", res)

# 9. shuffle() 原地打乱列表
def demo_shuffle():
    lst = [1,2,3,4,5]
    random.shuffle(lst)
    print("shuffle打乱后的列表：", lst)

# 统一执行所有案例
if __name__ == "__main__":
    demo_seed()
    demo_random()
    demo_uniform()
    demo_randint()
    demo_randrange()
    demo_choice()
    demo_choices()
    demo_sample()
    demo_shuffle()
