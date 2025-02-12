## 🌿 Bienvenido a **Rubus-VMS - API y Servicio de Memoria Vectorial (Rubus-VMS)**

## 🏗️ Introducción
El proyecto **Servicio de Memoria Vectorial** está diseñado para crear una **memoria vectorial** a partir de datos recogidos por el sistema **Rubus-Cron**. Esta memoria vectorial servirá como una **base de conocimiento dinámica** para agentes de IA especializados.

🔹 **Tecnologías:**
- **Lenguaje:** Python 🐍
- **Base de Datos Vectorial:** FAISS / Weaviate / Pinecone / ChromaDB
- **API Backend:** FastAPI ⚡
- **Almacenamiento de Metadatos:** PostgreSQL 🏛️
- **Integración con Agentes de IA:** API de OpenAI / LlamaIndex / RAG Personalizado (Generación Aumentada por Recuperación)

---

## 🎯 Objetivos y Características

1️⃣ **Ingesta y Preprocesamiento de Datos**
   - Extracción de **Rubus-Cron** 📡
   - Limpieza de texto y tokenización
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
   - Acceso a datos filtrados según las necesidades específicas del agente (por ejemplo, **agente económico**) 🏦

---

## ⚙️ **Instalación y Configuración**

### **1️⃣ Clonar el repositorio**
```sh
git clone https://github.com/0xrubusdata/rubus-vms
cd rubus-vms
```
### **2️⃣ Configurar variables de entorno**
Crea un archivo .env en la raíz del proyecto:
 - Definir fuente base (Rubus-PostgreSQL)
 - Definir localización base (métadatos VMS-PostgreSQL)
 - Definir API de Embedding (local o remota)

### **3️⃣ Ejecutar con Docker**
```sh
docker-compose up --build
```

---
