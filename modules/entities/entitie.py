from package.configs import colisiveis, escalaX, escalaY
import random
from package.printer import rgb_r

# Rômulo esteve aqui

class Entitie:
    def __init__(self, game, nome, classe, vida, defesa, posicao, letra, nivel=1, inventario=[], item_equipado=-1):
        self.nome = nome
        self.vida = vida
        self.nivel = nivel
        self.defesa = defesa
        self.classe = classe.capitalize()
        self.equipamento_id = item_equipado
        self.x, self.y = posicao
        self.vida_max = vida
        self.inventario = inventario

        self.cor = (random.randint(1,255),random.randint(1,255),random.randint(1,255))

        self.letra = letra

        self.game = game

    def mover(self, x, y):
        if self.game.mapa_to_show[self.y+y][self.x+x][0] in colisiveis:
            return self.game.mapa_to_show[self.y+y][self.x+x]
        
        self.x += x
        self.y += y
    
    def dano(self, dano):
        self.vida -= (dano - self.defesa) if dano >= self.defesa else (dano/self.vida_max)*self.defesa

        if self.vida <= 0:
            self.game.remove(self)
        
    def cura(self, cura):
        self.vida += cura if cura+self.vida <= self.vida_max else self.vida-self.vida_max

    def draw_in_map(self):
        self.game.mapa_to_show[self.y][self.x] = [self.letra, self.cor, self]

    def get_map(self):
        mapa = []
        for y in range(-escalaY,escalaY+1):
            mapa.append([])
            for x in range(-escalaX,escalaX+1):
                try:
                    mapa[-1].append(self.game.mapa_to_show[max(0,self.y+y)][max(0,self.x+x)])
                except:
                    break

        return mapa
    
    def remove_inventory_by_id(self, index):
        if self.equipamento_id == index:
            self.equipamento_id = -1
        else:
            self.equipamento_id -= 1

        self.inventario.pop(index)