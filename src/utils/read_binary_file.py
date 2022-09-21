from numpy import fromfile

from configs import DT_ENERGY_DISTRIBUTION


def read_binary_file(filename: str):
    return fromfile(filename, dtype=DT_ENERGY_DISTRIBUTION)
