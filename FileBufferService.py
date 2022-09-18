from io import BufferedWriter
import os
from struct import pack as struct_pack
from datetime import datetime
from config import configs

from pytz import timezone

class FileBufferService:
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
                self.file_buffer.write(struct_pack("d", data_point))

        except Exception as e:
            print(e)
            raise Exception("Couldn't write on file, exiting service") from e

    def openNewFile(self, client_filename: str = ""):
        self.instantiation_datetime = datetime.now().astimezone(self.__timezone)
        self.inst_datetime_string = self.instantiation_datetime.strftime(self.__filename_format)

        filename = f"{str(self.inst_datetime_string)}-{client_filename}.dat"
        self.file_path = os.path.join(self.__dirname, filename)
        self.file_buffer = open(self.file_path, "ab", buffering=2**20)

    def closeCurrentFile(self):
        self.file_buffer.flush()
        self.file_buffer.close()