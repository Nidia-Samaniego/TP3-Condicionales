#actividad 1
#edad= int(input("Ingrese su edad:"))

#if edad >= 18:
    #print("Sos mayor de edad")
#else:
    #print("Sos menor de edad")

#actividad 2

#nota= int(input("Ingrese su nota: "))

#if nota >= 6:
    #print("Aprobado")
#else:
    #print("desaprobado")

#ejercicio 3

#numero = int(input("Ingrese un numero: "))

#if numero % 2 == 0 :
    #print("Ha ingresado un numero par")
#else:
    #print("Por favor ingrese un numero par")

#ejercicio 4

#suedad= int(input("Ingrese su edad: "))

#if suedad < 12:
    #print("Usted es un Niño/a")
#elif suedad >=12 and suedad < 18:
    #print("Usted es adolescente ")
#elif suedad >= 18 and suedad < 30:
    #print("Usted es adulto/a joven")
#else:
    #print("Usted es mayo")


#ejercicio 5 

#contraseña= input("Ingrese una contraseña de entre 8 y 14 caracteres: ")
#longitud = len(contraseña)

#if longitud >=8 and longitud<= 14:
    #print("Ha ingresado una contraseña correcta")
#else:
    #print("Por favor ingrese una contraseña de entre 8 y 14 caracteres")

#ejercicio 6

import random
numeros_aletorios = [random.randint(1,100) for i in range(50)]
from statistics import mode, median, mean
mean (numeros_aletorios)

if numeros_aletorios == mode:
    print("Hay sesgo positivo")
elif numeros_aletorios == median:
    print("Hay sesgo negativo")
else:
    print("sin sesgo")




    
   
   