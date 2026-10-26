"""
pymysql 模块说明：
pymysql 是一个纯 Python 实现的 MySQL 客户端库。用于在 Python 中连接 MySQL 数据库，
并执行 SQL 语句（增删改查）。它完全兼容 Python 的 DB-API 2.0 规范，安装简单，无需编译，
是目前 Python 操作 MySQL 最常用、最轻量的驱动之一。

【常用方法清单】
1. pymysql.connect() : 建立与 MySQL 数据库的连接，返回 Connection 对象。
2. conn.cursor() : 创建一个游标对象（Cursor），用于执行 SQL 语句和获取结果。
3. cursor.execute() : 执行单条 SQL 语句（支持传入参数防止 SQL 注入）。
4. cursor.fetchone() : 从查询结果中获取下一行数据（返回元组）。
5. cursor.fetchall() : 从查询结果中获取所有剩余行数据（返回元组列表）。
6. conn.commit() : 提交事务，将增删改操作真正写入数据库（查询不需要）。
7. conn.rollback() : 回滚事务，撤销自上次提交以来的所有操作。
8. conn.close() : 关闭数据库连接，释放资源。
"""

import pymysql

# ⚠️ 注意：运行以下代码前，请确保你本地启动了 MySQL 服务，并且替换以下配置为你自己的数据库信息
DB_CONFIG = {
    'host': 'localhost',
    'port': 3306,
    'user': 'root',
    'password': '123456',  # 请替换为你的真实密码
    'database': 'test_db',  # 请替换为你实际存在的数据库名
    'charset': 'utf8mb4'
}


def demo_connect_and_create_table():
    """演示 1: 建立连接 (connect) 并执行建表语句 (execute)"""
    print("--- 1. 建立连接与执行建表 ---")
    try:
        # 1. 建立连接
        conn = pymysql.connect(**DB_CONFIG)
        print("数据库连接成功！")

        # 2. 获取游标并使用 with 语句自动管理
        with conn.cursor() as cursor:
            # 3. 执行 SQL 建表
            create_sql = """
                         CREATE TABLE IF NOT EXISTS demo_users \
                         ( \
                             id \
                             INT \
                             AUTO_INCREMENT \
                             PRIMARY \
                             KEY, \
                             name \
                             VARCHAR \
                         ( \
                             50 \
                         ) NOT NULL,
                             age INT
                             ) \
                         """
            cursor.execute(create_sql)
            print("建表语句执行成功！")

    except pymysql.MySQLError as e:
        print(f"发生错误: {e}")
    finally:
        if 'conn' in locals() and conn.open:
            conn.close()
            print("连接已关闭。\n")


def demo_insert_and_commit():
    """演示 2: 插入数据 (execute) 并提交事务 (commit)"""
    print("--- 2. 插入数据与提交事务 ---")
    try:
        conn = pymysql.connect(**DB_CONFIG)
        with conn.cursor() as cursor:
            # 使用 %s 占位符，防止 SQL 注入
            insert_sql = "INSERT INTO demo_users (name, age) VALUES (%s, %s)"

            # 插入单条
            cursor.execute(insert_sql, ("张三", 25))

            # 插入多条 (executemany 是游标的进阶常用方法)
            cursor.executemany(insert_sql, [("李四", 30), ("王五", 28)])

            # 提交事务（写操作必须 commit）
            conn.commit()
            print(f"成功插入 {cursor.rowcount} 条数据，并已 commit。")

    except pymysql.MySQLError as e:
        if 'conn' in locals() and conn.open:
            conn.rollback()  # 发生异常时回滚
        print(f"发生错误，已回滚: {e}")
    finally:
        if 'conn' in locals() and conn.open:
            conn.close()
            print("连接已关闭。\n")


def demo_select_fetchall():
    """演示 3: 查询数据并获取所有结果 (fetchall)"""
    print("--- 3. 查询数据 (fetchall) ---")
    try:
        conn = pymysql.connect(**DB_CONFIG)
        with conn.cursor() as cursor:
            select_sql = "SELECT id, name, age FROM demo_users"
            cursor.execute(select_sql)

            # fetchall 获取所有结果，返回一个元组列表
            results = cursor.fetchall()
            print("查询结果如下：")
            for row in results:
                print(f"ID: {row[0]}, 姓名: {row[1]}, 年龄: {row[2]}")

    except pymysql.MySQLError as e:
        print(f"发生错误: {e}")
    finally:
        if 'conn' in locals() and conn.open:
            conn.close()
            print("连接已关闭。\n")


def demo_select_fetchone():
    """演示 4: 获取单条结果 (fetchone) 与 字典游标 (DictCursor)"""
    print("--- 4. 查询单条数据 (fetchone) ---")
    try:
        conn = pymysql.connect(**DB_CONFIG)
        # 传入 DictCursor 可以让结果变成字典而不是元组，方便按列名取值
        with conn.cursor(pymysql.cursors.DictCursor) as cursor:
            select_sql = "SELECT * FROM demo_users WHERE age > %s LIMIT 1"
            cursor.execute(select_sql, (20,))

            # fetchone 只取第一条，返回一个元组（或字典）
            result = cursor.fetchone()
            if result:
                print(f"获取到的单条数据: {result}")
                print(f"直接通过键名获取姓名: {result['name']}")
            else:
                print("未查询到数据。")

    except pymysql.MySQLError as e:
        print(f"发生错误: {e}")
    finally:
        if 'conn' in locals() and conn.open:
            conn.close()
            print("连接已关闭。\n")


def demo_update_and_delete():
    """演示 5: 更新与删除数据"""
    print("--- 5. 更新与删除数据 ---")
    try:
        conn = pymysql.connect(**DB_CONFIG)
        with conn.cursor() as cursor:
            # 更新
            update_sql = "UPDATE demo_users SET age = %s WHERE name = %s"
            affected = cursor.execute(update_sql, (26, "张三"))
            print(f"更新操作影响了 {affected} 行。")

            # 删除
            delete_sql = "DELETE FROM demo_users WHERE name = %s"
            affected = cursor.execute(delete_sql, ("王五",))
            print(f"删除操作影响了 {affected} 行。")

            conn.commit()
            print("更新与删除已提交。")

    except pymysql.MySQLError as e:
        if 'conn' in locals() and conn.open:
            conn.rollback()
        print(f"发生错误，已回滚: {e}")
    finally:
        if 'conn' in locals() and conn.open:
            conn.close()
            print("连接已关闭。\n")


if __name__ == "__main__":
    print("开始运行 pymysql 学习演示...\n")

    # 按顺序执行演示流程
    demo_connect_and_create_table()
    demo_insert_and_commit()
    demo_select_fetchall()
    demo_select_fetchone()
    demo_update_and_delete()

    print("所有演示完成！")