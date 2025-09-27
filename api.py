import os,requests
from flask import Flask, request

# Replace string URL client with a proper Ollama client instance
OLLAMA_ENDPOINT = os.getenv("OLLAMA_ENDPOINT", "http://ollama:11434")

def get_answer(question):
    
    model = "gemma3"
    prompt = f"{question}\nAnswer with yes or no."

    data = request.get_json(force=True)
    prompt = data.get("prompt","Hello from Flask + Ollama!")
    payload = {"model":"gemma3", "prompt": prompt, "stream": False}
    r = requests.post(f"{OLLAMA_ENDPOINT}/api/generate", json=payload, timeout=120)
    r.raise_for_status()
    return str(r)