import numpy as np

from configs import DT_ENERGY_DISTRIBUTION


def read_binary_file(filename: str):
    return np.fromfile(filename, dtype=DT_ENERGY_DISTRIBUTION)
