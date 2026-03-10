=======
## Sumário

- [HIKORIME](#hikorime)
- [Tecnologias Utilizadas](#tecnologias-utilizadas)
- [Descrição do Domínio](#descrição-do-domínio)
- [Como Usar](#como-usar)
  - [1. Instalar Dependências](#1-instalar-dependências)
  - [2. Rodar a Aplicação](#2-rodar-a-aplicação)
- [Como Testar](#como-testar)
- [Estrutura do Projeto Atualmente](#estrutura-do-projeto-atualmente)
- [Diagrama UML das Principais Classes Planejadas](#diagrama-uml-das-principais-classes-planejadas)
- [Boas Práticas Adotadas](#boas-práticas-adotadas)
  - [Princípios SOLID Aplicados](#princípios-solid-aplicados)
    - [1. Princípio da Responsabilidade Única (SRP)](#1-princípio-da-responsabilidade-única-srp---single-responsibility-principle)
    - [2. Princípio Aberto/Fechado (OCP)](#2-princípio-abertofechado-ocp---openclosed-principle)
    - [3. Princípio da Substituição de Liskov (LSP)](#3-princípio-da-substituição-de-liskov-lsp---liskov-substitution-principle)
    - [4. Princípio da Segregação de Interfaces (ISP)](#4-princípio-da-segregação-de-interfaces-isp---interface-segregation-principle)
    - [5. Princípio da Inversão de Dependência (DIP)](#5-princípio-da-inversão-de-dependência-dip---dependency-inversion-principle)

>>>>>>> e9eae68826cd8b736c15dc4c98a3f491bf696845

# HIKORIME

Com foco em consolidar os nossos aprendizados em Programação Orientada a Objetos, desenvolvemos um sistema robusto onde colocamos em práticas princípios fundamentais, tais como: herança, encapsulamento, validação, polimorfismo, composição, os princípios SOLID, arquitetura em camadas e outros padrões importantes. O nosso sistema é um Sistema de Aeroportos responsável por intermediar o processo de compra e venda de passagens, recebe o nome de HIKORIME como uma junção de três termos em japonês que são: hiko: voo, ori: origami, me = azul índigo, representando um avião de papel que voa no céu, símbolo do nosso projeto.

## Tecnologias Utilizadas

Este projeto foi desenvolvido utilizando as seguintes tecnologias:

<div align="center">
  <img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python"/>
  <img src="https://img.shields.io/badge/FastAPI-009688?style=for-the-badge&logo=fastapi&logoColor=white" alt="FastAPI"/>
  <img src="https://img.shields.io/badge/Pydantic-E92063?style=for-the-badge&logo=pydantic&logoColor=white" alt="Pydantic"/>
  <img src="https://img.shields.io/badge/Uvicorn-FF69B4?style=for-the-badge&logo=uvicorn&logoColor=white" alt="Uvicorn"/>
  <img src="https://img.shields.io/badge/Jinja2-2196F3?style=for-the-badge&logo=jinja&logoColor=white" alt="Jinja2"/>
  <img src="https://img.shields.io/badge/SQLite-003B57?style=for-the-badge&logo=sqlite&logoColor=white" alt="SQLite"/>
  <img src="https://img.shields.io/badge/HTML5-E34F26?style=for-the-badge&logo=html5&logoColor=white" alt="HTML5"/>
  <img src="https://img.shields.io/badge/CSS3-1572B6?style=for-the-badge&logo=css3&logoColor=white" alt="CSS3"/>
  <img src="https://img.shields.io/badge/JavaScript-F7DF1E?style=for-the-badge&logo=javascript&logoColor=black" alt="JavaScript"/>
  <img src="https://img.shields.io/badge/Poetry-602F8D?style=for-the-badge&logo=poetry&logoColor=white" alt="Poetry"/>
  <img src="https://img.shields.io/badge/Pytest-0A9EDC?style=for-the-badge&logo=pytest&logoColor=white" alt="Pytest"/>
  <img src="https://img.shields.io/badge/Pandas-150458?style=for-the-badge&logo=pandas&logoColor=white" alt="Pandas"/>
  <img src="https://img.shields.io/badge/Matplotlib-11557C?style=for-the-badge&logo=matplotlib&logoColor=white" alt="Matplotlib"/>
</div>

## Descrição do Domínio

O Sistema de Aeroportos Hikorime é uma aplicação que possibilita às empresas de aviação uma melhor organização dos seus processos internos, permitindo a compra e venda de passagens e o cálculo dos valores a serem pagos – considerando o peso das bagagens. Será possível oferecer cupons de descontos para usuários que já tenham comprado uma quantidade determinada de passagens, o passageiro poderá receber notificações de alerta após comprar suas passagens para que não esqueça a data e o horário dos seus voos, os passageiros também poderão escolher o assento que irão sentar na compra da passagem conforme disponibilidade, considerando uma taxa adicional cobrada.

O comissário será o responsável por fazer o cadastro dos voos, quantidades de passagens e datas disponíveis para que os usuários façam a compra. O piloto poderá acessar os voos que estão sob sua responsabilidade com informações de data, horário de saída e horário previsto de chegada, distância, localização e quantidade de passageiros.

O sistema também deverá dispor de relatórios de quantidade de voos - semanal, mensal e anual, faturamento (semanal, mensal e anual), e quantidade de passageiros que compraram passagens mais vezes (ranking).

## Como Usar:

### 1. Instalar Dependências:

````bash
poetry install
````

### 2. Rodar a Aplicação:

````bash
poetry run uvicorn main:app
````

## Como Testar

### 1. Para rodar os testes insira em seu terminal o comando:

````bash
poetry run pytest
````

## Estrutura do Projeto Atualmente

``` bash
.
├── poetry.lock
├── pyproject.toml
├── pytest.ini
├── README.md
├── relatorios.json
└── src
    ├── hikorime
    │   ├── controller
    │   │   ├── root.py
    │   │   ├── rotas_bagagem.py
    │   │   ├── rotas_base.py
    │   │   ├── rotas_passagens.py
    │   │   ├── rotas_registro.py
    │   │   ├── rotas_relatorios.py
    │   │   └── rotas_voos.py
    │   ├── models
    │   │   ├── bagagem.py
    │   │   ├── basemodels
    │   │   │   ├── bm_aeronave.py
    │   │   │   ├── bm_bagagem.py
    │   │   │   ├── bm_compra.py
    │   │   │   ├── bm_cupom.py
    │   │   │   ├── bm_funcionario.py
    │   │   │   ├── bm_login.py
    │   │   │   ├── bm_passageiro.py
    │   │   │   ├── bm_passagem.py
    │   │   │   ├── bm_usuario.py
    │   │   │   └── bm_voo.py
    │   │   ├── compra.py
    │   │   ├── cupom.py
    │   │   ├── enums
    │   │   │   ├── const_bagagens.py
    │   │   │   ├── status_cupom.py
    │   │   │   ├── status_voo.py
    │   │   │   ├── tipo_bagagem.py
    │   │   │   ├── tipo_pagamento.py
    │   │   │   ├── tipo_passaporte.py
    │   │   │   └── tipo_usuario.py
    │   │   ├── notificacao.py
    │   │   ├── passagem.py
    │   │   ├── registro.py
    │   │   └── voo.py
    │   ├── repository
    │   │   ├── config.py
    │   │   ├── repository_bagagem.py
    │   │   ├── repository_compra.py
    │   │   ├── repository_connection.py
    │   │   ├── repository_passagem.py
    │   │   ├── repository_querys.py
    │   │   ├── repository_relatorio.py
    │   │   └── schema.sql
    │   ├── service
    │   │   ├── aeronave_service.py
    │   │   ├── autenticacao_service.py
    │   │   ├── bagagem_service.py
    │   │   ├── base_service.py
    │   │   ├── compra_service.py
    │   │   ├── cupom_service.py
    │   │   ├── passagem_service.py
    │   │   ├── relatorio_service.py
    │   │   └── voo_service.py
    │   └── ui/...
    ├── main.py
    └── test/...
```

## Diagrama UML das Principais Classes Planejadas

<img width="4855" height="2994" alt="Hikorime - Tema Escuro" src="https://github.com/user-attachments/assets/e2feebef-30db-4800-a637-5a3ea12cb214" />

# Boas Práticas adotadas
## Princípios SOLID Aplicados

O projeto Hikorime foi desenvolvido com a aplicação dos princípios SOLID, visando a criação de um código mais limpo, modular, testável e de fácil manutenção. Abaixo, detalhamos como cada princípio foi incorporado:

### 1. Princípio da Responsabilidade Única (SRP - Single Responsibility Principle)

Cada módulo, classe ou função deve ter apenas uma razão para mudar, ou seja, uma única responsabilidade. No projeto Hikorime, este princípio é evidente na separação clara de responsabilidades:

*   **Conexão e Operações de Banco de Dados:** A classe `RepositoryConnection` é exclusivamente responsável por gerenciar a conexão com o banco de dados SQLite e executar operações CRUD de baixo nível.
    ````python
    # src/hikorime/repository/repository_connection.py
    class RepositoryConnection:
        def __init__(self, db_path=DATABASE_PATH):
            self.db_path = db_path
            self._init_db()

        def save(self, query: str, params: Tuple | dict = ()) -> int:
            # ... lógica de salvar ...
    ````

*   **Construção e Execução de Queries:** A classe `RepositoryQuerys` foca na construção de queries SQL e na interação com `RepositoryConnection` para executá-las, sem se preocupar com a lógica de negócio específica de cada entidade.
    ````python
    # src/hikorime/repository/repository_querys.py
    class RepositoryQuerys:
        def __init__(self, table_name: str, id_column: str):
            self.table_name = table_name
            self.id_column = id_column
            self.conn = RepositoryConnection()

        def save(self, **kwargs: Any) -> int:
            # ... lógica de construção de query e chamada a self.conn.save ...
    ````

*   **Lógica de Negócio Específica:** As classes de serviço (e.g., `AeronaveService`, `PassagemService`) são responsáveis pela lógica de negócio de uma entidade específica, utilizando `RepositoryQuerys` para persistência de dados.
    ````python
    # src/hikorime/service/aeronave_service.py
    class AeronaveService(BaseService):
        def __init__(self):
            self.repo = RepositoryQuerys(table_name="aeronaves", id_column="id_aeronave")

        def cadastrar_aeronave(self, aeronave: Aeronave):
            # ... lógica de negócio para cadastrar aeronave ...
    ````

### 2. Princípio Aberto/Fechado (OCP - Open/Closed Principle)

"Entidades de software (classes, módulos, funções, etc.) devem ser abertas para extensão, mas fechadas para modificação. Isso significa que o comportamento de um módulo pode ser estendido sem alterar seu código-fonte original."

*   **Extensão de Serviços:** A classe `BaseService` fornece uma base para outros serviços, permitindo que novas funcionalidades sejam adicionadas através da criação de subclasses (extensão) sem a necessidade de modificar `BaseService` (fechado para modificação).
    ````python
    # src/hikorime/service/base_service.py
    class BaseService:
        def __init__(self, repository: RepositoryQuerys):
            self.repo = repository

        def save(self, model) -> int:
            # ... métodos genéricos ...
    ````
    ````python
    # src/hikorime/service/aeronave_service.py
    class AeronaveService(BaseService):
        # ... estende BaseService com lógica específica de aeronaves ...
    ````

*   **Rotas Genéricas:** A função `create_generic_router` em `rotas_base.py` permite a criação de rotas CRUD para qualquer entidade, bastando fornecer o serviço e o esquema Pydantic correspondente. Isso significa que novas rotas podem ser adicionadas para novas entidades sem modificar a função `create_generic_router`.
    ````python
    # src/hikorime/controller/rotas_base.py
    def create_generic_router(service: BaseService, schema: Type[SchemaType]) -> APIRouter:
        # ... lógica para criar rotas GET, POST, PATCH, DELETE genéricas ...
        return router
    ````

### 3. Princípio da Substituição de Liskov (LSP - Liskov Substitution Principle)

"Objetos de um programa devem ser substituíveis por instâncias de seus subtipos sem alterar a corretude do programa. Em outras palavras, se `S` é um subtipo de `T`, então objetos do tipo `T` podem ser substituídos por objetos do tipo `S` sem quebrar o programa."

*   **Hierarquia de Usuários:** As classes `Passageiro` e `Funcionario` herdam de `UsuarioBase`. Onde quer que um `UsuarioBase` seja esperado, uma instância de `Passageiro` ou `Funcionario` pode ser utilizada sem problemas, pois elas estendem o comportamento da classe base sem violar seu contrato.
    ````python
    # src/hikorime/models/basemodels/bm_usuario.py
    class UsuarioBase(BaseModel):
        # ... campos base de usuário ...
    ````
    ````python
    # src/hikorime/models/basemodels/bm_passageiro.py
    class Passageiro(UsuarioBase):
        # ... campos específicos de passageiro ...
    ````
    ````python
    # src/hikorime/models/basemodels/bm_funcionario.py
    class Funcionario(UsuarioBase):
        # ... campos específicos de funcionário ...
    ````

### 4. Princípio da Segregação de Interfaces (ISP - Interface Segregation Principle)

"Clientes não devem ser forçados a depender de interfaces que não utilizam. Interfaces grandes e genéricas devem ser divididas em interfaces menores e mais específicas."

*   **Serviços e Repositórios:** Embora Python não utilize interfaces formais como outras linguagens, o design do projeto adere ao ISP. As classes de serviço interagem com `RepositoryQuerys` que expõe apenas os métodos de consulta e persistência necessários. Da mesma forma, `BaseService` define um conjunto mínimo de operações que os serviços específicos precisam implementar ou estender, evitando que os serviços sejam acoplados a métodos que não utilizam.
    ````python
    # src/hikorime/service/base_service.py
    class BaseService:
        # ... métodos como save, get_all, get_by_id ...
    ````
    Cada serviço específico (e.g., `AeronaveService`) utiliza apenas os métodos de `BaseService` e `RepositoryQuerys` que são relevantes para sua responsabilidade, sem ser forçado a implementar ou depender de funcionalidades desnecessárias.

### 5. Princípio da Inversão de Dependência (DIP - Dependency Inversion Principle)

"Módulos de alto nível não devem depender de módulos de baixo nível. Ambos devem depender de abstrações. Abstrações não devem depender de detalhes. Detalhes devem depender de abstrações."

*   **Injeção de Dependência em Serviços:** A classe `BaseService` (módulo de alto nível) não depende de uma implementação concreta de repositório (módulo de baixo nível), mas sim de uma abstração (`RepositoryQuerys`). O repositório é injetado no construtor de `BaseService`.
    ````python
    # src/hikorime/service/base_service.py
    from hikorime.repository.repository_querys import RepositoryQuerys

    class BaseService:
        def __init__(self, repository: RepositoryQuerys):
            self.repo = repository
            # ...
    ````
    Isso permite que `BaseService` seja reutilizável com diferentes implementações de `RepositoryQuerys` (se houvesse, por exemplo, um `RepositoryQuerysSQL` e um `RepositoryQuerysNoSQL`), promovendo flexibilidade e testabilidade.

## Padrões de Código

• Siga as diretrizes da PEP 8 para o estilo de código Python.

• Utilize nomes de variáveis, funções e classes descritivos e em inglês, quando apropriado.

• Comente seu código quando a lógica não for imediatamente óbvia.

• Escreva docstrings para funções, classes e módulos.


## Justificativa da Complexidade

O sistema de Aeroportos Hikorime é complexo pois envolve processos críticos, concorrentes e regulados, integrando subsistemas. O projeto contém uma vasta gama de Regras de Negócio, devendo atender diferentes perfis de usuário, tais como passageiros, tripulação de voo, equipes de solo, equipes de manutenção, cada um com suas responsabilidades, permissões e formas de agir. Além disso, Hikorime precisa comandar variadas áreas do aeroporto: Controle de voos, despacho de bagagens, segurança e serviços de solo. Alterações em uma parte do sistema geram efeito nas outras, a exemplo do atraso de um voo, isso impactaria na conexão dos passageiros e cronograma da tripulação.

O domínio de aeroporto pode ser representado de forma mais fiel por meio da Orientação à Objetos, podendo encapsular dados e determinar comportamentos. Documentos, funcionários e usuários podem ser representados pelo sistema, usando encapsulamento, abstração e modularização.

Herança e polimorfismo podem ser aplicados ao domínio, podendo abranger diferentes tipos de voo, como nacional ou internacional, os tipos de funcionário do sistema, como piloto ou comissário de bordo. No contexto do sistema, o polimorfismo irá permitir extensões sem alterar o código já existente.

## Equipe

| Membros  | Funções | Contribuição
| ------------- | ------------- | ------------- |
| [Ana Aisha](https://github.com/aishatomaz)  | Desenvolvedor  | Desenvolvimento de classes de login e cadastro, classes de cupons, testes e documentação |
| [Dhonatan](https://github.com/sudo-invers) | Desenvolvedor  | Desenvolvimento de classes de serviço, api, persistência e testes de persistência|
| [Gabriel Santos](https://github.com/gabriel-so-santos) | Desenvolvedor  | Desenvolvimento de classes de Service, api, interface gráfica e revisão|
| [Sarah Mendes](https://github.com/sarahmendes-ufca)  | Desenvolvedor  | Desenvolvimento de classes modelo, classes de relatórios e apresentação|
| [Letícia Dias](https://github.com/leticia-software-engineer)  | Desenvolvedor  | Desenvolvimento de classes de modelo, serviço, testes e documentação|

| Nome | Função |
| ------------- | ------------- |
| [Jayr Alencar Pereira](https://github.com/jayralencar) | Orientador

## Regras de Negócio

**Para usuários**

- No cadastro de usuários deve ser possível criar uma conta como passageiro ou como funcionário, no caso do passageiro, devem ser informados seus dados pessoais, bem como seu passaporte, enquanto no cadastro de funcionários, os dados de matrícula e cargo também são exigidos.
- O usuário que não possui login na plataforma pode visualizar os voos previstos, mas não consegue comprar passagens.
- O usuário com login de passageiro pode visualizar voos, passagens, fazer a comprar e acompanhar as informações referentes aos seus voos.
- O funcionário ele tem permissões extras como, cadastro de voos, visualização de relatórios e aeronaves, funções mais técnicas do sistema.

**Para compra de passagens aéreas**
- Na compra de passagens para voos dentro do território nacional basta o login do usuário e a confirmação da sua passagem, escolha do assento, aplicação de cupom (se disponível), forma de pagamento e peso médio da sua bagagem.
- Na compra de passagens internacionais devem ser informados além dos dados do primeiro caso- passaporte, vistos, nacionalidade e motivo.

**Para cadastro de Voos e passagens disponíveis:**
- O comissário deve estar logado e deve adicionar nas informações do voo: data de saída, piloto responsável, local de saída e de chegada, quantidade de passagens disponíveis para serem vendidas e seus respectivos valores.

**Regras de Negócio:**
- Passageiro poderá visualizar voos com passagens disponíveis. Também poderá escolher a passagem e realizar a compra delas.
- Permite até 10 kg de massa total, e tem de caber no compartimento superior. Caso esse valor seja ultrapassado, o sistema deve informar que não é possível levar bagagens com esse peso.
- Regra importante: Se o passageiro adicionar uma quantidade de passagens superior à disponível não será possível prosseguir com a compra, deve ser exibida a mensagem informando que a quantidade de passagens não pode ser superior a quantidade disponível.
- Cupons devem ser aplicados automaticamente em compras de passagens de passageiros com mais de 3 compras no último ano. Os descontos são de 20% no valor total. (valores configuráveis caso necessário)
- O sistema deve seguir a LGPD para segurança dos dados dos passageiros e funcionários.
- O passageiro pode solicitar o cancelamento integral até 1 dia antes da viagem, e após isso, apenas solicitar o reembolso parcial (valores configuráveis por companhia).
- Atendimento prioritário por lei a idosos, gestantes, PCD e obesos e crianças de colo.
