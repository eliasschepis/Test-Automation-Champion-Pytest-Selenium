# ✅ QA Automation Framework (Selenium + Pytest + HTML Reports + Docker)

This is a complete QA automation framework built with **Python**, **Selenium WebDriver**, and **Pytest**, using the **Page Object Model (POM)** design pattern. It also includes **HTML reporting** and full **Docker integration** for isolated, reproducible test execution.

---

## 🚀 Features

- 🔹 Page Object Model structure (modular and scalable)
- 🔹 Selenium WebDriver for browser automation
- 🔹 Pytest for test execution
- 🔹 HTML reports with `pytest-html`
- 🔹 Docker integration for running tests in containers
- 🔹 Ready for CI/CD integration (GitHub Actions, etc.)

---

## 🧱 Project Structure

```
.
├── pages/          # Page Object classes (POM)
├── reports/        # Auto-generated HTML reports
├── tests/          # Test cases using Pytest
├── utils/          # Utility modules (waits, data, etc.)
├── Dockerfile      # Docker configuration
├── requirements.txt
└── README.md       # Project overview and instructions
```

---

## 🧪 How to Run Tests Locally

### 1. Install dependencies

```bash
pip install -r requirements.txt
```

### 2. Run tests with Pytest

```bash
pytest --html=reports/report.html --self-contained-html
```

The report will be saved in the `reports/` folder.

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

✅ This will:
- Mount your local `reports/` folder to the container
- Execute all tests inside Docker
- Output the `report.html` to your local `reports/` folder

📌 On Windows PowerShell, use:

```bash
docker run --rm -v ${PWD}.Path\reports:/app/reports qa-automation-framework
```

---

## 📊 Viewing the Test Report

After the test run, open:

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

---

## ✅ Next Steps (Optional)

- Add GitHub Actions for CI
- Add API testing with `requests`
- Add visual testing with `Playwright`
- Add environment configuration management
- Add test data generation utilities

---

## 📫 Contributions & Feedback

Feel free to fork this repo or submit issues and improvements.  
This project is intended for learning and as a production-ready foundation for your QA automation workflows.
