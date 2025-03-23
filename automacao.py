import subprocess
import os
from objeto import Texto
def menu():
    arqat = []
    arqs = subprocess.getoutput("ls exs/ex*.py").splitlines()
    for a in arqs:
         arqat.append(a.replace("exs/", "").replace(".py", ""))
    arqat.append("Finalizar")
    os.system("clear")
    global texto
    Texto.tabela(arqat)
    esc = input("Escolha: ")
    if(esc.isnumeric()):
        esc = int(esc)
        if(esc == len(arqat)):
            exit()
        else:
            if(esc >= 1 and esc < len(arqat)):
                os.system("clear")
                comando = f"python3 {arqs[esc-1]}"
                os.system(comando)
                input("")
                menu()

            else:
                menu()
    else:
        menu()





menu()