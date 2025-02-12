## 🌿 欢迎来到 **Rubus-VMS - API 和向量记忆服务 (Rubus-VMS)**

## 🏗️ 介绍
**向量记忆服务**项目旨在从**Rubus-Cron**系统收集的数据创建一个**向量记忆**。这个向量记忆将作为专业AI代理的**动态知识库**。

🔹 **技术栈：**
- **语言：** Python 🐍
- **向量数据库：** FAISS / Weaviate / Pinecone / ChromaDB
- **后端API：** FastAPI ⚡
- **元数据存储：** PostgreSQL 🏛️
- **与AI代理的集成：** OpenAI API / LlamaIndex / 自定义RAG（检索增强生成）

---

## 🎯 目标与功能

1️⃣ **数据摄取与预处理**
   - 从 **Rubus-Cron** 📡 提取
   - 文本清理和分词
   - 数据向量化（使用 BERT、SBERT 等进行嵌入）

2️⃣ **存储与索引**
   - 在 FAISS / Weaviate 中索引向量 🔍
   - 与存储在 **PostgreSQL** 中的 **元数据** 关联 📊

3️⃣ **搜索与检索 API**
   - 查询向量记忆的端点
   - 为 AI 代理提供高级语义搜索 🤖
   - **RAG（检索增强生成）的优化**

4️⃣ **与 AI 代理的集成**
   - 通过 **model-ai_microservice** 连接模型 🎯
   - 根据特定代理需求访问过滤后的数据（例如，**经济代理**） 🏦

---

## ⚙️ **安装与设置**

### **1️⃣ 克隆代码库**
```sh
git clone https://github.com/0xrubusdata/rubus-vms
cd rubus-vms
```
### **2️⃣ 配置环境变量**
在项目根目录创建一个 .env 文件：
 - 定义基础源（Rubus-PostgreSQL）
 - 定义基础语言环境（VMS-PostgreSQL）元数据
 - 定义嵌入 API（本地或远程）

### **3️⃣ 使用 Docker 运行**
```sh
docker-compose up --build
```

---