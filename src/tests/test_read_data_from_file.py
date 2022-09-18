from generators import (
    generate_senoidal_array,
    generate_inf_array,
    generate_nan_array,
    generate_zero_array,
)

amount_of_data_points = 1000

data_arrays = {
    "Senoidal": generate_senoidal_array(amount_of_data_points),
    "Noisy_Senoidal": generate_senoidal_array(
        amount_of_data_points, has_harmonics=True
    ),
    "Inf": generate_inf_array(amount_of_data_points),
    "Negative Inf": generate_inf_array(amount_of_data_points, negative_values=True),
    "NaN": generate_nan_array(amount_of_data_points),
    "Zeros": generate_zero_array(amount_of_data_points),
}


def test_read_senoidal_data_points_speed():
    pass


def test_read_noisy_senoidal_data_points_speed():
    pass


def test_read_infinity_data_point_type_speed():
    pass


def test_read_negative_infinity_data_point_type_speed():
    pass


def test_read_nan_data_point_type_speed():
    pass


def test_read_zero_data_point_type_speed():
    pass
