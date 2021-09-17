from config import *

class Perfil(db.Model):
        #Atributos do Perfil:
        id = db.Column(db.Integer, primary_key= True)
        nome = db.Column(db.String(254))
        senha = db.Column(db.String(254))
        email = db.Column(db.String(254))

        #Expressar Perfil em forma de texto:
        def __str__(self) -> str:
            return f"id: {self.id}. nome: {self.nome}. senha: {self.senha}. email: {self.email}."

        #Saída em Json:
        def json(self):
            return{
                "id": self.id,
                "nome": self.nome,
                "senha": self.senha,
                "email": self.email
            }
