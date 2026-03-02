\# Testing Strategy — Quick-Calc



\## What I tested

\- Unit tests for the calculation logic: addition, subtraction, multiplication, and division.

\- Edge cases: division by zero, negative numbers, decimal arithmetic, and very large numbers.

\- Integration tests that verify the CLI input layer works together with the core calculation logic:

&nbsp; - A full user flow such as `5 + 3 =`

&nbsp; - Reset behavior using `C`



\## What I did not test (and why)

\- Non-functional testing (performance, scalability, security): the application is a small CLI calculator, so these concerns are out of scope for this assignment.

\- GUI testing: the project uses a CLI to keep the focus on logic and test quality.



\## Relation to Lecture Concepts



\### 1) Testing Pyramid

The suite follows the testing pyramid: most tests are unit tests (fast and isolated), and fewer tests are integration tests (slower and broader). This gives quick feedback while still verifying components work together.



\### 2) Black-box vs White-box Testing

\- Unit tests are closer to white-box testing because they directly test internal functions like `add()` and `divide()`.

\- Integration tests are black-box style because they run the calculator through the CLI and verify outputs without relying on internal implementation details.



\### 3) Functional vs Non-Functional Testing

\- Functional testing: verifying operations (+, -, \*, /) produce correct outputs and `C` resets to `0`.

\- Non-functional testing was intentionally not performed because performance/security is not required for a basic calculator.



\### 4) Regression Testing

This test suite can be re-run after future changes. If any existing behavior breaks (e.g., division rules or clear behavior), the tests will fail and catch regressions early.



\## Test Results Summary



| Test Name                  | Type        | Status |

|---------------------------|-------------|--------|

| test\_addition\_basic        | Unit        | Pass   |

| test\_subtraction\_basic     | Unit        | Pass   |

| test\_multiplication\_basic  | Unit        | Pass   |

| test\_division\_basic        | Unit        | Pass   |

| test\_division\_by\_zero      | Unit        | Pass   |

| test\_negative\_numbers      | Unit        | Pass   |

| test\_decimals              | Unit        | Pass   |

| test\_large\_numbers         | Unit        | Pass   |

| test\_user\_flow\_addition    | Integration | Pass   |

| test\_clear\_resets          | Integration | Pass   |

