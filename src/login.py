import os
from src.ospause import pause
from src.osclear import clear

def requestLogin(come):
    from GitG import Main
    from GitGSave import MainSave

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
        Main() # Llamar a la funcion principal
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
        MainSave() # Llamar a la funcion principal
