# Test-Automation-Champion-Pytest-Selenium

End-to-end test automation framework using Python, Selenium, Pytest, and Page Object Model – focused on real-world eCommerce flows.

# 🧪 Test Automation Framework – Python + Selenium + Pytest

This is a complete **end-to-end test automation framework** built with Python, using **Selenium WebDriver**, **Pytest**, and the **Page Object Model (POM)** design pattern. It automates realistic eCommerce flows, follows QA best practices, and is designed for portfolio building and job interview preparation.

---

## 🚀 Key Features

- ✅ **Clean and scalable Python framework**
- 🧱 **Page Object Model architecture** (login, home, cart, checkout pages, etc.)
- 🔁 **Parameterized tests** with Pytest
- 🧪 Full **purchase flow validation**
- 🧼 Custom Selenium **fixtures** with browser config in `conftest.py`
- 📦 Reusable tests for multiple products
- 💬 **Fully commented code** to help learning and explanation during interviews

---

## 📁 Project Structure

```bash
.
├── conftest.py
├── requirements.txt
├── README.md
├── utils/
│   └── config.py
│   └── helpers.py
├── pages/
│   └── login_page.py
│   └── home_page.py
│   └── cart_page.py
│   └── checkout_page_1.py
│   └── checkout_page_2.py
│   └── checkout_complete_page.py
├── tests/
│   └── test_login.py
│   └── test_add_products.py
│   └── test_checkout.py
│   └── test_full_flow.py
```

# 🧰 Tech Stack
Python 3.10+

Selenium WebDriver

Pytest

ChromeDriver

PyCharm (recommended IDE)

# 🎯 Purpose of This Project
This repository is meant to:

Consolidate practical skills in UI test automation with Python

Prepare for QA Automation job interviews in Europe

Serve as a professional portfolio project on GitHub

# 🧪 Future Enhancements
CI/CD with GitHub Actions

HTML test reports

API testing with requests

Dockerized test execution

Visual regression testing (Playwright or similar)

# ⚙️ Quick Setup

pip install -r requirements.txt
pytest
