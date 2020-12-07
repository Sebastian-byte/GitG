"""Module to request login for Git"""

import os
import sys
from getpass import getpass

try:
    from .ospause import pause
    from .osclear import clear
    from .console_tools import ColorText
except ImportError:
    print('Hacen falta archivos necesarios para la ejecucion, asegurate que todos los archivos esten completos.')
    sys.exit(1)

try:
    from validate_email import validate_email
except ImportError:
    print('Instalando dependencias...')
    if sys.platform.startswith('win32'):
        try:
            os.system('python -m pip install -r requirements.txt')
            from validate_email import validate_email
            clear()
        except Exception as error:
            print(f'Ha ocurrido un error fatal y no se han instalado las dependencias\nError: {error}')
            sys.exit(1)
    else:
        try:
            os.system('python3 -m pip install -r requirements.txt')
            from validate_email import validate_email
            clear()
        except Exception as error:
            print(f'Ha ocurrido un error fatal y no se han instalado las dependencias\nError: {error}')
            sys.exit(1)


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
        if emailcheck is True:
            pass
        else:
            print(color.red('Email Invalido!, Porfavor vuelve a intentarlo.'))
            pause()
            clear()
            request_login(come)

        # Pedir contraseña al usuario
        password = getpass(color.blue('Contraseña: '))

        # Guardar credenciales en archivo .gitconfig
        try:
            if not sys.platform.startswith('win32'):
                os.system('git config credential.helper store')
            else:
                pass
            os.system(f'git config --global user.email {email}')
            os.system(f'git config --global user.name "{username}"')
            os.system(f'git config --global user.password "{password}"')
            print('\nInicio exitoso!')
            pause()
            clear()
            main()
        except Exception as error:
            print(f'Ha ocurrido un error fatal y no se han podido guardar tus credenciales.\nError: {error}')
            sys.exit(1)

    elif come == 2:
        from GitGSave import main_save
        print('Git Graphical (GitG)')

        print(color.green('\nTienes que iniciar sesion en Github!'))

        # Pedir nombre al usuario
        username = input(color.blue('\nNombre de usuario: '))

        # Pedir correo al usuario
        email = input(color.blue('Correo: '))

        # Solo para asegurarse que no se haya equivocado o este mientiendo
        emailcheck = validate_email(email_address=email, check_regex=True, check_mx=True, use_blacklist=True)
        if emailcheck is True:
            pass
        else:
            print(color.red('Email Invalido!, Porfavor vuelve a intentarlo.'))
            pause()
            clear()
            request_login(come)

        # Pedir contraseña al usuario
        password = getpass(color.blue('Contraseña: '))

        # Guardar credenciales en archivo .gitconfig
        try:
            if not sys.platform.startswith('win32'):
                os.system('git config credential.helper store')
            else:
                pass
            os.system(f'git config --global user.email {email}')
            os.system(f'git config --global user.name "{username}"')
            os.system(f'git config --global user.password "{password}"')
            print('\nInicio exitoso!')
            pause()
            clear()
            main_save()
        except Exception as error:
            print(f'Ha ocurrido un error fatal y no se han podido guardar tus credenciales.\nError: {error}')
            sys.exit(1)
