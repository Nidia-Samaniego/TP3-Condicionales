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

#import random
#numeros_aletorios = [random.randint(1,100) for i in range(50)]
#from statistics import mode, median, mean

#moda= mode(numeros_aletorios)
#mediana= median(numeros_aletorios)
#media= mean(numeros_aletorios)

#if media > mediana and mediana > moda:
    #print("Hay sesgo positivo")
#elif media < mediana and mediana < moda:
    #print("Hay sesgo negativo")
#else:
    #print("sin sesgo")

#Ejercicio 7

#palabra= input("Ingrese una palabra o frase: ")

#if palabra [-1].lower() in "aeiou":
    #print(palabra + "!")
#else:
    #print(palabra)

#ejercicio 8 

#nombre=input("Ingrese su nombre: ")
#print("Ingrese una opcion para mostrar su nombre: ")
#print("1- En mayuscula")
#print("2- En minuscula")
#print("3- La primer letra en mayuscula")
#opcion =int(input( "Ingresa: 1, 2, o 3: " ))

#if opcion == 1:
    #print(nombre.upper())
#elif opcion == 2:
    #print(nombre.lower())
#elif opcion == 3:
    #print(nombre.title())
#else:
    #print("Por favor ingrese una opcion valida")

#ejercicio 9

#terremoto= int(input("ingrese magnitud del terremoto: "))

#if terremoto < 3:
    #print("Muy leve (Imperceptible)")
#elif terremoto >= 3 and terremoto < 4:
    #print ("Leve (Ligeramente perceptible)")
#elif terremoto >= 4 and terremoto < 5:
    #print ("Moderado (Sentido por personas, pero generalmente no causa daño)")
#elif terremoto >=5 and terremoto < 6:
    #print ("Fuerte (Puede causa daño en estructuras debiles)")
#elif terremoto >=6 and terremoto < 7:
    #print("Muy Fuerte (Puede causar daños significativos)")
#else:
    #print("Extremo (Puede causar graves daños a gran escala)")

#ejercicio 10

hemisferio = input("¿En qué hemisferio te encuentras? (N/S): ").strip().upper()
mes = int(input("Ingresa el número del mes (1-12): "))
dia = int(input("Ingresa el día del mes: "))

if hemisferio == 'N':
    if (mes == 12 and dia >= 21) or (mes <= 2) or (mes == 3 and dia <= 20):
         print("estacion: Invierno")
    elif (mes == 3 and dia >= 21) or (mes <= 5) or (mes == 6 and dia <= 20):
        print("estacion: Primavera")
    elif (mes == 6 and dia >= 21) or (mes <= 8) or (mes == 9 and dia <= 20):
        print("estacion: Verano")
    elif (mes == 9 and dia >= 21) or (mes <= 11) or (mes == 12 and dia <= 20):
        print("estacion: Otoño")
    else:
        print("estacion: fecha invalida")

elif hemisferio == 'S':
    if (mes == 12 and dia >= 21) or (mes <= 2) or (mes == 3 and dia <= 20):
        print("estacion: Verano")
    elif (mes == 3 and dia >= 21) or (mes <= 5) or (mes == 6 and dia <= 20):
        print("estacion: Otoño")
    elif (mes == 6 and dia >= 21) or (mes <= 8) or (mes == 9 and dia <= 20):
        print("estacion: Invierno")
    elif (mes == 9 and dia >= 21) or (mes <= 11) or (mes == 12 and dia <= 20):
        print("estacion: Primavera")
    else:
        print("estacion: fecha invalida")
else:
    print("estacion: Hemisferio no válido. Por favor, ingresa 'N' o 'S'.")
    

















    
   
   