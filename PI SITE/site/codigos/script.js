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
// função que mostra um conteúdo e esconde os outros
function mostrar_conteudo(identificador) {
    // esconde todos os conteúdos
    $("#register").addClass('d-none');
    $("#login").addClass('d-none');
    // torna o conteúdo escolhido visível
    $("#" + identificador).removeClass('d-none');
}

// código para mapear click do link Inicio
$(document).on("click", "#link-register", function() {
    mostrar_conteudo("register");
});
// código para mapear click do link Inicio
$(document).on("click", "#link-login", function() {
    mostrar_conteudo("login");
});