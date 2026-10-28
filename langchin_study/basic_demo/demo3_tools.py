"""
【LangChain Tools 模块简介】
LangChain 的 Tools（工具）模块是构建智能体（Agent）的核心基石。
大语言模型（LLM）本身只能生成文本，无法直接联网、查数据库或执行代码。Tools 模块允许开发者将普通的 Python 函数（或 API 接口）封装成模型能够理解的“工具”。
大模型通过分析用户的意图，决定是否调用某个工具、提取工具所需的参数，由框架执行工具后，再将结果返回给大模型进行最终总结。

【常用方法清单】
1. @tool 装饰器                 : 最常用的方式，将普通 Python 函数直接转换为 LangChain 工具，函数的文档字符串（Docstring）会自动变成工具描述。
2. Tool(...) 构造类             : 传统的构造方式，需要手动传入工具名称、执行函数、描述信息。
3. StructuredTool.from_function() : 支持复杂参数结构（如 Pydantic 模型）的工具构造方式。
4. tools 列表绑定模型           : 使用 llm.bind_tools([...]) 将工具告知大模型，使其具备调用能力。
"""
from langchain.chat_models import init_chat_model
from langchain_core.tools import tool, Tool, StructuredTool
from pydantic import BaseModel, Field

# 初始化模型（演示用，temperature=0 保证输出稳定）
llm = init_chat_model(model="deepseek-flash", temperature=0.7)


def demo_tool_decorator():
    """1. @tool 装饰器：最快、最现代的定义方式。"""
    print("--- 1. @tool 装饰器 示例 ---")

    # 使用 @tool 装饰器，函数名变成工具名，Docstring 变成工具描述
    @tool
    def get_weather(city: str) -> str:
        """查询指定城市的天气情况"""
        # 模拟实际业务逻辑
        return f"{city}今天天气晴朗，气温25度。"

    # 查看工具的基本信息
    print(f"工具名称: {get_weather.name}")
    print(f"工具描述: {get_weather.description}")

    # 直接执行工具
    result = get_weather.invoke("北京")
    print(f"执行结果: {result}")
    print("\n")


def demo_tool_class():
    """2. Tool 构造类：传统且灵活的构造方式。"""
    print("--- 2. Tool 构造类 示例 ---")

    def search_web(query: str) -> str:
        return f"关于'{query}'的搜索结果：LangChain是一个强大的框架。"

    # 手动指定名称、绑定的函数和描述
    search_tool = Tool(
        name="web_search",
        func=search_web,
        description="当需要搜索最新资讯或未知信息时使用此工具。输入应为搜索关键词。"
    )

    print(f"工具名称: {search_tool.name}")
    result = search_tool.invoke("什么是LangChain")
    print(f"执行结果: {result}")
    print("\n")


def demo_structured_tool():
    """3. StructuredTool：处理多参数/复杂参数的工具。"""
    print("--- 3. StructuredTool 示例 ---")

    # 当工具有多个参数时，推荐使用 Pydantic 定义参数结构
    class CalculatorInput(BaseModel):
        a: float = Field(description="第一个数字")
        b: float = Field(description="第二个数字")
        operation: str = Field(description="运算类型，例如：add, subtract, multiply")

    def calculate(a: float, b: float, operation: str) -> str:
        if operation == "add": return str(a + b)
        if operation == "subtract": return str(a - b)
        if operation == "multiply": return str(a * b)
        return "不支持的运算"

    # 从函数自动生成结构化工具
    calc_tool = StructuredTool.from_function(
        func=calculate,
        name="calculator",
        description="用于数学计算，支持加、减、乘。",
        args_schema=CalculatorInput  # 关联参数模式
    )

    # 调用时必须传入符合 Schema 的字典
    result = calc_tool.invoke({"a": 5, "b": 3, "operation": "multiply"})
    print(f"计算结果: {result}")
    print("\n")


def demo_bind_tools_to_llm():
    """4. 将工具绑定给大模型并触发调用。"""
    print("--- 4. 工具绑定与触发 示例 ---")

    @tool
    def get_stock_price(company: str) -> str:
        """获取指定公司的今日股票价格。"""
        if "阿里" in company: return "100美元"
        return "未知"

    # 将工具列表绑定给 LLM
    llm_with_tools = llm.bind_tools([get_stock_price])

    # 当用户提问时，模型如果不需调用工具，会直接回复；如果需调用，会返回 tool_calls
    response = llm_with_tools.invoke("阿里巴巴今天的股价是多少？")

    print(f"模型回复类型: {type(response)}")
    print(response.model_dump_json())
    if response.tool_calls:
        print("模型决定调用工具！")
        # 取出模型决定的工具名称和参数
        tool_call = response.tool_calls[0]
        print(f"决定调用的工具名: {tool_call['name']}")
        print(f"提取的参数: {tool_call['args']}")
    else:
        print(f"模型直接回复: {response.content}")
    print("\n")


if __name__ == "__main__":
    demo_tool_decorator()
    demo_tool_class()
    demo_structured_tool()
    demo_bind_tools_to_llm()