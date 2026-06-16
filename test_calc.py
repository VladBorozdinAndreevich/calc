from calc import *
import unittest


class TestExec(unittest.TestCase):
    def test_exec_available(self):
        app = Calculator()
        try:
            app.exec("1 + 1")
        except AttributeError:
            self.fail("функции exec не существует")

    def test_addition(self):
        app = Calculator()
        self.assertEqual(app.exec("3 + 6"), 9)
        self.assertEqual(app.exec("-3 + 6"), 3)
        self.assertEqual(app.exec("3 + -6"), -3)
        self.assertEqual(app.exec("-3 + -6"), -9)

    def test_subtraction(self):
        app = Calculator()
        self.assertEqual(app.exec("3 - 6"), -3)
        self.assertEqual(app.exec("-3 - 6"), -9)
        self.assertEqual(app.exec("3 - -6"), 9)
        self.assertEqual(app.exec("-3 - -6"), 3)

    def test_multiplication(self):
        app = Calculator()
        self.assertEqual(app.exec("3 * 6"), 18)
        self.assertEqual(app.exec("-3 * 6"), -18)
        self.assertEqual(app.exec("3 * -6"), -18)
        self.assertEqual(app.exec("-3 * -6"), 18)

    def test_division(self):
        app = Calculator()
        self.assertEqual(app.exec("3 / 6"), 0.5)
        self.assertEqual(app.exec("-3 / 6"), -0.5)
        self.assertEqual(app.exec("3 / -6"), -0.5)
        self.assertEqual(app.exec("-3 / -6"), 0.5)

    def test_power(self):
        app = Calculator()
        self.assertEqual(app.exec("2 ** 3"), 8)
        self.assertEqual(app.exec("-2 ** 3"), -8)
        self.assertEqual(app.exec("2 ** -2"), 0.25)

    def test_floor_division(self):
        app = Calculator()
        self.assertEqual(app.exec("7 // 2"), 3)
        self.assertEqual(app.exec("-7 // 2"), -4)
        self.assertEqual(app.exec("7 // -2"), -4)

    def test_modulo(self):
        app = Calculator()
        self.assertEqual(app.exec("7 % 2"), 1)
        self.assertEqual(app.exec("-7 % 2"), 1)
        self.assertEqual(app.exec("7 % -2"), -1)


class TestInput(unittest.TestCase):
    def test_input_available(self):
        app = Calculator()
        try:
            app.input("7 + 4")
        except AttributeError:
            self.fail("функции input не существует")

    def test_valid_input(self):
        app = Calculator()
        self.assertEqual(app.input("7 + 4"), [7, "+", 4])
        self.assertEqual(app.input("7 - -4"), [7, "-", -4])
        self.assertEqual(app.input("-7 * 4"), [-7, "*", 4])
        self.assertEqual(app.input("-7 / -4"), [-7, "/", -4])
        self.assertEqual(app.input("-7 // -4"), [-7, "//", -4])
        self.assertEqual(app.input("-7 % -4"), [-7, "%", -4])
        self.assertEqual(app.input("-7 ** -4"), [-7, "**", -4])

    def test_invalid_input(self):
        app = Calculator()
        with self.assertRaises(ValueError):
            app.input("нШРУЫЛГОЙШ")
        with self.assertRaises(TypeError):
            app.input(4895.43944)
        with self.assertRaises(ZeroDivisionError):
            app.input("8 / 0")
        with self.assertRaises(ValueError):
            app.input("2 () 8")
        with self.assertRaises(ValueError):
            app.input("2  7")
        with self.assertRaises(ValueError):
            app.input((""))
        with self.assertRaises(ValueError):
            app.input("a + b")


if __name__ == '__main__':
    unittest.main()
