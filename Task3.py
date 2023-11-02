class Stationery:
    def __init__(self, title):
        self.title = title

    def draw(self):
        print("Запись отрисовки")


class Pen(Stationery):
    def draw(self):
        print(f'{self.get_class_name()} с названием "{self.title}" пишет')
    def get_class_name(self):
        return "Ручка"


class Pencil(Stationery):
    def draw(self):
        print(f'{self.get_class_name()} с названием "{self.title}" рисует')
    def get_class_name(self):
        return "Карандаш"


class Handle(Stationery):
    def draw(self):
        print(f'{self.get_class_name()} с названием "{self.title}" маркирует')
    def get_class_name(self):
        return "Маркер"


pen = Pen("Синяя")
pencil = Pencil("Простой")
handle = Handle("Черный")
pen.draw()
pencil.draw()
handle.draw()