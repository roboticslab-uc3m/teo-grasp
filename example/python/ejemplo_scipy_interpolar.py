#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import division

#----------------------------------------------------------------------
# Nombre:       ejemplo_scipy_interpolar.py
# Proposito:    Aprender como interpolar con python.
#
# Autor:        Raúl de Santos Rico
#
# Creacion:     23 de Febrero de 2018
# Historia:
#
# Dependencias:    scipy
# Licencia:        GPL
#----------------------------------------------------------------------

"""
Ejemplo de como hacer una interpolacion en python.
"""
import scipy as sp                  # Importamos scipy como el alias sp
from scipy import interpolate       # Importamos interpolate de scipy
import matplotlib.pyplot as plt     # Importamos matplotlib.pyplot como el alias plt

# Creamos el array dimensional
x = sp.linspace(0,3,10) # Crea un array con valor inicial start, valor final stop y num elementos

# Evaluamos x en la funcion y = e^(-x/3) (generando nuestros "datos experimentales")
y = 2*x**2+1 # ecuacion de la curva sp.exp(-x/3.0)

# Interpolamos
interpolacion = interpolate.interp1d(x, y)

# Creamos un nuevo array dimensional con mas puntos en el mismo intervalo
x2 = sp.linspace(0,3,10)

# Evaluamos x2 en la interpolacion
y2 = interpolacion(x2)

for i in range (len(x2)-1):
    print '(x, y) = ('+str(x2[i])+', '+str(y2[i])+')'


# Creamos la figura
# plt.figure

# Dibujamos las dos graficas juntas
plt.plot(x, y, 'o', x2, y2, '-')

# Añadimos la leyenda
# plt.legend(('Datos conocidos', 'Datos experimentales'))

# añadimos las etiquetas
plt.xlabel('Eje x')
plt.ylabel('Eje y')

# Mostramos en pantalla
plt.show()