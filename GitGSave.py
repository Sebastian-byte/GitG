"""Saves changes, and up it to a Github repository"""

import os
import sys
import time
from pathlib import Path

try:
    from src.console_tools import ColorText
    from src.osclear import clear
    from src.ospause import pause
    from src.login import request_login
except ImportError:
    print('Hacen falta archivos necesarios para la ejecucion, asegurate que todos los archivos estan completos.')
    sys.exit(1)

color = ColorText()

try:
    from progressbar import progressbar
except ImportError:
    print('Instalando Dependencias...')
    if sys.platform.startswith('win32'):
        try:
            os.system('python -m pip install progressbar2')
            from progressbar import progressbar
            clear()
        except Exception as error:
            print(color.red(f'Ha ocurrido un error fatal y no se han instalado las dependencias\nError: {error}'))
            sys.exit(1)
    else:
        try:
            os.system('python3 -m pip install progressbar2')
            from progressbar import progressbar
            clear()
        except Exception as error:
            print(color.red(f'Ha ocurrido un error fatal y no se han instalado las dependencias\nError: {error}'))
            sys.exit(1)


HOME = str(Path.home())

if len(sys.argv) >= 2:
    arg = sys.argv[1]
    if arg == '--version':
        print(color.red('\nGitGSave'))
        print('Version 0.9')
        print('Thanks for testing!')
else:
    pass


def main_save():
    """Main function to do the before mentionated."""
    print('Git Graphical (GitG) (Guardar Cambios)')

    print('\nTip: Si ya estas en el directorio pon "."')

    # Pedirle el directorio al usuario
    dir_name = input('Directorio del repositorio: ')

    # Nombre del commit
    commit_name = input('\nNombre del commit: ')

    # Revisar si existe el directorio
    if os.path.exists(dir_name):
        os.chdir(dir_name)
    # Si no existe, informarle al usuario y llevarlo al inicio
    else:
        print(color.red('\nEse directorio no existe!, intentalo de nuevo.'))
        pause()  # Pausar
        clear()  # Limpiar
        main_save()  # Llamar a la funcion principal

    loopvar = 1
    if sys.platform.startswith('win32'):
        nullvar = '>nul 2>&1'
    else:
        nullvar = '&> /dev/null'

    for i in progressbar(range(20)):
        if loopvar == 1:
            os.system(f'git add -A {nullvar}')
            os.system(f'git commit -m "{commit_name}" {nullvar}')

            try:
                os.system(f'git push{nullvar}')
            except OSError:
                os.system(f'git pull{nullvar}')
                os.system(f'git push{nullvar}')

        if loopvar >= 2:
            time.sleep(0.1)
        loopvar = loopvar + 1

    del i
    del loopvar

    print('\nTodo Listo!')
    pause()
    sys.exit(0)


if len(sys.argv) >= 2:
    pass
else:
    # Revisar si el usuario ya inicio sesión.
    if os.path.exists(HOME + '/.gitconfig'):
        main_save()
    # Si no lo ha hecho, Pedirle que lo haga.
    else:
        request_login(2)
