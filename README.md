
[🇬🇧 English](./) | [🇫🇷 Français](./i18n/readme/README_FR.md) | [🇪🇸 Español](./i18n/readme/README_ES.md) | [🇵🇹 Português](./i18n/readme/README_PT.md) | [🇯🇵 日本語](./i18n/readme/README_JP.md) | [🇷🇺 Русский](./i18n/readme/README_RU.md) | [🇸🇦 العربية](./i18n/readme/README_AR.md) | [🇨🇳 中文](./i18n/readme/README_CN.md) | [🇭🇰 🇹🇼 🇲🇴 中文](./i18n/readme/README_TR.md)  

---

# ![Rubus-VMS](./public/agents/Rubus-VMS.png)


## 🌿 Welcome to **Rubus-VMS - API & Vector Memory Service (Rubus-VMS)**


## 🏗️ Introduction
The **Vector Memory Service** project is designed to create a **vector memory** from data collected by the **Rubus-Cron** system. This vector memory will serve as a **dynamic knowledge base** for specialized AI agents.

🔹 **Tech Stack:**
- **Language:** Python 🐍
- **Vector Database:** FAISS / Weaviate / Pinecone / ChromaDB
- **Backend API:** FastAPI ⚡
- **Metadata Storage:** PostgreSQL 🏛️
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

## ⚙️ **Installation & Setup**

### **1️⃣ Clone the repository**
```sh
git clone https://github.com/0xrubusdata/rubus-vms
cd rubus-vms
```
### **2️⃣ Configure environment variables**
Create a .env file at the project root:
 - Define Base source (Rubus-PostgreSQL)
 - Define Base locale (VMS-PostgreSQL) métadata
 - Define Embedding API (local or remote)

### **3️⃣ Run with Docker**
```sh
docker-compose up --build
```
---

## 🧠 **Workflow of Rubus-VMS**
### **📌 How data flows**

- 1️⃣ Raw data is fetched from CRON-PostgreSQL using DataFetcher.fetch_data().
- 2️⃣ Text is cleaned and preprocessed with DataTransformer.preprocess().
- 3️⃣ The embedding is generated via DataTransformer.embed().
- 4️⃣ The embedding is stored in FAISS/ChromaDB via VectorStore.add_vectors().
- 5️⃣ The metadata is stored in VMS-PostgreSQL via MetadataStorage.store_metadata().
- 6️⃣ A search request is made via /api/search to find relevant results.

---

## 🚀 **Execution**
### **📌 /api/search**
```sh
curl -X GET "http://localhost:8001/api/search?model=llama3.2&memory_type=economic&query=Latest economic trends&top_k=5"
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
