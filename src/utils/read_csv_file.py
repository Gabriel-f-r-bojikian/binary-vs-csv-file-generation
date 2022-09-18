from numpy import genfromtxt

from configs import DT_ENERGY_DISTRIBUTION


def read_csv_file(filename: str):
    return genfromtxt(filename, dtype=DT_ENERGY_DISTRIBUTION, delimiter=",")
