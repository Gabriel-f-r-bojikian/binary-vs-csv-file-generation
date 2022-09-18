from typing import List

import numpy as np


def generate_senoidal_array(
    array_size: int, has_harmonics: bool = False
) -> List[np.float64]:
    f = 60  # Frequency
    samples = 1
    n = array_size + 1
    omega = 2.0 * np.pi * f
    t = np.linspace(0, samples / f, n)[:-1]

    if has_harmonics:
        v_a = (
            np.sin(omega * t)
            + 0.5 * np.sin(3.0 * omega * t)
            + 0.2 * np.sin(5 * omega * t)
        )
    else:
        v_a = np.sin(omega * t)

    return v_a.astype(np.float64).tolist()


def generate_inf_array(array_size: int, negative_values=False) -> List[np.float64]:
    fill_value = np.inf if not negative_values else np.NINF
    return np.full((array_size,), fill_value).astype(np.float64).tolist()


def generate_nan_array(array_size: int) -> List[np.float64]:
    return np.full((array_size,), np.nan).astype(np.float64).tolist()


def generate_zero_array(array_size: int) -> List[np.float64]:
    return np.zeros((array_size,)).astype(np.float64).tolist()
