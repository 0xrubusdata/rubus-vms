# Dockerfile

# Étape 1 : Utiliser une image Python slim
# [🇬🇧 Step 1: Use a slim Python image] | [🇪🇸 Paso 1: Usar una imagen de Python slim] | [🇵🇹 Etapa 1: Usar uma imagem Python slim] | [🇯🇵 ステップ 1: スリムな Python イメージを使用] | [🇷🇺 Шаг 1: Используем облегченное изображение Python] | [🇸🇦 الخطوة 1: استخدام صورة Python صغيرة]
FROM python:3.10

# Étape 2 : Configurer le dossier de l'application
# [🇬🇧 Step 2: Set up the application folder] | [🇪🇸 Paso 2: Configurar la carpeta de la aplicación] | [🇵🇹 Etapa 2: Configurar a pasta da aplicação] | [🇯🇵 ステップ 2: アプリケーションフォルダーを設定] | [🇷🇺 Шаг24: Настроить папку приложения] | [🇸🇦 الخطوة 2: إعداد مجلد التطبيق]
WORKDIR /app

# Étape 3 : Copier les fichiers de dépendances Python
# [🇬🇧 Step 3: Copy Python dependency files] | [🇪🇸 Paso 3: Copiar archivos de dependencias de Python] | [🇵🇹 Etapa 3: Copiar arquivos de dependências do Python] | [🇯🇵 ステップ 3: Python の依存ファイルをコピー] | [🇷🇺 Шаг 3: Скопировать файлы зависимостей Python] | [🇸🇦 الخطوة 3: نسخ ملفات تبعيات Python]
COPY requirements.txt ./

# Étape 4 : Installer les dépendances Python
# [🇬🇧 Step 4: Install Python dependencies] | [🇪🇸 Paso 4: Instalar dependencias de Python] | [🇵🇹 Etapa 4: Instalar dependências do Python] | [🇯🇵 ステップ 4: Python の依存関係をインストール] | [🇷🇺 Шаг 4: Установить зависимости Python] | [🇸🇦 الخطوة 4: تثبيت تبعيات Python]
RUN pip install --no-cache-dir -r requirements.txt

# Étape 5 : Copier les fichiers de l'application
# [🇬🇧 Step 5: Copy application files] | [🇪🇸 Paso 5: Copiar archivos de la aplicación] | [🇵🇹 Etapa 5: Copiar arquivos da aplicação] | [🇯🇵 ステップ 5: アプリケーションファイルをコピー] | [🇷🇺 Шаг 5: Скопировать файлы приложения] | [🇸🇦 الخطوة 5: نسخ ملفات التطبيق]
COPY . .

# Étape 6 : Exposer les ports nécessaires
# [🇬🇧 Step 6: Expose necessary ports] | [🇪🇸 Paso 6: Exponer los puertos necesarios] | [🇵🇹 Etapa 6: Expor portas necessárias] | [🇯🇵 ステップ 6: 必要なポートを公開] | [🇷🇺 Шаг 6: Открыть необходимые порты] | [🇸🇦 الخطوة 6: كشف المنافذ اللازمة]
EXPOSE 8000

# Ajout d'un message pour afficher que l'API est prête
CMD ["sh", "-c", "echo '✅ Rubus-VMS is running on http://localhost:8001' && uvicorn app.main:app --host 0.0.0.0 --port 8001 --reload"]
