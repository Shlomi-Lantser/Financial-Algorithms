# Egalitarian Allocation

A Python implementation of the **Egalitarian Allocation** algorithm using [CVXPY](https://www.cvxpy.org/) and NumPy.
This package computes a fair division of divisible resources among agents by maximizing the minimum utility (egalitarian welfare).

---

## 📦 Features

* **Egalitarian Objective**: Maximizes the minimum utility across all agents.
* **Linear Constraints**: Ensures each resource is fully allocated.
* **Custom Valuations**: Supports any non-negative valuation matrix of shape $n\times m$.
* **Pretty Output**: Simple functions to display allocation and utilities in human-readable form.

---

## 🛠️ Requirements

* Python 3.7 or higher
* [NumPy](https://numpy.org/)
* [CVXPY](https://www.cvxpy.org/)

Install via pip:

```bash
pip install numpy cvxpy
```

---

## 🚀 Usage

Save the code to a file, e.g., `egalitarian_allocation.py`. Then run:

```bash
python egalitarian_allocation.py
```

The script will execute several predefined test matrices and print allocation details for each.

### Importing in your project

```python
from egalitarian_allocation import egalitarian_allocation, pretty_output

# Define a valuation matrix (agents × resources)
matrix = [
    [81, 19, 1],
    [70,  1,29]
]

allocations, utilities, z = egalitarian_allocation(matrix)
pretty_output(allocations)
print(f"Minimum utility z = {z:.2f}")
```

---

## 🔎 Function Reference

### `egalitarian_allocation(matrix: list[list[float]]) -> tuple[np.ndarray, np.ndarray, float]`

* **matrix**: A 2D list or array of non-negative floats representing valuations.
* **Returns**:

  * **allocations** (`n×m` array): Fraction of each resource allocated to each agent.
  * **utilities** (`n`-vector): Utility of each agent.
  * **z** (`float`): The maximized minimum utility.

### `pretty_output(allocation: np.ndarray) -> None`

Prints a readable summary of the allocation.

### `pretty_print_matrix(V: list[list[float]]) -> None`

Prints the valuation matrix row by row.

---

## 📄 Examples

```
From_Example Matrix:
[81, 19, 1]
[70, 1, 29]
Agent #1 gets 0.53 of resource #1, 1.00 of resource #2, and 0.00 of resource #3.
Agent #2 gets 0.47 of resource #1, 0.00 of resource #2, and 1.00 of resource #3.

Symmetric Matrix:
[10, 10, 10]
[10, 10, 10]
[10, 10, 10]
Agent #1 gets 0.33 of resource #1, 0.33 of resource #2, and 0.33 of resource #3.
Agent #2 gets 0.33 of resource #1, 0.33 of resource #2, and 0.33 of resource #3.
Agent #3 gets 0.33 of resource #1, 0.33 of resource #2, and 0.33 of resource #3.

Diverse Interests Matrix:
[8, 1, 1]
[1, 8, 1]
[1, 1, 8]
Agent #1 gets 1.00 of resource #1, 0.00 of resource #2, and 0.00 of resource #3.
Agent #2 gets 0.00 of resource #1, 1.00 of resource #2, and 0.00 of resource #3.
Agent #3 gets 0.00 of resource #1, 0.00 of resource #2, and 1.00 of resource #3.

One Dominant Agent Matrix:
[100, 80, 60]
[1, 1, 1]
[2, 2, 2]
Agent #1 gets 0.02 of resource #1, 0.00 of resource #2, and 0.00 of resource #3.
Agent #2 gets 0.65 of resource #1, 0.67 of resource #2, and 0.67 of resource #3.
Agent #3 gets 0.33 of resource #1, 0.33 of resource #2, and 0.33 of resource #3.

Sparse Preferences Matrix:
[5, 0, 0]
[0, 0, 5]
[0, 5, 0]
Agent #1 gets 1.00 of resource #1, 0.00 of resource #2, and 0.00 of resource #3.
Agent #2 gets 0.00 of resource #1, 0.00 of resource #2, and 1.00 of resource #3.
Agent #3 gets 0.00 of resource #1, 1.00 of resource #2, and 0.00 of resource #3.


---
