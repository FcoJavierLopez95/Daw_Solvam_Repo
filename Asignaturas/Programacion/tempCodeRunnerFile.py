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