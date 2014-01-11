#!/usr/bin/python
# -*- coding: utf-8 -*- 

# Uso: python benchmark.py <URL>

import sys
import os

#Cogemos la URL del primer argumento:
url=sys.argv[1]

tiempos = []
tasas = []
repeticiones = 5

# Ejecutamos los test sin concurrencia:
for x in xrange(0,repeticiones):
	os.system("ab -c 1 -n 2500 "+url+" >> resSinConcurrencia")

resultados = file("resSinConcurrencia")
for line in resultados:
    array=line.split(" ")	#generamos una lista con las palabras de la línea
    if array[0]=="Time" and array[1]=="taken":	#buscamos las líneas que indican el tiempo
    	tiempos.append(array[6]) 	#añadimos el resultado, que está en la posición 6
    if array[0]=="Transfer" and array[1]=="rate:":	#buscamos las líneas que indican la tasa de transferencia
    	tasas.append(array[11]) 	#añadimos el resultado, que está en la posición 11
    

# Mostramos los resultados:
print("-------------- Resultados del test sin concurrencia --------------")
print("Tiempos, en segundos:")
for x in xrange(0,repeticiones):
	print("Repetición "+str(x)+" : "+tiempos[x])

print("Tasas de transferencia, en KB/s:")
for x in xrange(0,repeticiones):
	print("Repetición "+str(x)+" : "+tasas[x])

os.system("rm resSinConcurrencia")

# Ejecutamos los test con concurrencia:
for x in xrange(0,repeticiones):
	os.system("ab -c 100 -n 1900 "+url+" >> resConConcurrencia")

resultados = file("resConConcurrencia")
for line in resultados:
    array=line.split(" ")	#generamos una lista con las palabras de la línea
    if array[0]=="Time" and array[1]=="taken":	#buscamos las líneas que indican el tiempo
    	tiempos.append(array[6]) 	#añadimos el resultado, que está en la posición 6
    if array[0]=="Transfer" and array[1]=="rate:":	#buscamos las líneas que indican la tasa de transferencia
    	tasas.append(array[11]) 	#añadimos el resultado, que está en la posición 11
    

# Mostramos los resultados:
print("-------------- Resultados del test con concurrencia --------------")
print("Tiempos, en segundos:")
for x in xrange(0,repeticiones):
	print("Repetición "+str(x)+" : "+tiempos[x])

print("Tasas de transferencia, en KB/s:")
for x in xrange(0,repeticiones):
	print("Repetición "+str(x)+" : "+tasas[x])

os.system("rm resConConcurrencia")