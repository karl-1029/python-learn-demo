"""
collections模块说明：
collections是Python内置容器扩展模块，提供了dict、list、tuple的增强版本，用来解决普通容器效率低、缺少特殊功能的问题；
常用场景：计数、双端队列、带默认值字典、命名元组、有序字典，是面试高频模块。

===================== 常用方法清单 =====================
# 1. namedtuple()  创建命名元组，给元组字段起名字，可读性更强
# 2. deque()       双向队列，两端增删速度远快于list；appendleft/popleft O(1)
# 3. Counter()     字典子类，专门用于统计元素出现次数，支持most_common、elements
# 4. defaultdict() 带默认值的字典，键不存在时自动返回默认值，避免KeyError
# 5. OrderedDict() 有序字典，严格保留键值对插入顺序（3.7+普通dict也有序，但OrderedDict有move_to_end等独有方法）
"""

from collections import namedtuple, deque, Counter, defaultdict, OrderedDict

# 1. namedtuple：命名元组
def demo_namedtuple():
    # 定义结构
    Student = namedtuple("Student", ["name", "age", "score"])
    s = Student("张三", 20, 90)
    print("namedtuple对象：", s)
    print("通过字段取值：", s.name, s.age)

# 2. deque：双向队列
def demo_deque():
    dq = deque([1, 2, 3])
    dq.append(4)          # 右侧添加
    dq.appendleft(0)      # 左侧添加
    dq.pop()              # 右侧弹出
    dq.popleft()          # 左侧弹出
    print("deque操作结果：", dq)

# 3. Counter：计数统计
def demo_counter():
    c = Counter("abracadabra")
    print("Counter统计结果：", c)
    print("出现次数最多的前2个：", c.most_common(2))
    print("展开所有元素：", list(c.elements()))

# 4. defaultdict：默认值字典
def demo_defaultdict():
    # 键不存在时默认值为列表[]
    dd = defaultdict(list)
    data = [("水果", "苹果"), ("水果", "香蕉"), ("蔬菜", "白菜")]
    for k, v in data:
        dd[k].append(v)
    print("defaultdict分组结果：", dict(dd))

# 5. OrderedDict：有序字典
def demo_ordereddict():
    od = OrderedDict()
    od["b"] = 2
    od["a"] = 1
    od.move_to_end("b")  # 将b移动到末尾
    print("OrderedDict保持插入顺序：", dict(od))

if __name__ == "__main__":
    demo_namedtuple()
    demo_deque()
    demo_counter()
    demo_defaultdict()
    demo_ordereddict()
