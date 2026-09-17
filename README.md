# Python Beginner Tutorial: Step-by-Step Series

Welcome to your hands-on beginner Python tutorial repository! This repository is structured step-by-step so you can learn core Python concepts, write code, run verification tests, and track your progress with Git branches.

---

## Tutorial Roadmap Overview

1. **Step 1: Arithmetic & Conditional Logic** (`exercise_01.py`)
   - Variables, basic arithmetic operators (`*`, `+`), conditional statements (`if`/`else`), and return values.
2. **Step 2: Loops & State Tracking**
   - `for` loops, `range()`, tracking previous state / cumulative totals.
3. **Step 3: Strings & Indexing**
   - Zero-based indexing, slicing (`[start:stop:step]`), string manipulation.
4. **Step 4: Lists & Collections**
   - Creating, indexing, appending, removing, and iterating over lists.
5. **Step 5: Functions & Reusability**
   - Function arguments, default values, docstrings, and modular design.
6. **Step 6+: Dictionaries, File I/O, and OOP Basics**
   - Key-value data, reading/writing files, and introductory object-oriented programming.

---

## Step 1: Arithmetic Product and Conditional Logic

### Learning Objectives
- Define a Python function using `def`.
- Perform multiplication (`*`) and addition (`+`).
- Use an `if ... else` conditional statement to guide program logic.
- Return values from functions using `return`.

### Problem Statement
Write a function `calculate_product_or_sum(num1, num2)` that accepts two integer numbers:
- If `num1 * num2 <= 1000`, return their **product**.
- If `num1 * num2 > 1000`, return their **sum**.

### Test Cases
- Input: `num1 = 20, num2 = 30` -> Product is `600` (<= 1000) -> Output: `600`
- Input: `num1 = 40, num2 = 30` -> Product is `1200` (> 1000) -> Output: `70`

### Instructions to Complete Step 1
1. Switch to the `step-1` branch:
   ```bash
   git checkout step-1
   ```
2. Open `exercise_01.py` and replace `pass` with your implementation inside `calculate_product_or_sum`.
3. Run the script:
   ```bash
   python exercise_01.py
   ```
4. When all tests pass, commit and push your solution:
   ```bash
   git add exercise_01.py
   git commit -m "Complete Step 1: Arithmetic Product and Conditional Logic"
   git push origin step-1
   ```
