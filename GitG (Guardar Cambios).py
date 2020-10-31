import os

print('Git Graphical (GitG) (Guardar Cambios)')

print('\nTip: Si ya estas en el directorio pon "."')

# Pedirle el directorio al usuario
dirName = input(('Directorio del repositorio: '))

# Nombre del commit
commitName = input(('\nNombre del commit: '))

os.chdir(dirName)

os.system('git add .')

os.system('git commit -m "' + commitName + '"')

os.system('git push -u -f origin main')

print('\nTodo Listo!')
os.system('pause')
