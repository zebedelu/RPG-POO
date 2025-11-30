from package.printer import *
import os, package.configs as configs
from modules.entities.player import Player
from modules.cenarios.map import GetRandomSpace

def CreatePlayer(game_engine):
    while True:
        timed_print("Insira seu nome para o jogador", 0.3)
        nome = input(" > :").capitalize()
        if len(nome) >= 3:
            break
        rgb(255,0,0)
        print("O nome têm que ter 3 letras ou mais!")
        rgb()

    print()
    os.system("cls")

    while True:
        for n, v in enumerate(configs.classes_disponiveis):
            print(f"({n+1}) {v}:\n\
                vida: "+str(configs.classes_disponiveis[v]["vida"])+"\n\
                dano: "+str(configs.classes_disponiveis[v]["inventario"][configs.classes_disponiveis[v]["equipado_id"]][1])+"\n\
                defesa: "+str(configs.classes_disponiveis[v]["defesa"]))
        
        timed_print("Insira o nome da sua classe para o jogador", 0.3)
        classe = input(" > :").lower()
        if classe in list(configs.classes_disponiveis.keys()):
            break
        rgb(255,0,0)
        print(f"Essa classe '{classe}' não existe!")
        rgb()

    print()

    player = Player(game=game_engine,
                    letra="p",
                    nome=nome,
                    classe=classe,
                    vida=configs.classes_disponiveis[classe]["vida"],
                    defesa=configs.classes_disponiveis[classe]["defesa"],
                    posicao=GetRandomSpace(game_engine.mapa_original),
                    nivel=1,
                    inventario=configs.classes_disponiveis[classe]["inventario"],
                    item_equipado=configs.classes_disponiveis[classe]["equipado_id"])
    
    return player