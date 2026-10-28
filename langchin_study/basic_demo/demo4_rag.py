"""
【LangChain RAG (检索增强生成) 模块简介】
RAG (Retrieval-Augmented Generation) 是解决大模型“幻觉”和“知识过期”问题的核心架构。
它的核心思想是：在模型回答问题前，先从外部私有知识库（如文档、PDF、数据库）中检索出相关的信息，
然后将“检索到的信息”和“用户的提问”一起塞给大模型，让模型基于这些事实依据来生成准确的答案。
该模块主要包含两大流程：建库（加载 -> 切分 -> 向量化 -> 存储）和 检索生成（检索 -> 拼装 Prompt -> 生成）。

【常用方法清单】
1. TextLoader / DirectoryLoader : 文档加载器，用于读取本地文本或文件夹。
2. RecursiveCharacterTextSplitter: 文本切分器，将长文档切分成适合模型上下文长度的小块（Chunk）。
3. OpenAIEmbeddings             : 嵌入模型，将文本转化为向量（数字数组），以便计算语义相似度。
4. Chroma / FAISS               : 向量数据库，用于存储文本向量和原始文本片段。
5. as_retriever(search_kwargs)  : 将向量库转换为检索器，根据用户提问查找最相似的文本片段。
6. create_stuff_documents_chain : 将检索到的文档和用户问题拼装成最终发给大模型的 Prompt 链。
"""
from langchain_core.documents import Document
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_openai import OpenAIEmbeddings, ChatOpenAI
from langchain_chroma import Chroma
from langchain_core.prompts import ChatPromptTemplate
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain.chains import create_retrieval_chain

# 初始化基础组件（需配置 OPENAI_API_KEY）
llm = ChatOpenAI(model="gpt-3.5-turbo", temperature=0)
embeddings = OpenAIEmbeddings()  # 用于将文本转为向量


def demo_1_document_loader():
    """1. Loader：文档加载（此处用代码直接创建模拟文档）。"""
    print("--- 1. 文档加载 示例 ---")
    # 实际开发中，这里会使用 TextLoader("path.txt") 或 PyPDFLoader("doc.pdf")
    docs = [
        Document(page_content="LangChain 是一个用于开发大语言模型应用的框架。", metadata={"source": "intro.txt"}),
        Document(page_content="今天的天气非常晴朗，适合出去游玩。", metadata={"source": "weather.txt"})
    ]
    print(f"加载的文档数量: {len(docs)}")
    print(f"第一段内容: {docs[0].page_content}")
    print("\n")


def demo_2_text_splitter():
    """2. Splitter：文本切分。"""
    print("--- 2. 文本切分 示例 ---")
    long_text = "Python是一种广泛使用的解释型语言。" * 10
    # chunk_size 是每块最大字符数，chunk_overlap 是相邻块的重叠字符数（防止语义被切断）
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=50, chunk_overlap=10)
    splits = text_splitter.split_text(long_text)
    print(f"切分后的小块数量: {len(splits)}")
    print(f"第一块内容: {splits[0]}")
    print("\n")


def demo_3_vector_store():
    """3. Embeddings & Vector Store：向量化与入库。"""
    print("--- 3. 向量化与存储 示例 ---")
    docs = [
        Document(page_content="LangChain 是一个用于开发大语言模型应用的框架。"),
        Document(page_content="DeepSeek 是一家中国的人工智能公司。"),
        Document(page_content="Python 是一种流行的编程语言。")
    ]
    # 将文档转为向量并存入 Chroma 向量数据库
    vector_store = Chroma.from_documents(documents=docs, embedding=embeddings)
    print("向量数据库创建成功！")
    print("\n")
    return vector_store


def demo_4_retriever(vector_store):
    """4. Retriever：语义检索。"""
    print("--- 4. 检索器 示例 ---")
    # 将向量库转为检索器，设置返回最相似的 1 个文档
    retriever = vector_store.as_retriever(search_kwargs={"k": 1})

    # 模拟用户提问
    query = "LangChain是干什么的？"
    results = retriever.invoke(query)

    print(f"用户提问: {query}")
    print(f"检索到的相关文档: {results[0].page_content}")
    print("\n")


def demo_5_rag_chain(vector_store):
    """5. RAG 完整链：检索 + 拼装 Prompt + 生成。"""
    print("--- 5. RAG 完整链路 示例 ---")
    retriever = vector_store.as_retriever(search_kwargs={"k": 2})

    # 定义 RAG 的 Prompt 模板：{context} 会被自动替换为检索到的文档内容，{input} 是用户提问
    prompt = ChatPromptTemplate.from_messages([
        ("system", "你是一个问答助手。请仅根据以下提供的上下文回答问题，不要编造：\n\n{context}"),
        ("human", "{input}")
    ])

    # 将 Prompt 和 LLM 组合成处理文档的链
    combine_docs_chain = create_stuff_documents_chain(llm, prompt)

    # 最终组装成完整的 RAG 链：检索 -> 填充 Prompt -> LLM 生成
    rag_chain = create_retrieval_chain(retriever, combine_docs_chain)

    # 执行问答
    response = rag_chain.invoke({"input": "DeepSeek是什么公司？"})

    print(f"用户提问: {response['input']}")
    print(f"模型回答: {response['answer']}")
    print("\n")


if __name__ == "__main__":
    demo_1_document_loader()
    demo_2_text_splitter()

    # 实际运行时，这里需要真实的 OPENAI_API_KEY
    try:
        v_store = demo_3_vector_store()
        demo_4_retriever(v_store)
        demo_5_rag_chain(v_store)
    except Exception as e:
        print(f"跳过向量与 RAG 链演示（需要配置真实的 OpenAI API Key 以进行网络请求）: {e}")