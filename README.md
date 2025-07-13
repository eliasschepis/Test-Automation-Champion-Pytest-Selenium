# Test Automation Champion

End-to-end test automation project using Selenium, Pytest, and the Page Object Model (POM). This repository simulates a complete user purchase flow on the [Sauce Demo](https://www.saucedemo.com) e-commerce platform.

---

## ✅ Completed Features

- 🔧 **Framework Setup**  
  Configured with Pytest, Selenium, Page Object Model, and custom flows for reusable logic.

- 🔐 **Login Automation**  
  Automated login using data from a centralized configuration.

- 🛒 **Product Selection**  
  Ability to add multiple predefined products by ID.

- 🧾 **Cart Validation**  
  Verifies that all selected products appear in the shopping cart.

- 📦 **Checkout Process (Step 1 & 2)**  
  - Enters user information from config.  
  - Verifies the summary page contains at least one of the expected products (data-driven with a tuple).

- ✅ **Order Completion**  
  Finalizes the order and confirms a successful purchase.

- 📂 **Clean Folder Structure**  
  - `pages/`: Page Object Models for each page  
  - `tests/`: Pytest tests  
  - `utils/`: Configs and reusable flows

---

## 📍 Technologies Used

- Python 3
- Pytest
- Selenium WebDriver
- POM (Page Object Model) pattern
- Git + GitHub for version control

---

## 🚧 Next Steps (In Progress)

- 📊 **Integrate HTML Reports**  
  Add reporting functionality to visualize test results and logs.

- 🧪 **API Testing with `requests`**  
  Validate product and user endpoints.

- 🖼️ **Visual Testing with Playwright**  
  Snapshot validation and UI consistency.

- 🐳 **Docker Integration**  
  Run tests in isolated containers for CI/CD.

- ⚙️ **CI/CD via GitHub Actions**  
  Auto-run tests on every push, PR or scheduled event.

---

## 📁 How to Run

```bash
# Create virtual environment
python -m venv .venv
source .venv/bin/activate  # or .venv\Scripts\activate on Windows

# Install dependencies
pip install -r requirements.txt

# Run tests
pytest tests/
```

---

## 🙌 Author

Elias Schepis  
Automation QA Engineer  
🇪🇸 Based in Europe | 🌍 Open to international collaboration

---

```python
# test_buy.py
def test_complete_workflow(driver):
    # Full E2E test workflow implementation completed!
    pass
```

Stay tuned for API, visual testing and CI/CD integrations 🚀
