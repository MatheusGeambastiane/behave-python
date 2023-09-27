#language: pt

Funcionalidade: Contato instituto

    Como visitante da pagina
    Quero entrar em Contato
    Para me tornar facilitador
    @contato_ijj
    Cenário: Contato no site do instituto

    Dado que o usuario esteja na pagina do instituto
    Quando preencher os dados no formulario
    E selecionar a opção Ser facilitador
    E clicar em enviar
    Então O formulario sera enviado e um alert aparecerá na tela confirmando