import mysql.connector

def getConexao():
    conexao = mysql.connector.connect(
        host='10.1.1.109',
        user='admin',
        password='admin',
        database='loja_peixes'
    )
    return conexao

def cadastrar_peixe():
    nome = input('insira o nome do peixe: ')
    racas_id = input('insira id da raca: ')
    conexao = getConexao()
    cursor = conexao.cursor()
    sql = 'insert into peixes (nome, racas_id) values (%s, %s)'
    cursor.execute(sql, (nome, racas_id))
    id = cursor.lastrowid
    conexao.commit()
    cursor.close()
    conexao.close()
    print('Peixe cadastrado com sucesso!')
    return id

def alterar_peixe():
    listar_peixes
    conexao = getConexao()
    cursor = conexao.cursor()
    sql = 'SELECT * FROM peixes WHERE id=%s'


    PRECISA EDITAR PRA PRA LISTAR ANTES DE SELECIONAR
    O ID PRA EDITAR

    id = int(input('Id: '))
    conexao = getConexao()
    cursor = conexao.cursor()
    sql = 'select * from peixes where id=%s'
    cursor.execute(sql, (id, ))
    id, nome, racas_id = cursor.fetchone()
    novoNome = input('Digite o nome do peixe [{}]: '.format(nome))
    if novoNome == '':
        novoNome = nome
    sql = 'update peixes set nome=%s where id=%s'
    cursor.execute(sql, (novoNome, id))
    conexao.commit()
    cursor.close()
    conexao.close()
    print('Alteração realizada com sucesso!')

def listar_peixes():
    conexao = getConexao()
    cursor = conexao.cursor()
    sql = 'select * from peixes;'
    cursor.execute(sql)
    linhas = cursor.fetchall()
    cursor.close()
    conexao.close()
    print('id: nome: racas:')
    for id, nome, racas_id in linhas:
        print('{}: {}'.format(id, nome))
   

while True:
    print('1. Cadastrar peixe')
    print('2. Listar peixes')
    print('3. Alterar peixe')
    print('4. Sair')
    opcao = int(input())
    if opcao == 1:
        cadastrar_peixe()
    elif opcao == 2:
        listar_peixes()
    elif opcao == 3:
        alterar_peixe()
    elif opcao == 4:
        break