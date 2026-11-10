"""
Módulo de API FastAPI com LangChain utilizando FakeListLLM 
para simulação de chatbot em ambiente de testes e desenvolvimento.
"""

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from langchain_core.language_models.fake import FakeListLLM

# Inicializo a aplicação FastAPI definindo metadados descritivos
app = FastAPI(
    title="API de Chatbot com Fake LLM (LangChain)",
    description="Protótipo demonstrando a integração de FastAPI com LangChain e respostas simuladas.",
    version="1.0.0"
)

# Defino respostas simuladas que o FakeListLLM irá retornar em sequência
respostas_predefinidas = [
    "Olá! Como posso ajudar você com seus dados hoje?",
    "Entendi sua solicitação. Processando as informações...",
    "Esta é uma resposta simulada pelo Fake LLM para fins de teste.",
    "Operação concluída com sucesso no protótipo."
]

# Instancio o FakeListLLM do LangChain com a lista de respostas estáticas
try:
    fake_llm = FakeListLLM(responses=respostas_predefinidas)
except Exception as erro:
    raise RuntimeError(f"Erro ao inicializar o FakeListLLM: {str(erro)}")

# Defino o esquema de dados de entrada via Pydantic para validação do JSON
class RequisicaoChat(BaseModel):
    mensagem: str

@app.post("/chat", summary="Simula um chatbot básico com respostas estáticas")
def simular_chat(dados: RequisicaoChat):
    """
    Recebo uma mensagem de texto via JSON, passo pelo fluxo do LangChain 
    com Fake LLM e retorno a resposta simulada estruturada em JSON.
    """
    try:
        # Valido se a mensagem de entrada não está vazia
        if not dados.mensagem.strip():
            raise HTTPException(status_code=400, detail="A mensagem de entrada não pode estar vazia.")
        
        # Invocamos o modelo simulado do LangChain passando o input do usuário
        resposta_modelo = fake_llm.invoke(dados.mensagem)
        
        # Retorno o resultado estruturado para o cliente HTTP
        return {
            "mensagem_usuario": dados.mensagem,
            "resposta_simulada": resposta_modelo
        }
        
    except Exception as erro:
        raise HTTPException(status_code=500, detail=f"Erro interno no processamento do chatbot: {str(erro)}")

