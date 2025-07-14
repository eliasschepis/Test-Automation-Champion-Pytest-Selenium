# ✅ Continuous Integration with GitHub Actions

This project includes a complete CI workflow using **GitHub Actions** to automatically build the Docker container, run the Selenium + Pytest tests, and generate HTML reports on every `push` or `pull request`.

---

## 🚀 What does the workflow do?

Every time you push code or open a pull request, GitHub will:

1. **Clone your repo** on a temporary virtual machine (Ubuntu).
2. **Build the Docker image** using your existing `Dockerfile`.
3. **Run the tests** inside the Docker container using `pytest`.
4. **Copy the HTML reports** from inside the container to the runner.
5. **Upload the reports** as downloadable artifacts.
6. **Clean up the Docker container** after the test run.

---

## 🗂 Folder structure expected

Your repository should have at least the following structure:

```
📦 your-project/
 ┣ 📁 pages/
 ┣ 📁 tests/
 ┣ 📁 reports/
 ┣ 📁 .github/
 ┃ ┗ 📁 workflows/
 ┃    ┗ ci.yml           👈 GitHub Actions workflow lives here
 ┣ 📄 requirements.txt
 ┣ 📄 Dockerfile
 ┗ 📄 pytest.ini (optional)
```

---

## ⚙️ Workflow file: `.github/workflows/ci.yml`

Here is the full content of the GitHub Actions workflow file used for CI:

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
        uses: actions/checkout@v3

      - name: Build Docker image
        run: docker build -t selenium-tests .

      - name: Run tests inside Docker
        run: |
          docker run --name selenium-runner selenium-tests

      - name: Copy reports to host
        run: |
          docker cp selenium-runner:/app/reports ./reports

      - name: Clean up
        run: docker rm selenium-runner

      - name: Upload HTML Report
        uses: actions/upload-artifact@v3
        with:
          name: test-report
          path: ./reports
```

---

## 📥 How to use it

1. Create the folder: `.github/workflows/`
2. Inside it, create the file: `ci.yml`
3. Paste the workflow code above.
4. Commit and push:

```bash
git add .github/workflows/ci.yml
git commit -m "Add CI workflow with Docker and pytest"
git push origin main
```

5. Go to the **Actions** tab on your GitHub repo to see the workflow in action.
6. When it completes, you'll find the `test-report` available as an **artifact** to download.

---

## ❗ Note

If your IDE shows warnings like `Unresolved action reference` or `Undefined parameter`, don’t worry — those are false positives. GitHub fully supports this syntax.

---

## 🧼 Next Steps (Optional)

- Add test badges to the README.
- Send report results to Slack or email.
- Deploy or notify on test pass/fail.

---

Happy testing! 🧪🐍🐳
