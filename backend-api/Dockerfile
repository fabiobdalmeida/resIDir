# Usa uma imagem Python leve
FROM python:3.10-slim

# Define diretório de trabalho
WORKDIR /app

# Copia dependências e instala
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copia o código
COPY . .

# O Cloud Run injeta a variável PORT. O padrão é 8080.
CMD exec uvicorn main:app --host 0.0.0.0 --port ${PORT:-8080}