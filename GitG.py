import os

print('Git Graphical (GitG)')

dirName = input(('\nDirectorio del repositorio: '))
commitName = input(('\nNombre del commit: '))
user = input(('\nNombre de usuario: '))
repo = input(('\nNombre del repositorio: '))

# Esta linea debe modificarse -> Colocar la ubicacion de nuestra carpeta. Nota: va todo separado con '\\'
os.chdir(dirName)

os.system('git init')

os.system('git add .')

os.system('git commit -m "' + commitName + '"')

os.system('git branch -M main')

# Esta linea debe modificarse -> Colocar la ruta de nuestro repositorio
os.system('git remote add origin https://github.com/' + user + '/' + repo + '/')

os.system('git push -u origin main')

print('quiza completado')
os.system('pause')
