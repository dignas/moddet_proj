from run_all import sim_and_plot
from variants import model_set, shape_set
import initial_conditions as ic

import numpy as np
import matplotlib.pyplot as plt


if __name__ == "__main__":
	np.random.seed(3)
	n, m = shape_set[2]
	models_blur = [model_set[0], model_set[1], model_set[2], model_set[4]]

	v_init = ic.init_random(n, m)
	w_init = ic.init_const(n, m, 0)

	_, ax = plt.subplots(2, 2)
	ax = ax.flatten()
	for idx, model in enumerate(models_blur):
		v = sim_and_plot(model, v_init, w_init)
		ax[idx].imshow(v, cmap="autumn")

	plt.savefig("plots/blur.png", dpi=300)

	models_dots = [model_set[1], model_set[4]]
	
	v_init_rand = ic.init_random(n, m)
	v_init_const = ic.init_const(n, m, 1) + 0.1 * ic.init_random(n, m)

	v_init_dots = [v_init_rand, v_init_const]

	_, ax = plt.subplots(2, 2)
	for idy, model in enumerate(models_dots):
		for idx, v_init in enumerate(v_init_dots):
			v = sim_and_plot(model, v_init, w_init)
			ax[idx, idy].imshow(v, cmap="autumn")

	plt.savefig("plots/dots.png", dpi=300)
