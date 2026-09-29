# ------------------------------------------------------------------------------
# EJERCICIO 5
# Dadas dos variables numéricas A y B, que el usuario debe teclear, se pide
# realizar un algoritmo que intercambie los valores de ambas variables y muestre
# cuánto valen al final las dos variables.
# ------------------------------------------------------------------------------
A = input("Dime el valor de A:")
B = input("Dime el valor de B:")

i = A
A = B
B = i

print( f"Ahora B es: {B} y A vale {A}")

# ------------------------------------------------------------------------------
# EJERCICIO 6
# Algoritmo que lea dos números, calculando y escribiendo el valor de su suma,
# resta, producto y división.
# ------------------------------------------------------------------------------
num_a =int(input("Dime el valor de A:"))
num_b = int(input("Dime el valor de B:"))

sum = num_a + num_b
rest = num_a - num_b
prod = num_a * num_b
div = num_a / num_b 

print(f" Dados los valores de {num_a} y {num_b} obtenemos los siguientes resultados: \n suma: {sum} \n resta: {rest}: \n producto: {prod}: \n división: {div}:")

# ------------------------------------------------------------------------------
# EJERCICIO 7
# Calcular el salario de un trabajador, ingresando las horas trabajadas y el
# valor por hora, se debe mostrar el nombre del trabajador.
# ------------------------------------------------------------------------------

## Variable Declarations:
hour_price : float
time_work : int 
glos_salary : float

## Main body
time_work = float(input("Introduce cuantas horas has trabajado este mes:"))
hour_price = float(input("introduce a cuanto te pagan la hora:"))

## Calcular salario
glos_salary = hour_price * time_work
print(f" Este mes tas trabajado {time_work} horas, \n La hora te la pagan a {hour_price}€ \n Tu salario bruto son: {glos_salary}€")
         
# ------------------------------------------------------------------------------
# EJERCICIO 8
# Un colegio desea saber qué porcentaje de niños y qué porcentaje de niñas hay
# en el curso actual. Diseñar un algoritmo para este propósito (recuerda que
# para calcular el porcentaje puedes hacer una regla de 3).
# ------------------------------------------------------------------------------

## Variable Declarations:
boy =""
girl =""

percentage_boy:float
percentage_girl:float

## Main body  ==> En python no exixte do wile. se crea un bucle infinito con un breakpoint que rompe el bucle si se ejecuta el codigo correctamente.
while True:
    boy = input("Cuantos alumnos varones hay registrados?: ")
    girl = input("Cuantos alumnas mujeres hay registradas?: ")
    
    try:
        boy = int(boy)
        girl = int(girl)
        
        if boy < 0 or girl < 0:
            print("El valor introducido no puede ser negativo. Inténtalo de nuevo.")
        elif (boy + girl) == 0:
            print("El total de alumnos no puede ser cero. Inténtalo de nuevo.")
        else:
            break

    except ValueError: 
        print("El dato introducido no es un número entero válido. Inténtalo de nuevo.")

percentage_boy = (boy * 100) / (boy+girl)
percentage_girl = 100 - percentage_boy

print(f"Tienes un total de {boy+girl} alumnos\nTienes {boy} alumnos varones que representan un {round(percentage_boy ,1)}%\nTienes {girl} que representan un {round(percentage_girl ,1)}%")
print("Fin del programa")

# ------------------------------------------------------------------------------
# EJERCICIO 9
# Ingresar un tiempo en segundos y separarlos en horas, minutos y segundos.
# ------------------------------------------------------------------------------

## Zona de declaración de variables
total_sec=""
hour = ""
min =""
sec=""
result = [hour, min, sec]

## Verificación de datos: ==>  Bucle "Do while" y  exception "try catch" de python
while True:
    total_sec = input("introduce todo el tiempo en segundos: ")

    try:
        total_sec =float(total_sec)
        if total_sec <= 0:
            print ("El valor no puede ser 0 ni negativo, intentalo de nuevo")
        else:

            break
    except ValueError:
        print("El dato que has introducido no es válido. por favor inténtalo de nuevo.")

## Resolución del problema:

"""
### --------------------------------------------------------------------------
### En un Float no caben infinitos decimales por lo que este metodo no sirve.
        i= (total_sec /3600)
        hour = int(i)
        i = ((i - hour)*60)
        min = int(i)
        i = ((i - min)*60)
        sec = (i)
### --------------------------------------------------------------------------
"""

hour = int(total_sec // 3600)
min = int((total_sec //60 )% 60)
sec = int(total_sec % 60)


print(f"{hour}º:{min}':{sec}''")


# ------------------------------------------------------------------------------
# EJERCICIO 10
# Dado un tiempo en segundos, calcular los segundos restantes que le
# correspondan para convertirse exactamente en minutos.
# ------------------------------------------------------------------------------

## Verificación de datos:
while True:
    total_sec = input("introduce todo el tiempo en segundos: ")

    try:
        total_sec =float(total_sec)
        if total_sec <= 0:
            print ("El valor no puede ser 0 ni negativo, intentalo de nuevo")
        else:

            break
    except ValueError:
        print("El dato que has introducido no es válido. por favor inténtalo de nuevo.")

## Resolución del problema:

hour = int(total_sec // 3600)
min = int(total_sec //60 )% 60
sec = int(total_sec % 60)
sec_for_min = 60-sec

print(f"tienes:\n{hour} horas;\n{min} minutos;\n{sec} segundos\nTe faltan {sec_for_min} segundos para tener un minuto mas exacto.")