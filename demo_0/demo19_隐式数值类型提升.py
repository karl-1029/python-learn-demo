"""
隐式数值类型提升

数值运算中，Python会根据操作数的类型自动选择兼容的结果类型：
int 和 float 运算得到 float；float 和 complex 运算得到 complex。
"""

integer_value = 10
float_value = 2.5
complex_value = 1 + 3j

int_float_result = integer_value + float_value
print(f"int + float = {int_float_result}, 类型: {type(int_float_result).__name__}")

float_complex_result = float_value + complex_value
print(f"float + complex = {float_complex_result}, 类型: {type(float_complex_result).__name__}")

# 普通除法的结果始终是 float，即使两个操作数都是 int
division_result = 5 / 2
print(f"int / int = {division_result}, 类型: {type(division_result).__name__}")

# bool 是 int 的子类，因此也可以参与数值运算
bool_result = True + 2
print(f"bool + int = {bool_result}, 类型: {type(bool_result).__name__}")

# 字符串不会自动转换为数值，需要显式转换
numeric_string = "2"
converted_result = integer_value + int(numeric_string)
print(f"int + int(str) = {converted_result}, 类型: {type(converted_result).__name__}")
