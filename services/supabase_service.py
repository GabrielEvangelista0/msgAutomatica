from supabase import create_client
from config import SUPABASE_URL, SUPABASE_KEY

supabase = create_client(
    SUPABASE_URL,
    SUPABASE_KEY
)

def buscar_contatos():
    #Busca os contatos na tabela "contatos" do Supabase, limitando a 3 resultados
    try:
        response = ( 
            # Acessa a tabela "contatos" do supabase, seleciona todas as colunas
            supabase
            .table("contatos")
            .select("*")
            .limit(3) #limuta a 3 resultados
            .execute()
        )
        return response.data
    except Exception as e:
        print(f"Erro ao buscar contatos: {e}")
        return []
    