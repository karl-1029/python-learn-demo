"""
pandas 是Python数据分析核心库，基于numpy，用来做表格型数据处理，
可以加载csv/excel，筛选、分组、合并、统计数据，是数据分析、AI预处理常用库

【常用方法清单】
pd.DataFrame()       新建DataFrame表格（核心二维表格对象）
pd.Series()          新建Series一维序列（单列数据）
pd.read_csv()        读取csv文件，生成DataFrame
df.to_csv()          将DataFrame保存为csv
df.head(n)           查看前n行，默认前5行
df.tail(n)           查看后n行
df.info()            查看数据信息：类型、是否空值
df.describe()        统计描述：均值、最大最小、标准差等
df.loc[]             按标签（行名、列名）取值
df.iloc[]            按下标数字索引取值
df.drop()            删除行或者列
df.dropna()          删除有空值的行
df.fillna()          填充空值
df.groupby()         分组统计
df.merge()           表之间合并（类似sql join）
df.sort_values()     按指定列排序
df.value_counts()    统计元素出现次数
"""
import pandas as pd

def demo_dataframe():
    print("======== DataFrame 创建表格 ========")
    data = {
        "name": ["zhangsan", "lisi", "wangwu"],
        "age": [22, 25, 28],
        "score": [88, 92, 79]
    }
    df = pd.DataFrame(data)
    print(df)
    print("\n")
    df = pd.DataFrame(data,index=["a","b","c"])
    print(df)

def demo_series():
    print("======== Series 一维序列 ========")
    s = pd.Series([10,20,30,40], index=["a","b","c","d"])
    print(s)

def demo_head_tail():
    print("======== head / tail 查看首尾行 ========")
    df = pd.DataFrame({"num":[1,2,3,4,5,6]})
    print("head(3):\n", df.head(3))
    print("tail(2):\n", df.tail(2))

def demo_info_describe():
    print("======== info / describe 信息和统计 ========")
    df = pd.DataFrame({"a":[1,2,3,4,5], "b":[10,20,30,40,50]})
    print("df.info():")
    df.info()
    print("\n")
    print("\ndf.describe():\n", df.describe())

def demo_loc_iloc():
    print("======== loc(标签) iloc(下标) 取值 ========")
    df = pd.DataFrame([[1,2],[3,4],[5,6]], columns=["x","y"])
    print("原始df:\n", df)
    print("loc[0] 标签行0：", df.loc[0])
    print("iloc[1,1] 第1行第1列下标：", df.iloc[1,1])

def demo_drop_na_fillna():
    print("======== drop 删除、空值处理 ========")
    df = pd.DataFrame({"a":[1, None, 3], "b":[4,5, None]})
    print("原始带空值df:\n", df)
    print("dropna 删除有空的行:\n", df.dropna())
    print("fillna 填充0:\n", df.fillna(0))

def demo_groupby():
    print("======== groupby 分组 ========")
    df = pd.DataFrame({
        "class":["A","A","B","B"],
        "score":[80,90,75,85]
    })
    res = df.groupby("class")["score"].mean()
    print(res)

def demo_merge():
    print("======== merge 表合并 ========")
    df1 = pd.DataFrame({"id":[1,2,3], "name":["a","b","c"]})
    df2 = pd.DataFrame({"id":[2,3,4], "age":[20,21,22]})
    merge_df = pd.merge(df1, df2, on="id", how="inner")
    print(merge_df)

def demo_sort_value():
    print("======== sort_values 排序 ========")
    df = pd.DataFrame({"val":[5,2,9,1]})
    sort_df = df.sort_values("val", ascending=True)
    print(sort_df)

def demo_value_counts():
    print("======== value_counts 计数 ========")
    s = pd.Series(["apple","banana","apple","orange","apple"])
    print(s.value_counts())

if __name__ == "__main__":
    demo_dataframe()
    demo_series()
    demo_head_tail()
    demo_info_describe()
    demo_loc_iloc()
    demo_drop_na_fillna()
    demo_groupby()
    demo_merge()
    demo_sort_value()
    demo_value_counts()
