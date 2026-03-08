--DB reformulado

CREATE TABLE IF NOT EXISTS "usuarios" (
    "id_usuario" INTEGER PRIMARY KEY AUTOINCREMENT,
    "nome" TEXT,
    "cpf" TEXT,
    "data_nascimento" DATE,
    "email" TEXT,
    "senha" TEXT,
    "tipo_usuario" TEXT
) ;

CREATE TABLE IF NOT EXISTS "funcionarios" (
    "id_funcionario" INTEGER PRIMARY KEY AUTOINCREMENT,
    "id_usuario" INTEGER,
    "cargo" TEXT,
    "matricula" TEXT,
    FOREIGN KEY ("id_usuario") REFERENCES "usuarios" ("id_usuario")
) ;

CREATE TABLE IF NOT EXISTS "passageiros" (
    "id_passageiro" INTEGER PRIMARY KEY AUTOINCREMENT,
    "id_usuario" INTEGER,
    "codigo_passaporte" TEXT,
    "tipo_passaporte" TEXT,
    FOREIGN KEY ("id_usuario") REFERENCES "usuarios" ("id_usuario")
) ;

CREATE TABLE IF NOT EXISTS "aeronaves" (
    "id_aeronave" INTEGER PRIMARY KEY AUTOINCREMENT,
    "modelo" TEXT,
    "total_assentos" INTEGER
) ;

CREATE TABLE IF NOT EXISTS "voos" (
    "id_voo" INTEGER PRIMARY KEY AUTOINCREMENT,
    "id_aeronave" INTEGER,
    "data_hora_partida" DATETIME,
    "data_hora_chegada" DATETIME,
    "local_origem" TEXT,
    "local_destino" TEXT,
    "terminal" TEXT,
    "portao_embarque" TEXT,
    "valor_base_passagem" REAL,
    FOREIGN KEY ("id_aeronave") REFERENCES "aeronaves" ("id_aeronave")
) ;

CREATE TABLE IF NOT EXISTS "passagens" (
    "id_passagem" INTEGER PRIMARY KEY AUTOINCREMENT,
    "id_voo" INTEGER,
    "id_passageiro" INTEGER,
    "assento" TEXT,
    "valor_pago" REAL DEFAULT 0,
    "data_compra" DATETIME DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY ("id_voo") REFERENCES "voos" ("id_voo"),
    FOREIGN KEY ("id_passageiro") REFERENCES "passageiros" ("id_passageiro")
) ;

CREATE TABLE IF NOT EXISTS "cupons" (
    "id_cupom" INTEGER PRIMARY KEY AUTOINCREMENT,
    "id_passageiro" INTEGER,
    "percentual_desconto" REAL,
    "validade" DATE,
    "status" TEXT,
    "usado" INTEGER DEFAULT 0,
    "data_criacao" DATETIME DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY ("id_passageiro") REFERENCES "passageiros" ("id_passageiro")
) ;

CREATE TABLE IF NOT EXISTS "bagagens" (
    "id_bagagem" INTEGER PRIMARY KEY AUTOINCREMENT,
    "id_passageiro" INTEGER,
    "tipo_bagagem" TEXT,
    "peso" REAL,
    "valor_bagagem" REAL,
    "data_criacao" DATETIME DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY ("id_passageiro") REFERENCES "passageiros" ("id_passageiro")
) ;

CREATE TABLE IF NOT EXISTS "compras" (
    "id_compra" INTEGER PRIMARY KEY AUTOINCREMENT,
    "id_passageiro" INTEGER,
    "id_passagem" INTEGER,
    "id_bagagem" INTEGER,
    "id_cupom" INTEGER,
    "data_compra" DATETIME DEFAULT CURRENT_TIMESTAMP,
    "tipo_pagamento" TEXT,
    "valor_pago" REAL,
    "valor_desconto" REAL DEFAULT 0,
    "valor_total" REAL,
    FOREIGN KEY ("id_passageiro") REFERENCES "passageiros" ("id_passageiro"),
    FOREIGN KEY ("id_passagem") REFERENCES "passagens" ("id_passagem"),
    FOREIGN KEY ("id_bagagem") REFERENCES "bagagens" ("id_bagagem"),
    FOREIGN KEY ("id_cupom") REFERENCES "cupons" ("id_cupom")
) ;
