from ejercicio1 import MCD


def test__should_return_minus_1_when_x_equal_0():
    #TC: 13
    res = MCD(0, 1)

    assert res == -1
def test__should_return_minus_1_when_y_equal_0():
    #TC:123
    res = MCD(1, 0)
    
    assert res == -1

def test__should_return_1_when_x_1():
    #TC:1246
    res = MCD(1, 2)

    assert res == 1
    
def test__should_return_1_when_y_1():
    #TC: 12456
    res = MCD(2, 1)

    assert res == 1
    
def test__should_return_x_when_x_equal_y():
    #TC: 1245711
    res = MCD(4, 4)

    assert res == 4

def test__when_x_bigger_y():
    #TC: 1245789711
    res = MCD(8, 4)

    assert res ==4

def test__when_y_is_bigger_than_x():
    #TC: 12457810711
    res = MCD(4, 8)

    assert res ==4

