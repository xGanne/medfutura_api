# Medfutura API

## Descrição

Esta API permite a criação, consulta, busca, atualização e exclusão de pessoas utilizando os métodos GET, POST, PUT e DELETE, conforme pedido no processo seletivo da Medfutura.

## Tecnologias Utilizadas

- **Linguagem**: Python 3.9
- **Framework**: Django 5.1, Django REST Framework 3.15.2
- **Banco de Dados**: PostgreSQL

## Configuração do Ambiente

1. **Crie um ambiente virtual e ative-o**


2. **Instale as bibliotecas no requirements.txt:**

    ```bash
    pip install -r requirements.txt
    ```

3. **Configure o banco de dados PostgreSQL:**

    Crie o banco de dados no PostgreSQL e o usuário conforme as configurações no `.env`.

4. **Aplicar as migrações:**

    ```bash
    python manage.py makemigrations
    python manage.py migrate
    ```

5. **Rodar o servidor:**

    ```bash
    python manage.py runserver
    ```

## Funcionalidades Disponíveis

### 1. **Criar uma Pessoa**

- **URL:** `POST /api/pessoas/`
- **Exemplo da Requisição:**

    ```json
    {
        "id": 8,
        "apelido": "Carlinhos",
        "nome": "Carlos de Alcantara Silva",
        "nascimento": "2001-05-08",
        "stack": [
            "Django",
            "Flask"
        ]
    }
    ```

- **Respostas:**
    - **201 Created**: Pessoa criada com sucesso.
    - **422 Unprocessable Entity**: Dados inválidos.

### 2. **Consultar uma Pessoa pelo ID**

- **URL:** `GET /api/pessoas/{id}/`
- **Respostas:**
    - **200 OK**: Retorna os detalhes da pessoa.
    - **404 Not Found**: Pessoa não encontrada.

### 3. **Buscar Pessoas por Termo**

- **URL:** `GET /api/pessoas/?t=termo`
- **Parâmetros de Query:**
    - `t` (obrigatório): Termo para busca.
- **Respostas:**
    - **200 OK**: Retorna a lista de pessoas que correspondem ao termo.
    - **400 Bad Request**: Termo não informado.

### 4. **Atualizar uma Pessoa**

- **URL:** `PUT /api/pessoas/{id}/`
- **Respostas:**
    - **200 OK**: Pessoa atualizada com sucesso.
    - **422 Unprocessable Entity**: Dados inválidos.
    - **404 Not Found**: Pessoa não encontrada.

### 5. **Excluir uma Pessoa**

- **URL:** `DELETE /api/pessoas/{id}/`
- **Respostas:**
    - **204 No Content**: Pessoa excluída com sucesso.
    - **400 Bad Request**: Pessoa não encontrada.

## Executando os Testes

Para rodar os testes unitários, execute:

```bash
python manage.py test
```

## Estrutura administrativa do Django

É possível acessar o /admin/ do Django e verificar se os dados das Pessoas estão realmente armazenados. O SuperUser está disponível no arquivo .env.
