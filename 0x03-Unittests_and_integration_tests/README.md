#  0x03. Unittests and Integration Tests

##  Overview

This project focuses on the concepts and implementation of **unit testing** and **integration testing** in Python. Using the `unittest` framework, `mock`, and other testing patterns such as **parameterization**, **memoization**, and **fixtures**, this project helps solidify best practices for writing clean, maintainable, and testable backend code.

---

##  Learning Objectives

By the end of this project, you should be able to:

-  Differentiate between **unit tests** and **integration tests**
- Understand and use **mocking**, **patching**, and **fixtures**
-  Use `unittest`, `mock`, and `parameterized` libraries effectively
-  Structure tests to handle external API calls
-  Understand memoization and how to test memoized functions
-  Apply test coverage to functions, properties, and external requests

---



##  How to Run Tests

To execute all tests:

```bash
$ python3 -m unittest discover
````

Or run a specific test file:

```bash
$ python3 -m unittest test_utils.py
$ python3 -m unittest test_client.py
```

---

## Key Concepts Covered

###  Unit Testing

* Testing isolated function behavior with `unittest`
* Validating outputs for various input combinations
* Using `@parameterized.expand` to simplify repetitive test cases
* Handling exceptions with `assertRaises`

###  Integration Testing

* Testing end-to-end behavior of components
* Using fixtures to simulate API responses
* Setup/teardown using `setUpClass` / `tearDownClass`

###  Mocking

* Using `unittest.mock.patch()` to simulate network/database interactions
* Patching methods, properties, and classes
* Ensuring mocked methods are called the expected number of times

---

##  Dependencies

* Python 3.7+
* `unittest`
* `unittest.mock`
* `parameterized`

Install dependencies (optional):

```bash
pip install parameterized
```

---


##  Requirements

* Code must comply with **pycodestyle 2.5**
* All functions and classes are **type-annotated**
* Each module, class, and function contains **docstrings**
* Python version: **3.7**
* OS: **Ubuntu 18.04 LTS**

---

## Author & Credits

Project developed as part of the **ALX Backend Specialization**.

© 2025 ALX, All Rights Reserved.


