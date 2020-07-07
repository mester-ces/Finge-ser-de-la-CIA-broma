#Importar Librerias
from Colores.colors import red, green, bold, cyan, yellow, reset

import getpass

#Codigo Principal 
red()
user = input("Nombre de usuario:")


p = getpass.getpass()


reset()
yellow()
print("Bienvendido Agente", user)




