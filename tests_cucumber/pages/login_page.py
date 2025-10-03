from playwright.sync_api import Page
from objects.login_object import LoginObject
from models.user_model import User

class LoginPage:
    def __init__(self, page: Page):
        self.page = page

    def ir_pagina_login(self):
        self.page.goto(LoginObject.URL)

    def loguearse_y_acceder(self, tipoUsuario: User):
        self.page.fill(LoginObject.USERNAME_FIELD, tipoUsuario.username)
        self.page.fill(LoginObject.PASSWORD_FIELD, tipoUsuario.password)
        self.page.wait_for_timeout(2000)
        self.page.click(LoginObject.LOGIN_BUTTON)

    def accedi_pagina_inventario(self):
        return self.page.url == LoginObject.URL_INVENTORY