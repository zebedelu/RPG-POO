from modules.entities.entitie import Entitie
from modules.cenarios.batalha import Batalha
from package.printer import timed_print
import game, os

class Player(Entitie):
    def __init__(self, game, nome, classe, vida, defesa, posicao, letra, nivel=1, inventario=[], item_equipado=-1):
        super().__init__(game, nome, classe, vida, defesa, posicao, letra, nivel, inventario, item_equipado)
        self.contador_mortes = 0

    def dano(self, dano):
        self.vida -= (dano - self.defesa) if dano >= self.defesa else (dano/self.vida_max)*self.defesa
        if self.vida <= 0:
            print()
            while True:
                print('''\n\n\n
  ________                        ________                     
 /  _____/_____    _____   ____   \_____  \___  __ ___________ 
/   \  ___\__  \  /     \_/ __ \   /   |   \  \/ _/ __ \_  __ \\
\    \_\  \/ __ \|  Y Y  \  ___/  /    |    \   /\  ___/|  | \/
 \______  (____  |__|_|  /\___  > \_______  /\_/  \___  |__|   
        \/     \/      \/     \/          \/          \/       \n\n\n
''')            
                timed_print("Você morreu")
                timed_print("...", 1)
                timed_print(" ",1)
                os.system("cls")
                print()
                timed_print("Você recebeu outra chance do destino", 2)
                timed_print("...", 1)
                print()
                timed_print("Deseja tentar novamente? (S/n)", 1.5)
                escolha = input(" > : ").lower()
                if escolha == "n":
                    quit()
                elif escolha == "s":
                    os.system("cls")
                    game.Game().StartGame()

    def colisao(self, colisao):
        if colisao[0] == "i":
            self.brigar(colisao[2])
        elif colisao[0] == "b":
            colisao[2].GetItem()

    def brigar(self, inimigo_objeto):
        self.game.cenarioatual = Batalha(self, inimigo_objeto, self.game)