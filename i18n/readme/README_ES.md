
# 📌 Servicio de Memoria Vectorial - Indexación de Datos Impulsada por IA

## 🏗️ Introducción
El proyecto **Vector Memory Service** está diseñado para crear una **memoria vectorial** a partir de datos recopilados por el sistema **Rubus-Cron**. Esta memoria vectorial servirá como una **base de conocimiento dinámica** para agentes de IA especializados.

🔹 **Stack Tecnológico:**
- **Lenguaje:** Python 🐍
- **Base de Datos Vectorial:** FAISS / Weaviate / Pinecone / ChromaDB
- **API Backend:** FastAPI ⚡
- **Almacenamiento de Metadatos:** PostgreSQL 🏛️
- **Pipeline de PLN:** spaCy / SentenceTransformers / LangChain
- **Integración con Agentes de IA:** OpenAI API / LlamaIndex / RAG Personalizado (Generación Aumentada por Recuperación)

---

## 🎯 Objetivos y Características

1️⃣ **Ingesta y Preprocesamiento de Datos**
   - Extracción desde **Rubus-Cron** 📡
   - Limpieza y tokenización de texto
   - Vectorización de datos (incrustación con BERT, SBERT, etc.)

2️⃣ **Almacenamiento e Indexación**
   - Indexación de vectores en FAISS / Weaviate 🔍
   - Asociación con **metadatos** almacenados en **PostgreSQL** 📊

3️⃣ **API de Búsqueda y Recuperación**
   - Endpoint para **consultar** la memoria vectorial
   - Búsqueda semántica avanzada para agentes de IA 🤖
   - **Optimización de RAG (Generación Aumentada por Recuperación)**

4️⃣ **Integración con Agentes de IA**
   - Conexión a modelos a través de **model-ai_microservice** 🎯
   - Acceso a datos filtrados según necesidades específicas del agente (ej., **agente económico**) 🏦
   
---

## 🚀 Hoja de Ruta de Desarrollo

1️⃣ **Fase 1 - MVP:**
   - Desarrollo del **pipeline de ingesta y vectorización**
   - Despliegue de una **base de datos vectorial**
   - API para **almacenar y consultar embeddings**

2️⃣ **Fase 2 - Mejoras:**
   - Optimización de **búsqueda semántica** (Ajuste fino de modelos PLN)
   - Implementación de **RAG avanzado**
   - Integración con **otras fuentes de datos** (artículos económicos, publicaciones, etc.)

3️⃣ **Fase 3 - Integración con Agentes de IA:**
   - Conexión dinámica con el **marco de trabajo de agentes de IA**
   - **Personalización del acceso** según la misión del agente
   - Seguimiento y monitoreo del rendimiento 📈

---

## ⚙️ Despliegue y Uso
### **Instalación**
```bash
# Clonar el repositorio
git clone https://github.com/0xrubusdata/rubus-vms
cd rubus-vms

# Instalar dependencias
pip install -r requirements.txt

# Iniciar el servidor FastAPI
uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload

### **Ejemplo de Petición API**
```bash
curl -X POST "http://localhost:8000/search" \
     -H "Content-Type: application/json" \
     -d '{"query": "impacto de las subidas de tipos de interés"}'
```

---

## 📌 Conclusión
El proyecto **Vector Memory Service** es un componente **central** del ecosistema **RubusData**:
- **Permite la organización, búsqueda y recuperación eficiente de datos indexados**.
- **Proporciona una base sólida para agentes de IA capaces de acceder a memoria persistente y optimizada**.
- **Su integración flexible permite la adaptación a varios tipos de misiones de IA**.

🔥 **¡Siguiente paso: Integración con el marco de trabajo de agentes de IA!** 🚀
