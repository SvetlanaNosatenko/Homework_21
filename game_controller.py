from unit import Ghost
from field import Field
from terrain import Grass, Cell, Wall, Key, Door, Trap
from functions import  read_file

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
        self.field = None  # наше игровое поле, с которым мы будем взаимодействовать

    def make_field(self):
        fields = []
        file = read_file('fields_scheme.txt')
        row = len(file)
        col = len(file[0])

        for num, line in enumerate(file):
            field_line = []
            for item_num, item in enumerate(line.strip("\n")):
                if item == "W":
                    field_line.append(Cell(Wall()))
                if item == "g":
                    field_line.append(Cell(Grass()))
                if item == "G":
                    field_line.append(Cell(Grass()))
                    self.hero = Ghost(50, item_num, num)
                if item == "K":
                    field_line.append(Cell(Key()))
                if item == "D":
                    field_line.append(Cell(Door()))
                if item == "T":
                    field_line.append(Cell(Trap(10)))
            fields.append(field_line)

            self.field = Field(fields, self.hero, col, row)

    def draw_field(self):
        for y, line in enumerate(self.field.get_field()):
            textfield = ""
            for x, item in enumerate(line):
                if self.hero.has_position(x, y):
                    textfield += self.mapping['Ghost']
                else:
                    textfield += self.mapping[item.get_obj().get_terrain()]
            print(textfield)

    def play(self):
        # метод запускающий бесконечный цикл, который может быть прерван или по желанию игрока, или по прохождению уровня
        # self.game_on = False
        self.make_field()
        while self.game_on and not self.hero.has_escaped():
            self.draw_field()
            command = input(">")
            if command == "w":
                self.field.move_unit_up()
            elif command == "s":
                self.field.move_unit_down()
            elif command == "a":
                self.field.move_unit_left()
            elif command == "d":
                self.field.move_unit_right()
            elif command in ["stop", "exit"]:
                print("Конец игры")
                self.game_on = False

