from behave import given, when, then
from playwright.sync_api import sync_playwright

@given("el usuario esta en la pagina de login")
def step_open_login_page(context):
    context.playwright = sync_playwright().start()
    context.browser = context.playwright.chromium.launch(headless=False)
    context.page = context.browser.new_page()
    context.page.goto("https://www.saucedemo.com/")

@when("ingresa las credenciales correctas")
def step_enter_credentials(context):
    context.page.fill("#user-name", "standard_user")
    context.page.fill("#password", "secret_sauce")
    context.page.click("#login-button")

@then("visualiza la pagina de inventario")
def step_verify_inventory_page(context):
    assert "inventory.html" in context.page.url
    context.page.wait_for_timeout(2000)
    context.browser.close()
    context.playwright.stop()