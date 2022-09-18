import timeit
from os import remove as remove_file, listdir
from os.path import join

from scipy import stats

from generators import (
    generate_senoidal_array,
    generate_inf_array,
    generate_nan_array,
    generate_zero_array,
)
from services import FileBufferService, FileCSVService
from configs import DATA_DIR


def clean_up():
    for filepath in listdir(DATA_DIR):
        if filepath != ".gitkeep":
            remove_file(join(DATA_DIR, filepath))


##############
# Speed Test #
##############


def test_write_senoidal_data_points_speed():
    # Clean Up
    clean_up()

    # Global setup
    amount_of_data_points = 1000
    client_filename = "senoidal_data_points"
    data = generate_senoidal_array(amount_of_data_points)

    # Binary file setup
    bin_file_service = FileBufferService()

    def _test_writing_binary_file():
        bin_file_service.open_new_file(client_filename)
        bin_file_service.write(data)
        bin_file_service.close_current_file()

    # Binary file test
    timer = timeit.Timer(_test_writing_binary_file)
    n = 10
    results = [timer.timeit(n) / n for _ in range(100)]
    print("senoidal binary file\n", stats.describe(results))

    # CSV file setup
    csv_file_service = FileCSVService()

    def _test_writing_csv_file():
        csv_file_service.open_new_file(client_filename)
        csv_file_service.write(data)
        csv_file_service.close_current_file()

    # CSV file test
    timer = timeit.Timer(_test_writing_csv_file)
    n = 10
    results = [timer.timeit(n) / n for _ in range(100)]
    print("senoidal csv file\n", stats.describe(results))

    # Clean Up
    clean_up()


def test_write_noisy_senoidal_data_points_speed():
    # Clean Up
    clean_up()

    # Global setup
    amount_of_data_points = 1000
    client_filename = "noisy_senoidal_data_points"
    data = generate_senoidal_array(amount_of_data_points, True)

    # Binary file setup
    bin_file_service = FileBufferService()

    def _test_writing_binary_file():
        bin_file_service.open_new_file(client_filename)
        bin_file_service.write(data)
        bin_file_service.close_current_file()

    # Binary file test
    timer = timeit.Timer(_test_writing_binary_file)
    n = 10
    results = [timer.timeit(n) / n for _ in range(100)]
    print("noisy senoidal binary file\n", stats.describe(results))

    # CSV file setup
    csv_file_service = FileCSVService()

    def _test_writing_csv_file():
        csv_file_service.open_new_file(client_filename)
        csv_file_service.write(data)
        csv_file_service.close_current_file()

    # CSV file test
    timer = timeit.Timer(_test_writing_csv_file)
    n = 10
    results = [timer.timeit(n) / n for _ in range(100)]
    print("noisy senoidal csv file\n", stats.describe(results))

    # Clean Up
    clean_up()


def test_write_infinity_data_point_type_speed():
    # Clean Up
    clean_up()

    # Global setup
    amount_of_data_points = 1000
    client_filename = "infinity_data_type_data_points"
    data = generate_inf_array(amount_of_data_points)

    # Binary file setup
    bin_file_service = FileBufferService()

    def _test_writing_binary_file():
        bin_file_service.open_new_file(client_filename)
        bin_file_service.write(data)
        bin_file_service.close_current_file()

    # Binary file test
    timer = timeit.Timer(_test_writing_binary_file)
    n = 10
    results = [timer.timeit(n) / n for _ in range(100)]
    print("infinity data type binary file\n", stats.describe(results))

    # CSV file setup
    csv_file_service = FileCSVService()

    def _test_writing_csv_file():
        csv_file_service.open_new_file(client_filename)
        csv_file_service.write(data)
        csv_file_service.close_current_file()

    # CSV file test
    timer = timeit.Timer(_test_writing_csv_file)
    n = 10
    results = [timer.timeit(n) / n for _ in range(100)]
    print("infinity data type csv file\n", stats.describe(results))

    # Clean Up
    clean_up()


def test_write_negative_infinity_data_point_type_speed():
    # Clean Up
    clean_up()

    # Global setup
    amount_of_data_points = 1000
    client_filename = "negative_infinity_data_type_data_points"
    data = generate_inf_array(amount_of_data_points, True)

    # Binary file setup
    bin_file_service = FileBufferService()

    def _test_writing_binary_file():
        bin_file_service.open_new_file(client_filename)
        bin_file_service.write(data)
        bin_file_service.close_current_file()

    # Binary file test
    timer = timeit.Timer(_test_writing_binary_file)
    n = 10
    results = [timer.timeit(n) / n for _ in range(100)]
    print("negative infinity data type binary file\n", stats.describe(results))

    # CSV file setup
    csv_file_service = FileCSVService()

    def _test_writing_csv_file():
        csv_file_service.open_new_file(client_filename)
        csv_file_service.write(data)
        csv_file_service.close_current_file()

    # CSV file test
    timer = timeit.Timer(_test_writing_csv_file)
    n = 10
    results = [timer.timeit(n) / n for _ in range(100)]
    print("negative infinity data type csv file\n", stats.describe(results))

    # Clean Up
    clean_up()


def test_write_nan_data_point_type_speed():
    # Clean Up
    clean_up()

    # Global setup
    amount_of_data_points = 1000
    client_filename = "nan_data_type_data_points"
    data = generate_nan_array(amount_of_data_points)

    # Binary file setup
    bin_file_service = FileBufferService()

    def _test_writing_binary_file():
        bin_file_service.open_new_file(client_filename)
        bin_file_service.write(data)
        bin_file_service.close_current_file()

    # Binary file test
    timer = timeit.Timer(_test_writing_binary_file)
    n = 10
    results = [timer.timeit(n) / n for _ in range(100)]
    print("nan data type binary file\n", stats.describe(results))

    # CSV file setup
    csv_file_service = FileCSVService()

    def _test_writing_csv_file():
        csv_file_service.open_new_file(client_filename)
        csv_file_service.write(data)
        csv_file_service.close_current_file()

    # CSV file test
    timer = timeit.Timer(_test_writing_csv_file)
    n = 10
    results = [timer.timeit(n) / n for _ in range(100)]
    print("nan data type csv file\n", stats.describe(results))

    # Clean Up
    clean_up()


def test_write_zero_data_point_type_speed():
    # Clean Up
    clean_up()

    # Global setup
    amount_of_data_points = 1000
    client_filename = "zero_data_points"
    data = generate_zero_array(amount_of_data_points)

    # Binary file setup
    bin_file_service = FileBufferService()

    def _test_writing_binary_file():
        bin_file_service.open_new_file(client_filename)
        bin_file_service.write(data)
        bin_file_service.close_current_file()

    # Binary file test
    timer = timeit.Timer(_test_writing_binary_file)
    n = 10
    results = [timer.timeit(n) / n for _ in range(100)]
    print("zero binary file\n", stats.describe(results))

    # CSV file setup
    csv_file_service = FileCSVService()

    def _test_writing_csv_file():
        csv_file_service.open_new_file(client_filename)
        csv_file_service.write(data)
        csv_file_service.close_current_file()

    # CSV file test
    timer = timeit.Timer(_test_writing_csv_file)
    n = 10
    results = [timer.timeit(n) / n for _ in range(100)]
    print("zero csv file\n", stats.describe(results))

    # Clean Up
    clean_up()
