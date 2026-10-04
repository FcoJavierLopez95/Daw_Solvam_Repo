
cal =""
alpha_cal= ""

while True:
    try:
        cal= float(input("Introduce tu nota: "))

        match cal:
            case cal if cal < 0:
                print("Por muy burro que seas no puedes sacar menos de un 0, por favor intentalo de nuevo")
                continue

            case cal if cal >= 0  and cal <3:
                alpha_cal="Muy deficiente"
                break

            case cal if cal >= 3  and cal <5:
                alpha_cal="Insuficiente"
                break

            case cal if cal >= 5  and cal <9:
                alpha_cal="Aprobado"
                break

            case cal if cal >= 9  and cal <10:
                alpha_cal="Notable"
                break

            case cal if cal >= 9  and cal ==10:
                alpha_cal="Excelente"
                break

            case cal if cal > 10:
                print("No vayas de sobrado, no puedes sacar mas de un 10!")
                continue

    except ValueError:
        print("El valor introducido no es válido, por favor inténtalo de nuevo")

print(f"Con una nota de {cal} tu estado es: {alpha_cal} ")


