class Calculator:
    def __init__(self):
        self.operators = "+-*/**//%"

    def exec(self, expression: str):
        data = self.input(expression)
        if data[1] == "+":
            return data[0] + data[2]
        elif data[1] == "-":
            return data[0] - data[2]
        elif data[1] == "*":
            return data[0] * data[2]
        elif data[1] == "/":
            return data[0] / data[2]
        elif data[1] == "//":
            return data[0] // data[2]
        elif data[1] == "%":
            return data[0] % data[2]
        elif data[1] == "**":
            return data[0] ** data[2]

    def input(self,  expression: str):
        if not isinstance(expression, str):
            raise TypeError("Неправильный тип информации")
        data = expression.split()
        if len(data) != 3:
            raise ValueError("Неверное количество символов")
        if data[1] not in self.operators:
            raise ValueError("Неверный оператор")
        if not isinstance(int(data[0]), int) or not isinstance(int(data[2]), int):
            raise ValueError('Неверный тип значений')
        if data[1] == "/" and data[2] == "0":
            raise ZeroDivisionError("Нельзя делить на ноль")
        return [int(data[0]), data[1], int(data[2])]

