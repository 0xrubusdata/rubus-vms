[🇬🇧 English](./) | [🇫🇷 Français](./i18n/readme/README_FR.md) | [🇪🇸 Español](./i18n/readme/README_ES.md) | [🇵🇹 Português](./i18n/readme/README_PT.md) | [🇯🇵 日本語](./i18n/readme/README_JP.md) | [🇷🇺 Русский](./i18n/readme/README_RU.md) | [🇸🇦 العربية](./i18n/readme/README_AR.md) | [🇨🇳 简体中文](./i18n/readme/README_CN.md) | [🇹🇼 繁體中文](./i18n/readme/README_TC.md)

---

# 📌 向量記憶服務 - AI驅動的數據索引

## 🏗️ 簡介
**Vector Memory Service**專案旨在從**Rubus-Cron**系統收集的數據中創建**向量記憶**。這個向量記憶將作為專業AI代理的**動態知識庫**。

🔹 **技術棧：**
- **程式語言：** Python 🐍
- **向量資料庫：** FAISS / Weaviate / Pinecone / ChromaDB
- **後端API：** FastAPI ⚡
- **元數據儲存：** PostgreSQL 🏛️
- **自然語言處理流程：** spaCy / SentenceTransformers / LangChain
- **AI代理整合：** OpenAI API / LlamaIndex / 客製化RAG（檢索增強生成）

---

## 🎯 目標和功能

1️⃣ **數據擷取和預處理**
   - 從**Rubus-Cron**提取數據 📡
   - 文本清理和分詞
   - 數據向量化（使用BERT、SBERT等進行嵌入）

2️⃣ **儲存和索引**
   - 在FAISS / Weaviate中進行向量索引 🔍
   - 與儲存在**PostgreSQL**中的**元數據**關聯 📊

3️⃣ **搜尋和檢索API**
   - 向量記憶**查詢**端點
   - 面向AI代理的進階語意搜尋 🤖
   - **RAG（檢索增強生成）最佳化**

4️⃣ **AI代理整合**
   - 透過**model-ai_microservice**連接模型 🎯
   - 基於代理特定需求的數據篩選存取（如**經濟代理**） 🏦
   
---

## 🚀 開發路線圖

1️⃣ **第一階段 - MVP：**
   - 開發**擷取和向量化流程**
   - 部署**向量資料庫**
   - 用於**儲存和查詢嵌入**的API

2️⃣ **第二階段 - 改進：**
   - **語意搜尋**最佳化（NLP模型微調）
   - 實現**進階RAG**
   - 與**其他數據來源**整合（經濟文章、出版物等）

3️⃣ **第三階段 - AI代理整合：**
   - 與**AI代理框架**的動態連接
   - 基於代理任務的**存取客製化**
   - 效能追蹤和監控 📈

---

## ⚙️ 部署和使用
### **安裝**
```bash
# 複製儲存庫
git clone https://github.com/0xrubusdata/rubus-vms
cd rubus-vms

# 安裝相依套件
pip install -r requirements.txt

# 啟動FastAPI伺服器
uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload

### **API請求範例**
```bash
curl -X POST "http://localhost:8000/search" \
     -H "Content-Type: application/json" \
     -d '{"query": "利率調升的影響"}'
```

---

## 📌 結論
**Vector Memory Service**專案是**RubusData**生態系統的**核心**組件：
- **實現索引數據的高效組織、搜尋和檢索**。
- **為能夠存取持久化和最佳化記憶體的AI代理提供穩固基礎**。
- **其靈活的整合允許適應各種類型的AI任務**。

🔥 **下一步：與AI代理框架整合！** 🚀
