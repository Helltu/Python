class Calculator:
    def __init__(self):
        pass

    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        try:
            result = a/b
        except ZeroDivisionError:
            result = "Деление на ноль невозможно"
        return result

    def get_user_input(self):
        try:
            a = float(input("Введите первое число: "))
            b = float(input("Введите второе число: "))
        except ValueError:
            print("Ошибка ввода. Введите числа")
            return self.get_user_input()
        return a, b


calculator = Calculator()
a, b = calculator.get_user_input()
result = calculator.add(a, b)
print("Сумма:", result)
result = calculator.subtract(a, b)
print("Разность:", result)
result = calculator.multiply(a, b)
print("Произведение:", result)
result = calculator.divide(a, b)
print("Деление:", result)
