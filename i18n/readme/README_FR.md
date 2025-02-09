# 📌 Vector Memory Service - AI-Powered Data Indexing

## 🏗️ Introduction
Le projet **Vector Memory Service** est conçu pour créer une **mémoire vectorielle** à partir des données collectées par le système **Rubus-Cron**. Cette mémoire vectorielle servira de **base de connaissance dynamique** pour des agents IA spécialisés.

🔹 **Stack Technique :**
- **Langage :** Python 🐍
- **Base de données vectorielle :** FAISS / Weaviate / Pinecone / ChromaDB
- **API Backend :** FastAPI ⚡
- **Stockage des métadonnées :** PostgreSQL 🏛️
- **Pipeline NLP :** spaCy / SentenceTransformers / LangChain
- **Intégration avec des agents IA :** OpenAI API / LlamaIndex / Custom RAG (Retrieval-Augmented Generation)

---

## 🎯 Objectifs & Fonctionnalités

1️⃣ **Ingestion & Prétraitement des Données**
   - Extraction depuis **Rubus-Cron** 📡
   - Nettoyage et tokenization des textes
   - Vectorisation des données (embedding avec BERT, SBERT, etc.)

2️⃣ **Stockage & Indexation**
   - Indexation des vecteurs dans FAISS / Weaviate 🔍
   - Association avec des **métadonnées** stockées en **PostgreSQL** 📊

3️⃣ **API de Recherche & Récupération**
   - Endpoint pour **query** la mémoire vectorielle
   - Recherche sémantique avancée pour agents IA 🤖
   - **Optimisation du RAG (Retrieval-Augmented Generation)**

4️⃣ **Intégration avec des Agents AI**
   - Connexion aux modèles via **model-ai_microservice** 🎯
   - Accès aux données filtrées selon les besoins spécifiques d’un agent (ex : **agent économique**) 🏦
   
---

## 🚀 Roadmap de Développement

1️⃣ **Phase 1 - MVP :**
   - Développement du **pipeline d’ingestion et vectorisation**
   - Déploiement d’une **base de données vectorielle**
   - API de **stockage et requêtage des embeddings**

2️⃣ **Phase 2 - Améliorations :**
   - Optimisation de la **recherche sémantique** (Fine-tuning de modèles NLP)
   - Mise en place de **RAG avancé**
   - Intégration avec **d’autres sources de données** (articles économiques, publications, etc.)

3️⃣ **Phase 3 - Intégration avec les Agents AI :**
   - Connexion dynamique avec le **framework d’agents IA**
   - **Personnalisation des accès** selon la mission de l’agent
   - Suivi et monitoring des performances 📈

---

## ⚙️ Déploiement & Utilisation
### **Installation**
```bash
# Cloner le repo
git clone https://github.com/0xrubusdata/rubus-vms
cd rubus-vms

# Installer les dépendances
pip install -r requirements.txt

# Lancer l’API FastAPI
uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload
```

### **Exemple de Requête API**
```bash
curl -X POST "http://localhost:8000/search" \
     -H "Content-Type: application/json" \
     -d '{"query": "impact of interest rate hikes"}'
```

---

## 📌 Conclusion
Le projet **Vector Memory Service** est un élément **central** dans l’écosystème **RubusData** :
- **Il permet d’organiser, rechercher et récupérer des données indexées efficacement**.
- **Il offre un socle solide pour des agents IA capables d’accéder à une mémoire persistante et optimisée**.
- **Son intégration flexible permet une adaptation à plusieurs types de missions IA**.

🔥 **Prochaine étape : L’intégration avec le framework d’agents IA !** 🚀

