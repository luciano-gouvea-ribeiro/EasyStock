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
│   │   └── product_model.py
│   │
│   ├── schemas
│   │   └── product_schema.py
│   │
│   ├── repositories
│   │   └── product_repository.py
│   │
│   ├── services
│   │   └── product_service.py
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

### Produtos

| Método | Endpoint       | Descrição         |
| ------ | -------------- | ----------------- |
| POST   | v1/products      | Criar produto     |
| GET    | v1/products      | Listar produtos   |
| GET    | v1/products/{id} | Buscar produto    |
| PUT    | v1/products/{id} | Atualizar produto |
| DELETE | v1/products/{id} | Remover produto   |

---

# Regra de Negócio

Produtos possuem o campo **ativo**.

Produtos inativos não aparecem nas consultas da API.

---