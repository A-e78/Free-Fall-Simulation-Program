from platform import python_version
print("Python " + python_version())

import sys
import math
import sympy
import numpy as np

# Abrir archivos para escritura
archivo = open("caida.xyz", "w")
archiva = open("caida.dat", "w")

# Solicitar valores de entrada al usuario
print("")
x0 = float(input('x0: '))
y0 = float(input('y0: '))
n = int(input('npasos: '))
print("")

# Declaración de constantes
sigmar = 3.16
grave = 9.81
dt = 0.005
tiempo = 0.0

# Loop para calcular posiciones y escribir en archivos
for i in range(0, n + 1):
    archivo.write(str(1) + '\n')
    archivo.write('\n')
    
    x = 0.0
    z = 0.0
    y = y0 - (grave * tiempo * tiempo) / 2.0
    y = y * sigmar
    
    archiva.write(f"{x} {y}\n")
    archivo.write(f"H {x} {y} {z}\n")
    
    tiempo += dt

# Cerrar archivos
archivo.close()
archiva.close()

print("\nArchivo caida.xyz generado")
print("\nArchivo caida.dat generado")

print('')
print("¡Ya terminé!")
print('')
