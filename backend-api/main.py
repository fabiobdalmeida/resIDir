from fastapi import FastAPI
import os

app = FastAPI(title="resIDir API", version="1.0.0")

@app.get("/")
def read_root():
    return {"status": "online", "service": "resIDir Cloud Validation"}

@app.get("/health")
def health_check():
    return {"status": "ok"}

# Endpoint futuro para validar hash
@app.post("/register")
def register_document(data: dict):
    # Aqui entrará a lógica do Banco de Dados depois
    return {"message": "Endpoint de registro (WIP)", "received_data": data}