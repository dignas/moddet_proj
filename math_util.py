import numpy.typing as npt
import numpy as np


def get_laplace_indices(i: int, j: int) -> list[float]:
    d = [[0, 0], [-1, 0], [1, 0], [0, -1], [0, 1]]
    return [[i + di, j + dj] for di, dj in d]


# f should be a list of function values:
#          in the cell [i, j] where Laplacian should be calculated and it's neighboring cells in the following order:
# f(i, j), f(i - 1, j), f(i + 1, j), f(i, j - 1), f(i, j + 1)
# function get_laplace_indices can be helpful in accessing those values in the matrix
def laplace_operator(f: list[float], h: float) -> float:
    dfx2 = (f[1] + f[2] - 2 * f[0]) / h**2
    dfy2 = (f[3] + f[4] - 2 * f[0]) / h**2
    return dfx2 + dfy2


def neumann_condition(matrix: npt.ArrayLike) -> npt.ArrayLike:

    n, m = np.shape(matrix)

    matrix[0, :] = matrix[1, :]
    matrix[n - 1, :] = matrix[n - 2, :]
    matrix[:, 0] = matrix[:, 1]
    matrix[:, n - 1] = matrix[:, n - 2]

    return matrix
