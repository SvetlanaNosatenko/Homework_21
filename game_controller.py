from app import Ghost
from field import Field
from terrain import Grass, Cell


class GameController:
    def __init__(self):
        self.mapping = {
    'Wall': '🔲',
    'Grass': '⬜️',
    'Ghost': '👻',
    'Key': '🗝',
    'Door': '🚪',
    'Trap': '💀',
}  # словарь, через который мы будем преобразовывать наши имена объектов в значки.
        self.game_on = True # маркер, сообщающий что пользователь не выразил желание прервать игру
        self.hero = Ghost  # инициализация нашего игрового персонажа
        self.field = Field  # наше игровое поле, с которым мы будем взаимодействовать

    def make_field(self):
        cell_1 = Cell(Grass())
        cell_2 = Cell(Grass())
        cell_3 = Cell(Grass())
        cell_4 = Cell(Grass())
        cell_5 = Cell(Grass())
        cell_6 = Cell(Grass())
        cell_7 = Cell(Grass())
        cell_8 = Cell(Grass())
        cell_9 = Cell(Grass())
        cell_10 = Cell(Grass())
        cell_11 = Cell(Grass())
        cell_12 = Cell(Grass())
        cell_13 = Cell(Grass())
        cell_14 = Cell(Grass())
        cell_15 = Cell(Grass())


        self.field = Field()
        # метод, который будет отдавать нам по требованию готовое поле с размеченными значками элементами.
        return self.field

    def play(self):
        # метод запускающий бесконечный цикл, который может быть прерван или по желанию игрока, или по прохождению уровня
        self.game_on = False
        while not self.game_on or :
            self.make_field()
            break