from os import system
from sumar import suma
system ('cls')



while True:
    print("Welcome to the calculator program!")
    print("1. Sumar")
    print("2. Restar")
    print("0. Salir")
    op=input("Ingrese una opcion")
    match op:
        case "1":
            sumar()
            
        case "2":
            #restar()
            pass
        
        case "0":
            break