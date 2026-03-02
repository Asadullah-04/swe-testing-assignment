# Quick-Calc (Software Testing Assignment)

Quick-Calc is a simple calculator application that supports addition, subtraction, multiplication, division (with safe handling of division by zero), and a clear (C) function to reset the calculator state. The focus of this project is code quality, testing quality, and professional Git/GitHub workflow.

## Setup Instructions (Windows)

### 1) Clone the repository
```bash
git clone https://github.com/Asadullah-04/swe-testing-assignment.git
cd swe-testing-assignment


### 2) Install dependencies
py -m pip install -r requirements.txt


## Run the Application
py -m quickcalc.cli "5 + 3 ="
py -m quickcalc.cli "10 / 0 ="

## How to Run Tests
py -m pytest
```
## Testing Framework Research (Pytest vs Unittest)

Python offers `unittest` (built into the standard library) and `pytest` (a popular third-party testing framework). `unittest` is class-based and available without extra installation, but it often requires more boilerplate code (test classes and setup/teardown) to express simple tests.

`pytest` is widely used because it supports plain `assert` statements, provides clearer failure output, and offers powerful features like fixtures and parameterization. This makes tests faster to write and easier to maintain as projects grow.

For this assignment, `pytest` was chosen because it reduces boilerplate and made it easy to build a strong unit test suite plus a small set of integration tests while keeping everything readable.