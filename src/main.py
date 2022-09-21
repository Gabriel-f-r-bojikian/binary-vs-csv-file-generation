# import time
# import os

# import pandas as pd
# import matplotlib.pyplot as plt

# from generators import (
#     generate_senoidal_array,
#     generate_inf_array,
#     generate_nan_array,
#     generate_zero_array,
# )
# from services import FileBufferService, FileCSVService
# from utils import read_binary_file, read_csv_file


# bin_file_service = FileBufferService()
# csv_file_service = FileCSVService()

# amount_of_data_points = 1000
# data_arrays = {
#     "Senoidal": generate_senoidal_array(amount_of_data_points),
#     "Noisy_Senoidal": generate_senoidal_array(
#         amount_of_data_points, has_harmonics=True
#     ),
#     "Inf": generate_inf_array(amount_of_data_points),
#     "Negative Inf": generate_inf_array(amount_of_data_points, negative_values=True),
#     "NaN": generate_nan_array(amount_of_data_points),
#     "Zeros": generate_zero_array(amount_of_data_points),
# }

# columns = ["write time (us)", "read time (us)", "file size (bytes)"]
# aggregate_bin_experiment_results = pd.DataFrame(columns=columns)
# aggregate_csv_experiment_results = pd.DataFrame(columns=columns)


from tests import (
    # Write data
    test_write_senoidal_data_points_speed,
    test_write_noisy_senoidal_data_points_speed,
    test_write_infinity_data_point_type_speed,
    test_write_negative_infinity_data_point_type_speed,
    test_write_nan_data_point_type_speed,
    test_write_zero_data_point_type_speed,
    # File size
    test_file_size_in_senoidal_data_points,
    test_file_size_in_noisy_senoidal_data_points,
    test_file_size_in_infinity_data_type_data_points,
    test_file_size_in_negative_infinity_data_type_data_points,
    test_file_size_in_nan_data_type_data_points,
    test_file_size_in_zero_data_type_data_points,
    # Read data
    test_read_senoidal_data_points_speed,
    test_read_noisy_senoidal_data_points_speed,
    test_read_infinity_data_point_type_speed,
    test_read_negative_infinity_data_point_type_speed,
    test_read_nan_data_point_type_speed,
    test_read_zero_data_point_type_speed,
)


def main():
    print(
        (
            "######################\n"
            "## Write Speed Test ##\n"
            "######################\n"
        )
    )

    test_write_senoidal_data_points_speed()
    test_write_noisy_senoidal_data_points_speed()
    test_write_infinity_data_point_type_speed()
    test_write_negative_infinity_data_point_type_speed()
    test_write_nan_data_point_type_speed()
    test_write_zero_data_point_type_speed()

    print(
        ("\n####################\n" "## File Size Test ##\n" "####################\n")
    )

    test_file_size_in_senoidal_data_points()
    test_file_size_in_noisy_senoidal_data_points()
    test_file_size_in_infinity_data_type_data_points()
    test_file_size_in_negative_infinity_data_type_data_points()
    test_file_size_in_nan_data_type_data_points()
    test_file_size_in_zero_data_type_data_points()

    print(
        (
            "\n#####################\n"
            "## Read Speed Test ##\n"
            "#####################\n"
        )
    )

    test_read_senoidal_data_points_speed()
    test_read_noisy_senoidal_data_points_speed()
    test_read_infinity_data_point_type_speed()
    test_read_negative_infinity_data_point_type_speed()
    test_read_nan_data_point_type_speed()
    test_read_zero_data_point_type_speed()


if __name__ == "__main__":
    main()
    # for data_field in data_arrays:
    #     # Write bin file
    #     bin_write_start = time.time()
    #     bin_file_service.openNewFile(data_field)
    #     bin_file_service.write(data_arrays[data_field])
    #     bin_file_service.closeCurrentFile()
    #     bin_write_end = time.time()

    #     # Read bin file
    #     bin_read_start = time.time()
    #     bin_data = readBinaryData()
    #     bin_read_end = time.time()

    #     # Save results to pandas dataframe
    #     bin_write_time = (bin_write_end - bin_write_start) * 10**6  # ns
    #     bin_read_time = (bin_read_end - bin_read_start) * 10**6  # ns
    #     bin_file_size = os.path.getsize(configs.BIN_FILE_NAME)  # bytes
    #     bin_experiment_results = pd.DataFrame(
    #         [[bin_write_time, bin_read_time, bin_file_size]],
    #         columns=columns,
    #         index=[data_field],
    #     )

    #     aggregate_bin_experiment_results = aggregate_bin_experiment_results.append(
    #         bin_experiment_results
    #     )

    #     # Write CSV file
    #     csv_write_start = time.time()
    #     csv_file_service.openNewFile(data_field)
    #     csv_file_service.write(data_arrays[data_field])
    #     csv_file_service.closeCurrentFile()
    #     csv_write_end = time.time()

    #     # Read CSV file
    #     csv_read_start = time.time()
    #     CSV_data = readCSVData()
    #     csv_read_end = time.time()

    #     # Save result to pandas dataframe
    #     csv_write_time = (csv_write_end - csv_write_start) * 10**6  # us
    #     csv_read_time = (csv_read_end - csv_read_start) * 10**6  # us
    #     csv_file_size = os.path.getsize(configs.CSV_FILE_NAME)  # bytes
    #     csv_experiment_results = pd.DataFrame(
    #         [[csv_write_time, csv_read_time, csv_file_size]],
    #         columns=columns,
    #         index=[data_field],
    #     )
    #     aggregate_csv_experiment_results = aggregate_csv_experiment_results.append(
    #         csv_experiment_results
    #     )

    # print("\n\n")
    # print("Datasets size: " + str(amount_of_data_points))
    # print("\n\n")
    # print("BIN data:")
    # print(aggregate_bin_experiment_results)
    # print("\n\n")
    # print("CSV data:")
    # print(aggregate_csv_experiment_results)

    # # Running some statistics
    # indexes = aggregate_bin_experiment_results["write time (us)"].index
    # read_time_diff = (
    #     aggregate_bin_experiment_results["read time (us)"]
    #     - aggregate_csv_experiment_results["read time (us)"]
    # )

    # ## Write Time
    # fig_write_time = plt.figure()
    # write_time_diff = (
    #     aggregate_bin_experiment_results["write time (us)"]
    #     - aggregate_csv_experiment_results["write time (us)"]
    # )
    # write_time_diff.plot(
    #     kind="bar", color=(write_time_diff > 0).map({True: "r", False: "g"})
    # )
    # plt.xlabel("Dataset")
    # plt.ylabel("Tempo [μs]")
    # plt.title("Tempo de escrita: Binário - CSV")
    # plt.show()

    # ## Read Time
    # fig_read_time = plt.figure()
    # read_time_diff = (
    #     aggregate_bin_experiment_results["read time (us)"]
    #     - aggregate_csv_experiment_results["read time (us)"]
    # )
    # read_time_diff.plot(
    #     kind="bar", color=(read_time_diff > 0).map({True: "g", False: "r"})
    # )
    # plt.xlabel("Dataset")
    # plt.ylabel("Tempo [μs]")
    # plt.title("Tempo de leitura: Binário - CSV")
    # plt.show()
