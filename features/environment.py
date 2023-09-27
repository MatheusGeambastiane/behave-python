from selenium.webdriver import Firefox

def before_scenario(context, scenario):
    context.browser = Firefox()

def after_scneario(context,scenario):
    context.browser.quit()


