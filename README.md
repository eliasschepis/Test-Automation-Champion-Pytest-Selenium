# ✅ QA Automation Framework (Selenium + Pytest + HTML Reports + Docker + GitHub Actions)

![CI](https://github.com/eliasschepis/Test-Automation-Champion-SauceE2E/actions/workflows/ci.yml/badge.svg)

This is a complete QA automation framework built with **Python**, **Selenium WebDriver**, and **Pytest**, using the **Page Object Model (POM)** design pattern. It also includes **HTML reporting**, full **Docker integration**, a ready-to-use **GitHub Actions CI/CD pipeline**, **API testing**, and **visual regression testing with Playwright**.

---

## 🚀 Features

- 🔹 Page Object Model structure (modular and scalable)
- 🔹 Selenium WebDriver for browser automation
- 🔹 Pytest for test execution
- 🔹 HTML reports with `pytest-html`
- 🔹 Docker integration for running tests in containers
- 🔹 GitHub Actions CI/CD for automated testing on push and PR
- 🔹 REST API tests with `requests`
- 🔹 Visual Testing with Playwright (UI comparisons)

---

## 🧱 Project Structure

```
.
├── pages/                   # Page Object classes (POM)
├── reports/                 # Auto-generated HTML reports
├── tests/                   # Test cases using Pytest
│   └── api_tests/           # REST API tests using requests
├── visual_tests/            # Playwright visual UI tests
│   ├── baseline/            # Reference screenshots
│   ├── current/             # Screenshots taken during tests
│   ├── test_visual_homepage.py
│   ├── test_visual_login.py
│   └── test_visual_login_fail.py
├── utils/                   # Utility modules (waits, data, etc.)
├── .github/
│   └── workflows/
│       └── ci.yml           # GitHub Actions workflow
├── Dockerfile               # Docker configuration
├── requirements.txt
└── README.md                # Project overview and instructions
```

---

## 🧪 How to Run Tests Locally

### 1. Install dependencies

```bash
pip install -r requirements.txt
```

### 2. Run Selenium + Pytest tests

```bash
pytest --html=reports/report.html --self-contained-html
```

The report will be saved in the `reports/` folder.

---

## 🖼️ Visual Testing with Playwright

This framework includes **visual regression testing** using **Playwright** to detect unintended UI changes by comparing screenshots to reference images.

### 🔍 Visual Tests Included

- Home Page UI
- Successful Login UI
- Failed Login (error message)

### 🧪 Run visual tests

```bash
pytest visual_tests/
```

### 📁 Screenshot folders

- `visual_tests/baseline/`: reference images (expected UI)
- `visual_tests/current/`: screenshots generated during test runs

> Update baseline images manually only when the UI change is intentional.

### 🐳 Docker Support

Ensure your `Dockerfile` contains the required dependencies for Playwright. See `README_visual.md` for full details.

---

## 🐳 How to Run Tests with Docker

### 1. Build the Docker image

```bash
docker build -t qa-automation-framework .
```

### 2. Run the tests in a container

```bash
docker run --rm -v ${PWD}/reports:/app/reports qa-automation-framework
```

📌 On Windows PowerShell, use:

```bash
docker run --rm -v ${PWD}.Path\reports:/app/reports qa-automation-framework
```

✅ This will:
- Mount your local `reports/` folder to the container
- Execute all tests inside Docker
- Output the `report.html` to your local `reports/` folder

---

## ⚙️ Continuous Integration with GitHub Actions

This project includes a complete CI workflow using **GitHub Actions** to automatically build the Docker container, run tests, and generate HTML reports on every `push` or `pull request`.

### ✅ What the workflow does:

1. Clones your repository into a GitHub Actions runner (Ubuntu).
2. Builds the Docker image from your Dockerfile.
3. Runs all tests inside the container.
4. Copies the HTML report from the container to the runner.
5. Uploads the report as an artifact.
6. Cleans up the container.

### 📄 `.github/workflows/ci.yml`

```yaml
name: Run Selenium Pytest inside Docker

on:
  push:
  pull_request:

jobs:
  test:
    runs-on: ubuntu-latest

    steps:
      - name: Checkout repository
        uses: actions/checkout@v4

      - name: Build Docker image
        run: docker build -t selenium-tests .

      - name: Run tests inside Docker
        run: |
          docker run --name selenium-runner selenium-tests || docker logs selenium-runner

      - name: Copy reports to host
        run: |
          docker cp selenium-runner:/app/reports ./reports

      - name: Clean up
        run: docker rm selenium-runner

      - name: Upload HTML Report
        uses: actions/upload-artifact@v4
        with:
          name: test-report
          path: ./reports
```

---

## 📡 API Testing Included

This framework also includes tests for public REST APIs using Python's `requests` library.  
Located under `tests/api_tests/`.

### 🧪 Run API tests

```bash
pytest tests/api_tests/
```

Or with HTML report:

```bash
pytest tests/api_tests/ --html=reports/api_test_report.html
```

---

## 📊 Viewing the Test Report

After any test run (local or CI), open:

```
reports/report.html
```

It contains a full summary of passed and failed tests, logs, and metadata.

---

## 📌 Technologies Used

- Python 3.11
- Selenium WebDriver
- Pytest
- Pytest-HTML
- Docker
- GitHub Actions
- Playwright (for visual testing)
- Requests (for API tests)

---

## 🧼 Optional Next Steps

- Add a badge showing CI status in the README (✅ already done)
- Add more API endpoints and visual flows
- Add test data generators
- Add environment switching (dev/stage/prod)
- Integrate test result notifications (Slack, email, etc.)

---

## 📫 Contributions & Feedback

Feel free to fork this repo or submit issues and improvements.  
This project is intended for learning and as a production-ready foundation for robust QA automation.
