class InventoryObject:
    URL = "https://www.saucedemo.com/inventory.html"
    SELECTOR_BOTON_CARRITO = "#shopping_cart_container"
    def obtener_localizador_segun_nombre(nombre_producto : str):
        return f"text={nombre_producto} >> xpath=../../..//button[contains(text(), 'Add to cart')]"