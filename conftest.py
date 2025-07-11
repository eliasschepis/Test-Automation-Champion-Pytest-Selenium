import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

@pytest.fixture
def driver():
    chrome_options = Options()

    # ✅ Desactiva el warning de contraseñas y otras notificaciones molestas
    chrome_options.add_experimental_option("prefs", {
        "credentials_enable_service": False,
        "profile.password_manager_enabled": False
    })

    chrome_options.add_argument("--disable-notifications")
    chrome_options.add_argument("--disable-popup-blocking")
    chrome_options.add_argument("--start-maximized")
    chrome_options.add_argument("--disable-extensions")

    driver = webdriver.Chrome(options=chrome_options)
    driver.implicitly_wait(5)

    yield driver
    driver.quit()
