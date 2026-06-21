from services.supabase_service import buscar_contatos
from services.zapi_service import enviar_mensagem
import logging

logging.basicConfig(level=logging.INFO)

def main():
    logging.info("buscando contatos no banco de dados...")
    contatos = buscar_contatos()

    if not contatos:
        logging.info("Nenhum contato encontrado.")
        return

    for contato in contatos:
        logging.info(f"Processando contato: {contato['nome']} - ID: {contato['id']}, Telefone: {contato['telefone']}")
        mensagem = f"Olá, {contato['nome']} teste de envio de mensagem automática."
        # Envia a mensagem para o contato usando a função enviar_mensagem
        response = enviar_mensagem(contato['telefone'], mensagem)
        # Verifica se a mensagem foi enviada com sucesso e imprime o resultado
        if response and response.status_code == 200:
            logging.info(f"Mensagem enviada para {contato['nome']} - ID: {contato['id']}, Telefone: {contato['telefone']}")
        else:
            logging.error(f"Erro ao enviar mensagem para {contato['nome']} - ID: {contato['id']}, Telefone: {contato['telefone']}")


if __name__ == "__main__":
    main()