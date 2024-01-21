import numpy.typing as npt
import numpy as np
from typing import Tuple

import math_util as mat


def fitzhugh_nagumo_model(a: float, b: float, tau: float, k: float):

    def time_step(v: npt.NDArray[np.float64], w: npt.NDArray[np.float64], ht: float, hxy: float) -> Tuple[npt.NDArray[np.float64], npt.NDArray[np.float64]]:

        n, m = np.shape(v)

        vn, wn = np.zeros_like(v), np.zeros_like(w)

        for i in range(1, n-1):
            for j in range(1, m-1):
                laplacian_indices = mat.get_laplace_indices(i, j)
                laplacian_v = mat.laplace_operator([v[ind_i, ind_j] for ind_i, ind_j in laplacian_indices], hxy)
                laplacian_w = mat.laplace_operator([w[ind_i, ind_j] for ind_i, ind_j in laplacian_indices], hxy)

                vn[i, j] = v[i, j] + ht * (a * laplacian_v + v[i, j] - v[i, j]**3 - w[i, j] + k)
                wn[i, j] = w[i, j] + ht * (b * laplacian_w + v[i, j] - w[i, j]) / tau

                vn = mat.neumann_condition(vn)
                wn = mat.neumann_condition(wn)

        return vn, wn

    return time_step


common_model = fitzhugh_nagumo_model(2.8e-4, 5e-3, 0.1, -5e-3)
