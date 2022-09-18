from os import remove as remove_file, listdir
from os.path import join
from os import stat as get_file_stats
import zipfile

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


def test_file_size_in_senoidal_data_points():
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
    _test_writing_binary_file()
    bin_file_stats = get_file_stats(bin_file_service.file_path)

    print(
        "senoidal binary file",
        f"\n\tFile size in bytes: {bin_file_stats.st_size}",
        f"\n\tNumber of 512-byte blocks: {bin_file_stats.st_blocks}",
    )

    # CSV file setup
    csv_file_service = FileCSVService()

    def _test_writing_csv_file():
        csv_file_service.open_new_file(client_filename)
        csv_file_service.write(data)
        csv_file_service.close_current_file()

    # CSV file test
    _test_writing_csv_file()
    csv_file_stats = get_file_stats(csv_file_service.file_path)

    print(
        "senoidal csv file",
        f"\n\tFile size in bytes: {csv_file_stats.st_size}",
        f"\n\tNumber of 512-byte blocks: {csv_file_stats.st_blocks}",
    )

    # Ratio
    size_ratio = float(csv_file_stats.st_size) / float(bin_file_stats.st_size)
    block_512_ratio = float(csv_file_stats.st_blocks) / float(bin_file_stats.st_blocks)
    print(
        "senoidal file ratio",
        f"\n\tRatio csv by binary: {size_ratio}",
        f"\n\tNumber of 512-byte blocks: {block_512_ratio}",
    )

    ################
    # Zipped stuff #
    ################
    # Global setup
    compress_level = 9

    # Binary file test
    bin_zip_filename = bin_file_service.file_path + ".zip"

    def _test_writing_zipped_binary_file():
        with zipfile.ZipFile(
            bin_zip_filename,
            "w",
            compression=zipfile.ZIP_DEFLATED,
            compresslevel=compress_level,
        ) as zf:
            zf.write(
                bin_file_service.file_path, arcname=bin_file_service.current_file_name
            )

    _test_writing_zipped_binary_file()

    bin_zip_file_stats = get_file_stats(bin_zip_filename)

    bin_zip_compress_size_ratio = bin_file_stats.st_size / bin_zip_file_stats.st_size
    bin_zip_compress_block_ratio = (
        bin_file_stats.st_blocks / bin_zip_file_stats.st_blocks
    )
    print(
        "zipped senoidal binary file",
        f"\n\tFile size in bytes: {bin_zip_file_stats.st_size}",
        f"\n\tNumber of 512-byte blocks: {bin_zip_file_stats.st_blocks}",
        f"\n\tCompress size ratio: {bin_zip_compress_size_ratio}",
        f"\n\tCompress blocks ratio: {bin_zip_compress_block_ratio}",
    )

    # CSV file test
    csv_zip_filename = csv_file_service.file_path + ".zip"

    def _test_writing_zipped_csv_file():
        with zipfile.ZipFile(
            csv_zip_filename,
            "w",
            compression=zipfile.ZIP_DEFLATED,
            compresslevel=compress_level,
        ) as zf:
            zf.write(
                csv_file_service.file_path, arcname=csv_file_service.current_file_name
            )

    _test_writing_zipped_csv_file()

    csv_zip_file_stats = get_file_stats(csv_zip_filename)

    csv_zip_compress_size_ratio = csv_file_stats.st_size / csv_zip_file_stats.st_size
    csv_zip_compress_block_ratio = (
        csv_file_stats.st_blocks / csv_zip_file_stats.st_blocks
    )
    print(
        "zipped senoidal csv file",
        f"\n\tFile size in bytes: {csv_zip_file_stats.st_size}",
        f"\n\tNumber of 512-byte blocks: {csv_zip_file_stats.st_blocks}",
        f"\n\tCompress size ratio: {csv_zip_compress_size_ratio}",
        f"\n\tCompress blocks ratio: {csv_zip_compress_block_ratio}",
    )

    # Ratio
    zip_size_ratio = float(csv_zip_file_stats.st_size) / float(
        bin_zip_file_stats.st_size
    )
    zip_block_512_ratio = float(csv_zip_file_stats.st_blocks) / float(
        bin_zip_file_stats.st_blocks
    )
    print(
        "zipped senoidal file ratio",
        f"\n\tRatio csv by binary: {zip_size_ratio}",
        f"\n\tNumber of 512-byte blocks: {zip_block_512_ratio}",
    )

    # Clean Up
    clean_up()
    print("\n--------------------------------------------------------\n")


def test_file_size_in_noisy_senoidal_data_points():
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
    _test_writing_binary_file()
    bin_file_stats = get_file_stats(bin_file_service.file_path)

    print(
        "noisy senoidal binary file",
        f"\n\tFile size in bytes: {bin_file_stats.st_size}",
        f"\n\tNumber of 512-byte blocks: {bin_file_stats.st_blocks}",
    )

    # CSV file setup
    csv_file_service = FileCSVService()

    def _test_writing_csv_file():
        csv_file_service.open_new_file(client_filename)
        csv_file_service.write(data)
        csv_file_service.close_current_file()

    # CSV file test
    _test_writing_csv_file()
    csv_file_stats = get_file_stats(csv_file_service.file_path)

    print(
        "noisy senoidal csv file",
        f"\n\tFile size in bytes: {csv_file_stats.st_size}",
        f"\n\tNumber of 512-byte blocks: {csv_file_stats.st_blocks}",
    )

    # Ratio
    size_ratio = float(csv_file_stats.st_size) / float(bin_file_stats.st_size)
    block_512_ratio = float(csv_file_stats.st_blocks) / float(bin_file_stats.st_blocks)
    print(
        "noisy senoidal file ratio",
        f"\n\tRatio csv by binary: {size_ratio}",
        f"\n\tNumber of 512-byte blocks: {block_512_ratio}",
    )

    ################
    # Zipped stuff #
    ################
    # Global setup
    compress_level = 9

    # Binary file test
    bin_zip_filename = bin_file_service.file_path + ".zip"

    def _test_writing_zipped_binary_file():
        with zipfile.ZipFile(
            bin_zip_filename,
            "w",
            compression=zipfile.ZIP_DEFLATED,
            compresslevel=compress_level,
        ) as zf:
            zf.write(
                bin_file_service.file_path, arcname=bin_file_service.current_file_name
            )

    _test_writing_zipped_binary_file()

    bin_zip_file_stats = get_file_stats(bin_zip_filename)

    bin_zip_compress_size_ratio = bin_file_stats.st_size / bin_zip_file_stats.st_size
    bin_zip_compress_block_ratio = (
        bin_file_stats.st_blocks / bin_zip_file_stats.st_blocks
    )
    print(
        "zipped noisy senoidal binary file",
        f"\n\tFile size in bytes: {bin_zip_file_stats.st_size}",
        f"\n\tNumber of 512-byte blocks: {bin_zip_file_stats.st_blocks}",
        f"\n\tCompress size ratio: {bin_zip_compress_size_ratio}",
        f"\n\tCompress blocks ratio: {bin_zip_compress_block_ratio}",
    )

    # CSV file test
    csv_zip_filename = csv_file_service.file_path + ".zip"

    def _test_writing_zipped_csv_file():
        with zipfile.ZipFile(
            csv_zip_filename,
            "w",
            compression=zipfile.ZIP_DEFLATED,
            compresslevel=compress_level,
        ) as zf:
            zf.write(
                csv_file_service.file_path, arcname=csv_file_service.current_file_name
            )

    _test_writing_zipped_csv_file()

    csv_zip_file_stats = get_file_stats(csv_zip_filename)

    csv_zip_compress_size_ratio = csv_file_stats.st_size / csv_zip_file_stats.st_size
    csv_zip_compress_block_ratio = (
        csv_file_stats.st_blocks / csv_zip_file_stats.st_blocks
    )
    print(
        "zipped noisy senoidal csv file",
        f"\n\tFile size in bytes: {csv_zip_file_stats.st_size}",
        f"\n\tNumber of 512-byte blocks: {csv_zip_file_stats.st_blocks}",
        f"\n\tCompress size ratio: {csv_zip_compress_size_ratio}",
        f"\n\tCompress blocks ratio: {csv_zip_compress_block_ratio}",
    )

    # Ratio
    zip_size_ratio = float(csv_zip_file_stats.st_size) / float(
        bin_zip_file_stats.st_size
    )
    zip_block_512_ratio = float(csv_zip_file_stats.st_blocks) / float(
        bin_zip_file_stats.st_blocks
    )
    print(
        "zipped noisy senoidal file ratio",
        f"\n\tRatio csv by binary: {zip_size_ratio}",
        f"\n\tNumber of 512-byte blocks: {zip_block_512_ratio}",
    )

    # Clean Up
    clean_up()
    print("\n--------------------------------------------------------\n")


def test_file_size_in_infinity_data_type_data_points():
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
    _test_writing_binary_file()
    bin_file_stats = get_file_stats(bin_file_service.file_path)

    print(
        "infinity data type binary file",
        f"\n\tFile size in bytes: {bin_file_stats.st_size}",
        f"\n\tNumber of 512-byte blocks: {bin_file_stats.st_blocks}",
    )

    # CSV file setup
    csv_file_service = FileCSVService()

    def _test_writing_csv_file():
        csv_file_service.open_new_file(client_filename)
        csv_file_service.write(data)
        csv_file_service.close_current_file()

    # CSV file test
    _test_writing_csv_file()
    csv_file_stats = get_file_stats(csv_file_service.file_path)

    print(
        "infinity data type csv file",
        f"\n\tFile size in bytes: {csv_file_stats.st_size}",
        f"\n\tNumber of 512-byte blocks: {csv_file_stats.st_blocks}",
    )

    # Ratio
    size_ratio = float(csv_file_stats.st_size) / float(bin_file_stats.st_size)
    block_512_ratio = float(csv_file_stats.st_blocks) / float(bin_file_stats.st_blocks)
    print(
        "infinity data type file ratio",
        f"\n\tRatio csv by binary: {size_ratio}",
        f"\n\tNumber of 512-byte blocks: {block_512_ratio}",
    )

    ################
    # Zipped stuff #
    ################
    # Global setup
    compress_level = 9

    # Binary file test
    bin_zip_filename = bin_file_service.file_path + ".zip"

    def _test_writing_zipped_binary_file():
        with zipfile.ZipFile(
            bin_zip_filename,
            "w",
            compression=zipfile.ZIP_DEFLATED,
            compresslevel=compress_level,
        ) as zf:
            zf.write(
                bin_file_service.file_path, arcname=bin_file_service.current_file_name
            )

    _test_writing_zipped_binary_file()

    bin_zip_file_stats = get_file_stats(bin_zip_filename)

    bin_zip_compress_size_ratio = bin_file_stats.st_size / bin_zip_file_stats.st_size
    bin_zip_compress_block_ratio = (
        bin_file_stats.st_blocks / bin_zip_file_stats.st_blocks
    )
    print(
        "zipped infinity data type binary file",
        f"\n\tFile size in bytes: {bin_zip_file_stats.st_size}",
        f"\n\tNumber of 512-byte blocks: {bin_zip_file_stats.st_blocks}",
        f"\n\tCompress size ratio: {bin_zip_compress_size_ratio}",
        f"\n\tCompress blocks ratio: {bin_zip_compress_block_ratio}",
    )

    # CSV file test
    csv_zip_filename = csv_file_service.file_path + ".zip"

    def _test_writing_zipped_csv_file():
        with zipfile.ZipFile(
            csv_zip_filename,
            "w",
            compression=zipfile.ZIP_DEFLATED,
            compresslevel=compress_level,
        ) as zf:
            zf.write(
                csv_file_service.file_path, arcname=csv_file_service.current_file_name
            )

    _test_writing_zipped_csv_file()

    csv_zip_file_stats = get_file_stats(csv_zip_filename)

    csv_zip_compress_size_ratio = csv_file_stats.st_size / csv_zip_file_stats.st_size
    csv_zip_compress_block_ratio = (
        csv_file_stats.st_blocks / csv_zip_file_stats.st_blocks
    )
    print(
        "zipped infinity data type csv file",
        f"\n\tFile size in bytes: {csv_zip_file_stats.st_size}",
        f"\n\tNumber of 512-byte blocks: {csv_zip_file_stats.st_blocks}",
        f"\n\tCompress size ratio: {csv_zip_compress_size_ratio}",
        f"\n\tCompress blocks ratio: {csv_zip_compress_block_ratio}",
    )

    # Ratio
    zip_size_ratio = float(csv_zip_file_stats.st_size) / float(
        bin_zip_file_stats.st_size
    )
    zip_block_512_ratio = float(csv_zip_file_stats.st_blocks) / float(
        bin_zip_file_stats.st_blocks
    )
    print(
        "zipped infinity data type file ratio",
        f"\n\tRatio csv by binary: {zip_size_ratio}",
        f"\n\tNumber of 512-byte blocks: {zip_block_512_ratio}",
    )

    # Clean Up
    clean_up()
    print("\n--------------------------------------------------------\n")


def test_file_size_in_negative_infinity_data_type_data_points():
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
    _test_writing_binary_file()
    bin_file_stats = get_file_stats(bin_file_service.file_path)

    print(
        "negative infinity data type binary file",
        f"\n\tFile size in bytes: {bin_file_stats.st_size}",
        f"\n\tNumber of 512-byte blocks: {bin_file_stats.st_blocks}",
    )

    # CSV file setup
    csv_file_service = FileCSVService()

    def _test_writing_csv_file():
        csv_file_service.open_new_file(client_filename)
        csv_file_service.write(data)
        csv_file_service.close_current_file()

    # CSV file test
    _test_writing_csv_file()
    csv_file_stats = get_file_stats(csv_file_service.file_path)

    print(
        "negative infinity data type csv file",
        f"\n\tFile size in bytes: {csv_file_stats.st_size}",
        f"\n\tNumber of 512-byte blocks: {csv_file_stats.st_blocks}",
    )

    # Ratio
    size_ratio = float(csv_file_stats.st_size) / float(bin_file_stats.st_size)
    block_512_ratio = float(csv_file_stats.st_blocks) / float(bin_file_stats.st_blocks)
    print(
        "negative infinity data type file ratio",
        f"\n\tRatio csv by binary: {size_ratio}",
        f"\n\tNumber of 512-byte blocks: {block_512_ratio}",
    )

    ################
    # Zipped stuff #
    ################
    # Global setup
    compress_level = 9

    # Binary file test
    bin_zip_filename = bin_file_service.file_path + ".zip"

    def _test_writing_zipped_binary_file():
        with zipfile.ZipFile(
            bin_zip_filename,
            "w",
            compression=zipfile.ZIP_DEFLATED,
            compresslevel=compress_level,
        ) as zf:
            zf.write(
                bin_file_service.file_path, arcname=bin_file_service.current_file_name
            )

    _test_writing_zipped_binary_file()

    bin_zip_file_stats = get_file_stats(bin_zip_filename)

    bin_zip_compress_size_ratio = bin_file_stats.st_size / bin_zip_file_stats.st_size
    bin_zip_compress_block_ratio = (
        bin_file_stats.st_blocks / bin_zip_file_stats.st_blocks
    )
    print(
        "zipped negative infinity data type binary file",
        f"\n\tFile size in bytes: {bin_zip_file_stats.st_size}",
        f"\n\tNumber of 512-byte blocks: {bin_zip_file_stats.st_blocks}",
        f"\n\tCompress size ratio: {bin_zip_compress_size_ratio}",
        f"\n\tCompress blocks ratio: {bin_zip_compress_block_ratio}",
    )

    # CSV file test
    csv_zip_filename = csv_file_service.file_path + ".zip"

    def _test_writing_zipped_csv_file():
        with zipfile.ZipFile(
            csv_zip_filename,
            "w",
            compression=zipfile.ZIP_DEFLATED,
            compresslevel=compress_level,
        ) as zf:
            zf.write(
                csv_file_service.file_path, arcname=csv_file_service.current_file_name
            )

    _test_writing_zipped_csv_file()

    csv_zip_file_stats = get_file_stats(csv_zip_filename)

    csv_zip_compress_size_ratio = csv_file_stats.st_size / csv_zip_file_stats.st_size
    csv_zip_compress_block_ratio = (
        csv_file_stats.st_blocks / csv_zip_file_stats.st_blocks
    )
    print(
        "zipped negative infinity data type csv file",
        f"\n\tFile size in bytes: {csv_zip_file_stats.st_size}",
        f"\n\tNumber of 512-byte blocks: {csv_zip_file_stats.st_blocks}",
        f"\n\tCompress size ratio: {csv_zip_compress_size_ratio}",
        f"\n\tCompress blocks ratio: {csv_zip_compress_block_ratio}",
    )

    # Ratio
    zip_size_ratio = float(csv_zip_file_stats.st_size) / float(
        bin_zip_file_stats.st_size
    )
    zip_block_512_ratio = float(csv_zip_file_stats.st_blocks) / float(
        bin_zip_file_stats.st_blocks
    )
    print(
        "zipped negative infinity data type file ratio",
        f"\n\tRatio csv by binary: {zip_size_ratio}",
        f"\n\tNumber of 512-byte blocks: {zip_block_512_ratio}",
    )

    # Clean Up
    clean_up()
    print("\n--------------------------------------------------------\n")


def test_file_size_in_nan_data_type_data_points():
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
    _test_writing_binary_file()
    bin_file_stats = get_file_stats(bin_file_service.file_path)

    print(
        "nan data type binary file",
        f"\n\tFile size in bytes: {bin_file_stats.st_size}",
        f"\n\tNumber of 512-byte blocks: {bin_file_stats.st_blocks}",
    )

    # CSV file setup
    csv_file_service = FileCSVService()

    def _test_writing_csv_file():
        csv_file_service.open_new_file(client_filename)
        csv_file_service.write(data)
        csv_file_service.close_current_file()

    # CSV file test
    _test_writing_csv_file()
    csv_file_stats = get_file_stats(csv_file_service.file_path)

    print(
        "nan data type csv file",
        f"\n\tFile size in bytes: {csv_file_stats.st_size}",
        f"\n\tNumber of 512-byte blocks: {csv_file_stats.st_blocks}",
    )

    # Ratio
    size_ratio = float(csv_file_stats.st_size) / float(bin_file_stats.st_size)
    block_512_ratio = float(csv_file_stats.st_blocks) / float(bin_file_stats.st_blocks)
    print(
        "nan data type file ratio",
        f"\n\tRatio csv by binary: {size_ratio}",
        f"\n\tNumber of 512-byte blocks: {block_512_ratio}",
    )

    ################
    # Zipped stuff #
    ################
    # Global setup
    compress_level = 9

    # Binary file test
    bin_zip_filename = bin_file_service.file_path + ".zip"

    def _test_writing_zipped_binary_file():
        with zipfile.ZipFile(
            bin_zip_filename,
            "w",
            compression=zipfile.ZIP_DEFLATED,
            compresslevel=compress_level,
        ) as zf:
            zf.write(
                bin_file_service.file_path, arcname=bin_file_service.current_file_name
            )

    _test_writing_zipped_binary_file()

    bin_zip_file_stats = get_file_stats(bin_zip_filename)

    bin_zip_compress_size_ratio = bin_file_stats.st_size / bin_zip_file_stats.st_size
    bin_zip_compress_block_ratio = (
        bin_file_stats.st_blocks / bin_zip_file_stats.st_blocks
    )
    print(
        "zipped nan data type binary file",
        f"\n\tFile size in bytes: {bin_zip_file_stats.st_size}",
        f"\n\tNumber of 512-byte blocks: {bin_zip_file_stats.st_blocks}",
        f"\n\tCompress size ratio: {bin_zip_compress_size_ratio}",
        f"\n\tCompress blocks ratio: {bin_zip_compress_block_ratio}",
    )

    # CSV file test
    csv_zip_filename = csv_file_service.file_path + ".zip"

    def _test_writing_zipped_csv_file():
        with zipfile.ZipFile(
            csv_zip_filename,
            "w",
            compression=zipfile.ZIP_DEFLATED,
            compresslevel=compress_level,
        ) as zf:
            zf.write(
                csv_file_service.file_path, arcname=csv_file_service.current_file_name
            )

    _test_writing_zipped_csv_file()

    csv_zip_file_stats = get_file_stats(csv_zip_filename)

    csv_zip_compress_size_ratio = csv_file_stats.st_size / csv_zip_file_stats.st_size
    csv_zip_compress_block_ratio = (
        csv_file_stats.st_blocks / csv_zip_file_stats.st_blocks
    )
    print(
        "zipped nan data type csv file",
        f"\n\tFile size in bytes: {csv_zip_file_stats.st_size}",
        f"\n\tNumber of 512-byte blocks: {csv_zip_file_stats.st_blocks}",
        f"\n\tCompress size ratio: {csv_zip_compress_size_ratio}",
        f"\n\tCompress blocks ratio: {csv_zip_compress_block_ratio}",
    )

    # Ratio
    zip_size_ratio = float(csv_zip_file_stats.st_size) / float(
        bin_zip_file_stats.st_size
    )
    zip_block_512_ratio = float(csv_zip_file_stats.st_blocks) / float(
        bin_zip_file_stats.st_blocks
    )
    print(
        "zipped nan data type file ratio",
        f"\n\tRatio csv by binary: {zip_size_ratio}",
        f"\n\tNumber of 512-byte blocks: {zip_block_512_ratio}",
    )

    # Clean Up
    clean_up()
    print("\n--------------------------------------------------------\n")


def test_file_size_in_zero_data_type_data_points():
    # Clean Up
    clean_up()

    # Global setup
    amount_of_data_points = 1000
    client_filename = "zero_data_type_data_points"
    data = generate_zero_array(amount_of_data_points)

    # Binary file setup
    bin_file_service = FileBufferService()

    def _test_writing_binary_file():
        bin_file_service.open_new_file(client_filename)
        bin_file_service.write(data)
        bin_file_service.close_current_file()

    # Binary file test
    _test_writing_binary_file()
    bin_file_stats = get_file_stats(bin_file_service.file_path)

    print(
        "zero data type binary file",
        f"\n\tFile size in bytes: {bin_file_stats.st_size}",
        f"\n\tNumber of 512-byte blocks: {bin_file_stats.st_blocks}",
    )

    # CSV file setup
    csv_file_service = FileCSVService()

    def _test_writing_csv_file():
        csv_file_service.open_new_file(client_filename)
        csv_file_service.write(data)
        csv_file_service.close_current_file()

    # CSV file test
    _test_writing_csv_file()
    csv_file_stats = get_file_stats(csv_file_service.file_path)

    print(
        "zero data type csv file",
        f"\n\tFile size in bytes: {csv_file_stats.st_size}",
        f"\n\tNumber of 512-byte blocks: {csv_file_stats.st_blocks}",
    )

    # Ratio
    size_ratio = float(csv_file_stats.st_size) / float(bin_file_stats.st_size)
    block_512_ratio = float(csv_file_stats.st_blocks) / float(bin_file_stats.st_blocks)
    print(
        "zero data type file ratio",
        f"\n\tRatio csv by binary: {size_ratio}",
        f"\n\tNumber of 512-byte blocks: {block_512_ratio}",
    )

    ################
    # Zipped stuff #
    ################
    # Global setup
    compress_level = 9

    # Binary file test
    bin_zip_filename = bin_file_service.file_path + ".zip"

    def _test_writing_zipped_binary_file():
        with zipfile.ZipFile(
            bin_zip_filename,
            "w",
            compression=zipfile.ZIP_DEFLATED,
            compresslevel=compress_level,
        ) as zf:
            zf.write(
                bin_file_service.file_path, arcname=bin_file_service.current_file_name
            )

    _test_writing_zipped_binary_file()

    bin_zip_file_stats = get_file_stats(bin_zip_filename)

    bin_zip_compress_size_ratio = bin_file_stats.st_size / bin_zip_file_stats.st_size
    bin_zip_compress_block_ratio = (
        bin_file_stats.st_blocks / bin_zip_file_stats.st_blocks
    )
    print(
        "zipped zero data type binary file",
        f"\n\tFile size in bytes: {bin_zip_file_stats.st_size}",
        f"\n\tNumber of 512-byte blocks: {bin_zip_file_stats.st_blocks}",
        f"\n\tCompress size ratio: {bin_zip_compress_size_ratio}",
        f"\n\tCompress blocks ratio: {bin_zip_compress_block_ratio}",
    )

    # CSV file test
    csv_zip_filename = csv_file_service.file_path + ".zip"

    def _test_writing_zipped_csv_file():
        with zipfile.ZipFile(
            csv_zip_filename,
            "w",
            compression=zipfile.ZIP_DEFLATED,
            compresslevel=compress_level,
        ) as zf:
            zf.write(
                csv_file_service.file_path, arcname=csv_file_service.current_file_name
            )

    _test_writing_zipped_csv_file()

    csv_zip_file_stats = get_file_stats(csv_zip_filename)

    csv_zip_compress_size_ratio = csv_file_stats.st_size / csv_zip_file_stats.st_size
    csv_zip_compress_block_ratio = (
        csv_file_stats.st_blocks / csv_zip_file_stats.st_blocks
    )
    print(
        "zipped zero data type csv file",
        f"\n\tFile size in bytes: {csv_zip_file_stats.st_size}",
        f"\n\tNumber of 512-byte blocks: {csv_zip_file_stats.st_blocks}",
        f"\n\tCompress size ratio: {csv_zip_compress_size_ratio}",
        f"\n\tCompress blocks ratio: {csv_zip_compress_block_ratio}",
    )

    # Ratio
    zip_size_ratio = float(csv_zip_file_stats.st_size) / float(
        bin_zip_file_stats.st_size
    )
    zip_block_512_ratio = float(csv_zip_file_stats.st_blocks) / float(
        bin_zip_file_stats.st_blocks
    )
    print(
        "zipped zero data type file ratio",
        f"\n\tRatio csv by binary: {zip_size_ratio}",
        f"\n\tNumber of 512-byte blocks: {zip_block_512_ratio}",
    )

    # Clean Up
    clean_up()
    print("\n--------------------------------------------------------\n")
