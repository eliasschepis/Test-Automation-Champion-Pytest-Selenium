# Importamos pytest, que es el framework que usamos para correr los tests
import pytest
import time

# Importamos la clase LoginPage, que está escrita con el patrón Page Object Model (POM)
# Esto nos permite reutilizar la lógica de interacción con la interfaz

from utils.helpers import login_and_go_to_home
from pages.login_page import LoginPage
from pages.home_page import HomePage
from pages.cart_page import CartPage
from utils.config import Config

# Importamos las variables de configuración, como usuario, clave, etc.
# Evitamos hardcodear valores para mantener el código limpio y reutilizable
from utils.config import Config

# (nombre legible, id del producto en DOM)
product_test_data = [
    ("Sauce Labs Backpack", "sauce-labs-backpack"),
    ("Sauce Labs Bike Light", "sauce-labs-bike-light"),
    ("Sauce Labs Bolt T-Shirt", "sauce-labs-bolt-t-shirt"),
]

@pytest.mark.parametrize("expected_name, product_id", product_test_data)
def test_agregar_producto(driver, expected_name, product_id):
    login = LoginPage(driver)
    login.load()
    login.login(Config.USERNAME, Config.PASSWORD)

    home = HomePage(driver)
    home.add_product_to_cart(product_id)
    time.sleep(1)
    home.goToCheckoutPage()

    cart = CartPage(driver)
    nombres = cart.get_cart_product_names()

    assert expected_name in nombres


# Agregar varios productos
def test_agregar_varios_productos(driver):
    login = LoginPage(driver)
    login.load()
    login.login(Config.USERNAME, Config.PASSWORD)

    home = HomePage(driver)

    # Lista de IDs de producto en el DOM
    productos = [
        "sauce-labs-backpack",
        "sauce-labs-bike-light",
        "sauce-labs-bolt-t-shirt"
    ]

    # Agregamos todos con un solo método
    home.add_multiple_products(productos)
    home.goToCheckoutPage()

    cart = CartPage(driver)
    nombres_en_carrito = cart.get_cart_product_names()

    # Validamos que todos estén en el carrito
    nombres_esperados = [
        "Sauce Labs Backpack",
        "Sauce Labs Bike Light",
        "Sauce Labs Bolt T-Shirt"
    ]

    for nombre in nombres_esperados:
        assert nombre in nombres_en_carrito



