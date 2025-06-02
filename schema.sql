
-- schema.sql

-- Cria uma tabela simples para registrar cada vez que
-- o usuário clica no botão START.
CREATE TABLE IF NOT EXISTS processos (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
);
