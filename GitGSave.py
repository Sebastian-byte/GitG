"""Saves changes, and up it to a Github repository"""

import os
import sys
from pathlib import Path
from src.osclear import clear
from src.ospause import pause
from src.login import request_login

HOME = str(Path.home())

def main_save():
    """Main function to do the before mentionated."""
    print('Git Graphical (GitG) (Guardar Cambios)')

    print('\nTip: Si ya estas en el directorio pon "."')

    # Pedirle el directorio al usuario
    dir_name = input(('Directorio del repositorio: '))

    # Nombre del commit
    commit_name = input(('\nNombre del commit: '))

    # Revisar si existe el directorio
    if os.path.exists(dir_name):
        os.chdir(dir_name)
    # Si no existe, informarle al usuario y llevarlo al inicio
    else:
        print('\nEse directorio no existe!, intentalo de nuevo.')
        pause() # Pausar
        clear() # Limpiar
        main_save() # Llamar a la funcion principal

    os.system('git add .')

    os.system('git commit -m "' + commit_name + '"')

    os.system('git push -u -f origin main')

    print('\nTodo Listo!')
    pause()
    sys.exit(0)


# Revisar si el usuario ya inicio sesión.
if os.path.exists(HOME + '/.gitconfig'):
    main_save()
# Si no lo ha hecho, Pedirle que lo haga.
else:
    request_login(2)
