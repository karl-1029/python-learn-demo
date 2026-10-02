"""
字典
案例:
开发一个购物车管理系统，实现商品信息的添加、修改、删除、查询和统计功能。系统使用嵌套字典结构存储商品数据，通过控制台菜单与用户交互。

具体功能如下：
1．添加购物车：用户根据提示录入商品名称、以及该商品的价格、数量，保存该商品信息到购物车。
2．修改购物车：要求用户输入要修改的购物车商品名称，然后再提示输入该商品的价格、数量，输入完成后修改该商品信息。
3．删除购物车：要求用户输入要删除的购物车名称，根据名称删除购物车中的商品。
4．查询购物车：将购物车中的商品信息展示出来，格式为："商品名称：xxx，商品价格：xxx，商品数量：xxx"。
5．退出购物车

结构: shopping_cart = {"Meta80": {"price": 6999, "num": 2}, "鼠标": {...}}
"""

menu = """
########## 购物车系统 ##########
#        1. 添加购物车         #
#        2. 修改购物车         #
#        3. 删除购物车         #
#        4. 查询购物车         #
#        5. 退出购物车         #
##############################
"""
shopping_cart = {}

while True:
    print(menu)

    choice = input("请输入选项：")
    match choice:
        case "1":
            name = input("请输入商品名称：")
            price = input("请输入商品价格：")
            num = input("请输入商品数量：")
            if name in shopping_cart:
                print("商品已经存在,重新选择")
            else:
                shopping_cart[name] = {"price": price, "num": num}
                print("添加商品成功")
        case "2":
            name = input("请输入商品名称：")
            if name not in shopping_cart:
                print("商品不存在,重新选择")
                continue

            price = input("请输入商品价格：")
            num = input("请输入商品数量：")
            shopping_cart[name] = {"price": price, "num": num}
            print("修改商品成功")
        case "3":
            name = input("请输入商品名称：")
            if name not in shopping_cart:
                print("商品不存在,重新选择")
                continue

            del shopping_cart[name]
            print("删除商品成功")
        case "4":
            for name in shopping_cart.keys():
                goods_info = shopping_cart[name]
                price = goods_info["price"]
                num = goods_info["num"]
                print(f"商品名称：{name}，商品价格：{price}，商品数量：{num}")
        case "5":
            print("bye 退出购物车")
            break
        case _:
            pass