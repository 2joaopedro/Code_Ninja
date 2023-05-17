import mysql.connector

# Conexão com o banco de dados
try:
    connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="code_ninja"
    )
    cursor = connection.cursor()
except mysql.connector.Error:
    print("Erro ao conectar ao banco de dados")
    exit()

# Função pra cadastrar alunos
def cadastrar_alunos():
    nome = input("Digite seu nome: ")
    email = input("Digite seu email: ")
    senha = input("Digite sua senha: ")
    cursor = connection.cursor()
    sql = "INSERT INTO alunos (nome, email, senha) VALUES (%s, %s, %s)"
    valores = (nome, email, senha)
    cursor.execute(sql, valores)
    connection.commit()
    print("Aluno cadastrado com sucesso!")

# Função da listar os alunos
def listar_alunos():
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM alunos ORDER BY id")
    alunos = cursor.fetchall()
    if not alunos:
        print("Nenhum aluno cadastrado!")
    else:
        for aluno in alunos:
            print(f"ID: {aluno[0]}, Nome: {aluno[1]}, Email: {aluno[2]}, Senha: {aluno[3]}")

# Função para cadastrar professores
def cadastrar_professores():
    nome = input("Digite seu nome: ")
    email = input("Digite seu email: ")
    senha = input("Digite sua senha: ")
    especialidade = input("Digite sua especialidade: ")
    cursor = connection.cursor()
    sql = "INSERT INTO professores (nome, email, senha, especialidade) VALUES (%s, %s, %s, %s)"
    valores = (nome, email, senha, especialidade)
    cursor.execute(sql, valores)
    connection.commit()
    print("Professor cadastrado com sucesso!")

# Função para lista os professores 
def listar_professores():
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM professores ORDER BY id")
    professores = cursor.fetchall()
    if not professores:
        print("Nenhum professor cadastrado!")
    else:
        for professor in professores:
            print(f"ID: {professor[0]}, Nome: {professor[1]}, Email: {professor[2]}, Senha: {professor[3]}, Especialidade: {professor[4]}")

# Função para cadastrar os cursos
def cadastrar_cursos():
    nome = input("Digite o nome do curso: ")
    descricao = input("Descreva o curso: ")
    preco = input("Digite o preço: ")
    print("Escolha o professor para o curso:")
    listar_professores()
    professor_id = input("ID do professor selecionado: ")

    # Verificar se o ID do professor selecionado é válido
    cursor = connection.cursor()
    sql = "SELECT id FROM professores WHERE id = %s"
    valores = (professor_id,)
    cursor.execute(sql, valores)
    professor = cursor.fetchone()

    if professor is None:
        print("ID do professor inválido")
        return

    # Inserir um novo registro na tabela
    cursor = connection.cursor()
    sql = "INSERT INTO cursos (nome, descricao, professor_id, preco) VALUES (%s, %s, %s, %s)"
    valores = (nome, descricao, professor_id, preco)
    cursor.execute(sql, valores)
    connection.commit()
    print("Curso cadastrado com sucesso!")

# Função para listar os cursos
def listar_cursos():
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM cursos ORDER BY id")
    cursos = cursor.fetchall()
    if not cursos:
        print("Nenhum curso registrado!")
    else:
        for curso in cursos:
            print(f"ID: {curso[0]}, Nome: {curso[1]}, Descrição: {curso[2]}, ID do Professor: {curso[3]}, Preço: {curso[4]}")

while True:
    print("\nEscolha uma opção: ")
    print("1 - Cadastrar Aluno")
    print("2 - Cadastrar Professor")
    print("3 - Cadastrar Curso")
    print("4 - Listar Alunos")
    print("5 - Listar Professores")
    print("6 - Listar Cursos")
    print("0 - Sair")

    opcao = input("Opção selecionada: ")

    if opcao == "1":
        cadastrar_alunos()
    elif opcao == "2":
        cadastrar_professores()
    elif opcao == "3":
        cadastrar_cursos()
    elif opcao == "4":
        listar_alunos()
    elif opcao == "5":
        listar_professores()
    elif opcao == "6":
        listar_cursos()
    elif opcao == "0":
        break
