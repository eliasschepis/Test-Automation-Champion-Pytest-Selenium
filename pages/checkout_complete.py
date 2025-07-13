from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CheckoutComplete:
    def __init__(self, driver):
        self.driver = driver
        self.complete_locator = (By.CLASS_NAME, "complete-header")
        self.home_locator = (By.ID, "back-to-products")

    def get_completeHeader(self):
        WebDriverWait(self.driver, 5).until(
            EC.presence_of_all_elements_located(self.complete_locator)
        )
        self.driver.find_element(By.CLASS_NAME, "complete-header")

    def homeButton(self):
        WebDriverWait(self.driver, 5).until(
            EC.element_to_be_clickable(self.home_locator)
        ).click()