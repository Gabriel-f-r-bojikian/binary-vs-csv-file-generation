from typing import List

import numpy as np

def generate_senoidal_data(array_size: int, has_harmonics = False) -> List[np.float64]:
    # Arrays de tensões e correntes de fase, com harmônicas
    # n = 4001 # Numero de pontos
    f = 60  # Frequência
    f_nyquist = 6_000
    samples = 1
    # n = int(10 * np.ceil(f_nyquist / f))
    n = array_size + 1
    omega = 2.0 * np.pi * f
    t = np.linspace(0, samples / f, n)[:-1]

    if(has_harmonics):
        v_a = (
            np.sin(omega * t) + 0.5 * np.sin(3.0 * omega * t) + 0.2 * np.sin(5 * omega * t)
        )
    else:
        v_a = ( np.sin(omega * t))

    return v_a

def generate_Inf_array(array_size: int, negative_values = False) -> List[np.float64]:
    fill_value = np.inf if not negative_values else np.NINF
    return np.full((array_size,), fill_value)

def generate_NaN_array(array_size: int) -> List[np.float64]:
    return np.full((array_size,), np.nan)

def generate_Zero_array(array_size: int) -> List[np.float64]:
    return np.zeros((array_size,))