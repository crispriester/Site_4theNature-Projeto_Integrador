from flask import Flask, request
from servicos import pessoa_servico

app = Flask("4thenature")

# CONTROLADOR DE PESSOA

@app.route("/pessoa/obter/nome=<pessoaNome>", methods=["GET"])
def obterPessoasPeloNome(pessoaNome: str):

    pessoas = pessoa_servico.obterPessoasPeloNome(pessoaNome)
    return gerarResposta(200, "Pessoas Obtidas", "Pessoas", pessoas)

@app.route("/pessoa/login", methods=["GET"])
def concederAcessoParaPessoa():
    
    body = request.get_json()

    if("senha" not in body):
        return gerarResposta(400, "O parâmetro 'senha' é obrigatório.")

    if("email" not in body):
        return gerarResposta(400, "O parâmetro 'email' é obrigatório.")            

    person = pessoa_servico.concederAcessoParaPessoa(body["senha"], body["email"])

    if person == True:
        return gerarResposta(200, "Login Feito", "login", body)
    else:
        return gerarResposta(400, "Email ou senha inválidos", "login", body)


@app.route("/pessoa/cadastrar", methods=["POST"])
def cadastrarPessoa():

    body = request.get_json()

    if("nome" not in body):
        return gerarResposta(400, "O parâmetro 'nome' é obrigatório.")
    
    if("senha" not in body):
        return gerarResposta(400, "O parâmetro 'senha' é obrigatório.")

    if("email" not in body):
        return gerarResposta(400, "O parâmetro 'email' é obrigatório.")            

    person = pessoa_servico.cadastrarPessoa(body["nome"], body["senha"], body["email"])

    if person == True:
        return gerarResposta(200, "Pessoa cadastrada", "pessoa", body)
    else:
        return gerarResposta(400, "Este email já é cadastrado", "pessoa", body)


@app.route("/pessoa/editar/id=<pessoaId>", methods=["PUT"])
def editarPessoa(pessoaId: str):

    body = request.get_json()
    
    if("nome" not in body):
        return gerarResposta(400, "O parâmetro 'nome' é obrigatório.")
    
    if("senha" not in body):
        return gerarResposta(400, "O parâmetro 'senha' é obrigatório.")

    pessoa_servico.editarPessoa(body["nome"], body["senha"], pessoaId)

    return gerarResposta(200, "Pessoa editada", "pessoa", body)



# FUNÇÃO PARA EFETUAR RESPOSTAS

def gerarResposta(status, mensagem, nome_do_conteudo=False, conteudo=False):

    resposta = {}
    resposta["status"] = status
    

    if(nome_do_conteudo and conteudo):
        resposta[nome_do_conteudo] = conteudo
    
    resposta["mensagem"] = mensagem
    
    return resposta

app.run()