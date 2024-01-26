import initial_conditions as ic
from variants import model_set

import numpy as np
import matplotlib.pyplot as plt


if __name__ == "__main__":
    n, m = 20, 100

    ht = 0.01
    hxy = 0.05

    common_model = model_set[0]

    rand = ic.init_random(n, m)
    full = ic.init_const(n, m, 1) + 0.1 * ic.init_random(n, m)
    norm = ic.init_normal(n, m) + 0.1 * ic.init_random(n, m)
    trig = 0.2 * ic.init_trigonometric(n, m) + 0.1 * ic.init_random(n, m)

    w_rand = ic.init_const(n, m, 0)
    w_full = np.array(w_rand, copy=True)
    w_norm = np.array(w_rand, copy=True)
    w_trig = np.array(w_rand, copy=True)

    for step in range(200):
        rand, w_rand = common_model(rand, w_rand, ht, hxy)
        full, w_full = common_model(full, w_full, ht, hxy)
        norm, w_norm = common_model(norm, w_norm, ht, hxy)
        trig, w_trig = common_model(trig, w_trig, ht, hxy)

    _, ax = plt.subplots(2, 2)
    ax[0, 0].imshow(rand, cmap="autumn")
    ax[0, 1].imshow(full, cmap="autumn")
    ax[1, 0].imshow(norm, cmap="autumn")
    ax[1, 1].imshow(trig, cmap="autumn")

    plt.show()
