"""
调用大模型
1. 初始化模型
2. 创建消息列表
3. 调用模型
"""


import os
from dotenv import load_dotenv
from langchain.chat_models import init_chat_model
from langchain_core.messages import *

load_dotenv()  # 读取项目根目录 .env

api_key = os.getenv("DEEPSEEK_API_KEY")
base_url = os.getenv("DEEPSEEK_BASE_URL")
model_name = os.getenv("DEEPSEEK_MODEL")

llm = init_chat_model(model_name, temperature=0.7)
messages = [
    {"role": "system", "content": "You are a helpful assistant"},
    {"role": "user", "content": "你是谁"},
]
response = llm.invoke(
    input=messages
)
print(response)

print("==" * 50)

messages2 = [
    SystemMessage(content="You are a helpful assistant"),
    HumanMessage(content="你是谁")
]

response2 = llm.invoke(
    input=messages2,
    stream=True
)
print(response2)

