import copy, os, random
from package.printer import rgb
from package.configs import itens_usaveis
from modules.cenarios.map import GetRandomSpace

class Batalha:
    def __init__(self, player, inimigo, game):
        self.player = player
        self.inimigo = inimigo
        self.game = game
        self.chanceFugir = random.randint(10,80)
    
    def update(self):
        self.game.mapa_to_show = copy.deepcopy(self.game.mapa_original)

        for entidade in self.game.entities:
            entidade.draw_in_map()

        print(f"Sua vida: {self.player.vida}/{self.player.vida_max}")
        print("")
        rgb(205, 0, 0)
        print("#"*self.player.vida, end="")
        rgb(128, 128, 128)
        print("#"*(self.player.vida_max - self.player.vida))
        rgb()

        print(f"Vida do {self.inimigo.nome}: {self.inimigo.vida}/{self.inimigo.vida_max}\tNivel: {self.inimigo.nivel}\tDefesa: {self.inimigo.defesa}")
        print("")
        rgb(205, 0, 0)
        print("#"*self.inimigo.vida, end="")
        rgb(128, 128, 128)
        print("#"*(self.inimigo.vida_max - self.inimigo.vida))
        rgb()
        print("")
        print("\t\t\t(1) LUTAR\t\t(2) ITEM\t\t(3) FUGIR")

        escolha = input("> : ")
        if escolha == "1":
            dano = self.player.inventario[self.player.equipamento_id][1] + random.randint(-10,10)

            self.inimigo.dano(dano)

            os.system("cls")
            self.inimigo.renderSelf()
            print("")
            if self.inimigo.vida >= 1:
                input(f"Você deu {dano} de dano!")
                dano_inimigo = self.inimigo.inventario[self.inimigo.equipamento_id][1] + random.randint(-10,10)
                self.player.dano(dano_inimigo)
            else:
                #Ressucitar o inimigo
                self.inimigo.vida = self.inimigo.vida_max
                self.inimigo.x, self.inimigo.y = GetRandomSpace(self.game.mapa_original)

                self.game.resetCenario()
                self.game.resetScreen()
                for entidade in self.game.entities:
                    entidade.draw_in_map()
        
        elif escolha == "2":
            os.system("cls")
            self.inimigo.renderSelf()
            print("Qual item deseja usar:")
            items = []
            indice = 0
            for item in self.player.inventario:
                if item[0] in itens_usaveis["cura"]:
                    indice += 1
                    print(f"({indice}) {item[0]}: {item[1]}")
                    items.append(item)
            if len(items) == 0:
                print("Não há items de cura!")
            
            escolha = input(" > : ")
            if escolha.isdigit():
                escolha = int(escolha)-1
                try:
                    items[escolha]
                    for indice, item in enumerate(self.player.inventario):
                        if items[escolha] == item:
                            self.player.cura(item[1])
                            self.player.remove_inventory_by_id(indice)
                            break
                except:
                    print("Item inválido ou sem itens listados!")
            else:
                print("Opção inválida!")
        
        elif escolha == "3":
            os.system("cls")
            self.inimigo.renderSelf()
            print(f"Tem certeza que deseja TENTAR fugir? (chance de sucesso: {self.chanceFugir})")
            print("(1) Não.")
            print("(2) Sim.")
            escolha = input(" > : ")
            if escolha == "2":
                dado = random.randint(1,100)
                if dado < self.chanceFugir:
                    self.game.resetCenario()
                    input("Você fugiu!")
                else:
                    dano_inimigo = self.inimigo.inventario[self.inimigo.equipamento_id][1] + random.randint(-10,10)
                    self.player.dano(dano_inimigo)

        os.system("cls")