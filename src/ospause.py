import os
def pause():
    if os.name == 'nt':
        os.system('pause')
    else:
        os.system("read -rsp $'Presione una tecla para continuar...\n' -n 1 key")
