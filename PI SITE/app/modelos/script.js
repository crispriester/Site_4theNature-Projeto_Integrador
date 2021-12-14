// Códigos usados nas abas da página home:

// função que mostra um conteúdo e esconde os outros
function showContent(identificator) {
    // esconde todos os conteúdos
    $("#register").addClass('d-none');
    $("#login").addClass('d-none');
    // torna o conteúdo escolhido visível
    $("#" + identificator).removeClass('d-none');
}

// função para quando a página carregar, o juntar-se ser o primeiro a aparecer.
window.addEventListener('load', () => {
    document.getElementById("link-register").click();
    $("#link-register").addClass("active");
})

//função que ativa e desativa um elemento
function activeClass(active, unactive) {
    $(active).addClass("active");
    $(unactive).removeClass("active");
}

// código para mapear click do link Inicio
$(document).on("click", "#link-register", function () {
    showContent("register");
    activeClass("#link-register", "#link-login")

});

// código para mapear click do link Inicio
$(document).on("click", "#link-login", function () {
    showContent("login");
    activeClass("#link-login", "#link-register")

});


//Script do gráfico da terceira dica -> Materiais Biodegradáveis:
window.onload = function () {

    var chart = new CanvasJS.Chart("chartContainer", {
        animationEnabled: true,
        title: {
            text: "Sacolinhas Convencionais  vs  Sacolinhas Biodegradáveis"
        },
        axisX: {
            interval: 1
        },
        axisY: {
            title: "Tempo de Decomposição em Anos",
            includeZero: true,
        },
        data: [{

            type: "bar",
            toolTipContent: "<img src=\"../imagens/\"{url}\"\" style=\"width:40px; height:20px;\"> <b>{label}</b><br>Tempo: {y} anos<br>",
            dataPoints: [{
                label: "Biodegradáveis",
                y: 20,
                url: "sacola-biodegradavel-grafico.jpg",
                color: "rgb(81, 189, 72)"
            }, {
                label: "Convencionais",
                y: 100,
                url: "Sacolinha-plástica-grafico.jpg",
                color: "rgb(209, 107, 40)"
            },

            ]
        }]
    });
    chart.render();
}

//querySelector vai ser ligado ao contexto e ao escopo do document
/*const $ = document.querySelector.bind(document)

function TabNavigation() {
    const html = {
        links: [...$('.tab-links').children],
        links: [...$('.tab-content').children],
        openTab: $('[data-open]')
    }

    function hideAllTabContent() {
        // coloca-se o contents como uma array para que o forEach funcione
        const contents = [...html.contents.children] //children é uma html colection
        contents.forEach(section => {
            section.style.display = "none"
        })
    }
    // vai remover todas as classes ativas quando eu clicar em alguma  
    function removeAllActiveClass() {
        html.links.forEach(tab => {
            tab.className = tab.className.replace(" active", "")
        })
    }

    function showCurrentTab(id) {
        const tabContent = $('#' + id)
        tabContent.style.display = "block"
    }

    function selectTab(event) {
        hideAllTabContent()
        removeAllActiveClass()

        const target = event.currentTarget
        showCurrentTab(target.dataset.id)

        target.className += " active"

    }

    function listenForChange() {
        html.links.forEach(tab => {
            tab.addEventListener('click', selectTab)
        })
    }

    function init() {
        hideAllTabContent()
        listenForChange()

        html.openTab.click()
    }

    return {
        init
    }
}

window.addEventListener('load', () => {
    const TabNavigation = TabNavigation()
    TabNavigation.init()
})


*/

// código para mapear click do botão incluir pessoa 
$(document).on("click", "#btIncluirUsuario", function () {
    //pegar dados da tela 
    nome = $("#campoNome").val();
    email = $("#campoEmail").val();
    senha = $("#campoSenha").val();
    // preparar dados no formato json 
    var dados = JSON.stringify({ nome: nome, email: email, senha: senha });
    // fazer requisição para o back-end 
    $.ajax({
        url: 'http://localhost:5000/incluir_usuario',
        type: 'POST',
        dataType: 'json', // os dados são recebidos no formato json 
        contentType: 'application/json', // tipo dos dados enviados 
        data: dados, // estes são os dados enviados 
        success: usuarioIncluido, // chama a função listar para processar o resultado 
        error: erroAoIncluir
    });

    function usuarioIncluido(retorno) {
        if (retorno.resultado == "ok") { // a operação deu certo? 
            // informar resultado de sucesso 
            alert("Usuário incluído com sucesso!");
            // limpar os campos 
            $("#campoNome").val("");
            $("#campoEmail").val("");
            $("#campoSenha").val("");
        } else {
            // informar mensagem de erro 
            alert(retorno.resultado + ":" + retorno.detalhes);
        }
    }

    function erroAoIncluir(retorno) {
        // informar mensagem de erro 
        alert("ERRO: " + retorno.resultado + ":" + retorno.detalhes);
    }
});

// código para os ícones de excluir usuario (classe css) 
$(document).on("click", ".excluir_usuario", function () {
    // obter o ID do ícone que foi clicado 
    var componente_clicado = $(this).attr('id');
    // no id do ícone, obter o ID da usuario 
    var nome_icone = "excluir_";
    var id_usuario = componente_clicado.substring(nome_icone.length);
    // solicitar a exclusão da usuario 
    $.ajax({
        url: 'http://localhost:5000/excluir_usuario/' + id_usuario,
        type: 'DELETE', // método da requisição 
        dataType: 'json', // os dados são recebidos no formato json 
        success: usuarioExcluido, // chama a função listar para processar o resultado 
        error: erroAoExcluir
    });

    function usuarioExcluido(retorno) {
        if (retorno.resultado == "ok") { // a operação deu certo? 
            // remover da tela a linha cujo usuario foi excluído
            $("#linha_" + id_usuario).fadeOut(1000, function () {
                // informar resultado de sucesso 
                alert("Usuário removido com sucesso!");
            });
        } else {
            // informar mensagem de erro 
            alert(retorno.resultado + ":" + retorno.detalhes);
        }
    }

    function erroAoExcluir(retorno) {
        // informar mensagem de erro 
        alert("erro ao excluir dados, verifique o backend: ");
    }
});

// código para mapear click do botão Login 
$(document).on("click", "#btLogin", function () {
    //pegar dados da tela 
    email = $("#campoEmailLogin").val();
    senha = $("#campoSenhaLogin").val();
    // preparar dados no formato json 
    var dados = JSON.stringify({ email: email, senha: senha });
    // fazer requisição para o back-end 
    $.ajax({
        url: 'http://localhost:5000/login',
        type: 'POST',
        dataType: 'json', // os dados são recebidos no formato json 
        contentType: 'application/json', // tipo dos dados enviados 
        data: dados, // estes são os dados enviados 
        success: usuarioConectado, // chama a função listar para processar o resultado 
        error: erroAoConectar
    });
    alert("belezinha!!!");

    function usuarioConectado(resposta) {
        $.session.set('usuarioId', resposta.detalhes.id);
        $.session.set('usuarioNome', resposta.detalhes.nome);
        alert(resposta.detalhes.nome);
        window.location.href = "forum_inicio.html";
    }

    function erroAoConectar() {
        alert("não funcionou");
    }
});


// Script para clicar no ícone da foto e abrir o explorador de arquivos 
$("#imagem").click(function () {
    $("#arquivo").trigger('click');
});

// código para mapear click do botão postar 
$(document).on("click", "#btPostar", function () {

    var form_data = new FormData($('#MyForm')[0]);

    // faz o upload da foto
    $.ajax({
        url: 'http://localhost:5000/uploadajax',
        type: 'POST',
        data: form_data,
        contentType: false,
        cache: false,
        processData: false,
        success: function (data) {
            console.log('Success!');
            //alert("enviou a foto direitinho!");


            //pegar dados da tela 
            descricao = $("#campoDescricao").val();
            //c:\\fakepath\\nome da foto
            foto = $("#arquivo").val().substr(12);
            perfil_id = $.session.get('usuarioId');
            // preparar dados no formato json 
            var dados = JSON.stringify({ descricao: descricao, foto: foto, perfil_id: perfil_id });
            // fazer requisição para o back-end (grava a postagem)
            $.ajax({
                url: 'http://localhost:5000/incluir_publicacao',
                type: 'POST',
                dataType: 'json', // os dados são recebidos no formato json 
                contentType: 'application/json', // tipo dos dados enviados 
                data: dados, // estes são os dados enviados 
                success: publicacaoIncluida, // chama a função listar para processar o resultado 
                error: erroAoIncluir
            });

            function publicacaoIncluida(retorno) {
                if (retorno.resultado == "ok") { // a operação deu certo? 
                    // informar resultado de sucesso 
                    alert("Publicação incluída com sucesso!");
                    // limpar os campos 
                    $("#campoDescricao").val("");
                    //$("#campoFoto").val("");
                } else {
                    // informar mensagem de erro 
                    alert(retorno.resultado + ":" + retorno.detalhes);
                }
            }

            function erroAoIncluir(retorno) {
                // informar mensagem de erro 
                alert("ERRO: " + retorno.resultado + ":" + retorno.detalhes);
            }



        },
        error: function (data) {
            alert("deu ruim na foto");
        }
    });


});

