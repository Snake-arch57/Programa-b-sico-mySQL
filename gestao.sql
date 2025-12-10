# Aqui você pode criar o ambiente com os nomes que preferir
CREATE DATABASE seu banco de dados
    DEFAULT CHARACTER SET = 'utf8mb4';

USE seu banco de dados;

CREATE TABLE funcionários(
    id INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
    departamento VARCHAR(50),
    metas VARCHAR(50),
    funcionário VARCHAR(50)
);

CREATE TABLE usuários(
    id INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
    usuário VARCHAR(50),
    senha VARCHAR(50),
);

INSERT INTO funcionários (departamento, metas, funcionário) VALUES
    ('Vendas', 'Bater 50 vendas no mês', 'Ana Silva'),
    ('Financeiro', 'Fechar balanço trimestral', 'Carlos Pereira'),
    ('RH', 'Contratar 3 novos colaboradores', 'Julia Martins'),
    ('TI', 'Implementar novo sistema interno', 'Rafael Souza'),
    ('Marketing', 'Criar campanha de final de ano', 'Mariana Lopes'),
    ('Operações', 'Reduzir custos em 10%', 'Pedro Fernandes'),
    ('Logística', 'Aumentar eficiência de entregas', 'Lucas Andrade'),
    ('Jurídico', 'Revisar contratos pendentes', 'Beatriz Costa');


INSERT INTO usuarios (usuario, senha) VALUES
('admin', 'admin')