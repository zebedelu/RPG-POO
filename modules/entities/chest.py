import random
from package.configs import itens_usaveis, cenario_objs_letra

class Chest:
    def __init__(self, game, pos):
        self.x, self.y = pos
        items_possiveis = itens_usaveis["cura"]+itens_usaveis["dano"]
        self.item = random.choice(items_possiveis)
        self.game = game
        self.letra = "b"
        self.intensidade = random.randint(10,60)
        self.cor = (150, 70, 0)

    def GetItem(self):
        self.game.player.inventario.append([self.item, self.intensidade])
        self.game.entities.remove(self)
        input(f"Baú coletado! {self.item}; intensidade: {self.intensidade}")

    def draw_in_map(self):
        self.game.mapa_to_show[self.y][self.x] = [self.letra, self.cor, self]