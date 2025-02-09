
# 📌 Serviço de Memória Vetorial - Indexação de Dados Impulsionada por IA

## 🏗️ Introdução
O projeto **Vector Memory Service** foi projetado para criar uma **memória vetorial** a partir dos dados coletados pelo sistema **Rubus-Cron**. Esta memória vetorial servirá como uma **base de conhecimento dinâmica** para agentes de IA especializados.

🔹 **Stack Tecnológica:**
- **Linguagem:** Python 🐍
- **Banco de Dados Vetorial:** FAISS / Weaviate / Pinecone / ChromaDB
- **API Backend:** FastAPI ⚡
- **Armazenamento de Metadados:** PostgreSQL 🏛️
- **Pipeline de PLN:** spaCy / SentenceTransformers / LangChain
- **Integração com Agentes de IA:** OpenAI API / LlamaIndex / RAG Personalizado (Geração Aumentada por Recuperação)

---

## 🎯 Objetivos e Recursos

1️⃣ **Ingestão e Pré-processamento de Dados**
   - Extração do **Rubus-Cron** 📡
   - Limpeza e tokenização de texto
   - Vetorização de dados (embedding com BERT, SBERT, etc.)

2️⃣ **Armazenamento e Indexação**
   - Indexação de vetores no FAISS / Weaviate 🔍
   - Associação com **metadados** armazenados no **PostgreSQL** 📊

3️⃣ **API de Busca e Recuperação**
   - Endpoint para **consultar** a memória vetorial
   - Busca semântica avançada para agentes de IA 🤖
   - **Otimização de RAG (Geração Aumentada por Recuperação)**

4️⃣ **Integração com Agentes de IA**
   - Conexão com modelos via **model-ai_microservice** 🎯
   - Acesso a dados filtrados com base nas necessidades específicas do agente (ex., **agente econômico**) 🏦
   
---

## 🚀 Roteiro de Desenvolvimento

1️⃣ **Fase 1 - MVP:**
   - Desenvolvimento do **pipeline de ingestão e vetorização**
   - Implantação de um **banco de dados vetorial**
   - API para **armazenar e consultar embeddings**

2️⃣ **Fase 2 - Melhorias:**
   - Otimização da **busca semântica** (Fine-tuning de modelos PLN)
   - Implementação de **RAG avançado**
   - Integração com **outras fontes de dados** (artigos econômicos, publicações, etc.)

3️⃣ **Fase 3 - Integração com Agentes de IA:**
   - Conexão dinâmica com o **framework de agentes de IA**
   - **Personalização do acesso** baseado na missão do agente
   - Acompanhamento e monitoramento de desempenho 📈

---

## ⚙️ Implantação e Uso
### **Instalação**
```bash
# Clonar o repositório
git clone https://github.com/0xrubusdata/rubus-vms
cd rubus-vms

# Instalar dependências
pip install -r requirements.txt

# Iniciar o servidor FastAPI
uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload

### **Exemplo de Requisição API**
```bash
curl -X POST "http://localhost:8000/search" \
     -H "Content-Type: application/json" \
     -d '{"query": "impacto do aumento das taxas de juros"}'
```

---

## 📌 Conclusão
O projeto **Vector Memory Service** é um componente **central** do ecossistema **RubusData**:
- **Permite a organização, busca e recuperação eficiente de dados indexados**.
- **Fornece uma base sólida para agentes de IA capazes de acessar memória persistente e otimizada**.
- **Sua integração flexível permite adaptação a vários tipos de missões de IA**.

🔥 **Próximo passo: Integração com o framework de agentes de IA!** 🚀
