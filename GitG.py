import os
import platform

system = platform.system()

if system == 'Windows':
    pause = 'pause'
elif system == 'Linux':
    pause = "read -rsp $'Presione una tecla para continuar...\n' -n 1 key"
elif system == 'Darwin':
    pause = "read -rsp $'Presione una tecla para continuar...\n' -n 1 key"
else:
    print('Sistema no compatible!')
    quit()

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
