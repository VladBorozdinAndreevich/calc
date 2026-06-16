from main import *

def test_perimeter_of_faces():
    assert perimeter_of_faces(1, 2, 3) == 4 * 1 + 4 * 2 + 4 * 3, "ошибочный результат"


def test_avg_perimeter():
    assert avg_perimeter(3) == 0.5

def test_area_of_sides():
    assert area_of_sides(1, 4, 6) == 2 * (1 * 4 + 4 * 6 + 6 * 1)

def test_avg_area():
    assert  avg_area(12) == 2

def test_volume():
    assert volume(1, 1, 1) == 1



if __name__ == '__main__':
    test_perimeter_of_faces()
    test_avg_perimeter()
    test_area_of_sides()
    test_avg_area()
    test_volume()