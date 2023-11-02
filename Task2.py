class Worker:
    def __init__(self, name, surname, position, income):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = income


class Position(Worker):
    def get_full_name(self):
        return f"{self.name} {self.surname}"

    def get_total_income(self):
        return self._income["wage"] + self._income["bonus"]


worker_data = {
    "name": "Иван",
    "surname": "Иванов",
    "position": "Инженер",
    "income": {"wage": 50000, "bonus": 10000}
}

position = Position(**worker_data)

print("Имя сотрудника:", position.get_full_name())
print("Доход с учетом премии:", position.get_total_income())
