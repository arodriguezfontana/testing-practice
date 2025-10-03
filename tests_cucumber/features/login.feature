Feature: Login en SauceDemo
    
    Scenario: Usuario estandar inicia sesion exitosamente
        Given el usuario esta en la pagina de login
        When ingresa las credenciales correctas
        Then visualiza la pagina de inventario