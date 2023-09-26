## BEHAVE E SELENIUM PARA TESTES AUTOMATIZADOS

## O que é o Behave?


O behave é uma ferramenta de teste orientado a comportamento (BDD, Behavior-Driven Development) para Python. Ele permite que desenvolvedores e não-desenvolvedores colaborem na criação de testes através de cenários descritos em uma linguagem natural (Gherkin). Estes cenários são traduzidos em código executável para testar uma aplicação. Com o behave, equipes podem garantir que o software se comporte conforme o esperado pelos stakeholders.

## 1º Passo: Criar um ambiente virtual e ativar

```bash
python -m venv nomedoambiente

nomedoambiente\Scripts\activate ## Windows
nomedoambiente/bin/activate ##Mac ou Linux
```
## 2º Passo instalar o selenium e o behave
Partindo do pressuposto que você já tenha baixado o driver e o navegador atualizado

```bash
pip install selenium behave
```
Note que podemos executar mais de um pacote por vez, separando ele por espaço 


## 3º O Behave solicita que seja criada uma estrutura de pastas que deverão seguir este padrão:
```bash
projeto/
│
├── features/
│   ├── my_feature.feature
|   ├── my_feature2.feature
│   ├── steps/
│   │   ├──my_feature1_steps.py
│   │   └── my_feature2_steps.py
│   └── environment.py
│
└── ...
```

# Entendendo pastas e arquivos:

    - features/: Este diretório contém todos os seus cenários e steps.
    - .feature: Estes arquivos descrevem seus cenários de teste em uma linguagem de domínio específico chamada Gherkin.
    - steps/: Este diretório contém os arquivos Python que implementam a lógica dos steps definidos nos arquivos .feature.
    - environment.py: Este é um arquivo especial que pode conter funções de configuração e desmontagem que são executadas antes e depois de seus cenários ou features.

# Arquivo .feature
Dentro do arquivo .feature você deverá escrever seu caso de teste com o Gherkin, conforme exemplo abaixo:

```gherkin
#language: pt
Funcionalidade: Testar a funcionalidade X

  Cenário: Testar um detalhe específico de X
     Dado que estou na página inicial
     Quando eu clico no botão "Começar"
     Então eu devo ver a página "Bem-vindo"
```
## Arquivo Steps
Para cada step em seus arquivos .feature, você deve implementar a lógica correspondente em um arquivo dentro do diretório steps/.

Por exemplo, para o step Dado que estou na página inicial, você pode ter algo assim:

```python
from behave import given,when,then

@given('que estou na página inicial')
def step_impl(context):
    context.browser.get("https://jogajuntoinstituto.org")
```


## Environment e contexto:

O arquivo environment.py pode conter funções como before_feature, after_feature, before_scenario, e after_scenario. Elas são usadas para configurar ou limpar recursos antes ou depois de seus cenários ou features serem executados.

Por exemplo, para inicializar o navegador antes de cada cenário e fechá-lo depois:

```python
from selenium.webdriver import Firefox

def before_scenario(context, scenario):
    context.browser = Firefox()

def after_scenario(context, scenario):
    context.browser.quit()


```


# Como executar:

Para executar o behave, ponha em seu terminal o codigo abaixo e execute

```bash
behave
```

