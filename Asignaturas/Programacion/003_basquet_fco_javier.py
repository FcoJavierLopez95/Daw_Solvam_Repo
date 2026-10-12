# FRANCISCO JAVIER LOPEZ ARCE   

team_a=""
team_b=""
counter_a = 0
counter_b = 0
quart_counter_a = 0
quart_counter_b = 0
tiro_a = []
tiro_b = []
quart_tiro_a =[]
quart_tiro_b = []
tiro = ""
point= 0

# Separador
def sep():
    print("===============================================================")

# Marcador 
def marcador(team_a, team_b, counter_a, counter_b):
        print(f"{team_a} {counter_a} VS {team_b} {counter_b}\n")

# Registro de equipos
def registrar_equipo():
    sep()
    print("El partido va a comenzar!")
    sep()
    team_a = input("Registra El equipo visitante:\n")
    print("\nEquipo visitante registrado correctamente\n")
    sep()
    team_b = input("Registra el equipo local:\n")
    print("\nEquipo local registrado correctamente\n")
    sep()
    return team_a, team_b

#Selecciona el equipo que anota
def select_team():
    while True: 
        marcador(team_a, team_b, counter_a, counter_b)
        team_menu = input(f"\nQue equipo ha anotado?\nA.-{team_a}\nB.-{team_b}\nSelecciona una opcion:\n")
        match team_menu:

            case "A":
                select=team_a
                print (f"\nhas seleccionado {team_a}\n")
                return select
            case "B":
                select=team_b
                print (f"\nhas seleccionado {team_b}\n")
                return select
            case "C":
                print("Saliendo de la anotacion")
                break
            case _:
                team_menu = ""
                print("El dato introducido no es correcto, introducelo de nuevo.\n")
                continue          

# Selecciona el tipo de anotacion
def select_value():
    while True:                                                     
        try:    
            marcador(team_a, team_b, counter_a, counter_b)
                                                                                                 #\n4.-Cancelar anotacion
            point_menu = int(input(f"Que tanto han anotado?\n1.-Tiro libre\n2.-Tiro de area\n3.-Triple!!!\nSelecciona una ipcion:\n"))
            match point_menu:

                case 1:
                    print(f"\nHas seleccionado tiro libre\n")
                    tiro = "libre"
                    point = 1
                    return point, tiro
                case 2:
                    print(f"\nHas seleccionado tiro de area\n")
                    point = 2
                    tiro = "area"
                    return point, tiro
                case 3:
                    print("\nTRIPLEEE!!!\n")
                    point = 3
                    tiro = "Triple"
                    return point, tiro
#                case 4:
#                    print("Cancelando anotacion\n")  Falla???
#                    break         
                case _:
                    print("Has introducido un numero incorrecto, intentalo de nuevo\n")
        except ValueError:
            print ("Has introducido un valor incorrecto, intentalo de nuevo\n")


# Actualiza contadores
def anotar_tanto(counter_a, counter_b, tiro_a, tiro_b, quart_tiro_a, quart_tiro_b,quart_counter_a, quart_counter_b, point):
    select = select_team()
    point = select_value()
    if select == team_a:
        counter_a = counter_a + point
        quart_counter_a = quart_counter_a + point
        tiro_a.append(tiro)
        quart_tiro_a.append(tiro)
    elif select == team_b:
        counter_b = counter_b + point
        quart_counter_b = quart_counter_b + point
        tiro_b.append(tiro)
        quart_tiro_b.append(tiro)
    return counter_a, counter_b,tiro_a, tiro_b,quart_tiro_a, quart_tiro_b, quart_counter_a, quart_counter_b


# Imprime el resumen del cuarto
def resume_quart(team_a, team_b, counter_a, counter_b, quart_counter_a, quart_counter_b, quart_tiro_a, quart_tiro_b):

    for i in range (len(quart_tiro_a)):
        if quart_tiro_a[i] == "libre":
            libre_a += 1
        elif quart_tiro_a[i] == "area":
                area_a += 1
        elif quart_tiro_a[i] == "triple":
                triple_a += 1
            

    for i in range (len(quart_tiro_b)):
        if quart_tiro_b[i] == "libre":
            libre_b += 1
        elif quart_tiro_b[i] == "area":
                area_b += 1
        elif quart_tiro_b[i] == "triple":
                triple_b += 1
    sep()
    print(f"Resumen del cuarto")
    marcador(team_a, team_b, counter_a, counter_b)
    sep()
    print(f"{team_a}:\nAnotaciones en este cuarto:{quart_counter_a}\nAnotaciones de tiro libre: {libre_a}\n Anotaciones dentro del area: {area_a}\nTriples: {triple_a}\n")
    sep()
    print(f"{team_b}:\nAnotaciones en este cuarto:{quart_counter_b}\nAnotaciones de tiro libre: {libre_b}\n Anotaciones dentro del area: {area_b}\nTriples: {triple_b}\n")

# Fesumen final del partido
def resume_match(team_a, team_b, counter_a, counter_b):

    for i in range (len(tiro_a)):
        if tiro_a[i] == "libre":
            libre_a += 1
        elif tiro_a[i] == "area":
                area_a += 1
        elif tiro_a[i] == "triple":
                triple_a += 1
            

    for i in range (len(tiro_b)):
        if tiro_b[i] == "libre":
            libre_b += 1
        elif tiro_b[i] == "area":
                area_b += 1
        elif tiro_b[i] == "triple":
                triple_b += 1
    sep()
    print(f"Resumen del partido")
    marcador(team_a, team_b, counter_a, counter_b)
    sep()
    print(f"{team_a}:\nAnotaciones totales:{counter_a}\nAnotaciones de tiro libre: {libre_a}\n Anotaciones dentro del area: {area_a}\nTriples: {triple_a}\n")
    sep()
    print(f"{team_b}:\nAnotaciones totales:{counter_b}\nAnotaciones de tiro libre: {libre_b}\n Anotaciones dentro del area: {area_b}\nTriples: {triple_b}\n")



# Menú principal
def show_menu(team_a, team_b, counter_a, counter_b, quart_counter_a, quart_counter_b, tiro_a, tiro_b, quart_tiro_a, quart_tiro_b, point):
    cuarto = 1
    while cuarto < 4:  
        sep()
        print(f"Cuarto numero {cuarto}.")   
        sep()  
        try:
            marcador(team_a, team_b, counter_a, counter_b)
            menu=int(input ("0.-Terminar cuarto.\n1.-Anotar un tanto.\nSelecciona una opcion:\n"))
            sep()
            match menu:
                case 0:
                    if cuarto <= 4 : 
                        sep()
                        print(f"TERMINA EL  CUARTO {cuarto}º\n")
                        sep()
                        resume_quart(team_a, team_b, quart_counter_a, quart_counter_b,quart_tiro_a, quart_tiro_b)
                        quart_counter_a = 0
                        quart_counter_b = 0
                        quart_tiro_a = []
                        quart_tiro_b = []
                        print("")
                        cuarto = cuarto + 1
                        
                    else:
                        sep()
                        print("TERMINA EL PARTIDO!!!")
                        resume_match(team_a, team_b, counter_a, counter_b)
                        sep()
                case 1:
                    counter_a, counter_b, tiro_a, tiro_b, quart_tiro_a, quart_tiro_b,quart_counter_a, quart_counter_b, point = anotar_tanto(counter_a, counter_b, tiro_a, tiro_b, quart_tiro_a, quart_tiro_b,quart_counter_a, quart_counter_b, point)
                    
                case _:
                    print("Has introducido un numero incorrecto, intentalo de nuevo")
        except ValueError:
            print ("Has introducido un valor incorrecto, intentalo de nuevo")

#Programa
team_a, team_b = registrar_equipo()
print ("COMIENZA EL PARTIDO!!!\n")
show_menu(team_a, team_b, counter_a, counter_b, quart_counter_a, quart_counter_b, tiro_a, tiro_b, quart_tiro_a, quart_tiro_b, point)


    


