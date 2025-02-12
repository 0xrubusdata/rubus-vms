## 🌿 歡迎來到 **Rubus-VMS - API 與向量記憶服務 (Rubus-VMS)**

## 🏗️ 介紹
**向量記憶服務**專案旨在從 **Rubus-Cron** 系統收集的數據中創建一個 **向量記憶**。這個向量記憶將作為專門 AI 代理的 **動態知識庫**。

🔹 **技術棧:**
- **語言:** Python 🐍
- **向量數據庫:** FAISS / Weaviate / Pinecone / ChromaDB
- **後端 API:** FastAPI ⚡
- **元數據存儲:** PostgreSQL 🏛️
- **與 AI 代理的整合:** OpenAI API / LlamaIndex / 自訂 RAG (檢索增強生成)

---

## 🎯 目標與功能

1️⃣ **數據攝取與預處理**
   - 從 **Rubus-Cron** 📡 提取
   - 文本清理與斷詞
   - 數據向量化（使用 BERT、SBERT 等進行嵌入）

2️⃣ **存儲與索引**
   - 在 FAISS / Weaviate 🔍 中索引向量
   - 與存儲在 **PostgreSQL** 📊 的 **元數據** 相關聯

3️⃣ **搜索與檢索 API**
   - 查詢向量記憶的端點
   - 用於 AI 代理的高級語義搜索 🤖
   - **RAG（檢索增強生成）的優化**

4️⃣ **與 AI 代理的整合**
   - 通過 **model-ai_microservice** 🎯 連接模型
   - 根據特定代理需求（例如 **經濟代理**）訪問過濾數據 🏦

---

## ⚙️ **安裝與設置**

### **1️⃣ 克隆倉庫**
```sh
git clone https://github.com/0xrubusdata/rubus-vms
cd rubus-vms
```
### **2️⃣ 配置環境變量**
在項目根目錄創建一個 .env 文件：
 - 定義基礎來源（Rubus-PostgreSQL）
 - 定義基礎語言環境（VMS-PostgreSQL）元數據
 - 定義嵌入 API（本地或遠程）

### **3️⃣ 使用 Docker 運行**
```sh
docker-compose up --build
```

---