# EPic: Ejercicio: Parqueadero con 10 espacios
# Un parqueadero tiene **10 espacios disponibles**.  
# Al comenzar, **todos los espacios están vacíos**.

#     ## Objetivo
#     Crea un programa que permita:

#     1. **Mostrar** los espacios disponibles y ocupados.
#     2. **Ingresar un carro** (usando la placa).
#     3. **Sacar un carro** (usando la placa).
#     4. **Salir del programa**.

#     ## Reglas
#     - Si el parqueadero está **lleno**, no se pueden ingresar más carros.
#     - Si la **placa ya está dentro**, no se puede volver a ingresar.
#     - Si se intenta **sacar un carro que no está**, debe mostrarse un mensaje.
#     - Cuando un carro entra, ocupa el **primer espacio libre**.
#     - Cuando un carro sale, ese espacio vuelve a quedar **disponible**.

# ## Comportamiento del programa
# El programa debe **repetirse continuamente** hasta que el usuario decida salir.

#  **Sugerencia:**  
# Puedes usar **listas** para representar los espacios del parqueadero.
import os
from time import sleep
import msvcrt

def mostrar_menu ():
    print (f"""    MENU
    1. Espacios disponibles y ocupados.
    2. Ingresar un vehiculo.
    3. Retirar un vehiculo.
    4. Salir del programa.""")

def regresar_menu (n):
    output = "REGRESANDO AL MENU...."
    for _ in output:
            print (_, end="", flush=True)
            sleep(n)
    os.system("cls")


print ('Bienvenido al parqueadero, estas son las consultas disponibles:')

parking = ['Disponible']*10

while True:
    mostrar_menu()
    try:
        opcion = int (input ("Por favor seleccióne una opción --> "))
        if opcion <=0 or opcion >4:
            print ("Error: Su selección no esta dentro de las opciones. Intentelo de nuevo.\n")
            sleep(0.9)
            os.system("cls")

            continue
    except:
        print('Error: Ingresa una opcion valida***')
        sleep(1)
        os.system("cls")
        continue

    if opcion == 1: #Estatus del parking
        print ("                     PARKING")
        for i in range (5):
            print (f"""Espacio {i+1} : {parking [i]} | Espacio {i+6} : {parking [i+5]}""")
        print("\nPresiona cualquier tecla para continuar...")
        msvcrt.getch()
        regresar_menu(0.08)

    elif opcion == 2: #Ingresar un vehiculo
        while True:
            if "Disponible" not in parking: #Validacion de que haya espacio disponible
                print("No hay espacio disponible")

            placa = input ("INGRESAR VEHICULO |Ingrese la placa: ").strip().upper() #Solicitud al usuario

            if len(placa) <=0 or len (placa) >6: #Validacion de que ingrese una placa valida
                print("Error: Debe ingresar una placa valida. Ejemplo 'ABC123'. Intentelo nuevamente...")
                continue

            elif placa in parking: #Validacion de que existencia de placa ingresada
                print(f"""Ese carro ya existe en el parqueadero, en la posición {parking.index (placa)+1}
                Intentelo nuevamente...""")
                continue

            else: #Agregar un vehiculo
                indice = parking.index ('Disponible')
                parking [indice] = placa
                print (f'Vehiculo ingresado en la posición { indice + 1}')
            print("\nPresiona cualquier tecla para continuar...")
            msvcrt.getch()
            regresar_menu(0.06)
            break

    elif opcion == 3: #Retirar un vehiculo
        placa = input ("RETIRAR VEHICULO | Ingrese la placa: ") #Solicitud al usuario

        if placa not in parking: #Validacion de que existencia de placa ingresada
            print("La placa ingresada no existe.")
            print("\nPresiona cualquier tecla para continuar...")
            msvcrt.getch()
            regresar_menu(0.06)

        else:#Retirar un vehiculo
            indice = parking.index (placa)
            parking [indice] = 'Disponible'
            print (f'Vehiculo retirado de la posición { indice + 1}')
            msvcrt.getch()
            regresar_menu(0.06)

    elif opcion == 4:
        print ('Saliendo del programa.....')
        break