from dataclasses import dataclass
import timeit
from os import remove as remove_file, listdir
from os.path import join

# import numpy as np
from scipy import stats

from generators import (
    generate_senoidal_array,
    generate_inf_array,
    generate_nan_array,
    generate_zero_array,
)
from services import FileBufferService, FileCSVService
from utils import read_binary_file, read_csv_file
from configs import DATA_DIR, MICROSSECONDS


def clean_up():
    for filepath in listdir(DATA_DIR):
        if filepath != ".gitkeep":
            remove_file(join(DATA_DIR, filepath))


def print_scipy_stats(title: str, scipy_stats):
    scipy_stats_nobs = scipy_stats.nobs
    scipy_stats_min_us = scipy_stats.minmax[0] * MICROSSECONDS
    scipy_stats_max_us = scipy_stats.minmax[-1] * MICROSSECONDS
    scipy_stats_mean_us = scipy_stats.mean * MICROSSECONDS
    scipy_stats_variance_us = scipy_stats.variance * MICROSSECONDS
    scipy_stats_skewness = scipy_stats.skewness
    scipy_stats_kurtosis = scipy_stats.kurtosis
    to_print = (
        f"{title}"
        f"\n\tnobs={scipy_stats_nobs}"
        f"\n\tmin(us)={scipy_stats_min_us}"
        f"\n\tmax(us)={scipy_stats_max_us}"
        f"\n\tmean(us)={scipy_stats_mean_us}"
        f"\n\tvariance(us)={scipy_stats_variance_us}"
        f"\n\tskewness={scipy_stats_skewness}"
        f"\n\tkurtosis={scipy_stats_kurtosis}"
    )
    print(to_print)


def print_scipy_stats_ratio(title: str, csv_scipy_stats, bin_scipy_stats):
    csv_nobs = csv_scipy_stats.nobs
    csv_min_us = csv_scipy_stats.minmax[0] * MICROSSECONDS
    csv_max_us = csv_scipy_stats.minmax[-1] * MICROSSECONDS
    csv_mean_us = csv_scipy_stats.mean * MICROSSECONDS
    csv_variance_us = csv_scipy_stats.variance * MICROSSECONDS
    csv_skewness = csv_scipy_stats.skewness
    csv_kurtosis = csv_scipy_stats.kurtosis

    bin_nobs = bin_scipy_stats.nobs
    bin_min_us = bin_scipy_stats.minmax[0] * MICROSSECONDS
    bin_max_us = bin_scipy_stats.minmax[-1] * MICROSSECONDS
    bin_mean_us = bin_scipy_stats.mean * MICROSSECONDS
    bin_variance_us = bin_scipy_stats.variance * MICROSSECONDS
    bin_skewness = bin_scipy_stats.skewness
    bin_kurtosis = bin_scipy_stats.kurtosis

    ratio_nobs = csv_nobs / bin_nobs
    ratio_min = csv_min_us / bin_min_us
    ratio_max = csv_max_us / bin_max_us
    ratio_mean = csv_mean_us / bin_mean_us
    ratio_variance = csv_variance_us / bin_variance_us
    ratio_skewness = csv_skewness / bin_skewness
    ratio_kurtosis = csv_kurtosis / bin_kurtosis

    to_print = (
        f"{title}"
        f"\n\tnobs={ratio_nobs}"
        f"\n\tmin={ratio_min}"
        f"\n\tmax={ratio_max}"
        f"\n\tmean={ratio_mean}"
        f"\n\tvariance={ratio_variance}"
        f"\n\tskewness={ratio_skewness}"
        f"\n\tkurtosis={ratio_kurtosis}"
    )
    print(to_print)


@dataclass
class TableStats:
    test_title: str
    sample_size: int
    min: float
    p1: float
    p10: float
    p50: float
    p90: float
    p99: float
    p99_9: float
    p99_99: float
    max: float

    def __str__(self) -> str:
        return (
            f"{self.test_title} | "
            f"{self.sample_size} | "
            f"{self.min} | "
            f"{self.p1} | "
            f"{self.p10} | "
            f"{self.p50} | "
            f"{self.p90} | "
            f"{self.p99} | "
            f"{self.p99_9} | "
            f"{self.p99_99} | "
            f"{self.max}"
        )


def print_table_stats(data: TableStats):
    """
    test | sample size | min | p10 | p50 | p99 | p99.9 | p99.99 | max
    """
    print(str(data))


def test_read_senoidal_data_points_speed():
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

    def _test_reading_binary_file():
        read_binary_file(bin_file_service.file_path)

    # Binary file test
    _test_writing_binary_file()
    timer = timeit.Timer(_test_reading_binary_file)
    n = 10
    results = [timer.timeit(n) / n for _ in range(100)]
    # which_percentiles = [0, 1, 10, 50, 90, 99, 99.9, 99.99, 100]
    # percentiles = np.percentile(results, which_percentiles)
    # bin_table_stats = TableStats(
    #     "senoidal binary file",
    #     len(results),
    #     percentiles[0],  # 0
    #     percentiles[1],  # 1
    #     percentiles[2],  # 10
    #     percentiles[3],  # 50
    #     percentiles[4],  # 90
    #     percentiles[5],  # 99
    #     percentiles[6],  # 99.9
    #     percentiles[7],  # 99.99
    #     percentiles[8],  # 100
    # )
    # print_table_stats(bin_table_stats)
    bin_stats = stats.describe(results)
    print_scipy_stats("senoidal binary file", bin_stats)

    # CSV file setup
    csv_file_service = FileCSVService()

    def _test_writing_csv_file():
        csv_file_service.open_new_file(client_filename)
        csv_file_service.write(data)
        csv_file_service.close_current_file()

    def _test_reading_csv_file():
        read_csv_file(csv_file_service.file_path)

    # CSV file test
    _test_writing_csv_file()
    timer = timeit.Timer(_test_reading_csv_file)
    n = 10
    results = [timer.timeit(n) / n for _ in range(100)]
    csv_stats = stats.describe(results)
    print_scipy_stats("senoidal csv file", csv_stats)

    # Ratio
    print_scipy_stats_ratio("senoidal file ratio(csv/bin)", csv_stats, bin_stats)

    # Clean Up
    clean_up()
    print("\n--------------------------------------------------------\n")


def test_read_noisy_senoidal_data_points_speed():
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

    def _test_reading_binary_file():
        read_binary_file(bin_file_service.file_path)

    # Binary file test
    _test_writing_binary_file()
    timer = timeit.Timer(_test_reading_binary_file)
    n = 10
    results = [timer.timeit(n) / n for _ in range(100)]
    bin_stats = stats.describe(results)
    print_scipy_stats("noisy senoidal binary file", bin_stats)

    # CSV file setup
    csv_file_service = FileCSVService()

    def _test_writing_csv_file():
        csv_file_service.open_new_file(client_filename)
        csv_file_service.write(data)
        csv_file_service.close_current_file()

    def _test_reading_csv_file():
        read_csv_file(csv_file_service.file_path)

    # CSV file test
    _test_writing_csv_file()
    timer = timeit.Timer(_test_reading_csv_file)
    n = 10
    results = [timer.timeit(n) / n for _ in range(100)]
    csv_stats = stats.describe(results)
    print_scipy_stats("noisy senoidal csv file", csv_stats)

    # Ratio
    print_scipy_stats_ratio("noisy senoidal file ratio(csv/bin)", csv_stats, bin_stats)

    # Clean Up
    clean_up()
    print("\n--------------------------------------------------------\n")


def test_read_infinity_data_point_type_speed():
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

    def _test_reading_binary_file():
        read_binary_file(bin_file_service.file_path)

    # Binary file test
    _test_writing_binary_file()
    timer = timeit.Timer(_test_reading_binary_file)
    n = 10
    results = [timer.timeit(n) / n for _ in range(100)]
    bin_stats = stats.describe(results)
    print_scipy_stats("infinity data type binary file", bin_stats)

    # CSV file setup
    csv_file_service = FileCSVService()

    def _test_writing_csv_file():
        csv_file_service.open_new_file(client_filename)
        csv_file_service.write(data)
        csv_file_service.close_current_file()

    def _test_reading_csv_file():
        read_csv_file(csv_file_service.file_path)

    # CSV file test
    _test_writing_csv_file()
    timer = timeit.Timer(_test_reading_csv_file)
    n = 10
    results = [timer.timeit(n) / n for _ in range(100)]
    csv_stats = stats.describe(results)
    print_scipy_stats("infinity data type binary file", csv_stats)

    # Ratio
    print_scipy_stats_ratio(
        "infinity data type file ratio(csv/bin)", csv_stats, bin_stats
    )

    # Clean Up
    clean_up()
    print("\n--------------------------------------------------------\n")


def test_read_negative_infinity_data_point_type_speed():
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

    def _test_reading_binary_file():
        read_binary_file(bin_file_service.file_path)

    # Binary file test
    _test_writing_binary_file()
    timer = timeit.Timer(_test_reading_binary_file)
    n = 10
    results = [timer.timeit(n) / n for _ in range(100)]
    bin_stats = stats.describe(results)
    print_scipy_stats("negative infinity data type binary file", bin_stats)

    # CSV file setup
    csv_file_service = FileCSVService()

    def _test_writing_csv_file():
        csv_file_service.open_new_file(client_filename)
        csv_file_service.write(data)
        csv_file_service.close_current_file()

    def _test_reading_csv_file():
        read_csv_file(csv_file_service.file_path)

    # CSV file test
    _test_writing_csv_file()
    timer = timeit.Timer(_test_reading_csv_file)
    n = 10
    results = [timer.timeit(n) / n for _ in range(100)]
    csv_stats = stats.describe(results)
    print_scipy_stats("negative infinity data type csv file", csv_stats)

    # Ratio
    print_scipy_stats_ratio(
        "negative infinity data type file ratio(csv/bin)", csv_stats, bin_stats
    )

    # Clean Up
    clean_up()
    print("\n--------------------------------------------------------\n")


def test_read_nan_data_point_type_speed():
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

    def _test_reading_binary_file():
        read_binary_file(bin_file_service.file_path)

    # Binary file test
    _test_writing_binary_file()
    timer = timeit.Timer(_test_reading_binary_file)
    n = 10
    results = [timer.timeit(n) / n for _ in range(100)]
    bin_stats = stats.describe(results)
    print_scipy_stats("nan data type binary file", bin_stats)

    # CSV file setup
    csv_file_service = FileCSVService()

    def _test_writing_csv_file():
        csv_file_service.open_new_file(client_filename)
        csv_file_service.write(data)
        csv_file_service.close_current_file()

    def _test_reading_csv_file():
        read_csv_file(csv_file_service.file_path)

    # CSV file test
    _test_writing_csv_file()
    timer = timeit.Timer(_test_reading_csv_file)
    n = 10
    results = [timer.timeit(n) / n for _ in range(100)]
    csv_stats = stats.describe(results)
    print_scipy_stats("nan data type csv file", csv_stats)

    # Ratio
    print_scipy_stats_ratio("nan data type file ratio(csv/bin)", csv_stats, bin_stats)

    # Clean Up
    clean_up()
    print("\n--------------------------------------------------------\n")


def test_read_zero_data_point_type_speed():
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

    def _test_reading_binary_file():
        read_binary_file(bin_file_service.file_path)

    # Binary file test
    _test_writing_binary_file()
    timer = timeit.Timer(_test_reading_binary_file)
    n = 10
    results = [timer.timeit(n) / n for _ in range(100)]
    bin_stats = stats.describe(results)
    print_scipy_stats("zero data type binary file", bin_stats)

    # CSV file setup
    csv_file_service = FileCSVService()

    def _test_writing_csv_file():
        csv_file_service.open_new_file(client_filename)
        csv_file_service.write(data)
        csv_file_service.close_current_file()

    def _test_reading_csv_file():
        read_csv_file(csv_file_service.file_path)

    # CSV file test
    _test_writing_csv_file()
    timer = timeit.Timer(_test_reading_csv_file)
    n = 10
    results = [timer.timeit(n) / n for _ in range(100)]
    csv_stats = stats.describe(results)
    print_scipy_stats("zero data type csv file", csv_stats)

    # Ratio
    print_scipy_stats_ratio("zero data type file ratio(csv/bin)", csv_stats, bin_stats)

    # Clean Up
    clean_up()
    print("\n--------------------------------------------------------\n")
