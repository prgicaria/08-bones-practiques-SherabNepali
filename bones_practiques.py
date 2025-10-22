#!/usr/bin/env python

'''Divisió entera. Calcula el resultat d'una divisió entre dos nombres enters

Institut Icària
Programació - 1r Batxillerat - Curs 2025-26

El programa calcula el quocient i el residu d'una divisió en la qual tú dones 
el valor del dividend i el valor del divisor. En donar els dos valors el 
programa executa la divisió i inidica a la pantalla la divisió en forma de 
fracció, el quocient i el residu de la divisió'''

__author__ = "Sherab Odsel Nepali Dolkar" 
__email__ = "snepali@instituticaria.cat" 
__date__ = "22/10/2025"

dividend = int(input("Introdueix el dividend:"))
divisor = int(input("Introdueix el divisor:"))
quocient = dividend // divisor
residu = dividend % divisor
print(f"Divisió: {dividend}/{divisor}")
print("Quocient:", quocient)
print("Residu:", residu)