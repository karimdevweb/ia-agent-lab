# %%
import os
from google import genai
from dotenv import load_dotenv
#  load the api keys

# %%
#  load the api keys
load_dotenv("APIKeys.env")
GeminiKey = os.getenv('GEMINI_API_KEY')

# %% [markdown]
# ## 1- first start by calling Gemini model

# %%
#  create a function to automate the call
def CallGeminiModal(GeminiKey, query):

    client = genai.Client(api_key=GeminiKey)

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=query,
    )

    return response.text



# %%
#  ask a question
Geminiquery = "do you know Einstein"
GeminiRes = CallGeminiModal(GeminiKey, Geminiquery)

# %%
# import all libraries
# import API key
# define function calling the model
# define the query/the question
# catch and print the result
print(GeminiRes)



# ------------------------------------------------------------------------------------------------------------------------------------------------------------

# %% [markdown]
# ## 2- seconde, try ollama gpt model

# %%
# import library
import ollama
# define a function
def CallGptModel(model, role, query):
    response = ollama.chat(
        model=model, 
        messages=[
            {
                'role': role,
                'content': query,
            },
        ])
    return response['message']['content']

# %%
model = "gpt-oss:latest"
role= "user"
query = "do you know Einstein"
GptRes = CallGptModel(model, role, query)

# %%
print(GptRes)


# ------------------------------------------------------------------------------------------------------------------------------------------------------------

# %% [markdown]
# ## 3- third, try ollama mistral model

# %%
# import library
import ollama
# define a function
def CallMistralModel(model, role, query):
    response = ollama.chat(
        model=model, 
        messages=[
            {
                'role': role,
                'content': query,
            },
        ])
    return response['message']['content']

# %%
model = "mistral:latest"
role= "user"
query = "do you know Einstein"
MistralRes = CallMistralModel(model, role, query)

# %%
print(MistralRes)




# ------------------------------------------------------------------------------------------------------------------------------------------------------------



# %% [markdown]
# # II- prompt engineering

# %% [markdown]
# ### II 1.Gemini model with prompt engineering

# %%
from openai import OpenAI
from google import genai

# %%
# prompt engineering
role = "Tu brilles au ciel mais n’es pas une étoile."
context = "il y'a des soirs où tu montres ton visage, il y'a des soirs où t'es de profil."
todo = "Devine tout simplement qui tu es."
format = "En 2 phrases, décris qui tu es avec poésie ou rythme."

# %%
# gemini with parameters
def GeminiWithParam(GeminiKey, role, context, todo, format):

    client = genai.Client(api_key=GeminiKey)

    # Construire un prompt unique à partir des "variables"
    prompt = f"{role}\n{context}\n{todo}\n{format}"
    
    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
    )

    return response.text

# %%
# call the model gemini with all params , prompt engineering
GeminiParamRes = GeminiWithParam(GeminiKey,role, context, todo, format)

# %%
# print response
print(GeminiParamRes)



# %% [markdown]
# ---------------------------------------------------# ------------------------------------------------------------------------------------------------------------------------------------------------------------


# %% [markdown]
# ### II- 2.gpt model - with prompt engineering





# ########################## the model here accepted all variables , but the result was weird, i thinks it took only one variable to generate a response  ##########################################
# # %%
# # import library
# import ollama
# # define a function
# def OllamaWithParam(model, role, context, todo , format):
#     response = ollama.chat(
#         model=model, 
#         messages=[
#             {
#                 'role': role,
#                 'content': context,
#                 'todo': todo,
#                 'format': format
#             },
#         ])
#     return response['message']['content']


# # %%
# # prompt engineering
# role = "Tu brilles au ciel mais n’es pas une étoile."
# context = "il y'a des soirs où tu montres ton visage, il y'a des soirs où t'es de profil."
# todo = "Devine tout simplement qui tu es."
# format = "En 2 phrases, décris qui tu es avec poésie ou rythme."
# model = "gpt-oss:latest"

# GptParamRes = OllamaWithParam(model, role, context, todo, format)

# # %%
# # print the result
# print(GptParamRes)

# %% [markdown]
# -------------------------------------------------------------------

# %% [markdown]
# ### II- 3.Mistral model with prompt engineering

# %%
#  call the model mistral
# modelMistral = "mistral:latest"

# # %%
# #  the new params to teh function calling Ollama models
# MistralParamRes = OllamaWithParam(modelMistral, role, context, todo , format)

# # %%
# #  print the result
# print(MistralParamRes)
# ########################## the model here accepted all variables , but the result was weird, i thinks it took only one variable to generate a response  ##########################################




















# %% [markdown]
# ### II. 4 trying with only one text foramt for the prompt as for Gemini - API 

# %%
# prompt engineering
role = "Tu brilles au ciel mais n’es pas une étoile."
context = "il y'a des soirs où tu montres ton visage, il y'a des soirs où t'es de profil."
todo = "Devine tout simplement qui tu es."
format = "En 2 phrases, décris qui tu es avec poésie ou rythme."


# %%
prompt = f"{role}\n{context}\n{todo}\n{format}"

# %%
# ollama with one prompt
def OllamaOnePromptParam(model, prompt):
    response = ollama.chat(
        model=model, 
        messages=[
            {
                "role":"user",
                "content": prompt
            },
        ])
    return response['message']['content']

# %%
# result
Gptmodel = "gpt-oss:latest"
GptOneParam = OllamaOnePromptParam(Gptmodel, prompt)

# %%
#  print result
print(GptOneParam)



# %% [markdown]
# --------------

# %%
#  call the model mistral
modelMistral = "mistral:latest"
MistralOneParam = OllamaOnePromptParam(modelMistral, prompt)

# %%
#  print result
print(MistralOneParam)

# %%





# ------------------------------------------------------------------------------------------------------------------------------------------------------------

# %% [markdown]
# ## III- Agent Reactif

# %%
from openai import OpenAI

client = OpenAI(
    base_url="http://localhost:11434/v1/",  # Ollama local server
    api_key="ollama",  # obligatoire pour la lib OpenAI, mais ignoré localement
)

def reactive_agent(prompt):
    resp = client.chat.completions.create(
        model="mistral:latest",
        messages=[{"role":"user","content":prompt}]
    )
    return resp.choices[0].message.content.strip()

print("Tapez 'exit' ou 'quit' pour arrêter.\n")

while True:
    q = input("Vous : ")
    if q.lower() in ["quit", "exit"]:
        break
    print("Agent :", reactive_agent(q))

# %%







# ------------------------------------------------------------------------------------------------------------------------------------------------------------

# %% [markdown]
# ## IV- Mini Chat-bot

# %%
from openai import OpenAI

# Connexion à Ollama local
try:
    client = OpenAI(
        base_url="http://localhost:11434/v1/",  # Ollama local server
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


# %%



