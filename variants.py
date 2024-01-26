from model import fitzhugh_nagumo_model


model_set = [
    fitzhugh_nagumo_model(2.8e-4, 5e-3, 0.1, -5e-3),
    fitzhugh_nagumo_model(1e-3, 5e-3, 0.1, -5e-3),
    fitzhugh_nagumo_model(5e-3, 5e-3, 0.1, -5e-3),
    fitzhugh_nagumo_model(2.8e-4, 5e-1, 0.1, -5e-3),
    fitzhugh_nagumo_model(2.8e-2, 5e-2, 0.1, -5e-3),
]


shape_set = [
    (20, 100),
    (30, 70),
    (50, 50),
]
