"""
re模块说明：
re 是Python内置正则表达式（Regular Expression）模块，用于字符串匹配、查找、提取、分割、替换；
通过一套匹配规则处理复杂文本，减少大量if字符串判断代码。
核心要素：pattern匹配模式 + 目标字符串。

===================== re模块顶层方法清单（全部写在注释内）=====================
# 1. re.compile()    编译正则表达式，生成Pattern对象；多次复用正则可提升执行效率
# 2. re.match()      仅从字符串开头进行匹配，开头不满足直接返回None
# 3. re.search()      在整个字符串任意位置查找第一个匹配项，全文检索
# 4. re.fullmatch()  整段字符串必须和正则完全匹配，严格全串匹配
# 5. re.findall()    找出所有非重叠匹配内容，返回字符串列表，最常用文本提取方法
# 6. re.finditer()   找出所有匹配项，返回Match迭代器，处理大文本节省内存
# 7. re.split()      按照正则匹配内容分割字符串，支持复杂分割规则
# 8. re.sub()        正则批量替换文本，返回替换后的新字符串
# 9. re.subn()       实现替换功能，同时返回替换次数，返回元组(新字符串,替换次数)
# 10. re.escape()    自动转义正则特殊字符(. * + ? () [] \等)，避免符号被解析为正则语法

===================== Match匹配对象常用方法清单（注释）=====================
# .group()       获取匹配内容，支持普通分组、命名分组取值
# .groups()      获取所有捕获分组，以元组形式返回
# .groupdict()   获取命名分组，以字典形式返回键值对
# .span()        获取匹配内容的起止下标，返回(start, end)
# .start()       获取匹配内容起始索引
# .end()         获取匹配内容结束索引

===================== 常用匹配模式flags（注释）=====================
# re.I / re.IGNORECASE    忽略大小写匹配
# re.M / re.MULTILINE     多行模式，^匹配每行开头，$匹配每行结尾
# re.S / re.DOTALL        让点号 . 可以匹配换行符 \n
# re.X / re.VERBOSE       正则可以换行、写注释，美化正则表达式
"""

import re

# 1. re.compile 编译正则对象
def demo_compile():
    pat = re.compile(r"\d+")
    res = pat.search("abc123xyz")
    print("compile结果:", res.group())

# 2. re.match 开头匹配
def demo_match():
    r1 = re.match(r"\d+", "123abc")
    r2 = re.match(r"\d+", "abc123")
    print("match开头匹配:", r1, r2)

# 3. re.search 全文找第一个匹配
def demo_search():
    res = re.search(r"\d+", "abc123def456")
    print("search首个匹配:", res.group())

# 4. re.fullmatch 整串完全匹配
def demo_fullmatch():
    r1 = re.fullmatch(r"\d+", "666888")
    r2 = re.fullmatch(r"\d+", "666abc")
    print("fullmatch全匹配:", r1, r2)

# 5. re.findall 获取全部匹配，返回列表
def demo_findall():
    res = re.findall(r"\d+", "a1b2c3d4")
    print("findall所有匹配:", res)

# 6. re.finditer 返回迭代器
def demo_finditer():
    it = re.finditer(r"\d+", "a1b2c3")
    for item in it:
        print("finditer迭代匹配:", item.group())

# 7. re.split 按正则分割字符串
def demo_split():
    res = re.split(r"\d+", "a1b2c3d")
    print("split分割结果:", res)

# 8. re.sub 文本替换
def demo_sub():
    res = re.sub(r"\d+", "***", "a1b2c3")
    print("sub替换结果:", res)

# 9. re.subn 替换+统计次数
def demo_subn():
    new_str, cnt = re.subn(r"\d+", "***", "a1b2c3")
    print("subn结果与次数:", new_str, cnt)

# 10. re.escape 自动转义特殊字符
def demo_escape():
    raw = re.escape("a.b*c+d(123)")
    print("escape转义字符串:", raw)

# Match对象所有方法演示
def demo_match_obj():
    m = re.search(r"(?P<num>\d+)(?P<word>[a-z]+)", "123abc")
    print("group整体匹配:", m.group())
    print("group分组1:", m.group(1))
    print("group命名分组:", m.group("num"))
    print("groups全部分组:", m.groups())
    print("groupdict命名字典:", m.groupdict())
    print("span起止位置:", m.span())
    print("start起始下标:", m.start())
    print("end结束下标:", m.end())

# 统一运行所有案例
if __name__ == "__main__":
    demo_compile()
    demo_match()
    demo_search()
    demo_fullmatch()
    demo_findall()
    demo_finditer()
    demo_split()
    demo_sub()
    demo_subn()
    demo_escape()
    demo_match_obj()
