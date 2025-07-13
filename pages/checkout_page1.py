from selenium.webdriver.common.by import By
from utils.config import Config
import time

class CheckoutPage1:
    def __init__(self, driver):
        self.driver = driver
        self.firstname_locator = (By.ID, "first-name")
        self.lastname_locator = (By.ID, "last-name")
        self.postal_code_locator = (By.ID, "postal-code")
        self.continue_button_locator = (By.ID, "continue")

    def fill_checkout_info(self):
        self.driver.find_element(*self.firstname_locator).send_keys(Config.USER_FIRSTNAME)
        self.driver.find_element(*self.lastname_locator).send_keys(Config.USER_LASTNAME)
        self.driver.find_element(*self.postal_code_locator).send_keys(Config.USER_ZIPCODE)
        time.sleep(1)

    def get_info(self):
        return [
            self.driver.find_element(*self.firstname_locator).get_attribute("value"),
            self.driver.find_element(*self.lastname_locator).get_attribute("value"),
            self.driver.find_element(*self.postal_code_locator).get_attribute("value"),
        ]

    def click_continue_button(self):
        self.driver.find_element(*self.continue_button_locator).click()