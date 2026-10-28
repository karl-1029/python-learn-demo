"""
调用大模型
1. 初始化模型
2. 创建消息列表
3. 调用模型
"""

import os
import json
from dotenv import load_dotenv
from langchain.chat_models import init_chat_model
from langchain_core.messages import *

load_dotenv()  # 读取项目根目录 .env

api_key = os.getenv("DEEPSEEK_API_KEY")
base_url = os.getenv("DEEPSEEK_BASE_URL")
model_name = os.getenv("DEEPSEEK_MODEL")

llm = init_chat_model(model_name, temperature=0.7)


def demo_chat_invoke():
    messages = [
        {"role": "system", "content": "You are a helpful assistant"},
        {"role": "user", "content": "你是谁"},
    ]
    response: AIMessage = llm.invoke(
        input=messages
    )
    print(response.model_dump_json())
    print("==" * 50)


def demo_chat_invoke2():
    messages = [
        SystemMessage(content="You are a helpful assistant"),
        HumanMessage(content="你是谁")
    ]
    response = llm.invoke(
        input=messages,
    )
    print(response.model_dump_json())
    print("==" * 50)


# 流式输出
def demo_chat_stream():
    messages = [
        SystemMessage(content="You are a helpful assistant"),
        HumanMessage(content="你是谁")
    ]
    response3 = llm.stream(
        input=messages,
    )
    for chunk in response3:
        print(chunk.content, end="", flush=True)
    print("\n" + "==" * 50)


def demo_batch():
    """3. batch：批量并发调用。"""
    print("\n--- 3. batch 示例 ---")
    # 传入一个二维列表，每个子列表代表一个独立的请求
    inputs = [
        [HumanMessage(content="1+1等于几？只回答数字")],
        [HumanMessage(content="2+2等于几？只回答数字")]
    ]

    # 一次性发送，底层会自动并发执行
    responses = llm.batch(inputs)
    for i, res in enumerate(responses):
        print(f"请求{i + 1}结果: {res.content}")
    print("==" * 50)


if __name__ == "__main__":
    demo_chat_invoke()
    demo_chat_invoke2()
    demo_chat_stream()
    demo_batch()
