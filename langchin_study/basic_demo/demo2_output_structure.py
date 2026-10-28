"""
【LangChain Output Parsers 模块简介】
Output Parsers（输出解析器）是 LangChain 中用于处理大模型返回结果的核心模块。
由于大模型默认返回的都是纯文本字符串，但在实际开发中，我们往往需要结构化的数据（如 JSON、Pydantic 对象、列表等）。
该模块的主要用途就是：**提供提示词格式化（引导模型输出特定格式）** 和 **结果解析（将文本转回结构化数据）**，确保数据能够被后续程序准确消费。

【常用方法清单】
1. StrOutputParser()            : 最基础的字符串解析器，直接提取 AIMessage 的 content 字段。
2. JsonOutputParser()           : JSON 解析器，引导模型输出 JSON，并解析为 Python 字典 (dict)。
3. CommaSeparatedListOutputParser() : 逗号分隔列表解析器，引导模型输出列表格式，并解析为 Python 列表 (list)。
4. PydanticOutputParser()       : Pydantic 解析器，根据定义的 Pydantic 模型，将输出解析为强类型的对象。
5. get_format_instructions()    : 获取格式化指令，将解析器要求的格式说明注入到 Prompt 中。


langchain chain式调用
    # prompt | llm 这种写法叫做 LCEL（LangChain Expression Language）
    # | 是 Python 的"按位或"运算符，LangChain 重载了它，用于连接组件


阶段②：结构化输出 with_structured_output（Pydantic schema）
"""
from langchain.chat_models import init_chat_model
from langchain_core.output_parsers import (
    StrOutputParser,
    JsonOutputParser, PydanticOutputParser, CommaSeparatedListOutputParser,
)
from langchain_core.prompts import ChatPromptTemplate
from pydantic import BaseModel, Field

# 初始化模型（演示用）
llm = init_chat_model(model="deepseek-flash", temperature=0.7, )


def demo_str_output_parser():
    """1. StrOutputParser：最基础的字符串提取。"""
    print("--- 1. StrOutputParser 示例 ---")

    template = ChatPromptTemplate.from_template("写一句关于{subject}的诗")
    message = template.format(subject="月亮")
    response = llm.invoke(message)
    result = StrOutputParser().invoke(response)
    print(f"返回类型: {type(result)}")
    print(f"返回内容: {result}")

    # 当 llm.invoke 返回 AIMessage 时，StrOutputParser 可以自动提取其中的 .content
    # langchin chin式调用
    prompt = ChatPromptTemplate.from_template("写一句关于{subject}的诗")
    chain = prompt | llm | StrOutputParser()
    result = chain.invoke({"subject": "月亮"})

    print(f"返回类型: {type(result)}")
    print(f"返回内容: {result}")
    print("\n")


def demo_json_output_parser():
    """2. JsonOutputParser：解析为 Python 字典。"""
    print("--- 2. JsonOutputParser 示例 ---")
    parser = JsonOutputParser()
    print(f"解析器格式说明: {parser.get_format_instructions()}")

    # 关键：在 Prompt 中注入解析器的格式要求，让模型知道必须输出 JSON
    prompt = ChatPromptTemplate.from_messages([
        ("system", "你是一个数据提取助手。{format_instructions}"),
        ("human", "提取以下文本中的人物信息：张三今年25岁，是一名程序员。")
    ])

    # 将 format_instructions 传入 Prompt
    chain = prompt | llm | parser
    result = chain.invoke({"format_instructions": parser.get_format_instructions()})

    print(f"返回类型: {type(result)}")
    print(result)
    print(result.get("name"))
    print("\n")

    class Person(BaseModel):
        name: str = Field(description="人物名称")
        age: int = Field(description="人物年龄")

    parser = JsonOutputParser(pydantic_object=Person)
    print(f"解析器格式说明: {parser.get_format_instructions()}")
    chain = prompt | llm | parser
    result = chain.invoke({"format_instructions": parser.get_format_instructions()})

    print(f"返回类型: {type(result)}")
    print(result)
    print(result.get("name"))
    print("\n")


def demo_comma_list_output_parser():
    """3. CommaSeparatedListOutputParser：解析为 Python 列表。"""
    print("--- 3. CommaSeparatedListOutputParser 示例 ---")
    parser = CommaSeparatedListOutputParser()

    prompt = ChatPromptTemplate.from_messages([
        ("system", "{format_instructions}"),
        ("human", "列出三种常见的水果。")
    ])

    chain = prompt | llm | parser
    result = chain.invoke({"format_instructions": parser.get_format_instructions()})

    print(f"返回类型: {type(result)}")
    print(f"列表内容: {result}")
    print("\n")


def demo_pydantic_output_parser():
    """4. PydanticOutputParser：解析为强类型对象。"""
    print("--- 4. PydanticOutputParser 示例 ---")

    # 1. 定义期望的数据结构
    class BookInfo(BaseModel):
        title: str = Field(description="书名")
        author: str = Field(description="作者")
        year: int = Field(description="出版年份")

    # 2. 实例化解析器
    parser = PydanticOutputParser(pydantic_object=BookInfo)

    prompt = ChatPromptTemplate.from_messages([
        ("system", "你是一个图书管理员。{format_instructions}"),
        ("human", "提取《三体》的信息，作者是刘慈欣，2008年出版。")
    ])

    chain = prompt | llm | parser
    result = chain.invoke({"format_instructions": parser.get_format_instructions()})

    print(f"返回类型: {type(result)}")
    # 可以直接用点号访问属性，IDE 会有代码提示
    print(f"书名: {result.title}, 作者: {result.author}, 年份: {result.year}")
    print("\n")


class BookReview(BaseModel):
    title: str = Field(description="书名")
    score: int = Field(description="评分 0-10")
    summary: str = Field(description="一句话总结")


llm_disable_thinking = init_chat_model(model="deepseek-flash",
                                       temperature=0.7,
                                       # 关键：关闭思考模式
                                       extra_body={"thinking": {"type": "disabled"}})


# deepseek 定义大模型的时候关闭了思考模式
def demo_with_structured_output_auto_parser():
    structured = llm_disable_thinking.with_structured_output(BookReview)
    result = structured.invoke("评价一下刘慈欣的《三体》")
    print(type(result))
    print(result)


if __name__ == "__main__":
    # demo_str_output_parser()
    # demo_json_output_parser()
    # demo_comma_list_output_parser()
    # demo_pydantic_output_parser()
    demo_with_structured_output_auto_parser()
