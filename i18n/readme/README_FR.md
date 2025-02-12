## 🌿 Welcome to **Rubus-VMS - API & Vector Memory Service (Rubus-VMS)**


## 🏗️ Introduction
Le projet **Vector Memory Service** est conçu pour créer une **mémoire vectorielle** à partir des données collectées par le système **Rubus-Cron**. Cette mémoire vectorielle servira de **base de connaissances dynamique** pour des agents IA spécialisés.

🔹 **Technologies utilisées :**
- **Langage :** Python 🐍
- **Base de données vectorielle :** FAISS / Weaviate / Pinecone / ChromaDB
- **API Backend :** FastAPI ⚡
- **Stockage des métadonnées :** PostgreSQL 🏛️
- **Intégration avec les agents IA :** OpenAI API / LlamaIndex / RAG personnalisé (Génération augmentée par récupération)

---

## 🎯 Objectifs & Fonctionnalités

1️⃣ **Ingestion & Prétraitement des Données**
   - Extraction depuis **Rubus-Cron** 📡
   - Nettoyage du texte et tokenisation
   - Vectorisation des données (embedding avec BERT, SBERT, etc.)

2️⃣ **Stockage & Indexation**
   - Indexation des vecteurs dans FAISS / Weaviate 🔍
   - Association avec les **métadonnées** stockées dans **PostgreSQL** 📊

3️⃣ **API de Recherche & Récupération**
   - Point de terminaison pour **interroger** la mémoire vectorielle
   - Recherche sémantique avancée pour les agents IA 🤖
   - **Optimisation de RAG (Génération Augmentée par Récupération)**

4️⃣ **Intégration avec les Agents IA**
   - Connexion aux modèles via **model-ai_microservice** 🎯
   - Accès à des données filtrées en fonction des besoins spécifiques de l'agent (par exemple, **agent économique**) 🏦

---

## ⚙️ **Installation et Configuration**

### **1️⃣ Cloner le dépôt**
```sh
git clone https://github.com/0xrubusdata/rubus-vms
cd rubus-vms
```
### **2️⃣ Configurer les variables d'environnement**
Créez un fichier .env à la racine du projet :
 - Définir la source de base (Rubus-PostgreSQL)
 - Définir la locale de base (métadonnées VMS-PostgreSQL)
 - Définir l'API d'intégration (locale ou distante)

### **3️⃣ Exécuter avec Docker**
```sh
docker-compose up --build
```

---

