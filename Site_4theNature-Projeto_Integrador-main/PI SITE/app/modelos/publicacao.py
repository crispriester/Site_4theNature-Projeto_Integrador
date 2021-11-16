import perfil
from config import *

#relação de composição com a classe Perfil:
class Publicacao(db.Model):
    #Atributos da publicação:
    id = db.Column(db.Integer, primary_key= True)
    descricao = db.Column(db.String(254))
    foto = db.Column(db.String(254))
    #Chave estrangeira:
    perfil_id = db.Column(db.Integer, db.ForeignKey(perfil.Perfil.id), nullable=False)
    perfil = db.relationship("Perfil")

    #Expressar Publicacao em forma de texto:
    def __str__(self) -> str:
        return f"id: {self.id}. descricao: {self.descricao}. foto: {self.foto}. perfil: {self.perfil}."

    #Saída em Json:
    def json(self):
        return{
            "id": self.id,
            "descrição": self.descricao,
            "foto": self.foto,
            "perfil_id" : self.perfil_id,
            "perfil" : self.perfil.json() 
        }
