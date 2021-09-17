import publicacao
import perfil
from config import *

#relação de composição com a classe Publicacao:
class Comentario(db.Model):
    #Atributos do Comentario:
    id = db.Column(db.Integer, primary_key= True)
    comentario = db.Column(db.String(254))
    #Chaves estrangeiras:
    perfil_id = db.Column(db.Integer, db.ForeignKey(perfil.Perfil.id), nullable=False)
    perfil = db.relationship("Perfil")
    publicacao_id = db.Column(db.Integer, db.ForeignKey(publicacao.Publicacao.id), nullable=False)
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
