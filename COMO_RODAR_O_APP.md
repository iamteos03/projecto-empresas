# Guia de Instalação e Execução do Projeto

Este documento descreve os passos necessários para configurar o ambiente e executar a aplicação localmente.

## Pré-requisitos

* Python 3.10 ou superior
* Visual Studio Code (ou outro editor de sua preferência)
* Git

## Passo 1: Criar e Ativar o Ambiente Virtual (Virtualenv)

Após clonar o repositório e abrir a pasta do projeto no VS Code, abra o terminal e siga as instruções:

### No Windows (PowerShell):

1. Criar o ambiente virtual:
   ```bash
   python -m venv venv
   ```

2. Ativar o ambiente virtual:
   ```powershell
   .\venv\Scripts\Activate
   ```
   (A tag `(venv)` deverá aparecer no início da linha do terminal).

#### Solução para Erro de Permissão no PowerShell
Caso ocorra o erro informando que a execução de scripts foi desabilitada no sistema, execute o comando abaixo para liberar a permissão na sessão atual:

```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope Process
```
Confirme com `S` (Sim) e execute o comando de ativação novamente.

## Passo 2: Instalar as Dependências

Com o ambiente virtual ativado, instale os pacotes listados no arquivo de requisitos:

```bash
pip install -r requirements.txt
```

## Passo 3: Executar a Aplicação

A aplicação é dividida em duas partes: a API (FastAPI) e a Interface Gráfica (Streamlit). Ambas precisam rodar simultaneamente em terminais separados.

### Terminal 1: API Backend (FastAPI)

1. No terminal com o ambiente virtual ativo, execute:
   ```bash
   uvicorn api:app --reload
   ```
2. A API ficará disponível na porta 8000.
3. Documentação Swagger da API: `http://127.0.0.1:8000/docs`

### Terminal 2: Interface Frontend (Streamlit)

1. Abra um segundo terminal no VS Code (ícone `+` no painel do terminal).
2. Ative o ambiente virtual neste novo terminal:
   ```powershell
   .\venv\Scripts\Activate
   ```
3. Execute o comando do Streamlit:
   ```bash
   streamlit run app.py
   ```
4. Se o terminal solicitar um e-mail de cadastro do Streamlit, pressione `Enter` para ignorar.
5. A interface gráfica abrirá no navegador no endereço: `http://localhost:8501`

## Passo 4: Testar o CRUD

* **Interface Web (`http://localhost:8501`):** Utilize o formulário e as opções do menu para cadastrar, listar, editar e remover empresas.
* **Postman:**
  1. Abra o aplicativo Postman.
  2. Importe o arquivo `postman_collection.json` localizado na raiz do projeto.
  3. Execute o pedido `POST` para cadastrar o primeiro registro antes de testar as rotas `GET`, `PUT` e `DELETE`.

## Estrutura de Arquivos

* `api.py`: Código-fonte da API (FastAPI).
* `app.py`: Código-fonte da interface visual (Streamlit).
* `requirements.txt`: Lista de dependências do Python.
* `postman_collection.json`: Coleção de requisições para testes na API.
* `.gitignore`: Configuração para ignorar arquivos locais e a pasta `venv` no Git.