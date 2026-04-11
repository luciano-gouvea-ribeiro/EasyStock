# EasyStock 

API REST para gerenciamento de estoque desenvolvida com **FastAPI**.

O projeto foi criado como parte da materia Software Product: Analysis, Specification, Project & Implementation, utilizando arquitetura em camadas e boas práticas de desenvolvimento backend.

---

# Tecnologias utilizadas

* Python
* FastAPI
* Uvicorn
* PostgreSQL
* SQLAlchemy
* Git / GitHub

---

# Estrutura do Projeto

```
EasyStock
│
├── app
│   ├── core
│   │   └── database.py
│   │
│   ├── models
│   │   ├── product_model.py
│   │   └── stock_model.py
│   │
│   ├── schemas
│   │   ├── product_schema.py
│   │   └── movement_schema.py
│   │
│   ├── repositories
│   │   ├── product_repository.py
│   │   └── stock_movement_repository.py
│   │
│   ├── services
│   │   ├── product_service.py
│   │   └── stock_movement_service.py
│   │
│   └── routers
│       └── product_router.py
│
├── main.py
├── run.py
├── requirements.txt
├── .env.example
└── README.md
```

Arquitetura utilizada:

Router → Service → Repository → Database

---

# ⚙️ Como executar o projeto

### 1️⃣ Clonar o repositório

```
git clone https://github.com/SEU_USUARIO/EasyStock.git
```

### 2️⃣ Entrar na pasta

```
cd EasyStock
```

### 3️⃣ Criar ambiente virtual

```
python -m venv venv
```

### 4️⃣ Ativar ambiente

Windows:

```
venv\Scripts\activate
```

Linux / Mac:

```
source venv/bin/activate
```

### 5️⃣ Instalar dependências

```
pip install -r requirements.txt
```

### 6️⃣ Criar arquivo `.env`

Crie um arquivo `.env` baseado no `.env.example`.

Exemplo:

```
DATABASE_URL=postgresql://user:password@localhost:5432/easystock
```

### 7️⃣ Executar a API

```
uvicorn main:app --reload
```

---

# Documentação da API

Depois de iniciar o servidor, acesse:

Swagger:

```
http://localhost:8000/docs
```

---

# Endpoints disponíveis

## Produtos

| Método | Endpoint              | Descrição         |
| ------ | --------------------- | ----------------- |
| POST   | /api/v1/products      | Criar produto     |
| GET    | /api/v1/products      | Listar produtos   |
| GET    | /api/v1/products/{id} | Buscar produto    |
| PUT    | /api/v1/products/{id} | Atualizar produto |
| DELETE | /api/v1/products/{id} | Remover produto   |

---

## Movimentação de Estoque (AC2)

### Entrada de estoque

| Método | Endpoint                             | Descrição                   |
| ------ | ------------------------------------ | --------------------------- |
| POST   | /api/v1/products/{product_id}/entrada | Adiciona estoque ao produto |

Exemplo de body:

```
{
  "quantidade": 10
}
```

---

### Saída de estoque

| Método | Endpoint                           | Descrição                    |
| ------ | ---------------------------------- | ---------------------------- |
| POST   | /api/v1/products/{product_id}/saida | Remove estoque do produto    |

Exemplo de body:

```
{
  "quantidade": 5
}
```

---

# Regra de Negócio

## Produtos

Produtos possuem o campo **ativo**.

Produtos inativos não aparecem nas consultas da API.

---

## Movimentação de Estoque

- Quantidade deve ser maior que zero  
- Produto deve existir  
- Não é permitido saída com estoque insuficiente  
- Toda movimentação é registrada no banco de dados  

---

# Banco de Dados

### Tabela: products

- Armazena os dados dos produtos  

### Tabela: stock_movements

- Armazena histórico de movimentações de estoque  
- Tipos de movimentação:
  - entrada
  - saída  

---

# Testes realizados

- Entrada de estoque ✔  
- Saída de estoque ✔  
- Validação de quantidade inválida ✔  
- Validação de estoque insuficiente ✔  
- Validação de UUID inválido ✔  

---

# Status do Projeto

| Etapa | Status |
|------|-------|
| AC1 | ✅ Concluída |
| AC2 | ✅ Concluída |
| AC3 | 🔜 Em andamento |

---

