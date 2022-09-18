from io import BufferedWriter
import os
import csv
from datetime import datetime
from config import configs

from pytz import timezone

class FileCSVService:
    # Object properties
    file_path: str
    file_buffer: BufferedWriter
    # Private variables
    __dirname = configs.ROOT_DIR
    __filename_format: str = "%F"
    __timezone = timezone('America/Sao_Paulo')
    
    def __exit__(self):
        self.closeCurrentFile()
    
    def write(self, data_array):
        try:
            for data_point in data_array:
                self.writer.writerow( [data_point] )

        except Exception as e:
            raise Exception("Couldn't write on file, exiting service") from e

    def openNewFile(self, client_filename: str = ""):
        self.instantiation_datetime = datetime.now().astimezone(self.__timezone)
        self.inst_datetime_string = self.instantiation_datetime.strftime(self.__filename_format)

        filename = f"{str(self.inst_datetime_string)}-{client_filename}.csv"
        self.file_path = os.path.join(self.__dirname, filename)
        self.file_buffer = open(self.file_path, "w", buffering=2**20, encoding='UTF8', newline='')
        self.writer = csv.writer(self.file_buffer)

    def closeCurrentFile(self):
        self.file_buffer.flush()
        self.file_buffer.close()