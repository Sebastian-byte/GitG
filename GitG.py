import os
import platform
from pathlib import Path 

system = platform.system()
home = str(Path.home())

if system == 'Windows':
    pause = 'pause'
elif system == 'Linux':
    pause = "read -rsp $'Presione una tecla para continuar...\n' -n 1 key"
elif system == 'Darwin':
    pause = "read -rsp $'Presione una tecla para continuar...\n' -n 1 key"
else:
    print('Sistema no compatible!')
    quit()

def clear():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")

# Funcion principal
def Main():
    print('Git Graphical (GitG)')
    
    print('\nTip: Si ya estas en el directorio pon "."')

    # Pedirle el directorio al usuario
    dirName = input(('Directorio del repositorio: '))

    # Nombre del commit inicial
    commitName = input(('\nNombre del commit: '))

    # Nombre del usuario, para agregar a la URL
    user = input(('\nNombre de usuario: '))

    # Nombre del repositorio a hacer commit
    repo = input(('\nNombre del repositorio: '))

    os.chdir(dirName)

    os.system('git init')

    os.system('git add .')

    os.system('git commit -m "' + commitName + '"')

    os.system('git branch -M main')

    os.system('git remote add origin https://github.com/' + user + '/' + repo + '/')

    os.system('git push -u -f origin main')

    print('\nTodo Listo!')
    os.system(pause)

# Revisar si el usuario ya inicio sesión.
if os.path.exists(home + '/.gitconfig'):
    Main()
# Si no lo ha hecho, Pedirle que lo haga.
else:
    print('Git Graphical (GitG)')
    print('\nTienes que iniciar sesion en Github!')
    # Pedir nombre al usuario
    username = input(('\nNombre de usuario: '))
    # Pedir correo al usuario
    email = input(('Correo: '))
    # Pedir contraseña al usuario
    password = input(('Contraseña: '))
    # Guardar informacion en archivo .gitconfig
    os.system('git config --global user.name "' + username + '"')
    os.system('git config --global user.email ' + email)
    os.system('git config --global user.password "' + password + '"')
    print('\nInicio exitoso!')
    os.system(pause)
    clear() # Limpiar la consola
    Main() # Llamar a la funcion principal
    
