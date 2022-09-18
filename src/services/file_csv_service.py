from typing import TextIO, List
import os
import csv
from datetime import datetime

import numpy as np
from pytz import timezone

from configs import DATA_DIR, ONE_MEGA_BYTE


class FileCSVService:
    # Object properties
    file_path: str
    file_buffer: TextIO
    current_file_name: str
    # Private variables
    __dirname = DATA_DIR
    __filename_format: str = "%F"
    __timezone = timezone("America/Sao_Paulo")

    def __exit__(self):
        self.close_current_file()

    def write(self, data_array: List[np.float64]):
        try:
            for data_point in data_array:
                self.writer.writerow([data_point])

        except Exception as e:
            print(e)
            raise Exception("Couldn't write on file, exiting service") from e

    def open_new_file(self, client_filename: str = ""):
        self.instantiation_datetime = datetime.now().astimezone(self.__timezone)
        self.inst_datetime_string = self.instantiation_datetime.strftime(
            self.__filename_format
        )

        if not client_filename:
            self.current_file_name = f"{self.inst_datetime_string}.csv"
        else:
            self.current_file_name = (
                f"{self.inst_datetime_string}-{client_filename}.csv"
            )
        self.file_path = os.path.join(self.__dirname, self.current_file_name)
        self.file_buffer = open(self.file_path, "w", buffering=ONE_MEGA_BYTE)
        self.writer = csv.writer(self.file_buffer)

    def close_current_file(self):
        self.file_buffer.flush()
        self.file_buffer.close()
