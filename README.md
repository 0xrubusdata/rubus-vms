
[🇬🇧 English](./) | [🇫🇷 Français](./i18n/readme/README_FR.md) | [🇪🇸 Español](./i18n/readme/README_ES.md) | [🇵🇹 Português](./i18n/readme/README_PT.md) | [🇯🇵 日本語](./i18n/readme/README_JP.md) | [🇷🇺 Русский](./i18n/readme/README_RU.md) | [🇸🇦 العربية](./i18n/readme/README_AR.md) | [🇨🇳 中文](./i18n/readme/README_CN.md) | [🇭🇰 🇹🇼 🇲🇴 中文](./i18n/readme/README_TR.md)  

---

# ![Rubus-VMS](./public/agents/Rubus-VMS.png)


## 🌿 Welcome to **Rubus-VMS - Vector Memory Service - AI-Powered Data Indexing**


## 🏗️ Introduction
The **Vector Memory Service** project is designed to create a **vector memory** from data collected by the **Rubus-Cron** system. This vector memory will serve as a **dynamic knowledge base** for specialized AI agents.

🔹 **Tech Stack:**
- **Language:** Python 🐍
- **Vector Database:** FAISS / Weaviate / Pinecone / ChromaDB
- **Backend API:** FastAPI ⚡
- **Metadata Storage:** PostgreSQL 🏛️
- **NLP Pipeline:** spaCy / SentenceTransformers / LangChain
- **Integration with AI Agents:** OpenAI API / LlamaIndex / Custom RAG (Retrieval-Augmented Generation)

---

## 🎯 Goals & Features

1️⃣ **Data Ingestion & Preprocessing**
   - Extraction from **Rubus-Cron** 📡
   - Text cleaning and tokenization
   - Data vectorization (embedding with BERT, SBERT, etc.)

2️⃣ **Storage & Indexing**
   - Indexing vectors in FAISS / Weaviate 🔍
   - Association with **metadata** stored in **PostgreSQL** 📊

3️⃣ **Search & Retrieval API**
   - Endpoint to **query** the vector memory
   - Advanced semantic search for AI agents 🤖
   - **Optimization of RAG (Retrieval-Augmented Generation)**

4️⃣ **Integration with AI Agents**
   - Connection to models via **model-ai_microservice** 🎯
   - Access to filtered data based on specific agent needs (e.g., **economic agent**) 🏦
   
---

## 🚀 Development Roadmap

1️⃣ **Phase 1 - MVP:**
   - Development of the **ingestion and vectorization pipeline**
   - Deployment of a **vector database**
   - API for **storing and querying embeddings**

2️⃣ **Phase 2 - Improvements:**
   - Optimization of **semantic search** (Fine-tuning NLP models)
   - Implementation of **advanced RAG**
   - Integration with **other data sources** (economic articles, publications, etc.)

3️⃣ **Phase 3 - Integration with AI Agents:**
   - Dynamic connection with the **AI agent framework**
   - **Customization of access** based on the agent's mission
   - Performance tracking and monitoring 📈

---

## ⚙️ Deployment & Usage
### **Installation**
```bash
# Clone the repo
git clone https://github.com/0xrubusdata/rubus-vms
cd rubus-vms

# Install dependencies
pip install -r requirements.txt

# Start the FastAPI server
uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload

### **Example API Request**
```bash
curl -X POST "http://localhost:8000/search" \
     -H "Content-Type: application/json" \
     -d '{"query": "impact of interest rate hikes"}'
```

---

## 📌 Conclusion
The **Vector Memory Service** project is a **central** component of the **RubusData** ecosystem:
- **It enables efficient organization, search, and retrieval of indexed data**.
- **It provides a solid foundation for AI agents capable of accessing persistent and optimized memory**.
- **Its flexible integration allows adaptation to various types of AI missions**.

🔥 **Next step: Integration with the AI agent framework!** 🚀

---

## 📄 License
This project is licensed under the MIT License.

---

## 📝 **Author**
- 👤 0xRubusData 
- 📧 Contact: 0xRubusData@gmail.com
- 🌍 GitHub: https://github.com/0xrubusdata/rubus-vms

## 🌐 Connect with Us
- **Twitter (X)**: [0xRubusData](https://x.com/Data0x88850)
- **Website**: [RubusLab](https://rubus-lab.vercel.app/)

## 🎯 **Happy Coding!** 🚀
