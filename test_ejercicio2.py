from ejercicio2 import maximo


def test__should_return_the_value_of_the_input_numbers_if_all_numbers_are_equal():
    EXPECTED_RESULT = 1
    res = maximo(x=EXPECTED_RESULT, y=EXPECTED_RESULT, z=EXPECTED_RESULT)
    assert res == EXPECTED_RESULT


def test__should_return_z_value_when_z_is_the_biggest_number():
    EXPECTED_RESULT = 3
    res = maximo(x=2, y=1, z=EXPECTED_RESULT)
    assert res == EXPECTED_RESULT


def test__should_return_y_value_when_y_is_the_biggest_number():
    EXPECTED_RESULT = 3
    res = maximo(x=2, y=EXPECTED_RESULT, z=1)
    assert res == EXPECTED_RESULT


def test__should_return_x_value_when_x_is_the_biggest_number():
    EXPECTED_RESULT = 3
    res = maximo(x=EXPECTED_RESULT, y=2, z=1)
    assert res == EXPECTED_RESULT
