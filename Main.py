#Importar Librerias
from Colores.colors import red, green, bold, cyan, yellow 

import getpass

#Codigo Principal 
red()
user = input("Nombre de usuario:")


p = getpass.getpass()

yellow()
bold()
print("Bienvendido Agente", user)




