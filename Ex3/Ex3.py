import numpy as np
import cvxpy as cp


def weighted_ce(values, budgets):
    values = np.asarray(values, float)      
    budgets = np.asarray(budgets, float)

    if (values < 0).any():
        raise ValueError("valuations must be non-negative")
    if (budgets <= 0).any():
        raise ValueError("budgets must be positive")

    n, m = values.shape


    X = cp.Variable((n, m), nonneg=True)            # הקצאה
    U = cp.sum(cp.multiply(values, X), axis=1)           # תועלות

    supply_con = cp.sum(X, axis=0) == 1


    obj = cp.Maximize(cp.sum(cp.multiply(budgets, cp.log(U))))

    prob = cp.Problem(obj, [supply_con])
    prob.solve()

    if prob.status != "optimal":
        raise RuntimeError(f"solver status {prob.status}")

    prices = supply_con.dual_value     # וקטור המחירים p_j ≥ 0
    return X.value, prices, U.value



def pretty_eq(title, alloc, prices, utils):

    fmt = lambda x: f"{x:.1f}"

    print(f"\n{title}")

    print("Allocation (agents × goods):")
    print(np.array2string(alloc,
                          formatter={"float_kind": fmt},
                          max_line_width=80))

    p_str = " ".join(fmt(p) for p in prices)
    print("Prices :", p_str)


    u_str = " ".join(fmt(u) for u in utils)
    print("Utilities:", u_str)

if __name__ == "__main__":
    test_cases = [
        ("Symmetric", [
            [10, 10, 10],
            [10, 10, 10]
        ], [50, 50]),

        ("Opposite", [
            [10, 0, 0],
            [0, 0, 10]
        ], [50, 50]),

        ("Unequal Budgets", [
            [5, 5, 5],
            [10, 1, 1]
        ], [90, 10]),

        ("Rich but Weird", [
            [10, 5, 5],
            [0, 0, 1]
        ], [30, 70]),

        ("Sparse Interests", [
            [8, 0, 0],
            [0, 6, 0],
            [0, 0, 7]
        ], [20, 30, 50]),

        ("Strong Competition", [
            [9, 1, 1],
            [8, 1, 1],
            [7, 1, 1]
        ], [40, 30, 30]),
    ]

    for name, V, w in test_cases:
        alloc, prices, utils = weighted_ce(V, w)
        pretty_eq(name, alloc, prices, utils)
