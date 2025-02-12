import os
import openai

# OpenAI API Key
openai.api_key = os.getenv("OPENAI_API_KEY")

# Beispiel-Prompt
prompt = "Was sind die neuesten Trends in der KI-Forschung?"

response = openai.ChatCompletion.create(
    model="gpt-4",
    messages=[{"role": "user", "content": prompt}],
)

gpt_reply = response["choices"][0]["message"]["content"]

# GPT-Antwort als Datei speichern
file_path = "gpt_response.txt"
with open(file_path, "w", encoding="utf-8") as file:
    file.write(gpt_reply)

print("GPT-Antwort gespeichert!")
