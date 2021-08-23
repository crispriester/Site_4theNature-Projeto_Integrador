import sqlite3


nome_db = "dados/4thenature.db"


def obterPerfisPeloNome(nome): 
        
    conexao = sqlite3.connect(nome_db)
    cursor = conexao.cursor()

    lista_pessoas = []
    pessoas = cursor.execute('''SELECT * FROM Perfil WHERE nome = ?''', (nome,)).fetchone()
    for i in pessoas.fetchall():
        lista_pessoas.append({"nome" : i[1]})
    tupla_pessoas = tuple(lista_pessoas)

    conexao.close()
    return(tupla_pessoas)

def obterPerfilPeloEmail(email): 
        
    conexao = sqlite3.connect(nome_db)
    cursor = conexao.cursor()

    email_perfil = cursor.execute('''SELECT * FROM Perfil WHERE email = ?''', (email,)).fetchone()
    if email_perfil is None:
        email_existe = False
    else:
        email_existe = True

    conexao.close()
    return(email_existe)

def concederAcessoAoPerfil(senha, email):
    conexao = sqlite3.connect(nome_db)
    cursor = conexao.cursor()

    email_existe = obterPerfilPeloEmail(email)
    
    senha_certa = cursor.execute('''SELECT * FROM Perfil WHERE senha = ? AND email = ? ''', (senha, email,)).fetchone()
    if email_existe == True and senha_certa is not None:
      
        conexao.commit()
        conexao.close()
        return True

    else:
        conexao.close()
        return False

def cadastrarPerfil(nome, senha, email):
    conexao = sqlite3.connect(nome_db)
    cursor = conexao.cursor()

    email_existe = obterPerfilPeloEmail(email)
    if email_existe == False:
        cursor.execute('''INSERT INTO Perfil VALUES (NULL, ?, ?, ?)''', (nome, senha, email))
      
        conexao.commit()
        conexao.close()
        return True

    else:
        conexao.close()
        return False

def editarPerfil(nome, senha, email):
    conexao = sqlite3.connect(nome_db)
    cursor = conexao.cursor()
        
    cursor.execute('''UPDATE Perfil SET nome = ?, senha = ? WHERE email = ?''', (nome, senha, email))

    conexao.commit()
    conexao.close()
    return True

def deletarPerfil(id_perfil: int):
    conexao = sqlite3.connect(nome_db)
    cursor = conexao.cursor()
        
    cursor.execute('''DELETE FROM Perfil WHERE id = ?''', (id_perfil,))

    conexao.commit()
    conexao.close()
    return True
