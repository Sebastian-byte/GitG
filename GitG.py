import os
from pathlib import Path
from lib.osclear import clear
from lib.ospause import pause

home = str(Path.home())

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

    # Nombre del repositorio, para agregar a la URL
    repo = input(('\nNombre del repositorio: '))

    # Revisar si existe el directorio
    if os.path.exists(dirName): 
        os.chdir(dirName)
    # Si no existe, informarle al usuario y llevarlo al inicio
    else:
        print('\nEse directorio no existe!, intentalo de nuevo.')
        os.system(pause)
        clear() # Limpiar
        Main() # Llevar a la funcion principal

    os.system('git init')

    os.system('git add .')

    os.system('git commit -m "' + commitName + '"')

    os.system('git branch -M main')

    os.system('git remote add origin https://github.com/' + user + '/' + repo + '/')

    os.system('git push -u -f origin main')

    print('\nTodo Listo!')
    pause()

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
    os.system('git config --global user.email ' + email)
    os.system('git config --global user.name "' + username + '"')
    os.system('git config --global user.password "' + password + '"')
    
    print('\nInicio exitoso!')
    
    pause() # Pausar la consola
    clear() # Limpiar la consola
    Main() # Llamar a la funcion principal
