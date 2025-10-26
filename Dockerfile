FROM python:3.11-slim

WORKDIR /app

# Copier les dépendances
COPY requirements.txt .
COPY src ./src

RUN pip install --no-cache-dir -r requirements.txt

# Copier tout le reste du code
COPY . .

# Démarrer ton programme principal
CMD ["python", "src/AgentIA.py"]
