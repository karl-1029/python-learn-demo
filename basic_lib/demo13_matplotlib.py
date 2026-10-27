"""
matplotlib 是 Python 最基础、最主流的绘图库，是很多可视化库（如 seaborn、pandas 绘图）
的底层依赖。它可以绘制折线图、散点图、柱状图、直方图、饼图等，支持对图表的刻度、标签、
图例、颜色、布局等元素做精细控制，常用于数据分析探索、报告配图和论文出版级静态图输出。

【常用方法清单】
pyplot.plot(x, y)             绘制折线图
pyplot.scatter(x, y)          绘制散点图
pyplot.bar(x, height)         绘制柱状图
pyplot.barh(y, width)         绘制水平柱状图
pyplot.hist(data, bins)       绘制直方图（查看数据分布）
pyplot.pie(values)            绘制饼图
pyplot.title(s)               设置图表标题
pyplot.xlabel(s) / ylabel(s)  设置 x 轴 / y 轴标签
pyplot.xlim() / ylim()        设置 x 轴 / y 轴显示范围
pyplot.xticks() / yticks()    设置坐标轴刻度及刻度标签
pyplot.legend()               显示图例
pyplot.grid(True)             显示网格线
pyplot.text(x, y, s)          在指定坐标添加文字
pyplot.annotate()             添加带箭头的注释
pyplot.subplots()             创建 Figure 和 Axes 对象（面向对象画法）
pyplot.tight_layout()         自动调整子图布局，防止标签重叠
pyplot.savefig(path)          保存图片到文件
pyplot.show()                 显示图表
"""

import matplotlib
matplotlib.use("Agg")  # 无界面环境下也能运行，不弹窗

import matplotlib.pyplot as plt

# 让中文和负号正常显示（不同系统字体可能不同，这里做兼容尝试）
plt.rcParams["font.sans-serif"] = ["SimHei", "Microsoft YaHei", "Arial Unicode MS", "DejaVu Sans"]
plt.rcParams["axes.unicode_minus"] = False


def demo_plot():
    """折线图：展示趋势"""
    x = [1, 2, 3, 4, 5]
    y = [2, 4, 1, 5, 3]
    plt.figure()
    plt.plot(x, y, marker="o", color="blue", label="趋势")
    plt.title("折线图示例")
    plt.xlabel("x 轴")
    plt.ylabel("y 轴")
    plt.legend()
    plt.grid(True)
    plt.savefig("demo_plot.png")
    plt.close()
    print("plot: 已生成折线图 demo_plot.png")


def demo_scatter():
    """散点图：展示两个变量的关系"""
    x = [1, 2, 3, 4, 5]
    y = [5, 3, 4, 1, 2]
    plt.figure()
    plt.scatter(x, y, color="red", s=60)
    plt.title("散点图示例")
    plt.savefig("demo_scatter.png")
    plt.close()
    print("scatter: 已生成散点图 demo_scatter.png")


def demo_bar():
    """柱状图：比较类别大小"""
    categories = ["A", "B", "C", "D"]
    values = [10, 24, 15, 30]
    plt.figure()
    plt.bar(categories, values, color="green")
    plt.title("柱状图示例")
    plt.savefig("demo_bar.png")
    plt.close()
    print("bar: 已生成柱状图 demo_bar.png")


def demo_barh():
    """水平柱状图：类别名称较长时更友好"""
    categories = ["A", "B", "C", "D"]
    values = [10, 24, 15, 30]
    plt.figure()
    plt.barh(categories, values, color="orange")
    plt.title("水平柱状图示例")
    plt.savefig("demo_barh.png")
    plt.close()
    print("barh: 已生成水平柱状图 demo_barh.png")


def demo_hist():
    """直方图：查看数据分布"""
    data = [1, 1, 2, 2, 2, 3, 3, 4, 4, 4, 4, 5, 5, 6]
    plt.figure()
    plt.hist(data, bins=6, color="purple", edgecolor="black")
    plt.title("直方图示例")
    plt.savefig("demo_hist.png")
    plt.close()
    print("hist: 已生成直方图 demo_hist.png")


def demo_pie():
    """饼图：展示各部分占比"""
    labels = ["A", "B", "C"]
    sizes = [40, 35, 25]
    plt.figure()
    plt.pie(sizes, labels=labels, autopct="%1.1f%%")
    plt.title("饼图示例")
    plt.savefig("demo_pie.png")
    plt.close()
    print("pie: 已生成饼图 demo_pie.png")


def demo_title_labels():
    """标题与坐标轴标签"""
    plt.figure()
    plt.plot([1, 2, 3], [3, 2, 1])
    plt.title("标题设置")
    plt.xlabel("X 标签")
    plt.ylabel("Y 标签")
    plt.savefig("demo_title_labels.png")
    plt.close()
    print("title/xlabel/ylabel: 已设置标题与轴标签")


def demo_xlim_ylim():
    """设置坐标轴显示范围"""
    plt.figure()
    plt.plot([1, 2, 3, 4], [1, 4, 9, 16])
    plt.xlim(0, 5)
    plt.ylim(0, 20)
    plt.title("坐标轴范围")
    plt.savefig("demo_xlim_ylim.png")
    plt.close()
    print("xlim/ylim: 已设置坐标轴范围为 x(0,5), y(0,20)")


def demo_ticks():
    """自定义坐标轴刻度"""
    plt.figure()
    plt.plot([1, 2, 3], [10, 20, 30])
    plt.xticks([1, 2, 3], ["一", "二", "三"])
    plt.yticks([10, 20, 30], ["低", "中", "高"])
    plt.title("自定义刻度")
    plt.savefig("demo_ticks.png")
    plt.close()
    print("xticks/yticks: 已自定义刻度标签")


def demo_legend():
    """显示图例"""
    plt.figure()
    plt.plot([1, 2, 3], [1, 2, 3], label="线A")
    plt.plot([1, 2, 3], [3, 2, 1], label="线B")
    plt.legend()
    plt.title("图例示例")
    plt.savefig("demo_legend.png")
    plt.close()
    print("legend: 已显示图例")


def demo_grid():
    """显示网格线"""
    plt.figure()
    plt.plot([1, 2, 3], [2, 4, 1])
    plt.grid(True)
    plt.title("网格线示例")
    plt.savefig("demo_grid.png")
    plt.close()
    print("grid: 已显示网格线")


def demo_text():
    """在指定坐标添加文字"""
    plt.figure()
    plt.plot([1, 2, 3], [1, 2, 3])
    plt.text(2, 2, "这里是(2,2)", fontsize=12, color="red")
    plt.title("文字标注")
    plt.savefig("demo_text.png")
    plt.close()
    print("text: 已在坐标(2,2)添加文字")


def demo_annotate():
    """添加带箭头的注释"""
    plt.figure()
    plt.plot([1, 2, 3], [1, 4, 9])
    plt.annotate("峰值", xy=(3, 9), xytext=(2, 7),
                 arrowprops=dict(arrowstyle="->"))
    plt.title("箭头注释")
    plt.savefig("demo_annotate.png")
    plt.close()
    print("annotate: 已添加带箭头注释")


def demo_subplots():
    """创建多个子图（面向对象画法）"""
    fig, axes = plt.subplots(1, 2, figsize=(8, 3))
    axes[0].plot([1, 2, 3], [1, 2, 3])
    axes[0].set_title("子图1")
    axes[1].bar(["A", "B"], [3, 5])
    axes[1].set_title("子图2")
    plt.savefig("demo_subplots.png")
    plt.close()
    print("subplots: 已生成 1x2 子图")


def demo_tight_layout():
    """自动调整布局，防止标签重叠"""
    fig, axes = plt.subplots(1, 2, figsize=(8, 3))
    axes[0].plot([1, 2, 3], [1, 2, 3])
    axes[0].set_title("左图")
    axes[1].plot([1, 2, 3], [3, 2, 1])
    axes[1].set_title("右图")
    plt.tight_layout()
    plt.savefig("demo_tight_layout.png")
    plt.close()
    print("tight_layout: 已自动调整子图布局")


def demo_savefig():
    """保存图片到文件"""
    plt.figure()
    plt.plot([1, 2, 3], [3, 1, 2])
    plt.title("保存图片")
    plt.savefig("demo_savefig.png", dpi=100)
    plt.close()
    print("savefig: 已保存图片 demo_savefig.png")


def demo_show():
    """显示图表（无界面环境下仅作演示，不实际弹窗）"""
    plt.figure()
    plt.plot([1, 2, 3], [2, 3, 1])
    plt.title("show 示例")
    print("show: 调用 plt.show() 用于显示图表（当前 Agg 后端不弹窗）")
    plt.close()


if __name__ == "__main__":
    demo_plot()
    demo_scatter()
    demo_bar()
    demo_barh()
    demo_hist()
    demo_pie()
    demo_title_labels()
    demo_xlim_ylim()
    demo_ticks()
    demo_legend()
    demo_grid()
    demo_text()
    demo_annotate()
    demo_subplots()
    demo_tight_layout()
    demo_savefig()
    demo_show()