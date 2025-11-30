import time, random

def rgb(r=-1, g=-1, b=-1, variation=0):
    v = variation
    if sum([r,g,b]) == -3:
        print('\033[0m',end="")
        return

    r = min(255, max(0, r+random.randint(-1,1)*v))
    g = min(255, max(0, g+random.randint(-1,1)*v))
    b = min(255, max(0, b+random.randint(-1,1)*v))

    print(f"\033[38;2;{r};{g};{b}m",end="")
    
def rgb_r(r=-1, g=-1, b=-1):
    if sum([r,g,b]) == -3:
        return '\033[0m'
    return f"\033[38;2;{r};{g};{b}m"

def timed_print(mensagem, tempo=1):
    for letra in mensagem:
        time.sleep(tempo/len(mensagem))
        print(letra,end="",flush=True)