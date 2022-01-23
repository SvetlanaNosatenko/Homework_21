from app import Unit

class Terrain:
    def __init__(self, is_walkable, terrain):
        self.is_walkable = is_walkable # говорящий о том, можно ли юниту пройти через этот объект
        self.terrain = terrain # содержащий наименование объекта


    def step_on(self, unit: Unit):
        # метод step_on, которому в качестве аргумента должен передаваться объект типа Unit.

    def is_walkable(self):
        # bool - возвращающий флаг о "проходимости" объекта
        return self.is_walkable

    def get_terrain(self):
        #  - возвращает имя объекта
        return self.terrain

class Door(Terrain):
    def __init__(self):
        super().__init__(is_walkable=True, terrain="door")
    # Как только у нашего игрового юнита появляется ключ, которым можно открыть дверь, попадание юнита на дверь должно
    # завершать игру или переводить на следующий уровень. Отнаследуйтесь от класса Terrain,
    # у двери должны быть собственное свойство terrain содержащее наименование объекта
    # step_on — основной  метод — когда юнит наступает на дверь, должна проводиться проверка, есть ли у юнита
    # ключ, и если есть, то для юнита должен быть установлен флаг escaped
    def step_on(self, unit):
        if unit.get_coordinates() :
            if unit.set_key():
                unit.has_escaped()

class Key(Terrain):
    def __init__(self):
        super().__init__(is_walkable=True, terrain="key")

    def step_on(self, unit):
        # step_on — должен добавлять юниту, который наступил на ключ, этот самый ключ установкой ключа
        # has_key через публичный метод


class Trap(Terrain):
    def __init__(self):
        super().__init__(is_walkable=True, terrain="trap")
        self.damage = 0

    def step_on(self, unit):
        unit.get_damage(self.damage)

class Grass(Terrain):
    def __init__(self):
        super().__init__(is_walkable=True, terrain="grass")


class Wall(Terrain):
    def __init__(self):
        super().__init__(is_walkable=False, terrain="wall")


class Cell:
    def __init__(self, obj):
        self.obj = obj
    # хранилище для объектов, из которых будет состоять наше игровое поле.По умолчанию объект пустой
    # get_obj — возвращает объект, установленный в ячейку
    def get_obj(self):
        return self.obj

    def set_obj(self, obj):
        self.obj = obj
