from ejercicio2 import maximo


def test__all_variables_son_iguales():
    res = maximo(1, 1, 1)
    assert res == 1
