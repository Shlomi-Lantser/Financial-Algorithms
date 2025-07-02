import numpy as np
import cvxpy as cp

def egalitarian_allocation(matrix: list[list]):
    modified_matrix = np.asarray(matrix, dtype=float)

    if (modified_matrix < 0).any():
        raise ValueError("valuations must be non-negative")

    n, m = modified_matrix.shape

    X = cp.Variable((n, m), nonneg=True)

    utilities = cp.sum(cp.multiply(X, modified_matrix), axis=1)

    z = cp.Variable()

    # ───── אילוצים ─────────────────────────────────────────────
    constraints = [
        cp.sum(X, axis=0) == 1,   
        utilities >= z          
    ]

    problem = cp.Problem(cp.Maximize(z), constraints)
    problem.solve()    

    if problem.status != "optimal":
        raise RuntimeError(f"Solver ended with status {problem.status}")

    return X.value, utilities.value, z.value


def pretty_output(allocation: np.ndarray) -> None:
    n_agents, m_goods = allocation.shape

    for i in range(n_agents):
        row = allocation[i]

        parts = [f"{row[j]:.2f} of resource #{j+1}" for j in range(m_goods)]

        sentence = ", ".join(parts[:-1]) + f", and {parts[-1]}"
        print(f"Agent #{i+1} gets {sentence}.")



def pretty_print_matrix(V: list[list[float]]) -> None:
    for row in V:
        print(row)



if __name__ == "__main__":

    test_matrices = {
    "From_Example":[ 
        [81, 19, 1],
         [70,  1, 29]
    ],
    "Symmetric": [
        [10, 10, 10],
        [10, 10, 10],
        [10, 10, 10]
    ],
    "Diverse Interests": [
        [8, 1, 1],
        [1, 8, 1],
        [1, 1, 8]
    ],
    "One Dominant Agent": [
        [100, 80, 60],
        [1,   1,  1],
        [2,   2,  2]
    ],
    "Sparse Preferences": [
        [5, 0, 0],
        [0, 0, 5],
        [0, 5, 0]
    ]
}


for name, matrix in test_matrices.items():
    print(f"\n{name} Matrix:")
    pretty_print_matrix(matrix)
    alloc, util, z = egalitarian_allocation(matrix)
    pretty_output(alloc)

