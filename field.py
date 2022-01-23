from app import Unit
from game_item import Grass, Wall, Trap, Door, Key
from level import Level
from terrain import Cell


class Field:
    def __init__(self, rows: int, cols: int, field: list, unit: Unit):
        self.field = field  # В этом массиве мы будем хранить положение наших объектов. Этот объект мы будем изменять во время игры
        self.unit = unit  # unit: Unit — ссылка на наш Unit, размещенный на поле feld.
        self.rows = rows  # строки поля
        self.cols = cols  # столбцы поля

    def get_cell(self, x, y):  # метод, возвращающий объект находящийся по данным координатам
        return self.unit.set_coordinates(x, y)


    def move_unit_up(self, unit):
        # — метод, смещающий юнита вверх;
        unit.y += 1
        return unit.y

    def move_unit_down(self, unit):
        unit.y -= 1
        return unit.y

    def move_unit_right(self, unit):
        unit.x += 1
        return unit.x

    def move_unit_left(self, unit):
        unit.x -= 1
        return unit.x

    def get_field(self):
        # возвращает свойство field
        return self.field

    def get_cols(self):
        return self.cols

    def get_rows(self):
        return self.rows

