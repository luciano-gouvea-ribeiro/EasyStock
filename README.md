# EasyStock

Sistema de gerenciamento de estoque desenvolvido com **FastAPI**, **PostgreSQL** e **Frontend Web**, criado para a disciplina **Software Product: Analysis, Specification, Project & Implementation**.

O projeto utiliza arquitetura em camadas, boas práticas de desenvolvimento backend e integração entre API REST e interface web.

---

# Tecnologias Utilizadas

## Backend

* Python
* FastAPI
* SQLAlchemy
* PostgreSQL
* Uvicorn

## Frontend

* HTML5
* CSS3
* JavaScript
* Fetch API

## Ferramentas

* Git
* GitHub
* Swagger/OpenAPI
* VS Code

---

# Arquitetura do Projeto

O backend foi desenvolvido utilizando arquitetura em camadas:

```text
Router
 ↓
Service
 ↓
Repository
 ↓
Database
```

Separando responsabilidades entre:

* Rotas HTTP
* Regras de negócio
* Persistência de dados
* Banco de dados

---

# Estrutura do Projeto

```text
EasyStock
│
├── app
│   ├── core
│   │   └── database.py
│   │
│   ├── models
│   │   ├── product_model.py
│   │   ├── stock_model.py
│   │   └── category_model.py
│   │
│   ├── schemas
│   │   ├── product_schema.py
│   │   ├── movement_schema.py
│   │   └── category_schema.py
│   │
│   ├── repositories
│   │   ├── product_repository.py
│   │   ├── stock_movement_repository.py
│   │   └── category_repository.py
│   │
│   ├── services
│   │   ├── product_service.py
│   │   ├── stock_movement_service.py
│   │   └── category_service.py
│   │
│   └── routers
│       ├── product_router.py
│       ├── stock_router.py
│       └── category_router.py
│
├── frontend
│   ├── index.html
│   ├── css
│   │   └── style.css
│   └── js
│       └── api.js
│
├── docs
│   ├── diagrama_caso_uso.png
│   └── diagrama_classes.png
│
├── main.py
├── requirements.txt
├── .env.example
└── README.md
```

---

# Como Executar o Projeto

## 1. Clonar o Repositório

```bash
git clone https://github.com/SEU_USUARIO/EasyStock.git
```

## 2. Entrar na Pasta

```bash
cd EasyStock
```

## 3. Criar Ambiente Virtual

```bash
python -m venv venv
```

## 4. Ativar Ambiente Virtual

### Windows

```bash
venv\Scripts\activate
```

### Linux/Mac

```bash
source venv/bin/activate
```

## 5. Instalar Dependências

```bash
pip install -r requirements.txt
```

## 6. Configurar Variáveis de Ambiente

Criar um arquivo `.env` baseado no `.env.example`.

Exemplo:

```env
DATABASE_URL=postgresql://user:password@localhost:5432/easystock
```

## 7. Executar a API

```bash
uvicorn main:app --reload
```

---

# Documentação da API

Após iniciar a aplicação:

Swagger:

```text
http://localhost:8000/docs
```

OpenAPI:

```text
http://localhost:8000/redoc
```

---

# Funcionalidades Implementadas

## Produtos

* Criar produto
* Listar produtos
* Buscar produto por ID
* Atualizar produto
* Excluir produto (Soft Delete)

---

## Categorias

* Criar categoria
* Listar categorias
* Buscar categoria por ID
* Atualizar categoria
* Excluir categoria (Soft Delete)

---

## Movimentação de Estoque

### Entrada de Estoque

```http
POST /api/v1/products/{product_id}/entrada
```

Permite adicionar quantidade ao estoque.

---

### Saída de Estoque

```http
POST /api/v1/products/{product_id}/saida
```

Permite remover quantidade do estoque.

---

## Busca de Produtos

Busca por:

### Nome

```http
GET /api/v1/products?product_name=caneta
```

### SKU

```http
GET /api/v1/products?product_sku=ABC123
```

---

## Paginação

```http
GET /api/v1/products/paginated?page=1&limit=10
```

---

# Frontend

O sistema possui interface web integrada à API.

Funcionalidades disponíveis:

* Listagem de produtos
* Busca por nome
* Paginação
* Cadastro de produtos

---

# Regras de Negócio

## Produtos

* Produtos possuem campo `ativo`
* Produtos inativos não aparecem nas consultas

---

## Categorias

* Nome obrigatório
* Nome único
* Soft Delete

---

## Movimentação de Estoque

* Quantidade deve ser maior que zero
* Produto deve existir
* Não permite saída com estoque insuficiente
* Toda movimentação é registrada no banco

---

# Banco de Dados

## products

Armazena informações dos produtos.

---

## categories

Armazena categorias dos produtos.

---

## stock_movements

Armazena histórico de movimentações.

Tipos:

* entrada
* saída

---

# Diagramas

Os diagramas do projeto estão disponíveis na pasta:

```text
/docs
```

Diagramas disponíveis:

* Diagrama de Caso de Uso
* Diagrama de Classes

---

# Testes Realizados

## Produtos

* Cadastro ✔
* Consulta ✔
* Atualização ✔
* Exclusão ✔

## Estoque

* Entrada ✔
* Saída ✔
* Validação de estoque insuficiente ✔

## Categorias

* Cadastro ✔
* Consulta ✔
* Atualização ✔
* Exclusão ✔

## Frontend

* Cadastro ✔
* Busca ✔
* Paginação ✔

---
