"""
【LangChain Prompt Templates 模块简介】
Prompt Templates（提示词模板）是 LangChain 中用于管理和复用提示词的核心模块。
在实际开发中，我们很少直接拼接字符串，而是使用模板：先定义好带占位符（如 {topic}）的字符串，
然后在调用时传入不同的变量值，动态生成最终的 Prompt。
它支持纯文本、对话（System/Human/AI）、少样本（Few-shot）以及从文件中加载等多种形式，是构建复杂链（Chain）和智能体（Agent）的基础。

【常用方法清单】
1. PromptTemplate.from_template()       : 从单字符串模板创建，适用于纯文本补全模型（LLM）。
2. PromptTemplate.format()              : 传入变量字典，将模板渲染替换为最终的字符串。
3. ChatPromptTemplate.from_messages()   : 从消息列表（如 System/Human 角色）创建，适用于聊天模型。
4. ChatPromptTemplate.format_messages() : 渲染聊天模板，返回一个包含具体消息对象的列表。
5. FewShotPromptTemplate                : 少样本提示模板，通过提供示例（Examples）引导模型。
6. MessagesPlaceholder                  : 消息占位符，用于在聊天模板中动态插入历史对话消息列表。
"""
from langchain.chat_models import init_chat_model
from langchain_core.prompts import (
    PromptTemplate,
    ChatPromptTemplate,
    FewShotChatMessagePromptTemplate,
    MessagesPlaceholder,
)
from langchain_core.messages import HumanMessage, AIMessage


llm = init_chat_model("deepseek-flash")

def demo_prompt_template():
    """1 & 2. PromptTemplate：基础文本模板与格式化。"""
    print("--- 1 & 2. PromptTemplate ---")
    # 定义带占位符的字符串模板
    template = PromptTemplate.from_template("请给我讲一个关于{topic}的笑话，字数在{limit}字以内。")

    # 传入变量进行格式化（渲染）
    formatted_prompt = template.format(topic="程序员", limit=50)

    # 注意：直接打印 template 会显示包含 {} 的原样，打印 format 后的才是最终 Prompt
    print(f"渲染后的 Prompt: {formatted_prompt}")
    print(llm.invoke(formatted_prompt).model_dump_json())
    print("\n")


def demo_chat_prompt_template():
    """3 & 4. ChatPromptTemplate：对话模板与消息渲染。"""
    print("--- 3 & 4. ChatPromptTemplate ---")
    # 定义包含角色和占位符的对话模板
    chat_template = ChatPromptTemplate.from_messages([
        ("system", "你是一个擅长{tone}的翻译官。"),
        ("human", "请把这句话翻译成英文：{text}")
    ])

    # 传入变量进行格式化（返回的是消息对象的列表）
    messages = chat_template.format_messages(tone="幽默", text="今天天气真好")

    print(f"生成的消息数量: {len(messages)}")
    for msg in messages:
        print(f"[{msg.type}] {msg.content}")
    print(llm.invoke(messages).content)
    print("\n")


def demo_few_shot_prompt():
    """5. FewShotChatMessagePromptTemplate：少样本聊天示例模板。"""
    print("--- 5. FewShotChatMessagePromptTemplate ---")
    # 1. 准备示例数据
    examples = [
        {"input": "开心", "output": "😊"},
        {"input": "伤心", "output": "😢"}
    ]

    # 2. 定义单个示例的格式
    example_prompt = ChatPromptTemplate.from_messages([
        ("human", "{input}"),
        ("ai", "{output}"),
    ])

    # 3. 构建少样本模板
    few_shot_prompt = FewShotChatMessagePromptTemplate(
        examples=examples,
        example_prompt=example_prompt,
    )

    # 完整提示词
    final_prompt = ChatPromptTemplate.from_messages([
        ("system", "根据以下示例，为最后一个词语生成表情："),
        few_shot_prompt,
        ("human", "{input}"),
    ])
    final_messages = final_prompt.format_messages(input="生气")

    # 4. 渲染最终结果
    for message in final_messages:
        print(f"[{message.type}] {message.content}")
    print(llm.invoke("").content)
    print("\n")


def demo_messages_placeholder():
    """6. MessagesPlaceholder：动态插入历史消息的占位符。"""
    print("--- 6. MessagesPlaceholder ---")
    # 定义包含历史消息占位符的模板
    prompt_with_history = ChatPromptTemplate.from_messages([
        ("system", "你是一个智能助手。"),
        # 这里的 variable_name 就是我们要传入的变量名
        MessagesPlaceholder(variable_name="history"),
        ("human", "{question}")
    ])

    # 模拟历史对话消息
    history = [
        HumanMessage(content="我叫小明。"),
        AIMessage(content="你好小明，很高兴认识你。")
    ]

    # 渲染：传入历史消息列表和当前问题
    messages = prompt_with_history.format_messages(
        history=history,
        question="我叫什么名字？"
    )

    print("渲染后的完整对话上下文：")
    for msg in messages:
        print(f"[{msg.type}] {msg.content}")

    print(llm.invoke(messages).content)
    print("\n")


if __name__ == "__main__":
    demo_prompt_template()
    demo_chat_prompt_template()
    demo_few_shot_prompt()
    demo_messages_placeholder()