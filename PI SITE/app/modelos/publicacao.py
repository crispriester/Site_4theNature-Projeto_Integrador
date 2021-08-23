from perfil import *
from config import *

#relação de composição com a classe Perfil:
class Publicacao:
    #Atributos da publicação:
    id = db.Column(db.Integer, primary_key= True)
    descricao = db.Column(db.String(254))
    foto = db.Column(db.String(254))
    #Chave estrangeira:
    perfil_id = db.Column(db.Integer, db.ForeignKey(Perfil.id), nullable=False)
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


#Teste da classe Nova:
if __name__ == "__main__":
    #Apagar arquivo se houver:
    if os.path.exists(arquivobd):
        os.remove(arquivobd)

    #Criar tabelas:
    db.create_all()

    #Teste da classe: (dados apenas criados na memória)
    publicacao1 = Publicacao(descricao = "reflorestamento", foto = "01000010101", perfil = perfil1)
    publicacao2 = Publicacao(descricao = "telas solares", foto = "01010001010", perfil = perfil2)
    publicacao3 = Publicacao(descricao = "Composteira", foto = "10101010100", perfil = perfil3)

    #Adicionar os dados na sessão de persistência:
    db.session.add(publicacao1)
    db.session.add(publicacao2)
    db.session.add(publicacao3)

    db.session.commit()