# Deterministic modelling – project
Modelling pigment distribution in animal skin

Using Fitzhugh-Nagumo model we're simulating how patterns on animal skin are created.

Different shapes and sizes of the animal will be tested and compared.

## How to use

To run simulations of all the possible variants of shape, model params and initial conditions, run

```bash
python3 run_all.py
```

This will take a couple of minutes and generate a lot of plots `shape_n_m_model_x_init_y.png`. They will be saved in folder `plots/`.

You can also generate two additional comparative plots that I used in the report with

```bash
python3 run_comparative.py
```

Parameters in those plots were arbitrarily selected to highlight the more interesting outcomes.
