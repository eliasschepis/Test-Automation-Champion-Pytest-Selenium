# Importamos los métodos de localización de elementos de Selenium
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class CartPage:
    def __init__(self, driver):
        self.driver = driver
        self.checkoutButton = (By.ID, "checkout")

    def get_cart_product_names(self):
        items = self.driver.find_elements(By.CLASS_NAME, "inventory_item_name")
        return [item.text for item in items]

    def goTo_checkout_info(self):
        WebDriverWait(self.driver, 5).until(
            EC.element_to_be_clickable(self.checkoutButton)
        ).click()