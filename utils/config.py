# Este archivo contiene datos reutilizables para evitar hardcodeo
# Podés definir aquí credenciales, URLs, IDs de productos, etc.

class Config:
    BASE_URL = "https://www.saucedemo.com/"
    HOME_URL = BASE_URL + "inventory"
    CART_URL = BASE_URL + "cart"
    CHECKOUT_URL = BASE_URL + "checkout-step-one"
    CHECKOUT2_URL = BASE_URL + "checkout-step-two"
    CHECKOUT_COMPLETE = BASE_URL + "checkout-complete"
    USERNAME = "standard_user"
    PASSWORD = "secret_sauce"
    WRONG_USER = "usuario_invalido"
    WRONG_PASSWORD = "clave_invalida"
    USER_FIRSTNAME = "Elias"
    USER_LASTNAME = "Schepis"
    USER_ZIPCODE = "12345"
    PRODUCTS_TUPLE = (
        "Sauce Labs Backpack",
        "Sauce Labs Bike Light",
        "Sauce Labs Bolt T-Shirt",
        "Sauce Labs Fleece Jacket",
        "Sauce Labs Onesie",
        "Test.allTheThings() T-Shirt (Red)"
    )




