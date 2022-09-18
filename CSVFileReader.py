import csv
from config import configs

def readCSVData():     
    __filename = configs.CSV_FILE_NAME

    with open(__filename) as csv_file:
        return(csv.reader(csv_file, delimiter = ','))
        # csv_reader = csv.reader(csv_file, delimiter = ',')
        # line_count = 0
        # for row in csv_reader:
        #     if line_count == 0:
        #         print(f'Column names are {", ".join(row)}')
        #         line_count += 1
        #     else:
        #         print(row)
        #         # print(f'\t{row[0]} works in the {row[1]} department, and was born in {row[2]}.')
        #         line_count += 1
        # print(f'Processed {line_count} lines.')