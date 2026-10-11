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

    case number if number > 0:
        print("el número es positivo")

    case number if number < 0:
        print("el número es negativo")

    case _:
        print("El número vale 0")


# ------------------------------------------------------------------------------
# EJERCICIO 2
# Algoritmo que lea dos números y nos diga cuál de ellos es mayor o bien si son
# iguales.
# ------------------------------------------------------------------------------
while True:
    try:
        number1 = float(input(f"Dime un numero "))
        number2 = float(input(f"Dime otro numero "))
        break
    except ValueError:
        print("Has introducido un dato incorrecto.")

if number1 < number2:
    print(f"El número mayor es {number2}")

elif number1 > number2:
    print(f"El número mayor es {number1}")

else:
    print(f"Los numeros {number1} y {number2} son iguales")


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


if number == 0:
    print("El número es 0")
elif (number % 2) == 0:
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

note = ""
note_list = []
aproved = ""
i = 1

""" Verifico que el dato es un numeo """
while i < 4:
    try:
        note = input(f"Dime tu calificación número {i}: ")

        if float(note) > 10:
            print("No puedes sacar mas de un 10")

        elif float(note) < 0:
            print("Por muy burro que seas no has podido sacar menos de un 0")

        else:
            note_list.append(float(note))
            i += 1

    except ValueError:
        print("Has introducido un dato incorrecto, empecemos de nuevo.")

""" calculo la media """

med = sum(note_list) / 3

""" aprobado on suspendido """

if med < 5.00:
    aproved = "suspendido"
else:
    aproved = "Aprobado"


print(
    f"Teniendo en cuenta tus calificaciones de: {note_list} te sale una media de {med:.2f} por lo que has {aproved} "
)


# ------------------------------------------------------------------------------
# EJERCICIO 5
# A un trabajador le pagan según sus horas trabajadas por una tarifa de pago por
# hora. Si la cantidad de horas trabajadas es mayor a 40 horas. la tarifa se
# incrementa en un 50% para las horas extras. Calcular el salario del trabajador
# dadas las horas trabajadas y las tarifas.
# ------------------------------------------------------------------------------
work_time = ""
ord_time = 0
extra_time = 0
hour_price = ""
salary = 0

""" Verifico horas exactas y que introduce números """

while True:
    try:
        work_time = float(
            input(
                "Introduce tus horas trabajadas, recuerda que no pagamos horas incompletas por lo que solo puedes introducir un numero entero: "
            )
        )
        if work_time % 1 != 0:
            print("El numero introducido no es un numero entero.")
            work_time = ""
        else:
            hour_price = float(input("Introduce el precio de la hora trabajada: "))
            break
    except ValueError:
        print("Has introducido un valor no válido, por favor inténtalo de nuevo")

""" Calculo cuantas horas son extras """
if work_time > 40:
    extra_time = work_time - 40
    ord_time = 40
else:
    ord_time = work_time
    extra_time = 0

""" Calculo el salario """
salary = (ord_time * hour_price) + (extra_time * (hour_price * 1.5))

print(
    f"Esta semana has trabajado un total de {ord_time} horas ordinarias y  has realizado un total de {extra_time} horas extra.\nSueldo a percibir: {salary}€"
)

# ------------------------------------------------------------------------------
# EJERCICIO 6
# Algoritmo que lea tres números distintos y nos diga cuál de ellos es el mayor.
# ------------------------------------------------------------------------------

""" Declaración de variables """

num = ""
num_list = []
i = 1

""" Verifico que los datos son numeros """

print("Dime tres números distintos")

while i < 4:
    try:
        num = float(input(f"Dime el número {i}: "))

        if num in num_list:  # Verifico que los tres numeros son diferentes
            print("No puedes repetir el mismo número")
            continue
        else:
            num_list.append(num)
            i += 1
    except ValueError:
        print("Has introducido un dato incorrecto.")

" Recorro y ordeno la lista "

length = len(num_list)
for j in range(length):
    for k in range(0, (length - 1) - j):
        if num_list[k] < num_list[k + 1]:
            num_list[k], num_list[k + 1] = num_list[k + 1], num_list[k]

""" conclusion """

print(
    f"El número mayor es: {num_list[0]}\nQuedando ordenados de mayor a menor de esta forma: {num_list}"
)

""" 
### También puedo hacerlo con funciones nativas de python: ###

# lista.sort(num_list) --> Modifica (ordena) la lista original directamente en memoria.
# lista_ordenada = sorted(num_list) --> Deja la lista original tal cual y te devuelve una nueva lista ya ordenada.
# numero_mayor = max(num_list)  --> Asigna el número mas grande

"""

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

cal = ""
alpha_cal = ""

while True:
    try:
        cal = float(input("Introduce tu nota: "))

        match cal:
            case cal if cal < 0:
                print(
                    "Por muy burro que seas no puedes sacar menos de un 0, por favor intentalo de nuevo"
                )
                continue

            case cal if cal >= 0 and cal < 3:
                alpha_cal = "Muy deficiente"
                break

            case cal if cal >= 3 and cal < 5:
                alpha_cal = "Insuficiente"
                break

            case cal if cal >= 5 and cal < 6:
                alpha_cal = "Aprobado"
                break

            case cal if cal >= 6 and cal < 9:
                alpha_cal = "Notable"
                break

            case cal if cal >= 9 and cal == 10:
                alpha_cal = "Excelente"
                break

            case cal if cal > 10:
                print("No vayas de sobrado, no puedes sacar mas de un 10!")
                continue

    except ValueError:
        print("El valor introducido no es válido, por favor inténtalo de nuevo")

print(f"Con una nota de {cal} tu estado es: {alpha_cal} ")


# ------------------------------------------------------------------------------
# EJERCICIO 8
# Crear un programa que permita ingresar un nombre y una cantidad numérica
# para que así después el programa escriba este nombre tantas veces como su
# cantidad ingresada.
# ------------------------------------------------------------------------------

name = ""
repeat = ""

name = input("introduce tu nombre: ")

while True:
    try:
        repeat = float(input("Cuantas veces quieres que diga tu nombre?: "))
        if repeat % 1 != 0:
            print("Necesito que el numero sea entero")
            continue
        elif repeat < 0:
            print("No puedo desrepetir tu nombre, introduce un numero positivo")
            continue
        elif repeat == 0:
            print("Seguro? así no puedo decirlo. introduce uno que no sea 0")
            continue
        else:
            repeat = int(repeat)
            break
    except ValueError:
        print("El valor introducido no es válido, por favor intentalo de nuevo.")

for i in range(repeat):
    print(name)

# ------------------------------------------------------------------------------
# EJERCICIO 9
# Mostrar los múltiplos de 3 desde 1 hasta el numero n, ingresado por teclado.
# ------------------------------------------------------------------------------


while True:
    try:
        mult3 = float(input("Cuantos multiplos de 3 quieres que diga?: "))
        if mult3 % 1 != 0:
            print("Necesito que el numero sea entero")
            continue
        elif mult3 < 0:
            print("El número tiene que ser positivo")
            continue
        elif mult3 == 0:
            print("introduce uno que no sea 0")
            continue
        else:
            mult3 = int(mult3)
            break
    except ValueError:
        print("El valor introducido no es válido, por favor intentalo de nuevo.")

triple = 1

for i in range(mult3):
    triple = triple * 3
    print(triple)


# ------------------------------------------------------------------------------
# EJERCICIO 10
# Imprimir de forma descendente los 30 primeros números naturales menores de 30
# ------------------------------------------------------------------------------

for i in range(30, 0, -1):
    print(i)


# ------------------------------------------------------------------------------
# EJERCICIO 11
# Algoritmo que visualice los números que son múltiplos de 2 o de 3 que hay entre
# 1 y 100.
# ------------------------------------------------------------------------------

for i in range(1, 100):
    if i % 2 == 0:
        print(f"{i} es múltiplo de 2")
    elif i % 3 == 0:
        print(f"{i} es múltiplo de 3")
    else:
        print(i)


# ------------------------------------------------------------------------------
# EJERCICIO 12
# Se pide representar el algoritmo que nos calcule la suma de los N primeros
# números naturales. N se leerá por teclado
# ------------------------------------------------------------------------------
numtype = ""


def introduce_num(numtype):
    while True:
        try:
            n = int(input(f"Introduce un número {numtype} "))
            if n <= 0:
                print("El valor no puede ser igual o menor a 0")
                continue
            else:
                return n
        except ValueError:
            print("Has introducido un dato no válido, porfavor intentalo de nuevo.")


n = introduce_num("entero positivo")

nat = 0

for i in range(
    nat,
    n,
):
    nat = nat + i
    print(f"{i} + {i-1} = {nat}")


# ------------------------------------------------------------------------------
# EJERCICIO 13
# Se pide representar el algoritmo que nos calcule la suma de los N primeros
# números pares a partir de esa N. Es decir, si insertamos un 5, nos haga la suma de
# 6+8+10+12+14.
# ------------------------------------------------------------------------------

n = introduce_num("Entero positivo")

par = n
list_par = []

if n % 2 == 0:
    for par in range(
        n,
        n + n,
    ):
        list_par.append(n)
        n += 2
else:
    par = +1
    for par in range(
        n,
        n + n,
    ):
        list_par.append(n)
        n += 2

sum_list = sum(list_par)
print(f"La suma de los numeros {list_par} es: {sum_list}")


# ------------------------------------------------------------------------------
# EJERCICIO 14
# Realizar un algoritmo que permita calcular la suma de los números ingresados
# mientras que el valor acumulado no supere el valor 100. Mostrar el valor
# acumulado antes de superar 100.
# ------------------------------------------------------------------------------
list_100 = []
res = 0
while res < 100:
    n = introduce_num("Del 1 al 50: ")
    if n > 50:
        print("El número es muy grande.")
        continue
    else:
        if sum(list_100) + n > 100:
            print(f"Numeros introducidos: {list_100} Te has pasado.")
            print(f"valor acumulado 100, te pasas por {(100-sum(list_100))-n}!!!\n")
            break
        elif sum(list_100) + n == 100:
            print(f"Numeros introducidos: {list_100}")
            print("Has llegado exactamente a 100!!!\n")
            break
        else:
            list_100.append(n)
            print(f"Valores introducidos: {list_100}\n")


# ------------------------------------------------------------------------------
# EJERCICIO 15
# Ingresar por teclado 10 números enteros, se debe mostrar la suma de dichos
# números, calcular cuántos es la suma de los pares y el de los impares.
# ------------------------------------------------------------------------------
list_total = []
list_par = []
list_impar = []

for i in range(0, 10):
    n = introduce_num(f"enteroeste es el numero {i+1}: ")

    if n % 2:
        list_par.append(n)
        list_total.append(n)
        print((f"Numeros introducidos: {list_total}\n"))
    else:
        list_impar.append(n)
        list_total.append(n)
        print((f"Numeros introducidos: {list_total}\n"))

print(
    f"Numeros introducidos: {list_total}\nSuma total:{sum(list_total)}\nNumeros pares introducidos: {list_par} Suma de dichos numeros: {sum(list_par)}\nNumeros impares introducidos: {list_impar} Suma de dichos numeros: {sum(list_impar)}\n"
)


# ------------------------------------------------------------------------------
# EJERCICIO 16
# Teniendo en cuenta que la clave es “eureka”, escribir un algoritmo que nos pida
# una clave. Solo tenemos 3 intentos para acertar, si fallamos los 3 intentos nos
# mostrara un mensaje indicándonos que hemos agotado esos 3 intentos. Si
# acertamos la clave, el programa terminará.
# ------------------------------------------------------------------------------
counter = 3

while counter >0: 
    pasword=input(f"Introduce tu clave de acceso y diras eureka, tienes {counter} intentos : ")
    
    if pasword != "eureka":
        print("Intent fallido")
        
        counter -= 1
    else:
        print("Eureka! Has adivinado la contraseña!!!")
        break
    

if counter == 0:
        print("Has agotado tus intentos!")


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
def show_menu():
    print
    while True:
        try:
            menu = int(
                input(
                    "\nMENU CALCULADORA\n1.-Suma\n2.-Resta\n3.Producto\n4.-División\n5.-Salir\nSelecciona una opción: "
                )
            )

            match menu:
                case 1:
                    result, char, num1, num2 = suma()
                    show_result(result, char, num1, num2)
                    continue

                case 2:
                    result, char, num1, num2 = resta()
                    show_result(result, char, num1, num2)

                case 3:
                    result, char, num1, num2 = prod()
                    show_result(result, char, num1, num2)
                    continue

                case 4:
                    result, char, num1, num2 = div()
                    show_result(result, char, num1, num2)
                    continue

                case 5:
                    print("\nSaliendo del programa...")
                    break

                case _:
                    print(
                        "\nEl valor introducido no es válido, por favor inténtalo de nuevo"
                    )
                    continue

        except ValueError:
            print("\nEl valor introducido no es válido, por favor inténtalo de nuevo")


def comprobar_num():
    while True:
        try:
            num1 = float(input(f"Dime un numero "))
            num2 = float(input(f"Dime otro numero "))
            return num1, num2
        except ValueError:
            print("Has introducido un dato incorrecto.")


def suma():
    num1, num2 = comprobar_num()
    result = num1 + num2
    char = "+"
    return result, char, num1, num2


def resta():
    num1, num2 = comprobar_num()
    result = num1 - num2
    char = "-"
    return result, char, num1, num2


def prod():
    num1, num2 = comprobar_num()
    result = num1 + num2
    char = "x"
    return result, char, num1, num2


def div():
    num1, num2 = comprobar_num()
    result = num1 / num2
    char = "÷"
    return result, char, num1, num2


def show_result(result, char, num1, num2):
    print(f"\n{num1} {char} {num2} = {result}\n")


show_menu()
