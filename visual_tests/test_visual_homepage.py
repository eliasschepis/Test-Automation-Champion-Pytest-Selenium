import os
import pytest
from playwright.sync_api import sync_playwright
from PIL import Image, ImageChops

# visual_tests/save_baseline.py

# homepage test
with sync_playwright() as p:
    browser = p.chromium.launch()
    page = browser.new_page()
    page.goto("https://www.saucedemo.com/")
    page.screenshot(path="visual_tests/baseline/homepage.png", full_page=True)
    browser.close()

# login test

with sync_playwright() as p:
    browser = p.chromium.launch()
    page = browser.new_page()
    page.goto("https://www.saucedemo.com/")
    page.fill('input[data-test="username"]', 'standard_user')
    page.fill('input[data-test="password"]', 'secret_sauce')
    page.click('input[data-test="login-button"]')
    page.wait_for_selector(".inventory_list")
    page.screenshot(path="visual_tests/baseline/login_success.png", full_page=True)
    browser.close()

# login unhappy test

with sync_playwright() as p:
    browser = p.chromium.launch()
    page = browser.new_page()
    page.goto("https://www.saucedemo.com/")
    page.fill('input[data-test="username"]', 'locked_out_user')
    page.fill('input[data-test="password"]', 'wrong_password')
    page.click('input[data-test="login-button"]')
    page.wait_for_selector('h3[data-test="error"]')
    page.screenshot(path="visual_tests/baseline/login_fail.png", full_page=True)
    browser.close()

# Compara dos imágenes pixel por pixel
def compare_images(image1_path, image2_path):
    image1 = Image.open(image1_path)
    image2 = Image.open(image2_path)

    # Calcula la diferencia absoluta entre ambas imágenes
    diff = ImageChops.difference(image1, image2)

    # Si no hay diferencia (getbbox() devuelve None), las imágenes son iguales
    return diff.getbbox() is None

# Test visual de la página de inicio de saucedemo
def test_visual_homepage():
    baseline_path = "visual_tests/baseline/homepage.png"  # Imagen de referencia
    current_path = "visual_tests/current/homepage.png"    # Imagen generada al correr el test

    # Usamos Playwright para lanzar un navegador y tomar un screenshot actual
    with sync_playwright() as p:
        browser = p.chromium.launch()  # También puedes usar .firefox o .webkit
        page = browser.new_page()
        page.goto("https://www.saucedemo.com/")  # Página a testear
        page.screenshot(path=current_path, full_page=True)  # Captura de pantalla completa
        browser.close()

    # Verifica que la imagen de referencia exista
    assert os.path.exists(baseline_path), "Baseline image does not exist"

    # Compara la imagen actual con la de referencia
    assert compare_images(baseline_path, current_path), "Visual regression detected!"


# Test visual tras iniciar sesión con un usuario válido
def test_visual_login_success():
    baseline_path = "visual_tests/baseline/login_success.png"   # Imagen de referencia
    current_path = "visual_tests/current/login_success.png"     # Imagen tomada en el test

    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()

        # Abre la página de login
        page.goto("https://www.saucedemo.com/")

        # Completa el formulario de login con credenciales válidas
        page.fill('input[data-test="username"]', 'standard_user')
        page.fill('input[data-test="password"]', 'secret_sauce')
        page.click('input[data-test="login-button"]')

        # Espera a que el inventario esté cargado
        page.wait_for_selector(".inventory_list")

        # Captura la pantalla del estado luego de hacer login
        page.screenshot(path=current_path, full_page=True)
        browser.close()

    # Verifica que exista la imagen de referencia
    assert os.path.exists(baseline_path), "Baseline image does not exist"

    # Compara la imagen actual con la imagen base
    assert compare_images(baseline_path, current_path), "Visual regression detected after login!"

    # Test visual para validar mensaje de error tras login fallido
    def test_visual_login_fail():
        baseline_path = "visual_tests/baseline/login_fail.png"
        current_path = "visual_tests/current/login_fail.png"

        with sync_playwright() as p:
            browser = p.chromium.launch()
            page = browser.new_page()

            # Ir al login y usar credenciales inválidas
            page.goto("https://www.saucedemo.com/")
            page.fill('input[data-test="username"]', 'locked_out_user')
            page.fill('input[data-test="password"]', 'wrong_password')
            page.click('input[data-test="login-button"]')

            # Esperar a que aparezca el mensaje de error
            page.wait_for_selector('h3[data-test="error"]')

            # Capturar screenshot del estado con el error
            page.screenshot(path=current_path, full_page=True)
            browser.close()

        # Verificar si existe la imagen de referencia
        assert os.path.exists(baseline_path), "Baseline image does not exist"
        assert compare_images(baseline_path, current_path), "Visual regression detected on failed login!"
