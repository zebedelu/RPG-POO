import copy, os, random
from package.printer import *
from package.configs import *
from modules.cenarios.inventario import CenarioInventario

class CenarioDefault:
    def __init__(self, game):
        self.game = game

    def update(self):
        self.game.mapa_to_show = copy.deepcopy(self.game.mapa_original)

        print('''W, A, S e D para se mover.
E para abrir inventário.''')

        tecla = input().lower()
        mover = None
        if tecla in movs and len(tecla) >= 1:
            mover = movs[tecla[0]]
            self.game.ultimatecla = tecla
        elif tecla == "e":
            self.game.cenarioatual = CenarioInventario(self.game)
            self.game.cenarioatual.update()
        else:
            tecla = self.game.ultimatecla
            mover = movs[tecla[0]]
        
        for entidade in self.game.entities:
            entidade.draw_in_map()
            
        if mover:
            colisao = self.game.player.mover(*mover)

            #colisao
            if not (colisao is None):
                self.game.player.colisao(colisao)

            #mover o inimigo
            escolhido = random.choice(self.game.entities)
            if hasattr(escolhido, "player"):
                r = random.randint(-1,1)
                #controlar direção
                move = [0,r] if random.randint(0,1) == 1 else [r,0]

                directionX, directionY = 0,0
                try:
                    directionX = round((self.game.player.x-escolhido.x)/abs(self.game.player.x-escolhido.x), 0)
                    directionY = round((self.game.player.y-escolhido.y)/abs(self.game.player.y-escolhido.y), 0)
                except:
                    pass

                move = move if random.randint(1,5) < 2 else [int(directionX), int(directionY)]
                move = [0,move[1]] if random.randint(0,1) == 1 else [move[0],0]
                
                colisao = escolhido.mover(*move)
                if colisao and colisao[0] == "p":
                    self.game.player.colisao(["i", escolhido.cor, escolhido])
        
        self.game.resetScreen()

        for entidade in self.game.entities:
            entidade.draw_in_map()

        os.system("cls")