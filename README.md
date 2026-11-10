LangChain e FastAPI - Parte 2: Questão 1 (Chatbot / Fake LLM)

Aplicação desenvolvida para demonstrar a orquestração inicial de fluxos de chat e modelos simulados utilizando o framework LangChain integrado ao FastAPI.
Tecnologias Utilizadas

    Python

    FastAPI / Pydantic

    LangChain Core (FakeListLLM)

Como Executar

    Ative o ambiente virtual executando no PowerShell:
    .\venv\Scripts\Activate

    Instale as dependências executando:
    pip install fastapi uvicorn langchain langchain-core pydantic

    Execute o servidor FastAPI executando:
    uvicorn chatbot_fake_api:app --reload

    Teste a rota /chat na documentação interativa em:
    http://127.0.0.1:8000/docs
