"""Create Git repo, and publish to Github"""

import os
import sys
import time
import subprocess
import urllib.request
from pathlib import Path

try:
    from src.console_tools import ColorText
    from src.osclear import clear
    from src.ospause import pause
    from src.login import request_login
except ImportError:
    print("Hacen falta archivos necesarios para la ejecucion, asegurate que todos los archivos estan completos.", file=sys.stderr)
    sys.exit(1)

color = ColorText()

try:
    from progressbar import progressbar
    from dotenv import load_dotenv
except ImportError:
    print("Instalando Dependencias...")
    if sys.platform.startswith("win32"):
        try:
            subprocess.run(["pip" "install progressbar2"], shell=True)
            subprocess.run(["pip" "install python-dotenv"], shell=True)
            from progressbar import progressbar
            from dotenv import load_dotenv
            clear()
        except Exception as error:
            print(color.red(f"Ha ocurrido un error fatal y no \
se han instalado las dependencias\nError: {error}"), file=sys.stderr)
            sys.exit(1)
    else:
        try:
            subprocess.run(["pip3" "install progressbar2"])
            subprocess.run(["pip3" "install python-dotenv"])
            from progressbar import progressbar
            from dotenv import load_dotenv
            clear()
        except Exception as error:
            print(color.red(f"Ha ocurrido un error fatal y no \
se han instalado las dependencias\nError: {error}"), file=sys.stderr)
            sys.exit(1)

HOME = str(Path.home())

if len(sys.argv) >= 2:
    arg = sys.argv[1]
    if arg == "--version":
        print(color.red("\nGitG"))
        print("Version 0.9")
        print("Thanks for testing!")
else:
    pass


# Funcion principal
def main():
    """Main function to do the before mentionated."""
    print("Git Graphical (GitG)")

    print('\nTip: Si ya estas en el directorio pon "."')

    # Pedirle el directorio al usuario
    dir_name = input(("Directorio del repositorio: "))

    # Nombre del commit inicial
    commit_name = input(("\nNombre del commit: "))

    # Nombre del usuario, para agregar a la URL
    if not os.path.exists("./.env"):
        user = input(("\nNombre de usuario: "))
        with open("./.env", "w") as data:
            data.write(f"USERNAME={user}")

    # Nombre del repositorio, para agregar a la URL
    repo = input(("\nNombre del repositorio: "))

    # Revisar si existe el directorio
    if os.path.exists(dir_name):
        os.chdir(dir_name)
    # Si no existe, informarle al usuario y llevarlo al inicio
    else:
        print(color.red("\nEse directorio no \
existe!, intentalo de nuevo."), file=sys.stderr)
        pause()  # Pausar
        clear()  # Limpiar
        main()  # Llamar a la funcion principal

    if not sys.platform.startswith("win32"):
        if not os.path.exists("./.env"):
            checkurl = urllib.request.urlopen(f"https://\
github.com/{user}/{repo}.git").getcode()
        else:
            username = os.getenv("USERNAME")
            checkurl = urllib.request.urlopen(f"https://\
github.com/{username}/{repo}.git").getcode()

        if checkurl == 200 or 202:
            pass
        else:
            print(color.red("Ese repositorio no \
existe!, intentalo de nuevo."), file=sys.stderr)
            pause()
            clear()
            main()
    else:
        pass

    loopvar = 1
    if sys.platform.startswith("win32"):
        nullvar = ">nul 2>&1"
    else:
        nullvar = "&> /dev/null"

    for i in progressbar(range(20)):
        if loopvar == 1:
            subprocess.run(["git" f"init {nullvar}"], shell=True)
            subprocess.run(["git" "add -A"], shell=True)

            subprocess.run(['git' f'commit -m \
"{commit_name}" {nullvar}'], shell=True)
            subprocess.run(["git" f"branch -M \
main {nullvar}"], shell=True)

            if not os.path.exists("./.env"):
                subprocess.run(['git' f'remote add origin \
"https://github.com/{user}/{repo}.git" {nullvar}'], shell=True)
            else:
                username = os.getenv("USERNAME")
                subprocess.run(['git' f'remote add origin \
"https://github.com/{username}/{repo}.git" {nullvar}'],  shell=True)

            try:
                subprocess.run(["git" f"push -u origin \
main {nullvar}"], shell=True)
            except OSError:
                subprocess.run(["git" f"pull {nullvar}"], shell=True)
                subprocess.run(["git" f"push -u origin \
main {nullvar}"], shell=True)

        if loopvar >= 2:
            time.sleep(0.1)
        loopvar += 1

    del i
    del loopvar

    print("\nTodo Listo!")
    pause()
    sys.exit(0)


if len(sys.argv) >= 2:
    pass
else:
    # Revisar si el usuario ya inicio sesión.
    if os.path.exists(HOME + "/.gitconfig"):
        main()
    # Si no lo ha hecho, Pedirle que lo haga.
    else:
        request_login(1)
