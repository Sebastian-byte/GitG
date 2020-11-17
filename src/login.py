"""Module to request login for Git"""

import os
from getpass import getpass
from validate_email import validate_email
from .ospause import pause
from .osclear import clear
from .console_tools import ColorText


color = ColorText()


def request_login(come):
    """Request login and go to the main functions."""

    if come == 1:
        from GitG import main
        print('Git Graphical (GitG)')

        print(color.green('\nTienes que iniciar sesion en Github!'))

        # Pedir nombre al usuario
        username = input(color.blue('\nNombre de usuario: '))

        # Pedir correo al usuario
        email = input(color.blue('Correo: '))

        emailcheck = validate_email(email_address=email, check_regex=True, check_mx=True, use_blacklist=True)
        if emailcheck == True:
            pass
        else:
            print(color.red('Email Invalido!, Porfavor vuelve a intentarlo.'))
            request_login(come)

        # Pedir contraseña al usuario
        password = getpass(color.blue('Contraseña: '))

        # Guardar informacion en archivo .gitconfig
        os.system(f'git config --global user.email {email}')
        os.system(f'git config --global user.name "{username}"')
        os.system(f'git config --global user.password "{password}"')

        print('\nInicio exitoso!')

        pause()  # Pausar la consola
        clear()  # Limpiar la consola
        main()  # Llamar a la funcion principal
    elif come == 2:
        from GitGSave import main_save
        print('Git Graphical (GitG)')

        print(color.green('\nTienes que iniciar sesion en Github!'))

        # Pedir nombre al usuario
        username = input(color.blue('\nNombre de usuario: '))

        # Pedir correo al usuario
        email = input(color.blue('Correo: '))

        emailcheck = validate_email(email_address=email, check_regex=True, check_mx=True, use_blacklist=True)
        if emailcheck == True:
            pass
        else:
            print(color.red('Email Invalido!, Porfavor vuelve a intentarlo.'))
            pause()
            clear()
            request_login(come)

        # Pedir contraseña al usuario
        password = getpass(color.blue('Contraseña: '))

        # Guardar informacion en archivo .gitconfig
        os.system(f'git config --global user.email {email}')
        os.system(f'git config --global user.name "{username}"')
        os.system(f'git config --global user.password "{password}"')

        print('\nInicio exitoso!')

        pause()  # Pausar la consola
        clear()  # Limpiar la consola
        main_save()  # Llamar a la funcion principal
