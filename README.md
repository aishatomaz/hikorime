# HIKORIME

 O projeto Hikorime foi criado para simular um gerenciamento de aeroporto atraves da CLI.
 Com objetivo educacional, visamos entregar um projeto fácil de entender, bem documentado e
seguindo os princípios SOLID.

# Como usar:

### estrutura do projeto atualmente

ela sera atualizada ao menos uma vez por semana.
``` bash
.
├── poetry.lock
├── pyproject.toml
├── pytest.ini
├── README.md
└── src
    ├── hikorime
    │   ├── cli
    │   │   └── __init__.py
    │   ├── controller
    │   │   └── __init__.py
    │   ├── __init__.py
    │   ├── models
    │   │   ├── bagagem.py
    │   │   ├── cadastro_de_voo.py
    │   │   ├── compra.py
    │   │   ├── cupom.py
    │   │   ├── enums
    │   │   │   └── __init__.py
    │   │   ├── __init__.py
    │   │   ├── notificacaoModel.py
    │   │   ├── pagamento.py
    │   │   ├── passagem.py
    │   │   ├── statusvoo.py
    │   │   ├── tipobagagem.py
    │   │   ├── tipo_pagamento.py
    │   │   └── visualizacao_de_voo.py
    │   ├── repository
    │   │   ├── config.py
    │   │   ├── __init__.py
    │   │   ├── repository_connection.py
    │   │   └── repository_querys.py
    │   ├── service
    │   │   ├── base_service.py
    │   │   └── __init__.py
    │   └── utils
    └── tests
        ├── test_repository.py
        └── tests_unit
            ├── test_bagagem.py
            ├── test_compra.py
            ├── test_pagamento.py
            ├── test_passagem.py
            └── test_voo.py

12 directories, 32 files

```

## Diagrama UML das principais classes planejadas

<img width="4855" height="2994" alt="Hikorime - Tema Escuro" src="https://github.com/user-attachments/assets/e2feebef-30db-4800-a637-5a3ea12cb214" />


# Contribuição:

# Equipe

| Membros  | Funções |
| ------------- | ------------- |
| [Ana Aisha](https://github.com/aishatomaz)  | Desenvolvedor  |
| [Dhonatan](https://github.com/sudo-invers) | Desenvolvedor  |
| [Gabriel Santos](https://github.com/gabriel-so-santos) | Desenvolvedor  |
| [Sarah Mendes](https://github.com/sarahmendes-ufca)  | Desenvolvedor  |
| [Letícia Dias](https://github.com/leticia-software-engineer)  | Desenvolvedor  |