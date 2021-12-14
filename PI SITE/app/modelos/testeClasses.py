import publicacao
import perfil 
import curtida
import comentario
from config import *

#Teste da classe:
if __name__ == "__main__":
    #Apagar arquivo se houver:
    if os.path.exists(arquivobd):
        os.remove(arquivobd)

    #Criar tabelas:
    db.create_all()

    #Teste da classe Perfil: (dados apenas criados na memória)
    perfil1 = perfil.Perfil(nome = "Cris", senha = "n_sei123", email = "cris@gmail.com")
    perfil2 = perfil.Perfil(nome = "Maria", senha = "travesseirofofinho", email = "maria@gmail.com")
    perfil3 = perfil.Perfil(nome = "Gab", senha = "gabizito2004", email = "gab@gmail.com")
    perfil4 = perfil.Perfil(nome = "SenhorGabriel", senha = "abc321", email = "gabriel.hiebert@gmail.com")

    #Adicionar os dados na sessão de persistência:
    db.session.add(perfil1)
    db.session.add(perfil2)
    db.session.add(perfil3)

    
    #Teste da classe Publicacao: (dados apenas criados na memória)
    publicacao1 = publicacao.Publicacao(descricao = "reflorestamento", foto = "01000010101", perfil = perfil1)
    publicacao2 = publicacao.Publicacao(descricao = "telas solares", foto = "01010001010", perfil = perfil2)
    publicacao3 = publicacao.Publicacao(descricao = "Composteira", foto = "10101010100", perfil = perfil3)

    #Adicionar os dados na sessão de persistência:
    db.session.add(publicacao1)
    db.session.add(publicacao2)
    db.session.add(publicacao3)

    
    #Teste da classe Curtida: (dados apenas criados na memória)
    curtida1 = curtida.Curtida(data = "25/08/2021", perfil = perfil1, publicacao = publicacao2)
    curtida2 = curtida.Curtida(data = "25/08/2021", perfil = perfil2, publicacao = publicacao3)
    curtida3 = curtida.Curtida(data = "25/08/2021", perfil = perfil3, publicacao = publicacao1)

    #Adicionar os dados na sessão de persistência:
    db.session.add(curtida1)
    db.session.add(curtida2)
    db.session.add(curtida3)
    
    #Teste da classe Comentario: (dados apenas criados na memória)
    comentario1 = comentario.Comentario(comentario = "Que árvores lindas!", perfil = perfil2, publicacao = publicacao1)
    comentario2 = comentario.Comentario(comentario = "Quero placas solares também!", perfil = perfil3, publicacao = publicacao2)
    comentario3 = comentario.Comentario(comentario = "Boa ideia, vou fazer uma composteira igual essa!", perfil = perfil1, publicacao = publicacao3)

    #Adicionar os dados na sessão de persistência:
    db.session.add(comentario1)
    db.session.add(comentario2)
    db.session.add(comentario3)

    db.session.commit()
    

    # TESTES: 

    #Teste da classe Perfil:
    #Traz os dados do banco para uma lista 
    perfis = db.session.query(perfil.Perfil).all() 
    #Imprime as informações
    print("")
    for i in perfis:
        print(i)
        print(i.json())
        print("")

    #Teste da classe Publicacoes:
    publicacoes = db.session.query(publicacao.Publicacao).all() 
    print("")
    for i in publicacoes:
        print(i)
        print(i.json())
        print("")


    #Teste da classe Comentario:
    comentarios = db.session.query(comentario.Comentario).all() 
    print("")
    for i in comentarios:
        print(i)
        print(i.json())
        print("")
    

    #Teste da classe Curtida:
    curtidas = db.session.query(curtida.Curtida).all() 
    print("")
    for i in comentarios:
        print(i)
        print(i.json())
        print("")
