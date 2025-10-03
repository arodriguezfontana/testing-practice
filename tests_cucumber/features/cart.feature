Feature: Agregar productos al carrito y validarlos

    Scenario Outline: Usuario agrega productos al carrito y los valida
        Given el usuario inicia sesion como usuario estandar
        When navega a la pagina de inventario
        And agrega los productos "<Producto 1>" y "<Producto 2>" al carrito
        And hace click en el boton del carrito
        Then visualiza la pagina del carrito
        And los productos "<Producto 1>" y "<Producto 2>" estan en el carrito

    Examples:
        | Producto 1              | Producto 2            |
        | Sauce Labs Backpack     | Sauce Labs Bike Light |
        | Sauce Labs Bolt T-Shirt | Sauce Labs Onesie     | 