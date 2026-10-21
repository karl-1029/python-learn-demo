import os

"""
os 模块：操作操作系统（文件、文件夹、系统命令）

os模块综合练习脚本
所有方法都附带中文注释说明，运行后自动生成测试目录，最后自动清理，不会遗留文件


# ====================== 方法清单（带功能说明）======================
# os 模块核心方法：
# os.getcwd()      获取当前工作目录
# os.mkdir()       创建单层文件夹，不能创建多级目录
# os.makedirs()    递归创建多层文件夹，支持多级路径
# os.rename()      文件/文件夹重命名，也可以实现移动文件
# os.remove()      删除文件，只能删除文件，不能删文件夹
# os.rmdir()       删除空文件夹，仅能删除空目录
# os.listdir()     列出当前目录下所有文件与文件夹名称（仅名称，非全路径）
# os.walk()        递归遍历目录，自动遍历所有子文件夹下的文件
# os.getenv()      获取系统环境变量
# os.name          获取操作系统类型：nt=Windows，posix=Linux/Mac

# os.path 子模块核心方法：
# os.path.join()   拼接路径，自动适配Windows与Linux分隔符（跨平台首选）
# os.path.exists() 判断路径是否存在（文件/文件夹都可以判断）
# os.path.isdir()  判断路径是否为文件夹
# os.path.isfile() 判断路径是否为普通文件
# os.path.abspath() 获取文件绝对完整路径
# os.path.dirname() 获取文件所在父目录
# os.path.basename() 获取路径末尾的文件名（带后缀）
# os.path.splitext() 拆分文件名与后缀，返回(文件名, 后缀)
# =================================================================
"""



if __name__ == '__main__':
    print("===== OS 模块学习演示开始 =====")

    # 1. os.getcwd()：获取脚本当前工作目录
    current_work_dir = os.getcwd()
    print(f"\n1. os.getcwd() 当前工作目录：{current_work_dir}")

    # 2. os.path.abspath()：获取脚本自身绝对路径
    script_full_path = os.path.abspath(__file__)
    # os.path.dirname()：获取文件所在文件夹
    script_folder = os.path.dirname(script_full_path)
    print(f"2. os.path.abspath() 脚本完整路径：{script_full_path}")
    print(f"   os.path.dirname() 脚本所在文件夹：{script_folder}")

    # 3. os.path.join()：跨平台路径拼接
    base_test_dir = os.path.join(script_folder, "test_os")
    level2_dir = os.path.join(base_test_dir, "folder1")
    level3_dir = os.path.join(level2_dir, "folder2")
    print(f"\n3. os.path.join() 拼接测试根目录：{base_test_dir} {level2_dir} {level3_dir}")

    # 4. os.makedirs()：递归创建多层目录，exist_ok=True 目录已存在不报错
    os.makedirs(level3_dir, exist_ok=True)
    print("4. os.makedirs() 递归创建多层文件夹完成")

    # 5. os.mkdir()：仅创建单层文件夹，无法创建多级目录
    single_dir = os.path.join(base_test_dir, "single_folder")
    os.mkdir(single_dir)
    print("5. os.mkdir() 创建单层文件夹：single_folder")

    # 6. os.path.exists()：判断路径是否存在
    if os.path.exists(base_test_dir):
        print(f"6. os.path.exists()：{base_test_dir} 路径存在")

    # 7. os.path.isdir()：判断路径是否为文件夹
    if os.path.isdir(level2_dir):
        print(f"7. os.path.isdir()：{level2_dir} 是文件夹")

    # 8. 创建测试文件
    file1 = os.path.join(base_test_dir, "note.txt")
    with open(file1, "w", encoding="utf-8") as f:
        f.write("os module test content\nhello python")
    print(f"\n8. 创建测试文件：{file1}")

    # 9. os.path.isfile()：判断路径是否为普通文件
    if os.path.isfile(file1):
        print(f"9. os.path.isfile()：{file1} 是文件")

    # 10. basename / dirname / splitext 路径拆分
    # os.path.basename()：获取文件名（带后缀）
    file_name = os.path.basename(file1)
    # os.path.dirname()：获取父目录
    file_parent = os.path.dirname(file1)
    # os.path.splitext()：拆分文件名和扩展名
    name_no_suffix, suffix = os.path.splitext(file1)
    print(f"\n10. os.path.basename() 文件名：{file_name}")
    print(f"    os.path.dirname() 父目录：{file_parent}")
    print(f"    os.path.splitext() 拆分：名字={name_no_suffix}, 后缀={suffix}")

    # 11. os.listdir()：列出目录下所有条目（只返回名称，不是全路径）
    print(f"\n11. os.listdir() 列出 {base_test_dir} 里面内容：")
    print(os.listdir(base_test_dir))

    # 12. os.rename()：重命名文件，也可以移动文件
    new_file = os.path.join(base_test_dir, "note_rename.txt")
    os.rename(file1, new_file)
    print(f"\n12. os.rename() 重命名：note.txt -> note_rename.txt")

    # 13. os.walk()：递归遍历所有子目录与文件（面试高频）
    print("\n13. os.walk() 递归遍历全部文件：")
    for (root, dirs, files)  in os.walk(base_test_dir):
        for filename in files:
            full_path = os.path.join(root, filename)
            print(f"       {full_path}")

    # 14. os.getenv()：读取系统环境变量
    home_path = os.getenv("PATH")
    print(f"\n14. os.getenv() 获取环境变量PATH（前80字符）：{home_path[:80]}...")

    # 15. os.name：获取当前操作系统标识
    print(f"15. os.name 系统标记：{os.name} （nt=Windows，posix=Linux/Mac）")

    # ============ 清理资源（os.rmdir只能删除空文件夹！必须由内向外删除） ============
    print("\n===== 开始清理测试文件和文件夹 =====")
    # os.remove()：删除文件，只能删除文件
    if os.path.exists(new_file):
        os.remove(new_file)
        print(f"os.remove() 删除文件：{new_file}")

    # os.rmdir()：逐层删除空目录，必须先删内层再删外层
    os.rmdir(level3_dir)
    os.rmdir(level2_dir)
    os.rmdir(single_dir)
    os.rmdir(base_test_dir)
    print("os.rmdir() 逐层删除所有空文件夹，清理完成！")

    print("\n===== 演示全部结束 =====")
