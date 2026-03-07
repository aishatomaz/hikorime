CREATE TABLE IF NOT EXISTS `funcionarios` (
  `id_funcionario` integer,
  `id_pessoa` integer,
  `tipo_cargo` varchar(255),
  `disponivel_viagem` boolean,
  PRIMARY KEY (`id_funcionario`)
);

CREATE TABLE IF NOT EXISTS `pessoas` (
  `id_pessoa` integer,
  `nome` varchar(255),
  `cpf` varchar(14),
  `data_nacimento` date,
  PRIMARY KEY (`id_pessoa`)
);

CREATE TABLE IF NOT EXISTS `passageiros` (
  `id_passageiro` integer,
  `id_pessoa` integer,
  `tipo_identidade` varchar(255),
  `tipo_passageiro` varchar(255),
  `tipo_passaporte` varchar(255),
  PRIMARY KEY (`id_passageiro`)
);

CREATE TABLE IF NOT EXISTS `compras` (
  `id_compra` integer,
  `id_passageiro` integer,
  `id_bagagem` integer,
  `id_cupom` integer,
  `data_compra` date,
  `tipo_pagamento` varchar(255),
  `valor_compra` decimal(5, 2),
  PRIMARY KEY (`id_compra`),
  FOREIGN KEY (`id_passageiro`)
      REFERENCES `passageiro`(`id_passageiro`)
);

CREATE TABLE IF NOT EXISTS `bagagens` (
  `id_bagagem` integer,
  `tipo_bagagem` varchar(255),
  `peso` float,
  `valor_bagagem` decimal(5,2),
  PRIMARY KEY (`id_bagagem`),
  FOREIGN KEY (`id_bagagem`)
      REFERENCES `compra`(`id_bagagem`)
);

CREATE TABLE IF NOT EXISTS `usuarios` (
  `id_usuario` integer,
  `id_pessoa` integer,
  `email` varchar(255),
  `senha` varchar(255),
  PRIMARY KEY (`id_usuario`)
);

CREATE TABLE IF NOT EXISTS `passagens` (
  `id_passagem` integer,
  `id_voo` integer,
  `id_compra` integer,
  `id_passageiro` integer,
  `assento` smallint,
  `valor_passagem` decimal(5, 2),
  PRIMARY KEY (`id_passagem`)
);

CREATE TABLE IF NOT EXISTS `voos` (
  `id_voo` integer,
  `id_viagem` integer,
  `data_saida` date,
  `data_chegada` date,
  `local_origem` varchar(255),
  `local_destino` varchar(255),
  `distancia` float,
  `qtd_passagens_disponiveis` smallint,
  `valor_passagem` decimal(6,2),
  PRIMARY KEY (`id_voo`)
);

CREATE TABLE IF NOT EXISTS `viagens` (
  `id_viagem` integer,
  `id_funcionario` integer,
  PRIMARY KEY (`id_viagem`),
  FOREIGN KEY (`id_funcionario`)
      REFERENCES `funcionarios`(`id_funcionario`)
);

CREATE TABLE IF NOT EXISTS `cupons` (
  `id_cupom` integer,
  `percentual_desconto` float,
  `validade` date,
  PRIMARY KEY (`id_cupom`)
);