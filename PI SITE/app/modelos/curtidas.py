from publicacao import *
from config import *

#relação de composição com a classe Publicacao
class Curtida:
    #Atributos da Curtida:
    id = db.Column(db.Integer, primary_key= True)
    data = db.Column(db.String(254))
    #Chave estrangeira:
    perfil_id = db.Column(db.Integer, db.ForeignKey(Perfil.id), nullable=False)
    perfil = db.relationship("Perfil")
    publicacao_id = db.Column(db.Integer, db.ForeignKey(Publicacao.id), nullable=False)
    publicacao = db.relationship("Publicacao")

    #Expressar Curtida em forma de texto:
    def __str__(self) -> str:
        return f"id: {self.id}. data: {self.data}. perfil: {self.perfil} publicação: {self.publicacao}."

    def json(self):
        return{
            "id": self.id,
            "data": self.data,
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
    curtida1 = Curtida(data = "25/08/2021", perfil = perfil1, publicacao = publicacao2)
    curtida2 = Curtida(data = "25/08/2021", perfil = perfil2, publicacao = publicacao3)
    curtida3 = Curtida(data = "25/08/2021", perfil = perfil3, publicacao = publicacao1)

    #Adicionar os dados na sessão de persistência:
    db.session.add(curtida1)
    db.session.add(curtida2)
    db.session.add(curtida3)

    db.session.commit()