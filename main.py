from services.supabase_service import buscar_contatos

def main():
    contatos = buscar_contatos()
    if not contatos:
        print("Nenhum contato encontrado.")
        return

    for contato in contatos:
        print(f"ID: {contato['id']}, Nome: {contato['nome']}, Telefone: {contato['telefone']}")


if __name__ == "__main__":
    main()