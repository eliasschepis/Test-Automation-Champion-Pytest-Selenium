# Importamos los métodos de localización de elementos de Selenium
from selenium.webdriver.common.by import By
import time

class CartPage:
    def __init__(self, driver):
        self.driver = driver
        self.checkoutButton = (By.ID, "checkout")

    def get_cart_product_names(self):
        items = self.driver.find_elements(By.CLASS_NAME, "inventory_item_name")
        return [item.text for item in items]

    def goTo_checkout_info(self):
        self.driver.find_element(*self.checkoutButton).click()
        time.sleep(1)
