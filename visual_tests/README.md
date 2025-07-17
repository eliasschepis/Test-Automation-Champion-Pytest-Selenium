# 🎭 Visual Testing with Playwright (Standalone or Integrated with Selenium Framework)

This module adds **visual regression testing** to your existing Python automation framework using **Playwright**, ideal for detecting unexpected UI changes by comparing screenshots.

---

## 📦 Installation

```bash
pip install playwright pytest-playwright pillow
playwright install
```

> Playwright will install Chromium, Firefox, and WebKit.

---

## 📁 Folder Structure

```
visual_tests/
├── test_visual_homepage.py      # Main visual test
├── baseline/
│   └── homepage.png             # Reference screenshot (expected UI)
├── current/
│   └── homepage.png             # Captured screenshot during test
```

---

## 🧪 Sample Test (`visual_tests/test_visual_homepage.py`)

```python
import os
import pytest
from playwright.sync_api import sync_playwright
from PIL import Image, ImageChops

def compare_images(image1_path, image2_path):
    image1 = Image.open(image1_path)
    image2 = Image.open(image2_path)
    diff = ImageChops.difference(image1, image2)
    return diff.getbbox() is None  # True if identical

def test_visual_homepage():
    baseline_path = "visual_tests/baseline/homepage.png"
    current_path = "visual_tests/current/homepage.png"

    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()
        page.goto("https://www.saucedemo.com/")
        page.screenshot(path=current_path, full_page=True)
        browser.close()

    assert os.path.exists(baseline_path), "Baseline image does not exist"
    assert compare_images(baseline_path, current_path), "Visual regression detected!"
```

---

## 📸 How to Create the Reference Image (Baseline)

Run this helper script once:

```python
# visual_tests/save_baseline.py
from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch()
    page = browser.new_page()
    page.goto("https://www.saucedemo.com/")
    page.screenshot(path="visual_tests/baseline/homepage.png", full_page=True)
    browser.close()
```

---

## 🐳 Docker Support

Add the following to your `Dockerfile` to ensure visual testing works inside containers:

```dockerfile
RUN apt-get update && apt-get install -y wget gnupg libnss3 libatk-bridge2.0-0 libgtk-3-0 libxss1 libasound2 libxshmfence1 libgbm1 libx11-xcb1 libxcb1 libxcomposite1 libxdamage1 libxrandr2 libxinerama1 libxtst6 xdg-utils

RUN pip install playwright pytest-playwright pillow && playwright install --with-deps
```

---

## ✅ Run Visual Tests

```bash
pytest visual_tests/
```

If a difference is found, the test fails and you can manually compare `baseline/` and `current/` screenshots.

---

## 🧠 Best Practices

- Never update the reference screenshot automatically. Only do it manually after verifying changes are intended.
- Keep visual tests limited to key UI flows or components (homepage, cart, navbar, etc.)
- Consider adding tools for visual diffs (highlight pixel changes) if needed later.

---

## 🧩 Optional: GitHub Actions Support

You can add a job to your CI/CD workflow for visual tests:

```yaml
- name: Run visual tests
  run: pytest visual_tests/
```

---

Happy testing! 🧪🖼️

