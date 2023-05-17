import mysql.connector

def create_table(sql, connection, table):
    try:
        connection.execute(sql)
        print("Tabela", table, "criada com sucesso.")
    except mysql.connector.Error as err:
        print("Erro ao criar tabela:", table)
        print("Mensagem de erro:", err)
        exit()

# Cria uma conexão com o banco de dados
try:
    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="code_ninja"
    )
    cursor = connection.cursor()
except mysql.connector.Error:
    print("Erro ao conectar com o banco de dados")
    exit()


create_table(
    "CREATE TABLE alunos \
    (id INT NOT NULL AUTO_INCREMENT, \
    nome VARCHAR(255) NOT NULL, \
    email VARCHAR(100) NOT NULL, \
    senha VARCHAR(100) NOT NULL, \
    PRIMARY KEY (id), \
    INDEX (email))", cursor, "ALUNOS"
)

create_table(
    "CREATE TABLE professores \
    (id INT NOT NULL AUTO_INCREMENT, \
    nome VARCHAR(255) NOT NULL, \
    email VARCHAR(100) NOT NULL, \
    senha VARCHAR(100) NOT NULL, \
    especialidade VARCHAR(100) NOT NULL, \
    PRIMARY KEY (id), \
    INDEX (email))", cursor, "PROFESSORES"
)

create_table(
    "CREATE TABLE cursos \
    (id INT NOT NULL AUTO_INCREMENT, \
    nome VARCHAR(100), \
    descricao TEXT NOT NULL, \
    professor_id INT NOT NULL, \
    preco DECIMAL(10,2) NOT NULL, \
    PRIMARY KEY (id), \
    FOREIGN KEY (professor_id) REFERENCES professores(id), \
    INDEX (professor_id))", cursor, "CURSOS"
)

create_table(
    "CREATE TABLE carrinho \
    (id INT NOT NULL AUTO_INCREMENT, \
    aluno_id INT NOT NULL, \
    curso_id INT NOT NULL, \
    PRIMARY KEY (id), \
    FOREIGN KEY (aluno_id) REFERENCES alunos(id) ON DELETE CASCADE, \
    FOREIGN KEY (curso_id) REFERENCES cursos(id) ON DELETE CASCADE, \
    INDEX (aluno_id), \
    INDEX (curso_id))", cursor, "CARRINHO"
)

create_table(
    "CREATE TABLE itens \
    (id INT NOT NULL AUTO_INCREMENT, \
    carrinho_id INT NOT NULL, \
    nome VARCHAR(100) NOT NULL, \
    quantidade INT NOT NULL, \
    preco DECIMAL(10,2) NOT NULL, \
    PRIMARY KEY (id), \
    FOREIGN KEY (carrinho_id) REFERENCES carrinho(id) ON DELETE CASCADE, \
    INDEX (carrinho_id))", cursor, "ITENS"
)

create_table(
    "CREATE TABLE pagamento \
    (id INT NOT NULL AUTO_INCREMENT, \
    carrinho_id INT NOT NULL, \
    aluno_id INT NOT NULL, \
    data_pagamento DATE NOT NULL, \
    valor_pagamento DECIMAL(10, 2) NOT NULL, \
    PRIMARY KEY (id), \
    FOREIGN KEY (carrinho_id) REFERENCES carrinho(id) ON DELETE CASCADE, \
    FOREIGN KEY (aluno_id) REFERENCES alunos(id), \
    INDEX (carrinho_id), \
    INDEX (aluno_id))", cursor, "PAGAMENTO"
)