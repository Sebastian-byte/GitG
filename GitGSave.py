import os
import sys
from pathlib import Path
from src.osclear import clear
from src.ospause import pause
from src.login import requestLogin

Home = str(Path.home())

def MainSave():
    print('Git Graphical (GitG) (Guardar Cambios)')

    print('\nTip: Si ya estas en el directorio pon "."')

    # Pedirle el directorio al usuario
    Dir_Name = input(('Directorio del repositorio: '))

    # Nombre del commit
    Commit_Name = input(('\nNombre del commit: '))

    # Revisar si existe el directorio
    if os.path.exists(Dir_Name): 
        os.chdir(Dir_Name)
    # Si no existe, informarle al usuario y llevarlo al inicio
    else:
        print('\nEse directorio no existe!, intentalo de nuevo.')
        pause() # Pausar
        clear() # Limpiar
        MainSave() # Llamar a la funcion principal

    os.system('git add .')

    os.system('git commit -m "' + Commit_Name + '"')

    os.system('git push -u -f origin main')

    print('\nTodo Listo!')
    pause()
    sys.exit(0)


# Revisar si el usuario ya inicio sesión.
if os.path.exists(Home + '/.gitconfig'):
    MainSave()
# Si no lo ha hecho, Pedirle que lo haga.
else:
    requestLogin(2)
