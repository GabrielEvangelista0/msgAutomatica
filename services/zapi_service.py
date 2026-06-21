import requests

from config import (
    ZAPI_INSTANCE_ID,
    ZAPI_TOKEN,
    ZAPI_CLIENT_TOKEN
)

URL = (
    f"https://api.z-api.io/"
    f"instances/{ZAPI_INSTANCE_ID}/"
    f"token/{ZAPI_TOKEN}/send-text"
)

def enviar_mensagem(numero, mensagem):
    #Envia uma mensagem para o número especificado usando a API do ZAPI
    try:
        payload = {
            "phone": numero,
            "message": mensagem
        }

        headers = {
            "Client-Token": ZAPI_CLIENT_TOKEN
        }

        response = requests.post(
            URL,
            json=payload,
            headers=headers
        )

        return response
    except Exception as e:
        print(f"Erro ao enviar mensagem para {numero}: {e}")
        return None