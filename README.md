# Test-Automation-Champion-Pytest-Selenium
End-to-end UI testing framework using Python, Selenium, and Pytest to automate a complete purchase flow on SauceDemo. Built with Page Object Model architecture for scalability and maintainability.

# 🧪 Test Automation Champion: End-to-End UI Testing with Selenium & Pytest

This repository contains a fully functional end-to-end (E2E) automated UI test framework developed with **Python**, **Pytest**, and **Selenium WebDriver**, following best practices in **test automation architecture** and **Page Object Model (POM)** design.

## 🚀 Project Overview

This project simulates a complete purchase flow on [SauceDemo](https://www.saucedemo.com/), from login to order confirmation. The test is robust, reusable, and scalable, making it ideal as a portfolio project and a base for more complex automation pipelines.

### 🔁 Workflow covered

- ✅ User login
- ✅ Add multiple products to cart
- ✅ Validate products in cart
- ✅ Complete checkout information (form validation)
- ✅ Assert data integrity
- ✅ Finalize order
- ✅ Confirm success message

---

## 🧱 Tech Stack

| Tool | Description |
|------|-------------|
| **Python** | Programming language |
| **Pytest** | Test framework |
| **Selenium WebDriver** | Browser automation |
| **POM (Page Object Model)** | Pattern for page abstraction |
| **GitHub** | Version control & collaboration |
| **ChromeDriver** | Browser driver |
| **Config module** | Stores credentials and test data |

---

## 📁 Project Structure

``` bash
Test-Automation-Champion/
│
├── tests/ # Test cases (pytest-based)
│ └── test_buy.py # Full end-to-end test
│
├── pages/ # Page Object Models
│ ├── home_page.py
│ ├── cart_page.py
│ ├── checkout_page1.py
│ ├── checkout_page2.py
│ └── checkout_complete.py
│
├── utils/
│ ├── config.py # Test data and credentials
│ └── flows.py # Reusable flows like login
│
├── conftest.py # Pytest fixtures and WebDriver setup
└── requirements.txt # Project dependencies
```

---

## 🔑 Credentials (via `utils/config.py`)

```python
USERNAME = "standard_user"
PASSWORD = "secret_sauce"
USER_FIRSTNAME = "Elias"
USER_LASTNAME = "Schepis"
USER_ZIPCODE = "12345"
PRODUCTS_TUPLE = (
    "Sauce Labs Backpack",
    "Sauce Labs Bike Light",
    "Sauce Labs Bolt T-Shirt",
    "Sauce Labs Fleece Jacket",
    "Sauce Labs Onesie",
    "Test.allTheThings() T-Shirt (Red)"
)
```


🧠 Key Features
⏱️ Explicit waits (WebDriverWait + ExpectedConditions)

🧼 Clean locator management

🧪 Data-driven assertions

🔄 Reusability through helper flows

🛠️ Designed for scalability (can be integrated into CI/CD)

📌 Next Steps (Planned)
 Add pytest-html reporting

 Integrate Docker & GitHub Actions

 Extend tests with edge cases (e.g., invalid login, empty fields)

 Add visual regression testing (Playwright or Percy)

