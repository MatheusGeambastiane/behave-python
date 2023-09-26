from behave import given, when, then
from selenium.webdriver import Firefox
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from time import sleep


@given("que o usuario esteja na pagina do google")
def go_to_page(context):
    context.browser = Firefox()
    context.browser.get("https://google.com")

@when("ele clicar e pesquisar o {query}")
def search_for_instituitio(context, query):
    search_bar = context.browser.find_element(By.NAME, "q")
    search_bar.click()
    search_bar.send_keys(query)
    search_bar.send_keys(Keys.ENTER)

@then("O titulo da pagina sera sobre o resultado da pesquisa: instituto joga junto - Pesquisa Google")
def verify_title(context):
    expect_title = "instituto joga junto - Pesquisa Google"
    title = context.browser.title
    import ipdb;ipdb.sset_trace()
    print(title)
    sleep(8)

    title = context.browser.title




    assert expect_title in title