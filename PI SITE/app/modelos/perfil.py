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

#Teste da classe:
if __name__ == "__main__":
    #Apagar arquivo se houver:
    if os.path.exists(arquivobd):
        os.remove(arquivobd)

    #Criar tabelas:
    db.create_all()

    #Teste da classe: (dados apenas criados na memória)
    perfil1 = Perfil(nome = "Cris", senha = "n_sei123", email = "cris@gmail.com")
    perfil2 = Perfil(nome = "Maria", senha = "travesseirofofinho", email = "maria@gmail.com")
    perfil3 = Perfil(nome = "Gab", senha = "gabizito2004", email = "gab@gmail.com")

    #Adicionar os dados na sessão de persistência:
    db.session.add(perfil1)
    db.session.add(perfil2)
    db.session.add(perfil3)

    db.session.commit()