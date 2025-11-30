from package.printer import timed_print
from package.configs import *
from modules.cenarios.map import RenderMap
import os

class CenarioInventario:
    def __init__(self, game):
        self.game = game

    def update(self):
        os.system("cls")
        
        for entidade in self.game.entities:
            entidade.draw_in_map()
        RenderMap(self.game)
        
        print("Inventário:")
        for indice, (item, valor) in enumerate(self.game.player.inventario):
            print(f"\t{indice+1} - {item}; itensidade: {valor}")
        if len(self.game.player.inventario) == 0: print("Não há items")
        print("-"*120)
        print("(1) Jogar um item fora")
        print("(2) Usar/equipar um item")
        print("Tecle outra opção para cancelar.")
        timed_print("Oque deseja fazer?", 0.3)
        userchoice = input(" > :")
        if userchoice == "1":
            iditem = input("Insira o número do item para jogar fora: ")
            if iditem.isdigit() and int(iditem) >= 1:
                iditem = int(iditem)-1
                try:
                    self.game.player.inventario.pop(iditem)
                except:
                    print("Esse item não existe!")
        elif userchoice == "2":
            iditem = input("Insira o número do item para usar/equipar: ")
            if iditem.isdigit() and int(iditem) >= 1:
                iditem = int(iditem)-1
                try:
                    #verificar se o item existe
                    self.game.player.inventario[iditem]
                    if self.game.player.inventario[iditem][0] in itens_usaveis["cura"]:
                        self.game.player.cura(self.game.player.inventario[iditem][1])
                        self.game.player.inventario.pop(iditem)
                    elif self.game.player.inventario[iditem][0] in itens_usaveis["dano"]:
                        self.game.player.equipamento_id = iditem
                except:
                    print("Esse item não existe!")
        self.game.resetCenario()