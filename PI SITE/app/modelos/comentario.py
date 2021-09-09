from publicacao import *
from config import *

#relação de composição com a classe Publicacao:
class Comentario:
    #Atributos do Comentario:
    id = db.Column(db.Integer, primary_key= True)
    comentario = db.Column(db.String(254))
    #Chaves estrangeiras:
    perfil_id = db.Column(db.Integer, db.ForeignKey(Perfil.id), nullable=False)
    perfil = db.relationship("Perfil")
    publicacao_id = db.Column(db.Integer, db.ForeignKey(Publicacao.id), nullable=False)
    publicacao = db.relationship("Publicacao")

    #Expressar Comentario em forma de texto:
    def __str__(self) -> str:
        return f"id: {self.id}. comentário: {self.comentario}. perfil: {self.perfil} publicação: {self.publicacao}."

    def json(self):
        return{
            "id": self.id,
            "comentario": self.comentario,
            "perfil_id" : self.perfil_id,
            "perfil" : self.perfil.json(),
            "publicacao_id" : self.publicacao_id,
            "publicacao" : self.publicacao.json() 
        }


#Teste da classe Nova:
if __name__ == "__main__":
    #Apagar arquivo se houver:
    if os.path.exists(arquivobd):
        os.remove(arquivobd)

    #Criar tabelas:
    db.create_all()

    #Teste da classe: (dados apenas criados na memória)
    comentario1 = Comentario(comentario = "Que árvores lindas!", perfil = perfil2, publicacao = publicacao1)
    comentario2 = Comentario(comentario = "Quero placas solares também!", perfil = perfil3, publicacao = publicacao2)
    comentario3 = Comentario(comentario = "Boa ideia, vou fazer uma composteira igual essa!", perfil = perfil1, publicacao = publicacao3)

    #Adicionar os dados na sessão de persistência:
    db.session.add(comentario1)
    db.session.add(comentario2)
    db.session.add(comentario3)

    db.session.commit()
