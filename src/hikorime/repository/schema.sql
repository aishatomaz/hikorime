-- Temporario, apenas para fins de demonstracao e test;

CREATE TABLE IF NOT EXISTS usuarios (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    email TEXT NOT NULL UNIQUE,
    cpf TEXT NOT NULL,
    senha TEXT NOT NULL, -- Apenas para estudo, talvez usaremos bcrypt ou afins no futuro
    tipo TEXT NOT NULL CHECK (tipo IN ('passageiro', 'funcionario'))
);

CREATE TABLE IF NOT EXISTS passageiros (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    usuario_id INTEGER NOT NULL,
    passaporte TEXT,
    FOREIGN KEY (usuario_id) REFERENCES usuarios(id) ON DELETE CASCADE
);

CREATE TABLE IF NOT EXISTS funcionarios (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    usuario_id INTEGER NOT NULL,
    cargo TEXT NOT NULL,
    matricula TEXT NOT NULL,
    FOREIGN KEY (usuario_id) REFERENCES usuarios(id) ON DELETE CASCADE
);

CREATE TABLE IF NOT EXISTS passagens_vendidas (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    passageiro_id INTEGER NOT NULL
);
