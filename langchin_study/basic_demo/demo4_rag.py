"""
本脚本演示LangChain RAG（检索增强生成）全套核心模块。
RAG核心流程：文档加载→文本切分→向量化→向量库存储→文档检索→组装问答链，解决大模型知识滞后、幻觉问题；
核心模块包含：Document文档对象、文档加载器、文本分割器、Embedding嵌入模型、向量存储VectorStore、Retriever检索器、RAG问答链。

【常用方法清单】
1. Document(page_content, metadata)：构造文档对象，存储文本内容与元数据
2. TextLoader.load()：加载本地文本文件，返回Document列表
3. RecursiveCharacterTextSplitter.split_documents()：递归字符分割，把长文档切分为chunk片段
4. OpenAIEmbeddings.embed_query()：把文本转为向量嵌入
5. Chroma.from_documents()：把文档+向量存入Chroma向量数据库
6. vectorstore.similarity_search()：向量库相似度检索，返回匹配文档
7. vectorstore.as_retriever()：向量库转为检索器对象
8. RunnablePassthrough()：Runnable透传，把question字段直接传入链中
9. ChatPromptTemplate.from_template()：构造RAG问答提示词模板
10. StrOutputParser()：把模型输出转为纯字符串
11. chain.invoke()：执行整条RAG问答链路，输入问题输出答案
"""

import os

from langchain_core.documents import Document
from langchain_community.document_loaders import TextLoader
from langchain_community.document_loaders import PyPDFLoader
from langchain_community.embeddings import DashScopeEmbeddings
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_openai import OpenAIEmbeddings, ChatOpenAI
from langchain_chroma import Chroma
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnablePassthrough
from langchain_core.output_parsers import StrOutputParser
import dotenv

dotenv.load_dotenv()
model_name = os.getenv("QIANWEN_EMBEDDING_MODEL")
api_key = os.getenv("QIANWEN_API_KEY")
base_url = os.getenv("QIANWEN_BASE_URL")

# 准备文档
documents = [
    Document(page_content="LangChain 是一个强化大语言模型应用的框架", metadata={"source": "doc1"}),
    Document(page_content="LangGraph 用于构建有状态的 Agent 系统", metadata={"source": "doc2"}),
    Document(page_content="RAG 是一种技术，让 LLM 能够访问外部知识库", metadata={"source": "doc3"}),
    Document(page_content="向量数据库用于存储文档的向量表示", metadata={"source": "doc4"}),
]

# embeddings = OpenAIEmbeddings(
#     model=model_name,
#     openai_api_key=api_key,
#     openai_api_base=base_url,
#     check_embedding_ctx_length=False,
# )

embeddings = DashScopeEmbeddings (
    model=model_name,
    dashscope_api_key=api_key,
)


def demo_01_document_object():
    """构造Document文档对象"""
    doc = Document(
        page_content="RAG全称检索增强生成，用来降低大模型幻觉",
        metadata={"source": "demo_txt", "page": 1}
    )
    print("Document内容：", doc.page_content)
    print("Document元数据：", doc.metadata)
    print("Document：", documents)
    print("\n")


def demo_02_text_loader_load():
    """TextLoader加载本地文本文件"""
    # 临时写入测试文件

    file_path = "rag_test.txt"

    if not os.path.exists(file_path):
        with open(file_path, "w", encoding="utf-8") as f:
            for index in range(1, 6):
                f.write(f"LangChain RAG分为文档加载、文本切分、向量化、检索、问答生成五个步骤。{index} \n")

    loader = TextLoader("rag_test.txt", encoding="utf-8")
    docs = loader.load()
    print("加载文档数量：", len(docs))
    print("文档文本：\n", docs[0].page_content)
    print("\n")


def demo_02_pdf_loader():
    loder = PyPDFLoader(file_path="https://arxiv.org/pdf/alg-geom/9202012", extraction_mode="plain")
    doc = loder.load()
    print(doc)


def demo_03_split_documents():
    """RecursiveCharacterTextSplitter文档切分"""
    raw_doc = Document(page_content="RAG第一步加载文档；第二步分割文本块；第三步生成向量；第四步检索；第五步生成答案。")
    splitter = RecursiveCharacterTextSplitter(chunk_size=30, chunk_overlap=5)
    chunks = splitter.split_documents([raw_doc])
    print("切分后的块数量：", len(chunks))
    for idx, chunk in enumerate(chunks):
        print(f"块{idx + 1}：{chunk.page_content}")
    print("\n")


def demo_04_embed_query():
    """Embedding文本向量化"""
    text = "RAG检索增强生成"
    vec = embeddings.embed_query(text)
    print("向量长度：", len(vec))
    print("前5位向量值：", vec[:5])
    print("\n")


def demo_05_chroma_from_documents():
    """Chroma向量库存入文档向量"""
    docs = [Document(page_content="RAG可以减少大模型幻觉"), Document(page_content="向量数据库用来存储文本嵌入")]
    vector_db = Chroma.from_documents(documents=docs, embedding=embeddings, persist_directory="./chroma_db")
    print("向量库创建完成，已持久化")
    print("\n")


def demo_06_similarity_search():
    """向量库相似度检索"""
    vector_db = Chroma(persist_directory="./chroma_db", embedding_function=embeddings)
    res_docs = vector_db.similarity_search("如何降低大模型幻觉", k=1)
    print("检索到文档：", res_docs[0].page_content)
    print("\n")


def demo_07_as_retriever():
    """向量库转为Retriever检索器"""
    vector_db = Chroma(persist_directory="./chroma_db", embedding_function=embeddings)
    retriever = vector_db.as_retriever(search_kwargs={"k": 1})
    docs = retriever.invoke("大模型幻觉")
    print("检索器返回内容：", docs[0].page_content)
    print("\n")


def demo_08_runnable_passthrough():
    """RunnablePassthrough透传参数"""
    runnable = RunnablePassthrough()
    out = runnable.invoke({"question": "什么是RAG"})
    print("透传结果：", out)
    print("\n")


def demo_09_prompt_template():
    """构建RAG问答提示词模板"""
    prompt = ChatPromptTemplate.from_template("""
基于下面上下文回答问题：
{context}
问题：{question}
""")
    prompt_val = prompt.format(context="RAG是检索增强生成", question="什么是RAG")
    print("填充后的prompt：\n", prompt_val)
    print("\n")


def demo_10_str_output_parser():
    """字符串输出解析器"""
    parser = StrOutputParser()
    raw_msg = {"content": "RAG用来解决大模型知识不足的问题"}
    result = parser.invoke(raw_msg)
    print("解析后文本：", result)
    print("\n")


def demo_11_rag_chain_invoke():
    """组装完整RAG链路并调用"""
    vector_db = Chroma(persist_directory="./chroma_db", embedding_function=embeddings)
    retriever = vector_db.as_retriever(k=1)

    # 拼接链
    prompt = ChatPromptTemplate.from_template("使用上下文回答问题：{context}\n问题：{question}")
    llm = ChatOpenAI(temperature=0)
    rag_chain = (
            {"context": retriever, "question": RunnablePassthrough()}
            | prompt
            | llm
            | StrOutputParser()
    )
    # 仅演示结构，无真实key会请求失败
    print("RAG问答链构建完成，可调用invoke执行问答")
    print("\n")


if __name__ == "__main__":
    # demo_01_document_object()
    # demo_02_text_loader_load()
    # demo_02_pdf_loader()
    # demo_03_split_documents()
    # demo_04_embed_query()
    demo_05_chroma_from_documents()
    # demo_06_similarity_search()
    # demo_07_as_retriever()
    # demo_08_runnable_passthrough()
    # demo_09_prompt_template()
    # demo_10_str_output_parser()
    # demo_11_rag_chain_invoke()
