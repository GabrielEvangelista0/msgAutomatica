from services.supabase_service import buscar_contatos
from services.zapi_service import enviar_mensagem

def main():
    contatos = buscar_contatos()

    for contato in contatos:
        response = enviar_mensagem(contato['telefone'], f"Olá, {contato['nome']}! Esta é uma mensagem automática.")
        if response and response.status_code == 200:
            print(f"Mensagem enviada para {contato['nome']} - ID: {contato['id']}, Telefone: {contato['telefone']}")
        else:
            print(f"Erro ao enviar mensagem para {contato['nome']} - ID: {contato['id']}, Telefone: {contato['telefone']}")


if __name__ == "__main__":
    main()