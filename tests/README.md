# Test Setup and Execution

## Prerequisites

- Python 3.x installed

## 1. Create the virtual environment (venv)

From the project root, create the virtual environment:

```bash
python3 -m venv venv
```

## 2. Activate the virtual environment

**macOS/Linux:**
```bash
source venv/bin/activate
```

**Windows:**
```bash
venv\Scripts\activate
```

## 3. Install dependencies

With the venv activated, install the requirements:

```bash
pip install -r requirements.txt
```

## 4. Install Playwright browsers

```bash
playwright install
```

## 5. Run the tests

```bash
pytest
```

### Useful options

Run with detailed output:
```bash
pytest -v
```

Run a specific file:
```bash
pytest tests/playwright/tests/test_authentication.py -v
```

## 6. Deactivate the virtual environment

When you are done:
```bash
deactivate
```
