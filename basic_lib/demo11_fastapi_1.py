"""
FastAPI 浏览器交互式学习 Demo

【使用说明】
1. 运行本脚本：python main.py
2. 打开浏览器访问 Swagger UI: http://127.0.0.1:8001/docs
   （在网页里可以直接点击 "Try it out" 按钮测试所有接口）
3. 打开浏览器访问 ReDoc 文档: http://127.0.0.1:8001/redoc

【涵盖知识点】
- FastAPI 实例化
- GET/POST/PUT/PATCH/DELETE 请求
- Path 路径参数及校验
- Query 查询参数及校验
- BaseModel 请求体数据校验
- Depends 依赖注入
- HTTPException 异常处理
- TestClient 自动化测试（运行此脚本时自动执行）
"""

import uvicorn
from fastapi import FastAPI, Path, Query, HTTPException, Depends
from fastapi.testclient import TestClient
from pydantic import BaseModel, Field
from typing import Optional

# ============================================================
# 1. 创建 FastAPI 实例
# ============================================================
app = FastAPI(
    title="FastAPI 学习 Demo",
    description="这是一个用于在浏览器中进行测试的 FastAPI 学习项目。",
    version="1.0.0"
)


# ============================================================
# 2. GET 请求 (基础)
# ============================================================
@app.get("/", tags=["1. GET 基础"])
def root():
    """根路径，最简单的 GET 请求。"""
    return {"message": "欢迎来到 FastAPI 学习 Demo！请访问 /docs 测试其他接口。"}


@app.get("/hello/{name}", tags=["1. GET 基础"])
def say_hello(
        name: str = Path(..., description="你的名字", example="张三")
):
    """带有路径参数的 GET 请求 (Path 校验)。"""
    return {"message": f"你好, {name}!"}


# ============================================================
# 3. 查询参数 (Query)
# ============================================================
@app.get("/search/", tags=["2. Query 查询参数"])
def search_items(
        keyword: str = Query(..., min_length=2, max_length=20, description="搜索关键词，至少2字符", example="python"),
        limit: int = Query(10, ge=1, le=50, description="返回条数，1-50之间", example=5)
):
    """带有查询参数的 GET 请求 (Query 校验)。"""
    return {"keyword": keyword, "limit": limit, "msg": "搜索成功"}


# ============================================================
# 4. 请求体模型 (BaseModel) 与 POST
# ============================================================
class Item(BaseModel):
    name: str = Field(..., min_length=1, description="商品名称", example="机械键盘")
    price: float = Field(..., gt=0, description="商品价格，必须大于0", example=399.5)
    is_offer: Optional[bool] = Field(None, description="是否特价", example=True)


@app.post("/items/", tags=["3. POST 请求体"], response_model=Item)
def create_item(item: Item):
    """创建商品，接收 JSON 请求体。Pydantic 会自动校验类型和范围。"""
    # 这里只是演示，实际业务中通常会保存到数据库
    return item


# ============================================================
# 5. PUT 与 PATCH 请求 (更新)
# ============================================================
@app.put("/items/{item_id}", tags=["4. PUT/PATCH 更新"])
def update_item(item_id: int, item: Item):
    """全量更新：既需要路径参数，又需要完整的请求体。"""
    return {"item_id": item_id, "item": item, "msg": "全量更新成功"}


@app.patch("/items/{item_id}", tags=["4. PUT/PATCH 更新"])
def patch_item(item_id: int, name: Optional[str] = Query(None, description="新名字")):
    """部分更新：通过查询参数只修改部分字段。"""
    return {"item_id": item_id, "updated_name": name, "msg": "部分更新成功"}


# ============================================================
# 6. DELETE 请求 (删除) 与 HTTPException 异常处理
# ============================================================
fake_db = {1: "苹果", 2: "香蕉"}


@app.delete("/items/{item_id}", tags=["5. DELETE 与异常"])
def delete_item(item_id: int):
    """删除商品：如果商品不存在，抛出 404 异常。"""
    if item_id not in fake_db:
        raise HTTPException(status_code=404, detail=f"商品 ID {item_id} 不存在")
    del fake_db[item_id]
    return {"msg": f"商品 {item_id} 删除成功"}


# ============================================================
# 7. 依赖注入 (Depends)
# ============================================================
def common_pagination(skip: int = Query(0, ge=0), limit: int = Query(10, le=100)):
    """可复用的分页参数依赖。"""
    return {"skip": skip, "limit": limit}


@app.get("/users/", tags=["6. Depends 依赖注入"])
def list_users(pagination: dict = Depends(common_pagination)):
    """使用 Depends 注入分页参数，避免重复写查询参数。"""
    return {"pagination": pagination, "users": ["用户A", "用户B", "用户C"]}


# ============================================================
# 本地自动化测试函数 (使用 TestClient)
# ============================================================
def run_auto_tests():
    """运行脚本时自动执行，用于验证代码逻辑是否正常。"""
    client = TestClient(app)
    print("\n" + "=" * 50)
    print("开始自动测试 (TestClient)...")
    print("=" * 50)

    # 1. 测试 GET
    res = client.get("/hello/李四")
    print(f"1. GET 测试: {res.status_code} - {res.json()}")

    # 2. 测试 Query 校验
    res = client.get("/search/?keyword=book&limit=5")
    print(f"2. Query 测试: {res.status_code} - {res.json()}")

    # 3. 测试 POST 请求体校验
    res = client.post("/items/", json={"name": "手机", "price": 2999})
    print(f"3. POST 测试: {res.status_code} - {res.json()}")

    # 4. 测试异常处理
    res = client.delete("/items/99")
    print(f"4. 异常测试: {res.status_code} - {res.json()}")

    print("=" * 50)
    print("自动测试结束！")
    print("=" * 50 + "\n")


# ============================================================
# 主入口：启动 Web 服务器
# ============================================================
if __name__ == "__main__":
    # 如果你在终端运行，先执行一遍自动化测试，方便看控制台打印
    run_auto_tests()

    print("🚀 正在启动服务器...")
    print("👉 请在浏览器访问: http://127.0.0.1:8001/docs")
    print("👉 按 Ctrl+C 停止服务器")

    # 启动 uvicorn 服务器
    uvicorn.run(app, host="127.0.0.1", port=8001)