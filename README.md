# HIKORIME

 O projeto Hikorime foi criado para simular um gerenciamento de aeroporto atraves da CLI.
 Com objetivo educacional, visamos entregar um projeto fácil de entender, bem documentado e
seguindo os princípios SOLID.

# Como usar:
### 1. Instalar depêndencias:
````bash
poetry install
````
### 2. Rodar a aplicação:
````bash
poetry run uvicorn main:app
````

### Estrutura do projeto atualmente

``` bash
.
├── hikorime.db
├── poetry.lock
├── pyproject.toml
├── pytest.ini
├── README.md
└── src
    ├── hikorime
    │   ├── cli
    │   │   ├── comissario.py
    │   │   ├── cores.py
    │   │   ├── iniciar.py
    │   │   ├── menus.py
    │   │   ├── opcoes.py
    │   │   ├── passageiro.py
    │   │   ├── registro.py
    │   │   ├── relatorio.py
    │   │   └── utils.py
    │   ├── controller
    │   │   ├── __init__.py
    │   │   ├── rotas_comissario.py
    │   │   ├── rotas_passageiro.py
    │   │   └── rotas_relatorios.py
    │   ├── __init__.py
    │   ├── models
    │   │   ├── bagagem.py
    │   │   ├── cadastro_de_voo.py
    │   │   ├── compra.py
    │   │   ├── cupom.py
    │   │   ├── enums
    │   │   │   ├── __init__.py
    │   │   │   ├── status_cupom.py
    │   │   │   ├── status_voo.py
    │   │   │   ├── tipo_bagagem.py
    │   │   │   └── tipo_pagamento.py
    │   │   ├── __init__.py
    │   │   ├── notificacaoModel.py
    │   │   ├── passagem.py
    │   │   └── visualizacao_de_voo.py
    │   ├── registro
    │   │   ├── controle.py
    │   │   ├── __init__.py
    │   │   ├── modelos.py
    │   │   └── service.py
    │   ├── repository
    │   │   ├── config.py
    │   │   ├── hikorime.db
    │   │   ├── __init__.py
    │   │   ├── repository_connection.py
    │   │   ├── repository_querys.py
    │   │   └── schema.sql
    │   ├── schemas
    │   │   ├── compra_passagem.py
    │   │   └── voo.py
    │   └── service
    │       ├── base_service.py
    │       ├── cadastro_voo.py
    │       ├── compra_service.py
    │       ├── cupom_service.py
    │       ├── enums
    │       │   ├── const_bagagens.py
    │       │   └── const_voo.py
    │       ├── __init__.py
    │       ├── passagem_service.py
    │       └── visualizacao_de_voo.py
    ├── main_cli.py
    ├── main.py
    └── tests
        ├── test_repository.py
        └── tests_unit
            ├── test_bagagem.py
            ├── test_compra.py
            ├── test_pagamento.py
            ├── test_passagem.py
            └── test_voo.py

14 directories, 61 files

```

## Diagrama UML das principais classes planejadas

<img width="4855" height="2994" alt="Hikorime - Tema Escuro" src="https://github.com/user-attachments/assets/e2feebef-30db-4800-a637-5a3ea12cb214" />


# 

# Equipe

| Membros  | Funções | Contribuição
| ------------- | ------------- | ------------- |
| [Ana Aisha](https://github.com/aishatomaz)  | Desenvolvedor  | |
| [Dhonatan](https://github.com/sudo-invers) | Desenvolvedor  | |
| [Gabriel Santos](https://github.com/gabriel-so-santos) | Desenvolvedor  | |
| [Sarah Mendes](https://github.com/sarahmendes-ufca)  | Desenvolvedor  | |
| [Letícia Dias](https://github.com/leticia-software-engineer)  | Desenvolvedor  | |
