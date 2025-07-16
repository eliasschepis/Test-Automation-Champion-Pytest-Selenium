### 📡 API Testing with `requests` + `pytest`

This project includes a set of automated **API tests** using Python's `requests` library and `pytest`, following a clean and scalable structure.

---

#### 📁 Folder Structure

```
/tests
  └── api_tests
        ├── test_api_users.py     # All API tests (GET, POST, PUT, DELETE)
        └── conftest.py           # Fixtures (e.g. base_url)
```

---

#### ✅ Requirements

Install the required dependency:

```bash
pip install requests
```

> `pytest` is already assumed to be installed for the main framework.

---

#### 🚀 How to Run the API Tests

Run all tests inside the `api_tests/` folder:

```bash
pytest tests/api_tests/
```

Generate an HTML report (if HTML reporting is integrated):

```bash
pytest tests/api_tests/ --html=reports/api_test_report.html
```

---

#### 🧪 Example Tests Included

- `GET /users?page=2`: validates user list retrieval
- `POST /users`: simulates user creation
- `PUT /users/2`: simulates user update
- `DELETE /users/2`: simulates user deletion

All tests hit the public mock API [https://reqres.in](https://reqres.in) and check for:
- Status code validation
- Response structure and fields
- Common failure scenarios

---

#### 🔧 Fixtures

`conftest.py` defines shared test configuration like `base_url`:

```python
import pytest

@pytest.fixture
def base_url():
    return "https://reqres.in/api"
```

This allows injecting `base_url` into all test functions cleanly.

---

#### ℹ️ Notes

- No real data is created or modified — the API is a mock server for learning purposes.
- If tests fail with `401 Unauthorized`, check that you're hitting the correct `base_url` and that no proxy/VPN is interfering.
- You can swap out `reqres.in` with any other mock API (e.g. `jsonplaceholder.typicode.com`) using the same structure.

---
