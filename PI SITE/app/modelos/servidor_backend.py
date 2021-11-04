from config import * 
from perfil import Perfil 
 
@app.route("/") 
def inicio(): 
   return 'Sistema de cadastro de usuarios. '+\
         '<a href="/listar_usuarios">Operação listar</a>'

#inicio do cadastro de usuario
@app.route("/listar_usuarios") 
def listar_usuarios(): 
   # obter os ususários do cadastro 
   usuarios = db.session.query(Perfil).all() 
   # aplicar o método json que a classe Perfil possui a cada elemento da lista 
   usuarios_em_json = [ x.json() for x in usuarios ] 
   # converter a lista do python para json 
   resposta = jsonify(usuarios_em_json)
   #permitir resposta para outros pedidos oriundos de outras tecnologias
   resposta.headers.add("Access-Control-Allow-Origin", "*")
   return resposta #retornar...

@app.route("/incluir_usuario", methods=['post'])
def incluir_usuario():
   #preparar uma resposta otimista
   resposta = jsonify({"resultado": "ok","detalhes": "ok"})
   #receber as informações da nova pessoa
   dados = request.get_json() #(force=True) dipensa Content-Tpe na requisição
   try: #tentar executar operação
      nova = Perfil(**dados) #criar a nova pessoa
      db.session.add(nova) #adicionar no banco de dados
      db.session.commit() #Efetivar a operação de gravação
   except Exception as e: #em caso de erro...
      #Informar mensagem de erro
      resposta = jsonify({"resultado": "erro", "detalhes": str(e)})
   #Adicionar cabeçalho de liberação de origem
   resposta.headers.add("Access-Control-Allow-Origin", "*")
   return resposta #responder!

# teste: curl -X DELETE http://localhost:5000/excluir_usuario/1 
@app.route("/excluir_usuario/<int:usuario_id>", methods=['DELETE']) 
def excluir_usuario(usuario_id): 
   # preparar uma resposta otimista 
   resposta = jsonify({"resultado": "ok", "detalhes": "ok"}) 
   try: 
      # excluir o usuario do ID informado 
      Perfil.query.filter(Perfil.id == usuario_id).delete() 
      # confirmar a exclusão 
      db.session.commit() 
   except Exception as e: 
      # informar mensagem de erro 
      resposta = jsonify({"resultado":"erro", "detalhes":str(e)}) 
   # adicionar cabeçalho de liberação de origem 
   resposta.headers.add("Access-Control-Allow-Origin", "*") 
   return resposta # responder!
#fim do cadastro de usuario

#inicio do login
@app.route("/login")
def pegar_id_pelo_email():
   dados = request.get_json() #(force=True) dipensa Content-Tpe na requisição
   usuario = Perfil.query.filter(Perfil.email == dados['email']).first()
   return jsonify(usuario.id) if hasattr(usuario, 'id') else "Não encontrado"
   print(usuario.id)
   
#Fim do login

app.run(debug=True) 
