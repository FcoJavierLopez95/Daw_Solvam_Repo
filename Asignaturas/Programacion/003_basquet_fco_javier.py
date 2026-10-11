# FRANCISCO JAVIER LOPEZ ARCE   

team_a=""
team_b=""
CONST_LIBRE = 1   #Se que python no tiene constantes, lo hago por convencion y para que no se cambie.
CONST_AREA = 2
CONST_TRIPLE = 3

def registrar_equipo():
    print("El partido va a comenzar!")
    team_a = input("Registra El equipo visitante:")
    print("Equipo visitante registrado correctamente")
    team_b = input("Registra el equipo local")
    print("Equipo local registrado correctamente")

"""
no sabia hacer .toUpperCase() en python. lo busque en google. sorry 
"""
def anotar_tanto():

def select_team(team_a, team_b):
    while True: 
        team = (input(f"\nQue equipo ha anotado?\nA.-{team_a}B.-{team_b}\nSelecciona una opcion: ").upper)
        match team:

            case "A":
                select=team_a
                print (f"has seleccionado {team_a}")
                return select
            case "B":
                select=team_b
                print (f"has seleccionado {team_b}")
                return select
            case "C":
                print("Saliendo de la anotacion")
                break
            case _:
                team = ""
                print("El dato introducido no es correcto, introducelo de nuevo.")
                continue          


def select_value(select):
    while True:
        try:
            point_menu = int(input(f"Que tanto han anotado?\n1.-Tiro libre\n2.-Tiro de area\n3.-Triple!!!\n4.-Cambiar el equipo anotador\n5.-Cancelar anotacion"))
            match point_value:

                case 1:
                    print("Has seleccionado")
                    point = 1
                    return point
                case 2:
                    point = 2
                    return point
                case 3:
                    point = 3
                    return point
                case 4:
                    print("Atras...") #DONDE VOy AQUI????
                    point = 0
                    return point
                case 5:
                    print("Cancelando anotacion")
                    break         
                case _:
                    print("Has introducido un numero incorrecto, intentalo de nuevo")
        except ValueError:
            print ("Has introducido un valor incorrecto, intentalo de nuevo")


        

def cuartos_menu():
    while True:       
        try:
            cuartos=int(input ("0.-Terminar cuarto.\n1.-Anotar un tanto: "))
            
            match cuartos:
                case 0:
                    print("Terminamos el cuarto numero i")
                    point = 1
                    return point
                case 1:
                    point = 2
                    return point 
                case _:
                    print("Has introducido un numero incorrecto, intentalo de nuevo")
        except ValueError:
            print ("Has introducido un valor incorrecto, intentalo de nuevo")

#Programa
registrar_equipo()

    


