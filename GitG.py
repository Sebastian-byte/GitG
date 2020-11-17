﻿"""Create Git repo, and publish to Github"""

import os
import sys
from pathlib import Path
from src.osclear import clear
from src.ospause import pause
from src.login import request_login

HOME = str(Path.home())

# Funcion principal
def main():
    """Main function to do the before mentionated."""
    print('Git Graphical (GitG)')

    print('\nTip: Si ya estas en el directorio pon "."')

    # Pedirle el directorio al usuario
    dir_name = input(('Directorio del repositorio: '))

    # Nombre del commit inicial
    commit_name = input(('\nNombre del commit: '))

    # Nombre del usuario, para agregar a la URL
    user = input(('\nNombre de usuario: '))

    # Nombre del repositorio, para agregar a la URL
    repo = input(('\nNombre del repositorio: '))

    # Revisar si existe el directorio
    if os.path.exists(dir_name):
        os.chdir(dir_name)
    # Si no existe, informarle al usuario y llevarlo al inicio
    else:
        print('\nEse directorio no existe!, intentalo de nuevo.')
        pause() # Pausar
        clear() # Limpiar
        main() # Llamar a la funcion principal

    os.system('git init')

    os.system('git add .')

    os.system('git commit -m "' + commit_name + '"')

    os.system('git branch -M main')

    os.system('git remote add origin https://github.com/' + user + '/' + repo + '/')

    try:
        os.system('git push -u origin main')
    except:
        os.system('git pull')
        os.system('git push -u origin main')

    print('\nTodo Listo!')
    pause()
    sys.exit(0)


# Revisar si el usuario ya inicio sesión.
if os.path.exists(HOME + '/.gitconfig'):
    main()
# Si no lo ha hecho, Pedirle que lo haga.
else:
    request_login(1)
