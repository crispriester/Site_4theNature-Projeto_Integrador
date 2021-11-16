from publicacao import *
from perfil import *
from config import *

#relação de composição com a classe Publicacao
class Curtida(db.Model):
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
        return f"id: {self.id}. data: {self.data}. perfil: {self.perfil}. publicação: {self.publicacao}."

    def json(self):
        return{
            "id": self.id,
            "data": self.data,
            "perfil_id" : self.perfil_id,
            "perfil" : self.perfil.json(),
            "publicacao_id" : self.publicacao_id,
            "publicacao" : self.publicacao.json() 
        }
