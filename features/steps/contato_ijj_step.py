from behave import given, when, then
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select, WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


from time import sleep


@given("que o usuario esteja na pagina do instituto")
def go_to_page(context):
    context.browser.get("https://www.jogajuntoinstituto.org/")

@when("preencher os dados no formulario")
def form_text(context):
    context.browser.find_element(By.NAME, "nome").send_keys("Matheus")
    context.browser.find_element(By.NAME, "email").send_keys("mgeambastiane@gmail.com")
    context.browser.find_element(By.NAME, "body").send_keys("Teste - selenium ")

    


@when("selecionar a opção Ser facilitador")
def form_text(context):
    select_opt = context.browser.find_element(By.NAME, "assunto")

    select = Select(select_opt)

    select.select_by_visible_text("Ser facilitador")
    

@when("clicar em enviar")
def form_text(context):
    btn = context.browser.find_element(By.XPATH, "/html/body/div[1]/div[2]/section[8]/div[1]/form/button")
    btn.submit()


@then("O formulario sera enviado e um alert aparecerá na tela confirmando")
def verify_alert(context):
    try:
        navegador = context.browser

        alert = WebDriverWait(navegador, 10).until(EC.alert_is_present())
    
        alert_text = alert.text
        verify_text = "Dados recebidos!"

        assert verify_text in alert_text

        alert.accept()

    finally:
        sleep(10)

   