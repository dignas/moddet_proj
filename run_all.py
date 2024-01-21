from model import common_model
import initial_conditions as ic
from model import common_model

import numpy as np
import matplotlib.pyplot as plt


if __name__ == "__main__":
    n, m = 20, 100

    ht = 0.1
    hxy = 0.05

    rand = ic.init_random(n, m)
    full = ic.init_const(n, m, 1) + 0.1 * ic.init_random(n, m)
    norm = ic.init_normal(n, m) + 0.1 * ic.init_random(n, m)

    w_rand = ic.init_const(n, m, 0)
    w_full = np.array(w_rand, copy=True)
    w_norm = np.array(w_rand, copy=True)

    for step in range(100):
        rand, w_rand = common_model(rand, w_rand, ht, hxy)
        full, w_full = common_model(full, w_full, ht, hxy)
        norm, w_norm = common_model(norm, w_norm, ht, hxy)

    _, ax = plt.subplots(2, 2)
    ax[0, 0].imshow(rand, cmap="autumn")
    ax[0, 1].imshow(full, cmap="autumn")
    ax[1, 0].imshow(norm, cmap="autumn")

    plt.show()
