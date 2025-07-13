# 📊 Pytest HTML Reporting with Screenshots

This project includes full integration of HTML test reports using `pytest-html`, along with automatic screenshot capture on test failure.

The goal is to make it easy for anyone to:
- Run the tests
- Generate a full visual report
- Understand which tests failed and why
- See screenshots of failed steps for easy debugging

---

## ✅ Prerequisites

Make sure you have Python and `pip` installed. Then install the dependencies:

```bash
pip install -r requirements.txt
```

At minimum, you'll need:

```bash
pip install pytest pytest-html selenium
```

---

## 📁 Step 1: Create the `reports/` folder

This folder will store your HTML reports and screenshots.

```bash
mkdir reports
```

(Optional, but recommended: add it to `.gitignore` so it doesn’t get committed.)

---

## 🧪 Step 2: Run your tests with HTML reporting

Use the following command to run your tests and generate a standalone HTML report:

```bash
pytest --html=reports/report.html --self-contained-html
```

This creates an HTML file that can be opened in any browser without needing extra CSS/JS files.

---

## 🧷 Step 3: Enable screenshots on test failures

Make sure you have a file named `conftest.py` in your root folder, and add the following code to it:

```python
# conftest.py
import pytest
import os
from datetime import datetime

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    # Execute test
    outcome = yield
    rep = outcome.get_result()

    # Take screenshot on failure
    if rep.when == "call" and rep.failed:
        driver = item.funcargs.get("driver")
        if driver:
            screenshots_dir = os.path.join("reports", "screenshots")
            os.makedirs(screenshots_dir, exist_ok=True)

            file_name = f"{item.name}_{datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.png"
            destination_file = os.path.join(screenshots_dir, file_name)

            driver.save_screenshot(destination_file)

            # Attach screenshot to HTML report
            if "pytest_html" in item.config.pluginmanager.list_name_plugin():
                extra = getattr(rep, "extra", [])
                extra.append(pytest_html.extras.image(destination_file))
                rep.extra = extra
```

This hook will:
- Detect when a test fails
- Take a screenshot using the Selenium WebDriver
- Save it under `reports/screenshots/`
- Attach it to the generated HTML report

---

## 🧩 Step 4: Use the driver fixture properly

Make sure your tests receive the `driver` as a fixture. For example:

```python
def test_login_valid(driver):
    driver.get("https://example.com")
    assert "Example" in driver.title
```

And define the `driver` fixture like this (in `conftest.py` or a separate `fixtures.py`):

```python
import pytest
from selenium import webdriver

@pytest.fixture
def driver():
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")  # remove this if you want to see the browser
    driver = webdriver.Chrome(options=options)
    yield driver
    driver.quit()
```

This allows the `conftest.py` hook to access the browser and take screenshots.

---

## 🌐 Step 5: Open the report

After running the tests, you’ll find your report at:

```
reports/report.html
```

You can open it by double-clicking the file or using a command like:

```bash
start reports/report.html      # On Windows
open reports/report.html       # On macOS
xdg-open reports/report.html   # On Linux
```

---

## 📝 Tip: Ignore reports in Git

To prevent committing heavy reports and screenshots to GitHub, add this line to your `.gitignore` file:

```
reports/
```

---

## ✅ Example Command Summary

```bash
# Run tests and generate report
pytest --html=reports/report.html --self-contained-html
```

---

## 📸 Final Output

The HTML report will include:
- Test status (Passed, Failed, Skipped)
- Time and duration
- Inline screenshots of failures
- Clear test breakdown by function

Perfect for CI pipelines or manual debugging!

---

## 📦 Folder Structure Example

```
your-project/
│
├── tests/
│   └── test_example.py
├── reports/
│   └── report.html
│   └── screenshots/
├── conftest.py
├── requirements.txt
└── README.md
```

---

Happy testing! 💥
