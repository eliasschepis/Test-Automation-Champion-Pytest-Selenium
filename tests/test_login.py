# Importamos pytest, que es el framework que usamos para correr los tests
import pytest

# Importamos la clase LoginPage, que está escrita con el patrón Page Object Model (POM)
# Esto nos permite reutilizar la lógica de interacción con la interfaz

from pages.login_page import LoginPage


# Importamos las variables de configuración, como usuario, clave, etc.
# Evitamos hardcodear valores para mantener el código limpio y reutilizable
from utils.config import Config


# ✅ Test: Login exitoso con usuario y contraseña válidos
def test_login_exitoso(driver):
    # Creamos una instancia de LoginPage y le pasamos el driver de Selenium
    page = LoginPage(driver)

    # Cargamos la página de login usando el metodo definido en LoginPage
    page.load()

    # Ejecutamos el login usando credenciales válidas
    page.login(Config.USERNAME, Config.PASSWORD)

    # Verificamos que luego del login la URL contenga la palabra 'inventory'
    # Esto indica que el login fue exitoso y redirigió correctamente
    assert "inventory" in driver.current_url


# ❌ Test: Login fallido con contraseña inválida
def test_login_fallido(driver):
    # Instanciamos LoginPage nuevamente
    page = LoginPage(driver)

    # Cargamos la página como antes
    page.load()

    # Enviamos una contraseña incorrecta intencionalmente
    page.login(Config.USERNAME, Config.WRONG_PASSWORD)

    # Verificamos que aparezca un mensaje de error esperado
    # Esto confirma que la validación funciona correctamente ante un fallo
    assert "Epic sadface" in page.get_error_message()


# Parametrize testdata

# Lista de tuplas con combinaciones de usuario y contraseña
testdata = [
    (Config.USERNAME, Config.PASSWORD),         # válido
    (Config.USERNAME, Config.WRONG_PASSWORD),   # contraseña incorrecta
    (Config.WRONG_USER, Config.PASSWORD),       # usuario inválido
    ("", ""),                     # ambos vacíos
]

# Parametrizamos con dos variables: user y pwd

@pytest.mark.parametrize("user, pwd", testdata)
def testdata_login(driver, user, pwd):
    page = LoginPage(driver)
    page.load()
    page.login(user, pwd)

    # Verificamos si el login fue exitoso o no
    if user == Config.USERNAME and pwd == Config.PASSWORD:
        # Si las credenciales son válidas, esperamos redirección a inventory
        assert "inventory" in driver.current_url
    else:
        # Si las credenciales fallan, debe aparecer mensaje de error
        assert "Epic sadface" in page.get_error_message()
