from os.path import dirname, abspath, join

import numpy as np


CURRENT_DIR = dirname(abspath(__file__))
SOURCE_DIR = dirname(CURRENT_DIR)
ROOT_DIR = dirname(SOURCE_DIR)
DATA_DIR = join(ROOT_DIR, "data")
ONE_MEGA_BYTE = 2**20
DT_ENERGY_DISTRIBUTION = np.dtype(
    {
        "names": ["va"],
        "formats": [
            # Voltage
            np.float64
        ],
    }
)
