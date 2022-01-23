class Unit:
    def __init__(self, hp, x, y):
        self.hp = hp  # текущее количество хит-поинтов
        self.got_key = False  # наличие у юнита ключа для открытия двери в конце уровня
        self.coord = (x, y)  # координаты x, y
        self.escaped = False  # флаг, удалось ли сбежать из подземелья
        # self.defense = defense
        # self.x = 0
        # self.y = 0

    def has_key(self) -> bool:
        return self.got_key

    def set_key(self):
        self.got_key = True

    def has_escaped(self) -> bool:  # проверка удалось ли сбежать
        return self.escaped

    def is_alive(self) -> bool:
        # - _is_alive → bool — проверяет, есть ли еще у юнита положительное количество хит-поинтов.
        if self.hp <= 0:
            print("Game over")
            return False
        return True

        # except KeyError:
        #     raise "UnitDied"

    def get_damage(self, damage):
        # - get_damage — обрабатывает входящий урон с учетом текущего параметра защиты.
        # Если юнит умирает после атаки, должно быть выброшено исключение UnitDied.
        self.hp -= damage
        self.is_alive()


    def set_coordinates(self, x, y):
        self.coord = (x, y)

    def get_coordinates(self):
        return self.coord

    def has_position(self, x, y):
        return self.coord[0] == x and self.coord[1] == y


class Ghost(Unit):
    def __init__(self, hp, x, y):
        super().__init__(hp, x, y)
        self.name = "Ghost"



