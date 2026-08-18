Markdown
# FastAPI-MongoDB---Projeto-Loja

Uma API RESTful desenvolvida com FastAPI e MongoDB para uma gestão eficiente de produtos. Esta aplicação processa pedidos HTTP padrão para criar, ler, atualizar
e eliminar (CRUD) registos de produtos numa base de dados MongoDB.

## 🚀 Funcionalidades

* **Gestão de Produtos:** Operações CRUD completas (Criar, Ler, Atualizar, Eliminar) para produtos.
* **Integração com Base de Dados:** Ligação perfeita ao MongoDB para armazenamento de dados rápido e flexível.
* **Documentação Interativa:** Documentação automática e interativa da API fornecida pelo Swagger UI e ReDoc.

## 📋 Pré-requisitos

Antes de começar, certifique-se de que tem o seguinte instalado na sua máquina:
* [Python 3.8+](https://www.python.org/downloads/)
* [Atlas](https://www.mongodb.com/products/platform/atlas-database) (A correr via Atlas MongoDB ou localmente)
* [MongoDB](https://www.mongodb.com/try/download/community) 


## 🛠️ Instalação

**Siga estes passos para configurar o projeto na sua máquina local**


```
1. Clonar o repositório:

- git clone [https://github.com/Cyberwitcher1/FastAPI-MongoDB---Projeto-Loja.git](https://github.com/Cyberwitcher1/FastAPI-MongoDB---Projeto-Loja.git)
- cd FastAPI-MongoDB---Projeto-Loja

2. Criar um ambiente virtual:

- python -m venv venv

3. Ativar o ambiente virtual (Windows):

- .\venv\Scripts\activate
(Utilizadores de Mac/Linux: source venv/bin/activate)

4. Instalar as dependências:
Certifique-se de que o seu ambiente virtual está ativo e, em seguida, execute:

- pip install -r requirements.txt

⚙️ Configuração
Se houver algum dificuldade ou falta de depedências terá que ser instalado o seguinte em cmd/bash e com virtual environment ativado:

- pip install uvicorn
- pip install pymongo
- pip install bson

Depois no ficheiro database.py colocar a respectiva connection string/link para ter acesso a base de dados no atlas com o user e password.

🏃‍♂️ Executar a Aplicação
Para iniciar o servidor de desenvolvimento, execute o seguinte comando na raiz do seu projeto:

- uvicorn main:app --reload
A flag --reload garante que o servidor reinicia automaticamente sempre que fizer alterações ao código.

📖 Documentação da API
Assim que o servidor estiver a correr, o FastAPI gera automaticamente documentação interativa para a sua API. Pode aceder à mesma navegando
para os seguintes URLs no seu browser:

Swagger UI: http://127.0.0.1:8000/docs (Ideal para testar os endpoints diretamente)

ReDoc: http://127.0.0.1:8000/redoc (Excelente para ler a documentação padrão da API)
