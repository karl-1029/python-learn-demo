"""
一、json模块是什么？
JSON（JavaScript Object Notation）：轻量级文本数据交换格式，跨语言通用，常用于接口传输、配置文件保存。
python内置json模块：实现【序列化】与【反序列化】，不需要pip安装，直接import json。

两个核心概念：
1. 序列化（编码）：Python对象 → JSON字符串 / 写入JSON文件
2. 反序列化（解码）：JSON字符串 / JSON文件 → Python对象

Python与JSON类型对应：
dict <=> object；list/tuple <=> array；str <=> string；int/float <=> number；True <=> true；False <=> false；None <=> null
"""
import json

# ====================== 方法清单（含功能含义）======================
# 【序列化 4个核心】
# 1. json.dumps()   Python对象 → JSON字符串（内存字符串，不操作文件）
#    参数：indent=缩进；ensure_ascii=False 正常显示中文；sort_keys=True 字典按键排序
# 2. json.dump()    Python对象 → 直接写入JSON文件（操作文件对象fp）
# 3. default参数    自定义序列化：处理无法直接转JSON的对象（日期、自定义类）
# 4. JSONEncoder    编码器类，底层自定义序列化

# 【反序列化 3个核心】
# 1. json.loads()   JSON字符串 → Python对象（读取字符串）
# 2. json.load()    读取JSON文件 → Python对象（读取文件fp）
# 3. object_hook    自定义解析，把字典转为自定义对象

# 【高频易错点】
# JSON里只能用双引号""，不能用单引号''；不支持元组、datetime、自定义对象直接序列化
# 1. 接口收发 json 字符串：`dumps` + `loads`
# 2. 读写本地配置文件：`dump` + `load`
# 3. 中文不乱码：必须加上 `ensure_ascii=False`
# 4. 格式化输出：加上 `indent=4`
# =================================================================

if __name__ == '__main__':
    # 原始Python字典数据
    py_data = {
        "name": "张三",
        "age": 22,
        "hobby": ["看书", "跑步"],
        "is_student": True,
        "address": None
    }

    # ========== 1. dumps：对象转JSON字符串（最常用） ==========
    print("1. json.dumps() 序列化到字符串")
    json_str = json.dumps(py_data, ensure_ascii=False)
    print(json_str)
    # ensure_ascii=False：中文不变成\u编码；indent=4：格式化缩进；sort_keys：按键排序

    # ========== 2. loads：JSON字符串转回Python对象 ==========
    print("\n2. json.loads() 字符串反序列化为Python对象")
    parse_data = json.loads(json_str)
    print(f"解析后类型：{type(parse_data)}，姓名：{parse_data['name']}")

    # ========== 3. dump：把对象直接写入json文件 ==========
    print("\n3. json.dump() 把数据写入test.json文件")
    with open("test.json", "w", encoding="utf-8") as f:
        json.dump(py_data, f, ensure_ascii=False, indent=4)

    # ========== 4. load：读取json文件，转为Python对象 ==========
    print("\n4. json.load() 读取json文件")
    with open("test.json", "r", encoding="utf-8") as f:
        file_data = json.load(f)
    print(file_data["hobby"])

    # ========== 5. 扩展：自定义序列化（处理无法直接转换的对象） ==========
    print("\n5. default自定义序列化（处理日期/自定义对象）")
    from datetime import datetime
    time_data = {"time": datetime.now()}

    def serialize_obj(obj):
        # 遇到datetime就转字符串
        if isinstance(obj, datetime):
            return obj.strftime("%Y-%m-%d %H:%M:%S")
        raise TypeError("无法序列化该对象")

    time_json = json.dumps(time_data, default=serialize_obj, ensure_ascii=False)
    print(time_json)

    # ========== 6. object_hook：反序列化自动转为自定义对象 ==========
    print("\n6. object_hook 自定义解析字典")
    json_text = '{"name":"李四","score":90}'

    class Student:
        def __init__(self, name, score):
            self.name = name
            self.score = score

    def dict_to_student(d):
        return Student(**d)

    stu = json.loads(json_text, object_hook=dict_to_student)
    print(f"学生姓名：{stu.name}，分数：{stu.score}")

    print("\n===== json模块全部常用方法演示完成 =====")
