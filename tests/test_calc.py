from calc import Calculator

def test_division_valid():
    app = Calculator()
    assert app.exec("10 / 5") == 2