# ISM3232 Midterm: Seabreeze Inn

- **Name:** Ashley Marte
- **Version:** 1.0
- **Date:** October 25, 2026

## What This Program Does

This program calculates the cost of hotel stays at Seabreeze Inn based on the nightly rate and number of nights. It applies the correct discounts and cleaning fees, determines whether a credit check or welcome package is required, and prints a report summarizing all stays.

## Business Rules

1. The room cost is calculated by multiplying the nightly rate by the number of nights.
2. Stays shorter than four nights receive no standard discount. Stays of 4 to 13 nights receive a 6% discount, and stays of 14 nights or more receive an 18% discount.
3. Corporate guests receive at least a 6% discount, even if their stay is shorter than four nights.
4. A $40 cleaning fee is added when the discounted room cost is $300 or less.
5. A credit check is required when the total stay cost is $2,000 or more.
6. A welcome package is provided when a guest stays more than five nights and the total cost is at least $1,000.

## How to Run

Open a terminal in the project folder and run:

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python main.py
```

## How to Test

Activate the virtual environment, then run:

```bash
ruff check .
python -m pytest -v
```

I wrote 22 tests to check the business rules, calculations, boundary conditions, and report formatting.

## Files in This Repository

- `business_rules.py`: Contains the functions that calculate stay costs, discounts, fees, and guest benefits.
- `main.py`: Runs the program and prints the stay report.
- `commands.md`: Records the terminal commands and outputs used during the project.
- `README.md`: Explains the project, business rules, and how to run and test it.
- `requirements.txt`: Lists the Python packages required for the project.
- `.gitignore`: Excludes the virtual environment, Python cache folders, and compiled Python files from Git.
- `tests/__init__.py`: Identifies the tests folder as a Python package.
- `tests/test_business_rules.py`: Contains the automated tests for the business rule functions.

## AI Use Statement

I did not use AI on this exam.
