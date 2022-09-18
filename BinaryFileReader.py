import os
import uuid
from struct import pack as struct_pack, unpack_from as struct_unpack_from

import numpy as np

from config import configs

def readBinaryData():
    DT_ENERGY_DISTRIBUTION = np.dtype(
        {
            "names": [
                "va"
            ],
            "formats": [
                # Voltage
                np.float64
            ],
        }
    )

    file_name = "output.dat"
    return(np.fromfile(file_name))