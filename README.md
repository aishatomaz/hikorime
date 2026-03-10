# HIKORIME

 O Sistema de Aeroportos Hikorime será uma aplicação que possibilitará às empresas de aviação uma melhor organização dos seus processos internos, possibilitando a compra e venda de passagens e cálculo dos valores a serem pagos – considerando o peso das bagagens. Será possível oferecer cupons de descontos para usuários que já tenham comprado uma quantidade determinada de passagens, o passageiro poderá receber notificações de alerta após comprar suas passagens para que não esqueça a data e o horário dos seus voos, os passageiros também poderão escolher o assento que irão sentar na compra da passagem conforme disponibilidade, considerando uma taxa adicional cobrada.
O comissário será o responsável por fazer o cadastro dos voos, quantidades de passagens e datas disponíveis para que os usuários façam a compra. O piloto poderá acessar os voos que estão sob sua responsabilidade com informações de data, horário de saída e horário previsto de chegada, distância, localização e quantidade de passageiros. 
O sistema também deverá dispor de relatórios de quantidade de voos - semanal, mensal e anual, faturamento (semanal, mensal e anual). quantidade de passageiros que compraram passagens mais vezes(ranking).

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


# Regras de Negócio 

Para usuários

No cadastro do Piloto deverão ser informados seus dados pessoais:
nome,
CPF,
data de nascimento,
licença de habilitação,
senha para acessar o sistema

No cadastro de passageiros devem ser informados: 
nome,
CPF, 
email, 
data de nascimento, 
CPF do responsável (em caso de menores),
senha para acessar o sistema.

No cadastro de comissários devem ser informados também 
nome,
CPF,
data de nascimento,
número de identificação na empresa,
email e senha.

Para compra de passagens aéreas
Na compra de passagens para voos dentro do território nacional basta o login do usuário e a confirmação da sua passagem, escolha do assento, aplicação de cupom (se disponível), forma de pagamento e peso médio da sua bagagem.
Na compra de passagens internacionais devem ser informados além dos dados do primeiro caso- passaporte, vistos, nacionalidade e motivo.

Para cadastro de Voos e passagens disponíveis:
O comissário deve estar logado e deve adicionar nas informações do voo: data de saída, piloto responsável, local de saída e de chegada, quantidade de passagens disponíveis para serem vendidas e seus respectivos valores.
Regras de Negócio:
Passageiro poderá visualizar voos com passagens disponíveis. Também poderá escolher a passagem e realizar a compra delas. 
Permite até 10 kg de massa total, e tem de caber no compartimento superior. Caso esse valor seja ultrapassado, o sistema deve informar que não é possível levar bagagens com esse peso. 
Regra importante: Se o passageiro adicionar uma quantidade de passagens superior à disponível não será possível prosseguir com a compra, deve ser exibida a mensagem informando que a quantidade de passagens não pode ser superior a quantidade disponível.
Cupons devem ser aplicados automaticamente em compras de passagens de passageiros com mais de 3 compras no último ano. Os descontos são de 20% no valor total. (valores configuráveis caso necessário)
O sistema deve seguir a LGPD para segurança dos dados dos passageiros e funcionários.
O passageiro pode solicitar o cancelamento integral até 1 dia antes da viagem, e após isso, apenas solicitar o reembolso parcial (valores configuráveis por companhia).
Atendimento prioritário por lei a idosos, gestantes, PCD e obesos e crianças de colo.

# Justificativa da complexidade

O sistema de Aeroportos Hikorime é complexo pois envolve processos críticos, concorrentes e regulados, integrando subsistemas. O projeto contém uma vasta gama de Regras de Negócio, devendo atender diferentes perfis de usuário, tais como passageiros, tripulação de voo, equipes de solo, equipes de manutenção, cada um com suas responsabilidades, permissões e formas de agir. Além disso, Hikorime precisa comandar variadas áreas do aeroporto: Controle de voos, despacho de bagagens, segurança e serviços de solo. Alterações em uma parte do sistema geram efeito nas outras, a exemplo do atraso de um voo, isso impactaria na conexão dos passageiros e cronograma da tripulação.
O domínio de aeroporto pode ser representado de forma mais fiel por meio da Orientação à Objetos, podendo encapsular dados e determinar comportamentos. Documentos, funcionários e usuários podem ser representados pelo sistema, usando encapsulamento, abstração e modularização.
Herança e polimorfismo podem ser aplicados ao domínio, podendo abranger diferentes tipos de voo, como nacional ou internacional, os tipos de funcionário do sistema, como piloto ou comissário de bordo. No contexto do sistema, o polimorfismo irá permitir extensões sem alterar o código já existente.

# Princípios SOLID 

O projeto utilizou o princípio da Responsabiliade Única (SRP)
a fim de garantir que cada classe faça apenas uma coisa e
tenha um objetivo único, garantindo um baixo aclopamento;
O princípio OCP () foi aplicado, com a finalidade de adicionar
novos comportamentos através de herança ou interfaces, sem
alterar o código-fonte original;
O principio do ISP foi utilizado para dividir interfaces grandes
e genéricas em interfaces menores e mais específicas,
mantendo a organização;
