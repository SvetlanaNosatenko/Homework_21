class Field:
    def __init__(self, field, unit, cols, rows):
        self.field = field  # В массиве хранится положение наших объектов
        self.unit = unit  # unit — ссылка на Unit, размещенный на поле field.
        self.rows = rows  # строки поля
        self.cols = cols  # столбцы поля

    def cell(self, x, y):
        return self.field[y][x]

    # def get_cell(self, x, y):  # метод, возвращающий объект находящийся по данным координатам
    #     return self.unit.set_coordinates(x, y)

    def unit_move(self, x, y):
        if self.cell(x, y).get_obj().get_terrain() == 'Key':
            self.cell(x, y).get_obj().step_on(self.unit)
            print('Теперь у Вас есть ключ')

        if self.cell(x, y).get_obj().get_terrain() == 'Trap':
            self.cell(x, y).get_obj().step_on(self.unit)
            print(f'Ловушка! Осталось {self.unit.hp} хит-поинтов')

        if self.cell(x, y).get_obj().is_walkable:
            self.unit.set_coordinates(x, y)
        else:
            print('Выбрать другой путь')

        if self.cell(x, y).get_obj().get_terrain() == 'Door':
            if self.cell(x, y).get_obj().step_on(self.unit):
                print('Уровень пройден!')
            else:
                print('Чтобы выйти из подземелья нужен ключ!')

    def move_unit_up(self):
        x, y = self.unit.get_coordinates()
        self.unit_move(x, y - 1)

    def move_unit_down(self):
        x, y = self.unit.get_coordinates()
        self.unit_move(x, y + 1)

    def move_unit_right(self):
        x, y = self.unit.get_coordinates()
        self.unit_move(x + 1, y)

    def move_unit_left(self):
        x, y = self.unit.get_coordinates()
        self.unit_move(x - 1, y)

    def get_field(self):
        # возвращает свойство field
        return self.field

    def get_cols(self):
        return self.cols

    def get_rows(self):
        return self.rows

