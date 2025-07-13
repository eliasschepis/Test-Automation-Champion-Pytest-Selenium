# 🧪 tests/

This folder contains all the **test cases** written using **Pytest**.  
Each test simulates a user behavior or verifies a specific feature of the application under test, using the Page Object Model (POM) classes from the `pages/` directory.

---

## 🔍 Purpose

- Automate end-to-end browser interactions using Selenium.
- Validate UI behavior by combining page actions and Pytest assertions.
- Keep test logic readable, modular, and easy to debug.

---

## 📁 File Naming Conventions

- All test files should start with `test_` and be written in lowercase.  
  Example: `test_login.py`, `test_checkout.py`

- Inside each file, test functions should also begin with `test_` so Pytest can auto-discover them.

---

## 🧱 Recommended Structure

Each test file typically follows this structure:

1. Import necessary page objects.
2. Use fixtures (e.g., `browser`) to set up the driver.
3. Instantiate page objects.
4. Call page methods to perform actions.
5. Use assertions to validate the outcome.

---

## ✅ Example

```python
import pytest
from pages.login_page import LoginPage

def test_login_success(browser):
    login_page = LoginPage(browser)
    login_page.login("standard_user", "secret_sauce")
    assert "inventory" in browser.current_url
```

---

## 🧪 Pytest Features You Can Use

- `assert` statements for validations
- Custom fixtures in `conftest.py`
- Markers like:
  ```python
  @pytest.mark.smoke
  @pytest.mark.regression
  ```

- Parametrization:
  ```python
  @pytest.mark.parametrize("username,password", [
      ("standard_user", "secret_sauce"),
      ("locked_out_user", "secret_sauce")
  ])
  def test_login_various_users(browser, username, password):
      login_page = LoginPage(browser)
      login_page.login(username, password)
      assert "inventory" in browser.current_url
  ```

---

## 🧪 Running the Tests

### From the root of the project:

```bash
pytest --html=reports/report.html --self-contained-html
```

Or with markers:

```bash
pytest -m smoke
```

If using Docker:

```bash
docker run --rm -v ${PWD}/reports:/app/reports qa-automation-framework
```

---

## 💡 Best Practices

- Keep one feature per test file.
- Use the Page Object methods instead of raw Selenium calls.
- Avoid hardcoded waits (use WebDriverWaits instead).
- Organize tests logically: happy paths, edge cases, negative scenarios.

---

## 📂 Where Page Objects Come In

All interactions in tests should use classes from the `pages/` directory to maintain a clean separation of logic and assertions.

---

## 🧹 Maintenance Notes

When UI changes happen:
- You should only need to update the page object classes.
- Tests themselves rarely need to change, which improves long-term stability.

---
