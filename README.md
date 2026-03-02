# Quick-Calc (Software Testing Assignment)

Quick-Calc is a simple calculator application that supports addition, subtraction, multiplication, division (with safe handling of division by zero), and a clear (C) function to reset the calculator state. The focus of this project is code quality, testing quality, and professional Git/GitHub workflow.

## Setup Instructions (Windows)

### 1) Clone the repository
```bash
git clone https://github.com/Asadullah-04/swe-testing-assignment.git
cd swe-testing-assignment

py -m pip install -r requirements.txt

py -m quickcalc.cli "5 + 3 ="

py -m quickcalc.cli "10 / 0 ="
py -m pytest```