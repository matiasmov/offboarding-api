from fastapi import Header, HTTPException
import os


# Acho importante porque qualquer um com a URL conseguirá deletar, já que o token está integrado na api
# eu nao confio nos cladtequianos nao

async def validar_acesso(x_api_key: str = Header(None)):

    senha = os.getenv("API_KEY")
    if not senha or x_api_key != senha:
        raise HTTPException(status_code=500, detail="Erro config servidor")
    return True
