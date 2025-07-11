class SomePage:
    def __init__(self, driver):
        self.driver = driver
        self.some_element = (By.ID, "element-id")

    def do_something(self):
        self.driver.find_element(*self.some_element).click()
