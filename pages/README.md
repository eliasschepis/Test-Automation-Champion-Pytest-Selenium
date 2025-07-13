# 📄 pages/

This folder contains all the **Page Object Model (POM)** classes for the application under test.

Each file in this directory represents a single page or component of the user interface, encapsulating all element locators and page-specific methods.  
This separation allows for easier maintenance, better reusability, and cleaner test logic.

---

## 🔍 Purpose

- Encapsulate Selenium locators and actions for each page.
- Keep test files clean and high-level.
- Avoid code duplication across test cases.

---

## 🧱 Naming Conventions

- Files should be named after the page they represent, in lowercase with underscores.  
  Example: `login_page.py`, `home_page.py`, `checkout_page.py`

- Each class should follow the naming pattern: `LoginPage`, `HomePage`, etc.

---

## 📌 Structure of a Page Class

Every page class should:

1. Accept the Selenium `driver` in the constructor.
2. Contain locators and interactions for that page.
3. Use methods to abstract actions (e.g., `click_login_button()`).

---

## ✅ Example

```python
from selenium.webdriver.common.by import By

class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.username_input = (By.ID, "user-name")
        self.password_input = (By.ID, "password")
        self.login_button = (By.ID, "login-button")

    def enter_username(self, username):
        self.driver.find_element(*self.username_input).send_keys(username)

    def enter_password(self, password):
        self.driver.find_element(*self.password_input).send_keys(password)

    def click_login(self):
        self.driver.find_element(*self.login_button).click()

    def login(self, username, password):
        self.enter_username(username)
        self.enter_password(password)
        self.click_login()
```

---

## 📁 Where is it used?

These page classes are used in the `tests/` folder to structure user workflows and scenarios.  
For example, a test can look like:

```python
def test_login_success(browser):
    login_page = LoginPage(browser)
    login_page.login("standard_user", "secret_sauce")
    assert "inventory" in browser.current_url
```

---

## 💡 Tips

- Reuse actions between test cases to reduce code duplication.
- Keep logic in the page files, and assertions in the test files.
- Add small helper methods for specific actions instead of duplicating `find_element` calls.

---

## 🧹 Maintenance Notes

If the application UI changes:
- Update the affected locators only in the relevant page class.
- Test cases won’t need to change, which reduces maintenance overhead.

---

