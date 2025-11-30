import package.configs as configs, os, copy, random
from package.printer import *
from package.configs import *
from modules.createPlayer import CreatePlayer
from modules.cenarios.default import CenarioDefault
from modules.entities.inimigo import Inimigo
from modules.entities.chest import Chest
from modules.cenarios.map import RenderMap, GetRandomSpace

class Game:
    def __init__(self):
        [mapa.append(["v"]*len(mapa[0])) for _ in range(len(mapa[0]))]
        for linha in mapa:
            linha += ["v"]*len(mapa[0])

        self.mapa_original = copy.deepcopy(mapa)
        self.mapa_to_show = copy.deepcopy(mapa)

        self.cenariodefault = CenarioDefault(self)
        self.cenarioatual = self.cenariodefault

        self.entities = []

        self.ultimatecla = "w"

    def StartGame(self):
        timed_print('''
É recomendado colocar em janela maximizada.
ENTER para continuar, 0 para sair.''',0.3)
        if input("") == "0": quit()
        os.system("cls")
        
        self.player = CreatePlayer(self)

        self.entities.append(Inimigo(self, self.player, "Dragão", "Místico", 200, 10, GetRandomSpace(self.mapa_original), "i", 1, [["machado", 40]], 0))
        self.entities.append(Inimigo(self, self.player, "O Guardião", "Humano", 115, 7, GetRandomSpace(self.mapa_original), "i", 1, [["machado", 30]], 0))
        self.entities.append(Inimigo(self, self.player, "Mago", "Humano", 100, 5, GetRandomSpace(self.mapa_original), "i", 3, [["machado",25]], 0))
        self.entities.append(Inimigo(self, self.player, "Goblin", "Monstro", 100, 5, GetRandomSpace(self.mapa_original), "i", 3, [["machado",25]], 0))
        self.entities.append(Inimigo(self, self.player, "Anão", "Místico", 50, 3, GetRandomSpace(self.mapa_original), "i", 2, [["machado",30]], 0))

        for _ in range(random.randint(1,8)):
            self.entities.append(Chest(self, GetRandomSpace(self.mapa_original)))

        self.entities.append(self.player)

        timed_print("Para começar, tecle W, A, S ou D.",0.3)

        self.run()
    
    def run(self):
        os.system("cls")

        for entidade in self.entities:
            entidade.draw_in_map()

        RenderMap(self)
        while True:
            self.cenarioatual.update()
            RenderMap(self)

    def resetScreen(self):
        self.mapa_to_show = copy.deepcopy(self.mapa_original)

    def resetCenario(self):
        self.cenarioatual = self.cenariodefault