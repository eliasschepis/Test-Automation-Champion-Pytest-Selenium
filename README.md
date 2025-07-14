# ✅ QA Automation Framework (Selenium + Pytest + HTML Reports + Docker + GitHub Actions)

This is a complete QA automation framework built with **Python**, **Selenium WebDriver**, and **Pytest**, using the **Page Object Model (POM)** design pattern. It also includes **HTML reporting**, full **Docker integration**, and a ready-to-use **GitHub Actions CI/CD pipeline** for isolated, reproducible, and automated test execution.

---

## 🚀 Features

- 🔹 Page Object Model structure (modular and scalable)
- 🔹 Selenium WebDriver for browser automation
- 🔹 Pytest for test execution
- 🔹 HTML reports with `pytest-html`
- 🔹 Docker integration for running tests in containers
- 🔹 GitHub Actions CI/CD for automated testing on push and PR

---

## 🧱 Project Structure

```
.
├── pages/          # Page Object classes (POM)
├── reports/        # Auto-generated HTML reports
├── tests/          # Test cases using Pytest
├── utils/          # Utility modules (waits, data, etc.)
├── .github/
│   └── workflows/
│       └── ci.yml  # GitHub Actions workflow
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

## ⚙️ Continuous Integration with GitHub Actions

This project includes a complete CI workflow using **GitHub Actions** to automatically build the Docker container, run the Selenium + Pytest tests, and generate HTML reports on every `push` or `pull request`.

### ✅ What the workflow does:

1. Clones your repository into a GitHub Actions runner (Ubuntu).
2. Builds the Docker image from your Dockerfile.
3. Runs all tests inside the container.
4. Copies the HTML report from the container to the runner.
5. Uploads the report as an artifact you can download.
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

### 📥 How to use it

1. Create the folder `.github/workflows/` if it doesn't exist.
2. Add the file `ci.yml` with the contents above.
3. Commit and push to GitHub:

```bash
git add .github/workflows/ci.yml
git commit -m "Add CI workflow with Docker and pytest"
git push origin main
```

4. Go to the **Actions** tab on GitHub to monitor the workflow.
5. Once complete, download the HTML report from the **Artifacts** section.

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

---

## 🧼 Optional Next Steps

- Add a badge showing CI status in the README
- Add API testing with `requests`
- Add visual testing with `Playwright`
- Add configuration per environment (dev/stage/prod)
- Add test data generators or factories
- Integrate with Slack/email for test results

---

## 📫 Contributions & Feedback

Feel free to fork this repo or submit issues and improvements.  
This project is intended for learning and as a production-ready foundation for your QA automation workflows.
