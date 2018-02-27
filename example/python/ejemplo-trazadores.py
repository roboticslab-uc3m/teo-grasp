# -*- coding: utf-8 -*-

#----------------------------------------------------------------------
# Nombre:       ejemplo_trazadores.py
# Proposito:    Aprender como interpolar usando trazadores con python.
#
# Autor:        Raúl de Santos Rico
#
# Creacion:     27 de Febrero de 2018
# Historia:
#
# Dependencias:    scipy
# Licencia:        GPL
#----------------------------------------------------------------------

"""
Ejemplo de trazadores o splines (curvas polinómicas definidas a trozos)
"""
import numpy as np
import matplotlib.pyplot as plt # graficos
from scipy.interpolate import InterpolatedUnivariateSpline # trazador cubico

print("Trazador bidimensional con interpolación 1.0")
print("--------------------------------------------")

print("Elija los puntos por los que desea pasar: ")
puntos = input()

# Matriz bidimensional de puntos 
matriz = []

for i in range(puntos):
    matriz.append([])
    print("indique las coordenadas (x,y) del pto "+str(i))
    for j in range(2): # 2 columnas (bidimensional)        
        if j == 0: 
            print('x: ')            
        else:
            print('y: ')
        matriz[i].append(input())
        
print("-------------------------------------------")   
print("Indique la resolución de la interpolación: ")
res = input()  
print("Indique el grado del trazador (Ej: 1-lineal, 2-cuadrado, 3-cúbico.... 5)")  
k = input() 
    
# Puntos de ejemplo
"""
P = [(0.9, 1.3), (1.3, 1.5), (1.9, 1.8), (2.1,2.1), (2.6, 2.6), (3.0, 2.7),
     (3.9, 2.3), (4.4, 2.1), (4.8, 2.0), (5.0, 2.1), (6, 2.2), (7, 2.3),
     (8, 2.2), (9.1, 1.9), (10.5, 1.4), (11.2, 0.9), (11.6, 0.8), (12, 0.6),
     (12.6, 0.5), (13, 0.4), (13.2, 0.2)] # lista de puntos
"""

xi, yi = zip(*matriz) 
x = np.linspace(min(xi), max(xi), num=res)  # Dominio
# y1d = np.interp(x, xi, yi) # El trazador más elemental lineal (grado 1)
# y1d = InterpolatedUnivariateSpline(xi, yi, k=1)(x)  # Mismo resultado donde k es el grado del trazador
ysp = InterpolatedUnivariateSpline(xi, yi, k=k)(x)  # Llamamos a la clase con x. K por defecto es cúbico (grado 3)

# Imprimimos los valores de (x, y) resultantes de la interpolación
for i in range (len(x)):
    print 'Pto '+str(i)+': (x, y) = ('+str(x[i])+', '+str(ysp[i])+')'


# Dibujamos la grafica con los puntos
plt.plot(xi, yi, 'o', x, ysp, '-')

# Añadimos la leyenda
plt.legend(('Puntos conocidos', 'Interpolacion'))

# añadimos las etiquetas
plt.xlabel('Eje x')
plt.ylabel('Eje y')

# Mostramos en pantalla
plt.show()