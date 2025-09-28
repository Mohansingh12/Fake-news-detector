import os,requests
from flask import Flask, request, jsonify

# Replace string URL client with a proper Ollama client instance
OLLAMA_ENDPOINT = os.getenv("OLLAMA_ENDPOINT", "http://ollama:11434")

def get_answer(question):
    
    model = "gemma3"
    prompt = f"{question}\nAnswer with yes or no."
    payload = {"model": model, "prompt": prompt, "stream": False}
    r = requests.post(f"{OLLAMA_ENDPOINT}/api/generate", json=payload, timeout=120)
    return r.json().get("response", "No response from model.")