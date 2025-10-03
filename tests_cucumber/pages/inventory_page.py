from playwright.sync_api import Page
from objects.inventory_object import InventoryObject

class InventoryPage:
    def __init__(self, page : Page):
        self.page = page

    def en_pagina_inventario(self):
        return self.page.url == InventoryObject.URL
    
    def agregar_producto_carrito(self, nombre_producto):
        selector_producto = InventoryObject.obtener_localizador_segun_nombre(nombre_producto)
        self.page.locator(selector_producto).click()
        self.page.wait_for_timeout(2000)

    def ir_pagina_carrito(self):
        self.page.locator(InventoryObject.SELECTOR_BOTON_CARRITO).click()