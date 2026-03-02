# Testing Strategy — Quick-Calc

## What I tested
- Unit tests for the calculation logic: addition, subtraction, multiplication, and division.
- Edge cases: division by zero, negative numbers, decimal arithmetic, and very large numbers.
- Integration tests that verify the CLI input layer works together with the core calculation logic:
  - A full user flow such as `5 + 3 =`
  - Reset behavior using `C`

## What I did not test (and why)
- Non-functional testing (performance, scalability, security): the application is a small CLI calculator, so these concerns are out of scope for this assignment.
- GUI testing: the project uses a CLI to keep the focus on logic and test quality.

## Relation to Lecture Concepts

### 1) Testing Pyramid
The suite follows the testing pyramid: most tests are unit tests (fast and isolated), and fewer tests are integration tests (slower and broader). This gives quick feedback while still verifying components work together.

### 2) Black-box vs White-box Testing
- Unit tests are closer to white-box testing because they directly test internal functions like `add()` and `divide()`.
- Integration tests are black-box style because they run the calculator through the CLI and verify outputs without relying on internal implementation details.

### 3) Functional vs Non-Functional Testing
- Functional testing: verifying operations (+, -, *, /) produce correct outputs and `C` resets to `0`.
- Non-functional testing was intentionally not performed because performance/security is not required for a basic calculator.

### 4) Regression Testing
This test suite can be re-run after future changes. If any existing behavior breaks (e.g., division rules or clear behavior), the tests will fail and catch regressions early.

## Test Results Summary

| Test Name                       | Type        | Status |
|--------------------------------|-------------|--------|
| test_addition_basic            | Unit        | Pass   |
| test_subtraction_basic         | Unit        | Pass   |
| test_multiplication_basic      | Unit        | Pass   |
| test_division_basic            | Unit        | Pass   |
| test_division_by_zero          | Unit        | Pass   |
| test_negative_numbers          | Unit        | Pass   |
| test_decimals                  | Unit        | Pass   |
| test_large_numbers             | Unit        | Pass   |
| test_user_flow_addition        | Integration | Pass   |
| test_clear_resets              | Integration | Pass   |
