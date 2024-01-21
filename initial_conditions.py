from math_util import neumann_condition

import numpy as np
import numpy.typing as npt


def init_random(n: int, m: int) -> npt.NDArray[np.float64]:
	return neumann_condition(np.random.uniform(size=(n, m)))


def init_const(n: int, m: int, x: np.float64) -> npt.NDArray[np.float64]:
	return np.full((n, m), x)


def init_normal(n: int, m: int) -> npt.NDArray[np.float64]:
	
	def norm_2d_pdf(x: np.float64, y: np.float64) -> np.float64:
		return 0.5 / np.pi * np.exp(-0.5 * (x**2 + y**2))

	xs = np.linspace(-3, 3, n)
	ys = np.linspace(-3, 3, m)

	result = np.zeros((n, m))

	for i in range(1, n - 1):
		for j in range(1, m - 1):
			result[i, j] = norm_2d_pdf(xs[i], ys[j])

	return neumann_condition(result)
