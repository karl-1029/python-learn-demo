"""
在 LangChain 中，“上下文与记忆（Context & Memory）”模块用于让无状态的 LLM 具备“记住”历史对话的能力。
它的核心用途是将多轮对话的历史记录（Context）保存下来，并在下一次请求时自动拼接到 Prompt 中，使模型能够理解上下文语境。

【常用方法清单】

关键步骤说明
第1步：初始化记忆引擎：checkpointer = InMemorySaver() ——创建一个内存级的记忆存储。
注意：InMemorySaver内存中保存，进程结束就丢失数据，适合测试。生产环境可换成数据库持久化的 SqliteSaver、PostgresSaver 等
第2步：绑定Agent：在 create_agent 时传入 checkpointer，让 Agent 具备状态存储能力。
第3步：设定会话ID：通过 config = {"configurable": {"thread_id": "1"}} 为每次调用指定线程标识。同一个thread_id共享记忆，不同thread_id完全隔离。


"""
import json

from langchain.chat_models import init_chat_model
from dotenv import load_dotenv
import os
from langgraph.checkpoint.memory import InMemorySaver
from langchain.agents import create_agent
from langchain_core.messages import HumanMessage, AIMessage

# 从.env文件中加载环境变量
load_dotenv(override=True)

model_name = os.getenv("DEEPSEEK_MODEL")
llm = init_chat_model(model_name, temperature=0.7)

agent = create_agent(
    model=llm,
    tools=[],
)


def demo_memory_1():
    messages1 = [
        HumanMessage("你好，我叫小明"),
        AIMessage("很高兴认识你，小明"),
        HumanMessage("你用一句话介绍下你自己"),
    ]
    response1 = agent.invoke({"messages": messages1})

    for msg in response1["messages"]:
        msg.pretty_print()

    # 发现AI是没有记忆的
    messages2 = [HumanMessage("我叫什么名字？")]
    response2 = agent.invoke({"messages": messages2})

    for msg in response2["messages"]:
        msg.pretty_print()


def demo_memory_2():
    messages3 = [
        HumanMessage("你好，我叫小明"),
        AIMessage("很高兴认识你，小明"),
        HumanMessage("你用一句话介绍下你自己"),
        AIMessage("我是一个由 OpenAI 训练的人工智能助手，可以帮你回答问题、写作和解决各种任务。"),
        HumanMessage("我叫什么名字？")
    ]
    # 转换为字典
    messages_dict = [msg.dict() for msg in messages3]
    print(json.dumps(messages_dict, ensure_ascii=False, indent=2))

    response3 = agent.invoke({"messages": messages3})

    for msg in response3["messages"]:
        msg.pretty_print()


def demo_inmemorysaver():
    agent = create_agent(
        model=llm,
        tools=[]
    )

    print("第一轮对话：")
    response1 = agent.invoke({
        "messages": [HumanMessage("我叫张三")]
    })
    print(f"Agent: {response1['messages'][-1].content}")

    print("第二轮对话：")
    response2 = agent.invoke({
        "messages": [HumanMessage("我叫什么？")]
    })
    print(f"Agent: {response2['messages'][-1].content}")

    checkpointer = InMemorySaver()

    print("\n\n使用内存管理器=============\n\n")
    # 说明：你只需传入 checkpointer 和 config，Agent 就能自然具备连续对话能力。



    # 1. 创建 Agent 时添加 checkpointer
    """
    此时，checkpointer 自动：同一进程内有效（不支持跨进程共享）
        ① 读取之前的历史
        ② 追加新消息
        ③ 调用模型（传入完整历史）
        ④ 保存新的历史
        说明：checkpointer 会自动管理历史
    """
    agent = create_agent(
        model=llm,
        checkpointer=checkpointer  # 添加内存管理
    )

    # 2. 调用时指定 thread_id
    config = {
        "configurable": {
            "thread_id": "1"
        }
    }

    print("第一轮对话：")
    response1 = agent.invoke({
        "messages": [HumanMessage("我叫张三")]},
        config=config  # 传入 config
    )
    print(f"Agent: {response1['messages'][-1].content}")

    print("第二轮对话：")
    response2 = agent.invoke({
        "messages": [HumanMessage("我叫什么？")]},
        config=config  # 使用相同的 thread_id
    )
    print(f"Agent: {response2['messages'][-1].content}")

    latest_state = agent.get_state(config)
    print(json.dumps(latest_state, indent=4, ensure_ascii=False, default=str))

    print("第三轮对话：")
    response3 = agent.invoke({
        "messages": [HumanMessage("我刚才问了什么问题？")]},
        config=config  # 使用相同的 thread_id
    )
    print(f"Agent: {response3['messages'][-1].content}")

    # 说明：第三轮对话中的 "我刚才问了什么问题？" 就能在第二轮存储的消息历史中找到答案。
    # 所有消息历史都会自动追加到 AgentState 的 messages 字段中，无需手动维护。
    latest_state = agent.get_state(config)
    print(json.dumps(latest_state, indent=4, ensure_ascii=False, default=str))

    # 说明：thread_id 隔离不同会话空间。
    print("第三轮对话 切换 thread_id：")
    config2 = {
        "configurable": {
            "thread_id": "2"
        }
    }
    response4 = agent.invoke(
        {"messages": [HumanMessage("你还记得我叫什么名字么？")]},
        config=config2
    )
    print(response4['messages'][-1].content)




def demo_inmemorysaver_diff_thread_id():
    """
    场景1：多用户聊天
    不同 thread_id = 不同会话，Agent 能正确记住每个会话的内容。
    """
    checkpointer = InMemorySaver()
    # 1. 创建 Agent 时添加 checkpointer
    agent = create_agent(
        model=llm,
        checkpointer=checkpointer  # 添加内存管理
    )

    # 2. 区分不通用户
    config_alice = {"configurable": {"thread_id": "user_alice"}}
    config_bob = {"configurable": {"thread_id": "user_bob"}}

    base_messages = [HumanMessage("请你记住，你现在是一个严格的面试官。")]

    # 用户 Alice
    agent.invoke({"messages": [*base_messages, HumanMessage("我叫Alice")]}, config=config_alice)
    # 用户 Bob
    agent.invoke({"messages": [*base_messages, HumanMessage("我叫bob")]}, config=config_bob)

    print("Alice和李四已完成初始化并自我介绍。")
    print("\n\n=============================")

    # ================= 第二步：测试记忆隔离 =================
    print("\n--- 第二步：分别提问，测试记忆 ---")

    # Alice 提问（完全独立的新消息）
    response_alice = agent.invoke(
        {"messages": [HumanMessage("我叫什么名字？我有什么设定？")]},
        config=config_alice
    )
    print(f"Alice 的回复: {response_alice['messages'][-1].content}")

    # Bob 提问（完全独立的新消息）
    response_bob = agent.invoke(
        {"messages": [HumanMessage("我叫什么名字？我有什么设定？")]},
        config=config_bob
    )
    print(f"Bob 的回复: {response_bob['messages'][-1].content}")




if __name__ == "__main__":
    # demo_memory_1()
    # demo_memory_2()
    # demo_inmemorysaver()
    demo_inmemorysaver_diff_thread_id()

