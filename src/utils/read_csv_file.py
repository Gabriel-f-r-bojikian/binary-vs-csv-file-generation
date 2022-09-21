from numpy import loadtxt

from configs import DT_ENERGY_DISTRIBUTION


def read_csv_file(filename: str):
    return loadtxt(filename, dtype=DT_ENERGY_DISTRIBUTION, delimiter=",")
