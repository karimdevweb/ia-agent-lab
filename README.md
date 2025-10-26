# IAAgent

## Reactive AI Agent

Un agent réactif simple utilisant Ollama ou OpenAI pour répondre à des prompts en Python.  
Ce projet permet de tester un agent IA localement ou via Docker.

## Description

Cet agent :
- Reçoit un prompt utilisateur.
- Interagit avec un modèle LLM (`Mistral` ou `GPT`) via Ollama ou OpenAI.
- Renvoie une réponse textuelle directement dans le terminal ou le notebook.

Le fonctionnement est **réactif**, c’est-à-dire que l’agent ne garde pas de mémoire entre les interactions.

## Installation

### Localement
1. Installer Ollama et les modèles (ex: Mistral) :  
```bash
ollama run mistral "Bonjour !"


2. Installer les dépendances Python :

pip install -r requirements.txt

3. Lancer l’agent :
python src/AgentIA.py

Avec Docker
Construire l’image :
docker build -t ai-agent-lab .

Lancer le conteneur :
docker run --rm -it -v ~/.ollama:/root/.ollama ai-agent-lab


et cela devrait fonctionner !!



src/
├── AgentIA.py       # Agent réactif principal
├── main.py          # Script de lancement
Dockerfile           # Conteneurisation Docker
requirements.txt     # Dépendances Python
