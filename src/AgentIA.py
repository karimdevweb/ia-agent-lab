from openai import OpenAI
import ollama
import os
from google import genai
from dotenv import load_dotenv
#  load the api keys

# %%
#  load the api keys
load_dotenv("APIKeys.env")
GeminiKey = os.getenv('GEMINI_API_KEY')



# Connexion à Ollama local
try:
    client = OpenAI(
        base_url="http://host.docker.internal:11434/v1/",  # Ollama local server
        api_key="ollama",  # obligatoire pour la lib OpenAI, mais ignoré localement
    )
except Exception as e:
    print(f"[Erreur] Impossible de connecter au serveur Ollama : {e}")
    exit(1)


def reactive_agent(prompt, temperature=0.7):
    """
    Envoie un message à Mistral avec une température donnée.
    """
    try:
        resp = client.chat.completions.create(
            model="mistral:latest",
            messages=[{"role": "user", "content": prompt}],
            temperature=temperature
        )
        return resp.choices[0].message.content.strip()
    except Exception as e:
        return f"[Erreur] Le modèle n’a pas pu répondre : {e}"


print("Tapez 'exit' ou 'quit' pour arrêter.")
print("Vous pouvez ajuster la créativité avec une température entre 0 et 1 (ex: 0.3 = plus logique, 0.9 = plus créatif)\n")

# Température initiale
temperature = 0.1

while True:
    try:
        q = input("Vous : ")
        if q.lower() in ["quit", "exit"]:
            print("Fin du chat. À bientôt !")
            break

        # Permettre de changer la température dynamiquement
        if q.lower().startswith("temp "):
            try:
                new_temp = float(q.split()[1])
                if 0 <= new_temp <= 1:
                    temperature = new_temp
                    print(f"Température mise à jour : {temperature}")
                else:
                    print("Entrez une valeur entre 0 et 1.")
            except ValueError:
                print("Format incorrect. Exemple : temp 0.8")
            continue

        print("Agent :", reactive_agent(q, temperature))

    except KeyboardInterrupt:
        print("\nChat interrompu par l’utilisateur.")
        break
    except Exception as e:
        print(f"[Erreur inattendue] {e}")