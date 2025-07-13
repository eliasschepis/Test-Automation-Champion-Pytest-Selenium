# Importamos pytest, que es el framework que usamos para correr los tests

import pytest
import time

# Importamos la clase LoginPage, que está escrita con el patrón Page Object Model (POM)
# Esto nos permite reutilizar la lógica de interacción con la interfaz

from pages.home_page import HomePage
from pages.cart_page import CartPage
from pages.checkout_page1 import CheckoutPage1
from pages.checkout_page2 import CheckoutPage2
from pages.checkout_complete import CheckoutComplete
from utils.flows import login_and_go_to_home
from utils.config import Config

# Importamos las variables de configuración, como usuario, clave, etc.
# Evitamos hardcodear valores para mantener el código limpio y reutilizable

# Workflow completo

@pytest.mark.e2e
def test_complete_workflow(driver):
    login_and_go_to_home(driver)
    home = HomePage(driver)

    # Lista de IDs de producto en el DOM
    productos = [
        "sauce-labs-backpack",
        "sauce-labs-bike-light",
        "sauce-labs-bolt-t-shirt"
    ]

    # Agregamos todos con un solo metodo
    home.add_multiple_products(productos)
    home.goToCheckoutPage()

# CART PAGE

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

    assert "cart" in driver.current_url
    time.sleep(2)

# CHECKOUT 1 PAGE

    cart.goTo_checkout_info()
    assert "checkout-step-one" in driver.current_url

    checkout_info = CheckoutPage1(driver)
    checkout_info.fill_checkout_info()

    info_esperada = checkout_info.get_info()

    userinfo_list = [
        "Elias",
        "Schepis",
        "12345"
    ]

    for check_info in userinfo_list:
        assert check_info in info_esperada

    checkout_info.click_continue_button()

# CHECKOUT 2 PAGE

    checkout_page2 = CheckoutPage2(driver)
    checkout_summary = checkout_page2.get_lastInfo()  # Esto debe retornar una lista de strings con productos visibles

    # Validamos si al menos uno de los productos válidos está presente
    assert any(product in checkout_summary for product in Config.PRODUCTS_TUPLE)

    checkout_page2.finishButton()

# COMPLETE PAGE

    complete_page = CheckoutComplete(driver)
    complete_page.get_completeHeader()
    complete_page.homeButton()







