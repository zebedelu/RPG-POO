
from package.printer import *
from package.configs import *
import random

def GetRandomSpace(mapa):
    espacos_escontrados = []
    for x, linha in enumerate(mapa):
        for y, elemento in enumerate(linha):
            if elemento == " ":
                espacos_escontrados.append([y,x])
    return random.choice(espacos_escontrados)

def RenderMap(self):
    print("-"*120)
    for indice_linha, linha in enumerate(self.player.get_map()):
        for _ in range(height):
            print("|",end="")
            for indice_block, bloco in enumerate(linha):
                if type(bloco) != type([]):
                    bloco = [bloco, None]

                #[" ", (255,128,64), objeto_player]

                if indice_block != 0 and linha[indice_block-1] == " " and bloco[0] != " ":
                    rgb(100,100,100)
                    print(random.choice(cenario_objs_letra[bloco[0]]), end="")
                    rgb()
                else:
                    if bloco[1] != None: rgb(*bloco[1], variation=8)
                    print(random.choice(cenario_objs_letra[bloco[0]]), end="")
                    rgb()

                for _1 in range(width):
                    if bloco[1] != None: rgb(*bloco[1], variation=8)
                    print(random.choice(cenario_objs_letra[bloco[0]]), end="")
                    rgb()

            print("|",end="")
            
            if (indice_linha, _) in list(rightpainel.keys()):
                painelinfo = rightpainel[(indice_linha, _)]
                print(painelinfo[0], eval(painelinfo[1]) if painelinfo[1] else "")
                rgb()
            else:
                print()
    print("-"*120)