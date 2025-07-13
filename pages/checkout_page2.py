from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CheckoutPage2:
    def __init__(self, driver):
        self.driver = driver
        self.product_locator = (By.CLASS_NAME, "inventory_item_name")
        self.finish_locator = (By.ID, "finish")

    def get_lastInfo(self):
        WebDriverWait(self.driver, 5).until(
            EC.presence_of_all_elements_located(self.product_locator)
        )
        products = self.driver.find_elements(*self.product_locator)
        return [product.text for product in products]

    def finishButton(self):
        WebDriverWait(self.driver, 5).until(
            EC.element_to_be_clickable(self.finish_locator)
        ).click()