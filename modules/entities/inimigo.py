from modules.entities.entitie import Entitie
from package.photos import photos
from modules.cenarios.map import GetRandomSpace

class Inimigo(Entitie):
    def __init__(self, game, player, nome, classe, vida, defesa, posicao, letra, nivel=1, inventario=[], item_equipado=-1):
        super().__init__(game, nome, classe, vida, defesa, posicao, letra, nivel, inventario, item_equipado)
        self.player = player
        self.photo = photos[self.nome]
    
    def dano(self, dano):
        self.vida -= (dano - self.defesa) if dano >= self.defesa else (dano/self.vida_max)*self.defesa

        self.vida = int(self.vida)
        if self.vida <= 0:
            print("")
            print("Nivel: +1")
            print("Sua vida se restaurou!")
            input("O inimigo morreu! mas ele sempre voltará...")
            self.player.defesa += self.defesa//2
            self.player.nivel += 1
            self.player.vida = self.player.vida_max
            self.player.contador_mortes += 1
    
    def renderSelf(self):
        print(f"Representação da criatura: {self.nome}")
        print(self.photo)