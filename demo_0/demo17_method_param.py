"""
函数作为参数

"""


def add(x, y):
    return x + y


def sub(x, y):
    return x - y


def mul(x, y):
    return x * y


def div(x, y):
    return x / y


def calc(x, y, func):
    return func(x, y)


print(calc(1, 2, add))
print(calc(1, 2, sub))
print(calc(1, 2, mul))
print(calc(1, 2, div))

# 匿名参数
"""
lambda 参数列表 : 函数体
"""
print_outline = lambda: print("=======匿名函数======")
print_outline()

add_lambda_methon = lambda x, y: x + y
print(add_lambda_methon(200, 300))

# 安装元素长度排序 list
data_list = ["C++", "Python", "Java", "C", "PHP", "Go", "Ruby", "Swift"]
print(data_list)
data_list.sort()
print(data_list)
data_list.sort(key=lambda x: len(x))
print(data_list)
data_list.sort(key=lambda x: len(x), reverse=True)
print(data_list)


# 递归
# 求n的阶乘
def jiecheng(n):
    if n == 1:
        return 1
    return n * jiecheng(n - 1)


print(f"递归demo: {jiecheng(5)}")

"""
案例2：定义一个用于根据传入的一批商品信息（商品名、价格、数量）、优惠（优惠券、积分抵扣）、运费信息计算订单的总金额的函数。

具体规则如下：
1. 优惠券需要商品金额满5000才可以使用，且优惠券金额不能超过商品总价。
2. 积分抵扣需要商品总金额满5000才可以使用，100积分抵扣1元（且抵扣金额不能超过商品总价，积分只能整百抵扣）。
"""


def calc_order_price(*goods, coupon=0, deduction=0, freight=10):
    """
    计算订单总价
    :param goods: 商品信息
    :param coupon: 优惠券
    :param deduction: 积分抵扣
    :return:
    """
    total_price_list = [item["price"] * item["num"] for item in goods]
    total_cost = sum(total_price_list)

    if total_cost >= 5000 and coupon <= total_cost:
        total_cost -= coupon

    if total_cost >= 5000 and deduction // 100 <= total_cost:
        total_cost -= deduction // 100
    total_cost += freight
    return total_cost


goods_info = calc_order_price({"name": "电脑", "price": 5000, "num": 2}, {"name": "鼠标", "price": 100, "num": 2},
                              coupon=50, deduction=500, freight=10)
print(goods_info)
goods_info = calc_order_price({"name": "电脑", "price": 5000, "num": 2}, {"name": "鼠标", "price": 100, "num": 2})
print(goods_info)
