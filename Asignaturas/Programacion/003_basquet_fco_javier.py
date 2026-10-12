# FRANCISCO JAVIER LOPEZ ARCE   

team_a=""
team_b=""
counter_a = 0
counter_b = 0

def registrar_equipo():
    print("El partido va a comenzar!")
    team_a = input("Registra El equipo visitante:\n")
    print("Equipo visitante registrado correctamente")
    team_b = input("Registra el equipo local:\n")
    print("Equipo local registrado correctamente\n")
    return team_a, team_b

def anotar_tanto(counter_a, counter_b):
    select = select_team()
    point = select_value()
    if select == team_a:
        counter_a = counter_a + point
    elif select == team_b:
            counter_b = counter_b + point
    return counter_a, counter_b


def show_cuarto(team_a, team_b, counter_a, counter_b):
    print(f"Resumen del cuarto {team_a} VS {team_b}:\n{team_a}: {counter_a}.\n{team_b}: {counter_b}")


def select_team():
    while True: 
        team_menu = input(f"\nQue equipo ha anotado?\nA.-{team_a}\nB.-{team_b}\nSelecciona una opcion:\n")
        match team_menu:

            case "A":
                select=team_a
                print (f"has seleccionado {team_a}\n")
                return select
            case "B":
                select=team_b
                print (f"has seleccionado {team_b}\n")
                return select
            case "C":
                print("Saliendo de la anotacion")
                break
            case _:
                team_menu = ""
                print("El dato introducido no es correcto, introducelo de nuevo.\n")
                continue          


def select_value():
    while True:                                                     
        try:                                                                                             #\n4.-Cancelar anotacion
            point_menu = int(input(f"Que tanto han anotado?\n1.-Tiro libre\n2.-Tiro de area\n3.-Triple!!!\nSelecciona una ipcion:\n"))
            match point_menu:

                case 1:
                    print(f"Has seleccionado tiro libre\n")
                    point = 1
                    return point
                case 2:
                    print(f"Has seleccionado tiro de area\n")
                    point = 2
                    return point
                case 3:
                    print("Tripleee!!!\n")
                    point = 3
                    return point
#                case 4:
#                    print("Cancelando anotacion\n")  Falla???
#                    break         
                case _:
                    print("Has introducido un numero incorrecto, intentalo de nuevo\n")
        except ValueError:
            print ("Has introducido un valor incorrecto, intentalo de nuevo\n")

def show_menu(team_a, team_b, counter_a, counter_b,):
    cuarto = 1
    while cuarto < 4:  
        print(f"Cuarto numero {cuarto}.")     
        try:
            menu=int(input ("0.-Terminar cuarto.\n1.-Anotar un tanto.\nSelecciona una opcion:\n"))
            
            match menu:
                case 0:
                    if cuarto >= 4 : 
                        print(f"Terminamos el cuarto numero {cuarto}")
                        show_cuarto(team_a, team_b, counter_a, counter_b)
                        cuarto = cuarto + 1
                    else:
                        print("Termina el partido!!!")
                        show_cuarto(team_a, team_b, counter_a, counter_b)
                case 1:
                    counter_a, counter_b = anotar_tanto(counter_a, counter_b)
                    
                case _:
                    print("Has introducido un numero incorrecto, intentalo de nuevo")
        except ValueError:
            print ("Has introducido un valor incorrecto, intentalo de nuevo")

#Programa
team_a, team_b = registrar_equipo()
print ("Comienza el partido!!!\n")
show_menu(team_a, team_b, counter_a, counter_b)


    


