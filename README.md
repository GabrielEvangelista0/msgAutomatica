# Msg Automática

Aplicação desenvolvida em Python para integração entre Supabase e Z-API. O sistema busca até 3 contatos cadastrados no banco de dados e envia automaticamente mensagens personalizadas via WhatsApp.

## Setup da Tabela

Crie uma tabela chamada `contatos` no Supabase no editor sql com a seguinte estrutura:

create table contatos(
  id bigint generated always as identity primary key,
  nome text not null,
  telefone text unique not null
);
Para inserir valores na tabela no editor sql rode o comando:

insert into contatos(nome, telefone)
values
('nome1', '999999999'),
('nome2', '999999998'),
('nome3', '999999997');

## Variáveis de Ambiente

Crie um arquivo `.env` na raiz do projeto com as seguintes variáveis:

```env
# Supabase
SUPABASE_URL=sua_url_supabase
SUPABASE_KEY=sua_chave_supabase

# ZAPI
ZAPI_INSTANCE_ID=seu_instance_id
ZAPI_TOKEN=seu_token
ZAPI_CLIENT_TOKEN=seu_client_token
```

## Como Rodar

1. Instale as dependências:
```bash
pip install -r requirements.txt
```

2. Configure o arquivo `.env` com suas credenciais

3. Execute a aplicação:
```bash
python main.py
```

A aplicação buscará até 3 contatos do Supabase e enviará a mensagem "Olá, <nome_contato> tudo bem com você?" automaticamente.
