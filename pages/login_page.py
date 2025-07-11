# Importamos los métodos de localización de elementos de Selenium
from selenium.webdriver.common.by import By

# Esta clase representa la página de login del sitio
# Usamos Page Object Model (POM) para separar la lógica de UI de los tests
class LoginPage:
    # Constructor de la clase: se ejecuta al crear la instancia
    def __init__(self, driver):
        self.driver = driver  # Guardamos el WebDriver que nos permite controlar el navegador

        # Definimos los "localizadores" de los elementos que vamos a usar
        # Estos localizadores pueden cambiar según la UI, así que se aíslan aquí
        self.username_input = (By.ID, "user-name")            # Campo de texto para el nombre de usuario
        self.password_input = (By.ID, "password")             # Campo de texto para la contraseña
        self.login_button = (By.ID, "login-button")           # Botón para enviar el formulario
        self.error_message = (By.XPATH, "//h3[@data-test='error']")  # Mensaje de error (si login falla)

    # Método para abrir la página (URL del sitio)
    def load(self):
        self.driver.get("https://www.saucedemo.com")

    # Método para ejecutar el login: completa los campos y hace clic
    def login(self, username, password):
        self.driver.find_element(*self.username_input).send_keys(username)
        self.driver.find_element(*self.password_input).send_keys(password)
        self.driver.find_element(*self.login_button).click()

    # Método para obtener el texto del mensaje de error (si aparece)
    def get_error_message(self):
        return self.driver.find_element(*self.error_message).text
