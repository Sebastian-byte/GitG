import os
from src.ospause import pause
from src.osclear import clear

def request_login(come):
    from GitG import main
    from GitGSave import main_save

    if come == 1:
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
        main() # Llamar a la funcion principal
    elif come == 2:
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
        main_save() # Llamar a la funcion principal
