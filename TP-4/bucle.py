# ejercicio 1

#for numero in range (0,101):
    #print (numero)

# ejercicio 2 

#numero = input("Ingrese un numero entero: ")

#if numero.lstrip('-').isdigit(): 
    #cantidad_digitos = 0
    
    #for digito in numero.lstrip('-'): 
        #cantidad_digitos += 1  

    #print(f"La cantidad de dígitos en el número {numero} es: {cantidad_digitos}")
#else:
    #print("Error: Debes ingresar un número entero válido.")

#ejercicio 3

#numero1 = int(input("Ingrese el primer valor: "))
#numero2 = int(input("Ingrese el segudo valor: "))
#suma = 0
#for numero in range (numero1+1,numero2):
    #suma += numero

#print(f"la suma de los numeros enteros entre {numero1} y {numero2} es : {suma}")

#ejercicio 4

#numeros= int(input("Ingrese un numero enteros, ingrece 0 para salir: "))
#suma = numeros

#while numeros != 0:
    #numeros= int(input("Ingrese otro numero enteros, ingrece 0 para salir: "))
    #suma += numeros
    #print(f"La suma de los numeros ingresados es {suma}")

#ejercicio 5

#import random
#rand = random.randint(0,9)
#contador = 0

#numero= int(input("Ingrese un numero entre el 0 y el 9 : "))

#while numero != rand:
    #contador += 1
    #numero= int(input("Ingrese otro numero entre el 0 y el 9 : "))

#print(f"Usted adivino en {contador} intentos")

#ejercicio 6

#for numero in range (100,0,-1):
    #if numero % 2 == 0:
        #print(numero)

#ejercicio 7

#numero = int(input("Ingrese un numero entero y positivo: "))
#suma= 0

#if numero > 0:

    #for i in range (0,numero+1):
        #suma += i
#else:
    #print("Error, el numero ingresado no es entero y positivo")

#print(f"La suma de todos los numero comprendidos entre o y {numero} es: {suma}")

# ejercicio 8

#cantidad_numeros = 10  

#contadores = {
    #"pares": 0,
    #"impares": 0,
    #"negativos": 0,
    #"positivos": 0
#}

#print(f"Por favor, ingresa {cantidad_numeros} números enteros:")

#for i in range(cantidad_numeros):
    #numero = int(input(f"Número {i + 1}: "))

    #if numero % 2 == 0:
        #contadores["pares"] += 1
    #else:
        #contadores["impares"] += 1

    #if numero < 0:
        #contadores["negativos"] += 1
    #elif numero > 0:
        #contadores["positivos"] += 1

#print(f"\nResultados:")
#print(f"Números pares: {contadores['pares']}")
#print(f"Números impares: {contadores['impares']}")
#print(f"Números negativos: {contadores['negativos']}")
#print(f"Números positivos: {contadores['positivos']}")

#ejercicio 9

#cantidad_numeros = 100
#suma = 0

#print(f"Por favor, ingresa {cantidad_numeros} números enteros:")

#for i in range(cantidad_numeros):
    #numero = int(input(f"Número {i + 1}: "))
    #suma += numero  

#media = suma / cantidad_numeros

#print(f"\nLa media de los {cantidad_numeros} números ingresados es: {media}")


#ejercicio 10

#numero = input("Por favor, ingresa un número: ")
#numero_invertido = numero[::-1]

#print(f"El número con los dígitos invertidos es: {numero_invertido}")










 





