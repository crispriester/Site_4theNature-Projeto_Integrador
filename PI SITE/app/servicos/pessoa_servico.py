import sqlite3


nome_db = "dados/4thenature.db"


def obterPessoasPeloNome(nome): 
        
    conexao = sqlite3.connect("dados/evento.db")
    cursor = conexao.cursor()

    lista_pessoas = []
    pessoas = cursor.execute('''SELECT * FROM Pessoa WHERE nome = ?''', (nome,)).fetchone()
    for i in pessoas.fetchall():
        lista_pessoas.append({"nome" : i[1]})
    tupla_pessoas = tuple(lista_pessoas)

    conexao.close()
    return(tupla_pessoas)

def obterPessoaPeloEmail(email): 
        
    conexao = sqlite3.connect(nome_db)
    cursor = conexao.cursor()

    email_pessoa = cursor.execute('''SELECT * FROM Pessoa WHERE email = ?''', (email,)).fetchone()
    if email_pessoa is None:
        email_existe = False
    else:
        email_existe = True

    conexao.close()
    return(email_existe)

def concederAcessoParaPessoa(email, senha):
    conexao = sqlite3.connect(nome_db)
    cursor = conexao.cursor()

    email_existe = obterPessoaPeloEmail(email)
    
    senha_certa = cursor.execute('''SELECT * FROM Pessoa WHERE senha = ? AND email = ? ''', (senha, email,)).fetchone()
    if email_existe == True and senha_certa is not None:
      
        conexao.commit()
        conexao.close()
        return True

    else:
        conexao.close()
        return False

def cadastrarPessoa(nome, email, senha):
    conexao = sqlite3.connect(nome_db)
    cursor = conexao.cursor()

    email_existe = obterPessoaPeloEmail(email)
    if email_existe == False:
        cursor.execute('''INSERT INTO Pessoa VALUES (NULL, ?, ?, ?)''', (nome, senha, email))
      
        conexao.commit()
        conexao.close()
        return True

    else:
        conexao.close()
        return False

def editarPessoa(nome, senha, email):
    conexao = sqlite3.connect(nome_db)
    cursor = conexao.cursor()
        
    cursor.execute('''UPDATE Pessoa SET nome = ?, senha = ? WHERE email = ?''', (nome, senha, email))

    conexao.commit()
    conexao.close()
    return True

def deletarPessoa(id_pessoa: int):
    conexao = sqlite3.connect(nome_db)
    cursor = conexao.cursor()
        
    cursor.execute('''DELETE FROM Pessoa WHERE id = ?''', (id_pessoa,))

    conexao.commit()
    conexao.close()
    return True
