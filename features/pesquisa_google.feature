#language: pt

Funcionalidade: Pesquisa no google

    @pesquisa_google
    Cenário: Pesquisar o Instituto Joga Junto

    Dado que o usuario esteja na pagina do google
    Quando ele clicar e pesquisar o "instituto joga junto"
    Então O titulo da pagina sera sobre o resultado da pesquisa: "instituto joga junto - Pesquisa Google"

