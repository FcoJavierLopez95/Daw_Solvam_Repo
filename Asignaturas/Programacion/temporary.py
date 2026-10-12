team_a = 0
team_b =0
def select_team():
    while True: 
        team_menu = input(f"\nQue equipo ha anotado?\nA.-{team_a}\nB.-{team_b}\nSelecciona una opcion: ")
        match team_menu:

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
                team_menu = ""
                print("El dato introducido no es correcto, introducelo de nuevo.")
                continue  
select_team()