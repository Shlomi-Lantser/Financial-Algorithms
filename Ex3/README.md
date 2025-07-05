![image](https://github.com/user-attachments/assets/2ead113c-c23f-4c0a-9c10-d4b2797ee330)





# Weighted Competitive Equilibrium (Fisher Market)

A Python implementation of the **Budget-Weighted Competitive** algorithm using [CVXPY](https://www.cvxpy.org/) and NumPy.  It computes equilibrium allocations and prices for divisible goods given agents' valuations and budgets by maximizing the weighted Nash welfare objective.

---

## 📦 Features

* **Budget-Weighted Objective**: Maximizes $\sum_i b_i \log(u_i)$, where $b_i$ are budgets and $u_i$ utilities.
* **Market Clearing Prices**: Returns equilibrium prices (dual variables) satisfying supply constraints.
* **Flexible Valuations**: Supports any non-negative valuation matrix of size $n\times m$.
* **Pretty Print**: Displays allocations, prices, and utilities in a clean format.

---

## 🛠️ Requirements

* Python 3.7+
* [NumPy](https://numpy.org/)
* [CVXPY](https://www.cvxpy.org/)

Install via pip:

```bash
pip install numpy cvxpy
```

---

## 🚀 Usage

Save the code to a file, e.g., `weighted_ce.py`, then run:

```bash
python weighted_ce.py
```

This will execute predefined test cases and print for each:

* **Allocation (agents × goods)**
* **Prices**
* **Utilities**

### Importing in Your Project

```python
from weighted_ce import weighted_ce, pretty_eq

values = [
    [10, 0, 0],
    [0, 0, 10]
]
budgets = [50, 50]

alloc, prices, utils = weighted_ce(values, budgets)
pretty_eq("Opposite Interests", alloc, prices, utils)
```

---

## 🔎 Function Reference

### `weighted_ce(values: list[list[float]], budgets: list[float]) -> tuple[np.ndarray, np.ndarray, np.ndarray]`

* **values**: 2D list or array $n\times m$ of non-negative valuations.
* **budgets**: 1D list or array of positive budgets for each agent.
* **Returns**:

  * `allocations` (`n×m` array): Fraction of each good allocated to each agent.
  * `prices` (`m`-vector): Equilibrium prices for goods.
  * `utilities` (`n`-vector): Utilities (value sums) of each agent.

### `pretty_eq(title: str, alloc: np.ndarray, prices: np.ndarray, utils: np.ndarray) -> None`

Prints:

* A title
* The allocation matrix
* Prices vector
* Utilities vector

---

## 📄 Examples

```
Symmetric
Allocation (agents × goods):
[[0.5 0.5 0.5]
 [0.5 0.5 0.5]]
Prices : 33.3 33.3 33.3
Utilities: 15.0 15.0

Opposite
Allocation (agents × goods):
[[1.0 0.5 0.0]
 [0.0 0.5 1.0]]
Prices : 50.0 0.0 50.0
Utilities: 10.0 10.0

Unequal Budgets
Allocation (agents × goods):
[[0.7 1.0 1.0]
 [0.3 0.0 0.0]]
Prices : 33.3 33.3 33.3
Utilities: 13.5 3.0

Rich but Weird
Allocation (agents × goods):
[[1.0 1.0 0.0]
 [0.0 0.0 1.0]]
Prices : 20.0 10.0 70.0
Utilities: 15.0 1.0

Sparse Interests
Allocation (agents × goods):
[[1.0 0.0 0.0]
 [0.0 1.0 0.0]
 [0.0 0.0 1.0]]
Prices : 20.0 30.0 50.0
Utilities: 8.0 6.0 7.0

Strong Competition
Allocation (agents × goods):
[[0.5 0.0 0.0]
 [0.4 0.0 0.0]
 [0.1 1.0 1.0]]
Prices : 77.8 11.1 11.1
Utilities: 4.6 3.1 2.7
```

---



