from playwright.sync_api import Page
from objects.cart_object import CartObject

class CartPage:
    def __init__(self, page : Page):
        self.page = page

    def en_pagina_carrito(self):
        return self.page.url == CartObject.URL
    
    def obtener_productos_carrito(self):
        return self.page.locator(CartObject.SELECTOR_LISTA_CARRITO).all_text_contents()