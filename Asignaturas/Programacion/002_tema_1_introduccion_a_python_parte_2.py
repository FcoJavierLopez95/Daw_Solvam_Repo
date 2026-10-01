# ------------------------------------------------------------------------------
# EJERCICIO 1
# Escriba un algoritmo que determine si un número introducido por teclado es
# positivo, negativo o cero.
# ------------------------------------------------------------------------------
while True:
    
    try:
        number = float(input("Introduce un número cualquiera positivo o negativo :")) 
        break           
    except ValueError:
        print("Has introducido un dato no válido, porfavor intentalo de nuevo")     

match number:

    case number if number>0:
        print("el número es positivo")

    case number if number<0:
        print("el número es negativo")

    case _:
        print("El número vale 0")


# ------------------------------------------------------------------------------
# EJERCICIO 2
# Algoritmo que lea dos números y nos diga cuál de ellos es mayor o bien si son
# iguales.
# ------------------------------------------------------------------------------
""" while True:
    print(input("introduce dos valores:"))
    for i in range (2):
        num_[i] =  """
    



# ------------------------------------------------------------------------------
# EJERCICIO 3
# Realizar un algoritmo que, dado un número entero, visualice en pantalla si es par
# o impar. En el caso de ser 0, debe visualizar “el número no es par ni impar” (para
# que un número sea par, se debe dividir entre dos y que su resto sea 0)
# ------------------------------------------------------------------------------


while True:    
    try:
        number = int(input("Introduce un número entero cualquiera: ")) 
        break           
    except ValueError:
        print("Has introducido un dato no válido, porfavor intentalo de nuevo.")  


if number==0:
    print("El número es 0")
elif (number%2) == 0:
    print(f"El número{number} es par")
else:
    print(f"El número{number} es impar")
 



# ------------------------------------------------------------------------------
# EJERCICIO 4
# Determinar si un alumno aprueba o suspende un curso, sabiendo que aprobará si
# su promedio de tres calificaciones es mayor o igual a 5.0; suspende en caso
# contrario. Deberá permitir ingresar las tres calificaciones y luego calcular su
# promedio.
# ------------------------------------------------------------------------------




# ------------------------------------------------------------------------------
# EJERCICIO 5
# A un trabajador le pagan según sus horas trabajadas por una tarifa de pago por
# hora. Si la cantidad de horas trabajadas es mayor a 40 horas. la tarifa se
# incrementa en un 50% para las horas extras. Calcular el salario del trabajador
# dadas las horas trabajadas y las tarifas.
# ------------------------------------------------------------------------------




# ------------------------------------------------------------------------------
# EJERCICIO 6
# Algoritmo que lea tres números distintos y nos diga cuál de ellos es el mayor.
# ------------------------------------------------------------------------------




# ------------------------------------------------------------------------------
# EJERCICIO 7
# Algoritmo que lea una calificación numérica entera, sin decimales, entre 0 y 10 y
# la transforma en calificación alfabética, escribiendo el resultado.
# • de 0 a <3 Muy Deficiente.
# • de 3 a <5 Insuficiente.
# • de 5 a <6 Bien.
# • de 6 a <9 Notable
# • de 9 a 10 Sobresaliente
# ------------------------------------------------------------------------------




# ------------------------------------------------------------------------------
# EJERCICIO 8
# Crear un programa que permita ingresar un nombre y una cantidad numérica
# para que así después el programa escriba este nombre tantas veces como su
# cantidad ingresada.
# ------------------------------------------------------------------------------




# ------------------------------------------------------------------------------
# EJERCICIO 9
# Mostrar los múltiplos de 3 desde 1 hasta el numero n, ingresado por teclado.
# ------------------------------------------------------------------------------




# ------------------------------------------------------------------------------
# EJERCICIO 10
# Imprimir de forma descendente los 30 primeros números naturales menores de 30
# ------------------------------------------------------------------------------




# ------------------------------------------------------------------------------
# EJERCICIO 11
# Algoritmo que visualice los números que son múltiplos de 2 o de 3 que hay entre
# 1 y 100.
# ------------------------------------------------------------------------------




# ------------------------------------------------------------------------------
# EJERCICIO 12
# Se pide representar el algoritmo que nos calcule la suma de los N primeros
# números naturales. N se leerá por teclado
# ------------------------------------------------------------------------------




# ------------------------------------------------------------------------------
# EJERCICIO 13
# Se pide representar el algoritmo que nos calcule la suma de los N primeros
# números pares a partir de esa N. Es decir, si insertamos un 5, nos haga la suma de
# 6+8+10+12+14.
# ------------------------------------------------------------------------------




# ------------------------------------------------------------------------------
# EJERCICIO 14
# Realizar un algoritmo que permita calcular la suma de los números ingresados
# mientras que el valor acumulado no supere el valor 100. Mostrar el valor
# acumulado antes de superar 100.
# ------------------------------------------------------------------------------




# ------------------------------------------------------------------------------
# EJERCICIO 15
# Ingresar por teclado 10 números enteros, se debe mostrar la suma de dichos
# números, calcular cuántos es la suma de los pares y el de los impares.
# ------------------------------------------------------------------------------




# ------------------------------------------------------------------------------
# EJERCICIO 16
# Teniendo en cuenta que la clave es “eureka”, escribir un algoritmo que nos pida
# una clave. Solo tenemos 3 intentos para acertar, si fallamos los 3 intentos nos
# mostrara un mensaje indicándonos que hemos agotado esos 3 intentos. Si
# acertamos la clave, el programa terminará.
# ------------------------------------------------------------------------------




# ------------------------------------------------------------------------------
# EJERCICIO 17
# Algoritmo que lea números enteros hasta teclear 0, y nos muestre el máximo, el
# mínimo y la media de todos ellos.
# ------------------------------------------------------------------------------




# ------------------------------------------------------------------------------
# EJERCICIO 18
# Calcular las calificaciones de un grupo de alumnos. La nota final de cada alumno
# se calcula según el siguiente criterio: la parte práctica vale el 10%; la parte de
# problemas vale el 50% y la parte teórica el 40%. El algoritmo leerá el nombre del
# alumno, las tres notas, escribirá el resultado y volverá a pedir los datos del
# siguiente alumno hasta que el nombre sea una cadena vacía. Las notas deben
# estar entre 0 y 10, si no lo están, no imprimirá las notas, mostrará un mensaje de
# error y volverá a pedir otro alumno.
# ------------------------------------------------------------------------------




# ------------------------------------------------------------------------------
# EJERCICIO 20
# Diseñar un algoritmo que permita mostrar en pantalla el siguiente menú:
# 1.-Suma
# 2.-Resta
# 3.- Producto
# 4.- División
# 5.- Salir.
# El usuario podrá elegir cualquier alternativa, luego ingresar A y B y realizar la
# operación seleccionada. Solamente con “5” podrá Salir. Tener en cuenta que si
# elige 4.- División deberá reingresar el denominador hasta que ingrese un valor
# diferente a 0 (cero). Si ingresa un número negativo o mayor que 5 deberá
# informar “Opción no válida”.
# ------------------------------------------------------------------------------