from behave import given, when, then
from pages.login_page import LoginPage
from models.user_model import UserModel
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage

@given("el usuario inicia sesion como usuario estandar")
def step_impl(context):
    context.login_page = LoginPage(context.page)
    context.login_page.ir_pagina_login()
    context.login_page.loguearse_y_acceder(UserModel.STANDARD_USER)

@when("navega a la pagina de inventario")
def step_impl(context):
    context.inventory_page = InventoryPage(context.page)
    assert context.inventory_page.en_pagina_inventario(), "No esta en la pagina de inventario"

@when('agrega los productos "{producto1}" y "{producto2}" al carrito')
def step_impl(context, producto1, producto2):
    context.inventory_page.agregar_producto_carrito(producto1)
    context.inventory_page.agregar_producto_carrito(producto2)

@when("hace click en el boton del carrito")
def step_impl(context):
    context.inventory_page.ir_pagina_carrito()

@then("visualiza la pagina del carrito")
def step_impl(context):
    context.cart_page = CartPage(context.page)
    assert context.cart_page.en_pagina_carrito(), "No esta en a pagina del carrito"

@then('los productos "{producto1}" y "{producto2}" estan en el carrito')
def step_impl(context, producto1, producto2):
    productos_carrito = context.cart_page.obtener_productos_carrito()
    assert producto1 in productos_carrito, f"{producto1} no esta en el carrito"
    assert producto2 in productos_carrito, f"{producto2} no esta en el carrito"