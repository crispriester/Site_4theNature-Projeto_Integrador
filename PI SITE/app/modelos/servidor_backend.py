from config import * 
from perfil import Perfil 
from publicacao import Publicacao
 
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
@app.route("/login", methods=['POST'])
def pegar_id_pelo_email():
   dados = request.get_json() #(force=True) dipensa Content-Tpe na requisição
   usuario = Perfil.query.filter(Perfil.email == dados['email'], Perfil.senha == dados['senha']).first()
   return jsonify({"resultado": "ok", "detalhes": usuario.json()}) if hasattr(usuario, 'id') else jsonify({"resultado": "Erro", "detalhes": "Usuario ou senha invalidos!"})
   print(usuario.id)
#Fim do login

#inicio do cadastro de publicacao
@app.route("/listar_publicacao") 
def listar_publicacao(): 
   # obter as publicacao do cadastro 
   publicacao = db.session.query(Publicacao).all() 
   # aplicar o método json que a classe Publicacao possui a cada elemento da lista 
   publicacoes_em_json = [ x.json() for x in publicacao ] 
   # converter a lista do python para json 
   resposta = jsonify(publicacoes_em_json)
   #permitir resposta para outros pedidos oriundos de outras tecnologias
   resposta.headers.add("Access-Control-Allow-Origin", "*")
   return resposta #retornar...

@app.route("/incluir_publicacao", methods=['post'])
def incluir_publicacao():
   #preparar uma resposta otimista
   resposta = jsonify({"resultado": "ok","detalhes": "ok"})
   #receber as informações da nova postagem
   dados = request.get_json() #(force=True) dipensa Content-Tpe na requisição
   try: #tentar executar operação
      nova = Publicacao(**dados) #criar a nova pessoa
      db.session.add(nova) #adicionar no banco de dados
      db.session.commit() #Efetivar a operação de gravação
   except Exception as e: #em caso de erro...
      #Informar mensagem de erro
      resposta = jsonify({"resultado": "erro", "detalhes": str(e)})
   #Adicionar cabeçalho de liberação de origem
   resposta.headers.add("Access-Control-Allow-Origin", "*")
   return resposta #responder!
#fim do cadastro de publicacao

"""
@app.route('/uploadajax', methods = ['POST'])
def upldfile():
    r = jsonify({"mensagem":"tentando..."})
    if request.method == 'POST':
        file_val = request.files['file']
        print("vou salvar em: "+file_val.filename)
        arquivoimg = os.path.join(path, 'img_pet/'+file_val.filename)
        file_val.save(arquivoimg)
        r = jsonify({"mensagem":"ok"})
    r.headers.add("Access-Control-Allow-Origin", "*")
    return r

@app.route('/get_image/<int:pet_id>')
def get_image(pet_id):
    pet = db.session.query(Pet).get(pet_id)
    # if request.args.get('type') == '1':
    #    filename = 'ok.gif'
    # else:
    #    filename = 'error.gif'
    arquivoimg = os.path.join(path, 'img_pet/'+ pet.foto)
    # arquivoimg = os.path.join('/home/ingguk/mysite/img_pet', pet.foto)
    # /home/ingguk/mysite/img_pet
    return send_file(arquivoimg, mimetype='image/gif')

repositorio ingrid:
https://github.com/hadDOTpy/PI2021/tree/main/dotis

js:
        var form_data = new FormData($('#MyForm')[0]);

        $.ajax({
            url: 'http://localhost:5000/uploadajax',
            type: 'POST',
            data: form_data,
            contentType: false,
            cache: false,
            processData: false,
            success: function(data) {
                console.log('Success!');
                alert("enviou a foto direitinho!");
            },
            error: function(data) {
                alert("deu ruim na foto");
            }
        });
"""

app.run(debug=True) 