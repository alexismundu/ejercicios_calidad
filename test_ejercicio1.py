import ejercicio1


def test__should_return_minus_1_when_x_or_y_equal_0():
    res = ejercicio1.funcion(0, 1)

    assert res == -1
