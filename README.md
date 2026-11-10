# Cadastro de Empresas (CRUD)

Mini-projecto de Integração de Sistemas: sistema web CRUD, sem login e sem HTML.

- **Backend:** API REST com FastAPI (`api.py`)
- **Base de dados:** SQLite (`empresas.db`, criada automaticamente)
- **Frontend:** Streamlit, só Python (`app.py`)
- **Testes da API:** Postman (`postman_collection.json`)

## Campos da tabela `empresas`
`id`, `nome`, `nif`, `telefone`, `cidade`

## Como executar

```bash
python -m venv venv
venv\Scripts\activate          # Windows
# source venv/bin/activate     # Linux/Mac
pip install -r requirements.txt
```

Abra **dois terminais** na pasta do projecto:

```bash
# Terminal 1: API
uvicorn api:app --reload

# Terminal 2: interface
streamlit run app.py
```

- Interface: http://localhost:8501
- API / documentação: http://127.0.0.1:8000/docs

## Endpoints

| Método | Rota | Descrição |
|--------|------|-----------|
| POST | `/empresas` | Cadastrar |
| GET | `/empresas` | Listar todas |
| GET | `/empresas/{id}` | Ver uma |
| PUT | `/empresas/{id}` | Atualizar |
| DELETE | `/empresas/{id}` | Remover |

## Equipa
- Backend: _Teodoro de Oliveira_
- Frontend: _Domingos Pereira_
- Base de dados: _Tércio Francisco_
