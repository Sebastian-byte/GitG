import os
from pathlib import Path
from lib.osclear import clear
from lib.ospause import pause

home = str(Path.home())

def Main():
    print('Git Graphical (GitG) (Guardar Cambios)')

    print('\nTip: Si ya estas en el directorio pon "."')

    # Pedirle el directorio al usuario
    dirName = input(('Directorio del repositorio: '))

    # Nombre del commit
    commitName = input(('\nNombre del commit: '))

    # Revisar si existe el directorio
    if os.path.exists(dirName): 
        os.chdir(dirName)
    # Si no existe, informarle al usuario y llevarlo al inicio
    else:
        print('\nEse directorio no existe!, intentalo de nuevo.')
        pause() # Pausar
        clear() # Limpiar
        Main() # Llamar a la funcion principal

    os.system('git add .')

    os.system('git commit -m "' + commitName + '"')

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
