# Importamos los métodos de localización de elementos de Selenium

from selenium.webdriver.common.by import By
from utils.helpers import wait_for_element
import time


class HomePage:
    def __init__(self, driver):
        self.driver = driver
        self.burgerButton = (By.ID, "react-burger-menu-btn")
        self.logoutButton = (By.ID, "logout_sidebar_link")
        self.checkoutButton = (By.CLASS_NAME, "shopping_cart_link")

    def add_product_to_cart(self, product_id):
        # product_id por ejemplo: "sauce-labs-backpack"
        button = (By.ID, f"add-to-cart-{product_id}")
        self.driver.find_element(*button).click()


    def add_multiple_products(self, product_ids: list):
        for product_id in product_ids:
            self.add_product_to_cart(product_id)
            time.sleep(2)

    def goToCheckoutPage(self):
        wait_for_element(self.driver, self.checkoutButton).click()
        self.driver.find_element(*self.checkoutButton).click()


    def logout (self):
        self.driver.find_element(*self.burgerButton).click()
        self.driver.find_element(*self.logoutButton).click()
