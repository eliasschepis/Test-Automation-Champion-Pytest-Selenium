import pytest
import os
from datetime import datetime
from selenium import webdriver

@pytest.fixture
def driver():
    options = webdriver.ChromeOptions()

    # ✅ Modo limpio: sin historial, sin sesión, sin logins previos
    options.add_argument("--guest")
    options.add_argument("--incognito")

    # ✅ Opcional: iniciar maximizado (recomendado para evitar problemas de resolución)
    options.add_argument("--start-maximized")

    # ✅ Desactivar advertencias del administrador de contraseñas
    options.add_argument("--disable-features=AutofillServerCommunication")
    options.add_argument("--disable-features=PasswordManagerEnableAccountStorage")
    options.add_argument("--disable-features=PasswordLeakDetection")

    # ✅ Desactivar popup del password manager
    prefs = {
        "credentials_enable_service": False,
        "profile.password_manager_enabled": False
    }
    options.add_experimental_option("prefs", prefs)

    driver = webdriver.Chrome(options=options)
    yield driver
    driver.quit()


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    # Ejecutamos el código del test
    outcome = yield
    rep = outcome.get_result()

    # Si falló y es la parte del 'call' (no setup/teardown)
    if rep.when == "call" and rep.failed:
        # Recuperamos el WebDriver si está en item.funcargs
        driver = item.funcargs.get("driver")
        if driver:
            # Creamos carpeta si no existe
            screenshots_dir = os.path.join("reports", "screenshots")
            os.makedirs(screenshots_dir, exist_ok=True)

            # Nombre único por test y timestamp
            file_name = f"{item.name}_{datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.png"
            destination_file = os.path.join(screenshots_dir, file_name)

            # Tomamos screenshot
            driver.save_screenshot(destination_file)

            # Agregamos como extra en el reporte
            if "pytest_html" in item.config.pluginmanager.list_name_plugin():
                extra = getattr(rep, "extra", [])
                extra.append(pytest_html.extras.image(destination_file))
                rep.extra = extra
