# Importamos pytest, que es el framework que usamos para correr los tests
import pytest
import time

# Importamos la clase LoginPage, que está escrita con el patrón Page Object Model (POM)
# Esto nos permite reutilizar la lógica de interacción con la interfaz

from utils.flows import login_and_go_to_home
from pages.login_page import LoginPage
from pages.home_page import HomePage
from pages.cart_page import CartPage

# Importamos las variables de configuración, como usuario, clave, etc.
# Evitamos hardcodear valores para mantener el código limpio y reutilizable
from utils.config import Config


# Logout

def test_logout(driver):
    page = LoginPage(driver) # Iniciamos el módulo de login page
    time.sleep(1)

    page.load() # Cargamos la pagina
    time.sleep(1)

    page.login(Config.USERNAME, Config.PASSWORD) # Ejecutamos login
    time.sleep(1)

    page = HomePage(driver)
    time.sleep(1)

    page.logout()
    time.sleep(1)

    assert Config.BASE_URL in driver.current_url
