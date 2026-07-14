# Encurtador de URL API

API RESTful desenvolvida em Python e Flask para encurtar URLs e redirecionar acessos nativamente (Status HTTP 302). Arquitetura baseada no padrão Application Factory, garantindo modularidade e fácil manutenção.

## Tecnologias Utilizadas

- Python 3.11
- Flask & Blueprints
- SQLAlchemy (ORM)
- Docker

## Como Executar o Projeto

### Opção 1: Via Docker (Recomendado)

Certifique-se de ter o Docker em execução e rode os comandos na raiz do projeto:

```bash
docker build -t encurtador-url-api .
docker run -p 5000:5000 encurtador-url-api
```

### Opção 2: Localmente

```bash
# Instale as dependências
pip install -r requirements.txt

# Execute o servidor (O banco SQLite será criado automaticamente)
python run.py
```

## Como Mudar o Banco de Dados

O projeto foi construído de forma agnóstica de banco de dados utilizando SQLAlchemy. Para migrar do SQLite padrão para PostgreSQL ou MySQL:

1. Instale o driver correspondente no seu ambiente (ex: `pip install psycopg2` para PostgreSQL ou `pip install pymysql` para MySQL).

2. Acesse o arquivo `app/__init__.py` e substitua a string de conexão:

```python
# Exemplo para PostgreSQL:
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://usuario:senha@localhost/nome_do_banco'

# Exemplo para MySQL:
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://usuario:senha@localhost/nome_do_banco'
```

## Testes de Endpoint (PyCharm HTTP Client)

> **Importante:** O recurso **HTTP Client (`.http`) é exclusivo do PyCharm Professional**. Caso utilize o **PyCharm Community**, você poderá testar os endpoints utilizando ferramentas como Postman, Insomnia ou qualquer cliente HTTP de sua preferência.

Este repositório inclui um arquivo `testes.http` configurado para testes ágeis diretamente pela IDE, dispensando o uso de ferramentas externas para usuários da versão Professional.

**Como utilizar:**

1. Abra o arquivo `testes.http` localizado na raiz do projeto utilizando o **PyCharm Professional**.

2. O arquivo já contém o payload configurado:

```http
### Criar nova URL encurtada
POST http://127.0.0.1:5000/encurtar
Content-Type: application/json

{
  "url": "SUA URL AQUI"
}
```

3. Clique no ícone verde de execução ("Play") que aparece na margem esquerda da linha `POST`. O PyCharm executará a requisição HTTP contra o servidor local e exibirá o JSON de resposta (com o status **201 Created** e a URL encurtada) no painel de ferramentas integrado.