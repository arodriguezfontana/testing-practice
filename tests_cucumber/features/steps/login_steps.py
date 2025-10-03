from behave import given, when, then
from pages.login_page import LoginPage
from models.user_model import UserModel

@given("el usuario esta en la pagina de login")
def step_open_login_page(context):
    context.login_page = LoginPage(context.page)
    context.login_page.ir_pagina_login()

@when("ingresa las credenciales correctas")
def step_enter_credentials(context):
    context.login_page.loguearse_y_acceder(UserModel.STANDARD_USER)

@then("visualiza la pagina de inventario")
def step_verify_inventory_page(context):
    assert context.login_page.accedi_pagina_inventario(), "El usuario no pudo iniciar sesion"