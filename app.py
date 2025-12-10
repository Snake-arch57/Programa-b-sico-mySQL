import pymysql.cursors
 
def open_connection():
    return pymysql.connect(host='localhost',
                           user='seu usuário',
                           password='sua senha',
                           database='seu banco de dados',
                           cursorclass=pymysql.cursors.DictCursor)

logado = False
conexao = open_connection()

while True:
    
    print("---- MENU ----")
    print("1. Listar funcionários")
    print("2. Login")
    print("3. Inserir funcionários ")
    print("4. Buscar por id: ")
    print("5. Editar meta: ")
    print("6. Excluir funcionário")
    print("7. Fechar")
    print("--------------")
 
    opcao = input("Digite a opção: ")

    if opcao == "1":
        if logado == False:
            print("Você não está logado!")
            continue
 
        cursor = conexao.cursor()
        sql = "SELECT * FROM funcionários"
        cursor.execute(sql)
        result = cursor.fetchall()
        print(result)

    if opcao == "2":
        usuario = input("Digite seu usuário: ")
        senha = input("Digite sua senha: ")

        sql = "SELECT * FROM usuarios WHERE usuario = %s AND senha = %s"
        cursor = conexao.cursor()
        cursor.execute(sql, (usuario, senha))
        result = cursor.fetchone()

        if result:
            print("Login bem-sucedido!")
            logado = True
        else:
            print("Usuário ou senha incorretos.")

    if opcao == "3":
        if logado == False:
            print("Você não está logado!")
            continue

        sql = "INSERT INTO funcionários (departamento, metas, funcionário) VALUES (%s, %s, %s)"
        cursor = conexao.cursor()
        
        departamento = input("Digite o departamento: ")
        metas = input("Digite a meta: ")
        funcionário = input("Digite o nome do funcionário: ")
 
        cursor.execute(sql, (departamento, metas, funcionário))
        conexao.commit()
        print("Funcionário inserido!")

   
    if opcao == "4":
        if logado == False:
            print("Você não está logado!")
            continue

        id_func = input("Digite o ID: ")

        cursor = conexao.cursor()
        sql = "SELECT * FROM funcionários WHERE id = %s"
        cursor.execute(sql, (id_func,))
        result = cursor.fetchone()

        print(result)

    
    if opcao == "5":
        if logado == False:
            print("Você não está logado!")
            continue
        id_func = input("Digite o ID do funcionário: ")
        nova_meta = input("Digite a nova meta: ")

        sql = "UPDATE funcionários SET metas = %s WHERE id = %s"
        cursor = conexao.cursor()
        cursor.execute(sql, (nova_meta, id_func))
        conexao.commit()

        print("Meta atualizada!")

    if opcao == "6":
        if logado == False:
            print("Você não está logado!")
            continue

        nome = input("Digite o nome do funcionário:")
        sql = "DELETE FROM funcionários WHERE funcionário = %s;"
        cursor = conexao.cursor()
        cursor.execute(sql,(nome))
        conexao.commit()
        result = cursor.fetchone()

    if opcao == "7":
        print("Fechando")
        conexao.close()
        break

