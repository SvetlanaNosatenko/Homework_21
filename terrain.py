
class Terrain:
    def __init__(self, is_walkable, terrain):
        self.is_walkable = is_walkable # говорящий о том, можно ли юниту пройти через этот объект
        self.terrain = terrain # содержащий наименование объекта
        self.unit = None

    def step_on(self, unit):
        self.unit = unit

    def is_walkable(self):
        # bool - возвращающий флаг о "проходимости" объекта
        return self.is_walkable

    def get_terrain(self):
        #  - возвращает имя объекта
        return self.terrain

class Door(Terrain):
    def __init__(self):
        super().__init__(is_walkable=True, terrain="Door")
    # Как только у нашего игрового юнита появляется ключ, которым можно открыть дверь, попадание юнита на дверь должно
    # завершать игру или переводить на следующий уровень. Отнаследуйтесь от класса Terrain,
    # у двери должны быть собственное свойство terrain содержащее наименование объекта
    # step_on — основной  метод — когда юнит наступает на дверь, должна проводиться проверка, есть ли у юнита
    # ключ, и если есть, то для юнита должен быть установлен флаг escaped
    def step_on(self, unit):
        if unit.has_key:
            unit.escaped = True
            return True
        return False

class Key(Terrain):
    def __init__(self):
        super().__init__(is_walkable=True, terrain="Key")

    def step_on(self, unit):
        unit.set_key()

class Trap(Terrain):
    def __init__(self, damage):
        super().__init__(is_walkable=True, terrain="Trap")
        self.damage = damage

    def step_on(self, unit):
        unit.get_damage(self.damage)

class Grass(Terrain):
    def __init__(self):
        super().__init__(is_walkable=True, terrain="Grass")


class Wall(Terrain):
    def __init__(self):
        super().__init__(is_walkable=False, terrain="Wall")


class Cell:
    def __init__(self, obj):
        self.obj = obj
    # хранилище для объектов, из которых будет состоять наше игровое поле.По умолчанию объект пустой
    # get_obj — возвращает объект, установленный в ячейку
    def get_obj(self):
        return self.obj

    def set_obj(self, obj):
        self.obj = obj
