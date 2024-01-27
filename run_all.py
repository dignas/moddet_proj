import initial_conditions as ic
from variants import model_set, shape_set
from params import ht, hxy

import numpy as np
import matplotlib.pyplot as plt
from math import floor


tmax = 200
evolution_plots_arange = (2, 3)
evolution_plots_no = np.prod(evolution_plots_arange)
plot_at = np.arange(0, tmax + 1, floor(tmax / (evolution_plots_no - 1)))


def sim_and_plot(model, v_init, w_init, ax=None):
    if ax is not None:
        _, py = np.shape(ax)
        px_at, py_at = 0, 0

    v = np.array(v_init, copy=True)
    w = np.array(w_init, copy=True)
    for step in range(tmax + 1):
        v, w = model(v, w, ht, hxy)

        if ax is not None and step in plot_at:
            ax[px_at, py_at].imshow(v, cmap="autumn")
            ax[px_at, py_at].set_title(f"t={round(step/100, 1)}yrs")
            py_at += 1
            if py_at >= py:
                py_at = 0
                px_at += 1

    return v    


if __name__ == "__main__":
    np.random.seed(3)
    
    for n, m in shape_set:
        rand = ic.init_random(n, m)
        full = ic.init_const(n, m, 1) + 0.1 * ic.init_random(n, m)
        norm = ic.init_normal(n, m) + 0.1 * ic.init_random(n, m)
        trig = 0.2 * ic.init_trigonometric(n, m) + 0.1 * ic.init_random(n, m)

        w_init = ic.init_const(n, m, 0)

        for id_model, model in enumerate(model_set):

            for idx, v_init in enumerate([rand, full, norm, trig]):
                
                _, ax = plt.subplots(*evolution_plots_arange)
                sim_and_plot(model, v_init, w_init, ax)
                plt.savefig(f"plots/shape_{n}_{m}_model_{id_model}_init_{idx}.png", dpi=300)
