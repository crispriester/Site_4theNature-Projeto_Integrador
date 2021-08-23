from flask import Flask, request
from servicos import perfil_servico

app = Flask("4thenature")

# CONTROLADOR DE PESSOA

@app.route("/perfil/obter/nome=<perfilNome>", methods=["GET"])
def obterPerfisPeloNome(perfilNome: str):

    perfis = perfil_servico.obterPerfisPeloNome(perfilNome)
    return gerarResposta(200, "Perfil Obtidas", "perfil", perfis)

@app.route("/perfil/login", methods=["GET"])
def concederAcessoAoPerfil():
    
    body = request.get_json()

    if("senha" not in body):
        return gerarResposta(400, "O parâmetro 'senha' é obrigatório.")

    if("email" not in body):
        return gerarResposta(400, "O parâmetro 'email' é obrigatório.")            

    perfil = perfil_servico.concederAcessoAoPerfil(body["senha"], body["email"])

    if perfil == True:
        return gerarResposta(200, "Login Feito", "login", body)
    else:
        return gerarResposta(400, "Email ou senha inválidos", "login", body)


@app.route("/perfil/cadastrar", methods=["POST"])
def cadastrarPerfil():

    body = request.get_json()

    if("nome" not in body):
        return gerarResposta(400, "O parâmetro 'nome' é obrigatório.")
    
    if("senha" not in body):
        return gerarResposta(400, "O parâmetro 'senha' é obrigatório.")

    if("email" not in body):
        return gerarResposta(400, "O parâmetro 'email' é obrigatório.")            

    perfil = perfil_servico.cadastrarPerfil(body["nome"], body["senha"], body["email"])

    if perfil == True:
        return gerarResposta(200, "Perfil cadastrado", "perfil", body)
    else:
        return gerarResposta(400, "Este email já é cadastrado", "perfil", body)


@app.route("/perfil/editar/id=<perfilId>", methods=["PUT"])
def editarPerfil(perfilId: str):

    body = request.get_json()
    
    if("nome" not in body):
        return gerarResposta(400, "O parâmetro 'nome' é obrigatório.")
    
    if("senha" not in body):
        return gerarResposta(400, "O parâmetro 'senha' é obrigatório.")

    perfil_servico.editarPerfil(body["nome"], body["senha"], perfilId)

    return gerarResposta(200, "Perfil editado", "perfil", body)



# FUNÇÃO PARA EFETUAR RESPOSTAS

def gerarResposta(status, mensagem, nome_do_conteudo=False, conteudo=False):

    resposta = {}
    resposta["status"] = status
    

    if(nome_do_conteudo and conteudo):
        resposta[nome_do_conteudo] = conteudo
    
    resposta["mensagem"] = mensagem
    
    return resposta

app.run()