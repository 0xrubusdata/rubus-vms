## 🌿 Bem-vindo ao **Rubus-VMS - API & Serviço de Memória Vetorial (Rubus-VMS)**

## 🏗️ Introdução
O projeto **Serviço de Memória Vetorial** foi projetado para criar uma **memória vetorial** a partir de dados coletados pelo sistema **Rubus-Cron**. Essa memória vetorial servirá como uma **base de conhecimento dinâmica** para agentes de IA especializados.

🔹 **Tecnologia:**
- **Linguagem:** Python 🐍
- **Banco de Dados Vetorial:** FAISS / Weaviate / Pinecone / ChromaDB
- **API Backend:** FastAPI ⚡
- **Armazenamento de Metadados:** PostgreSQL 🏛️
- **Integração com Agentes de IA:** API OpenAI / LlamaIndex / RAG Personalizado (Geração Aumentada por Recuperação)

---

## 🎯 Objetivos & Recursos

1️⃣ **Ingestão de Dados & Pré-processamento**
   - Extração do **Rubus-Cron** 📡
   - Limpeza de texto e tokenização
   - Vetorização de dados (embedding com BERT, SBERT, etc.)

2️⃣ **Armazenamento & Indexação**
   - Indexação de vetores no FAISS / Weaviate 🔍
   - Associação com **metadados** armazenados no **PostgreSQL** 📊

3️⃣ **API de Busca & Recuperação**
   - Endpoint para **consultar** a memória vetorial
   - Busca semântica avançada para agentes de IA 🤖
   - **Otimização de RAG (Geração Aumentada por Recuperação)**

4️⃣ **Integração com Agentes de IA**
   - Conexão com modelos via **model-ai_microservice** 🎯
   - Acesso a dados filtrados com base nas necessidades específicas do agente (por exemplo, **agente econômico**) 🏦

---

## ⚙️ **Instalação e Configuração**

### **1️⃣ Clone o repositório**
```sh
git clone https://github.com/0xrubusdata/rubus-vms
cd rubus-vms
```
### **2️⃣ Configure as variáveis de ambiente**
Crie um arquivo .env na raiz do projeto:
 - Defina a fonte base (Rubus-PostgreSQL)
 - Defina o local base (metadados do VMS-PostgreSQL)
 - Defina a API de Embedding (local ou remota)

### **3️⃣ Execute com Docker**
```sh
docker-compose up --build
```

---