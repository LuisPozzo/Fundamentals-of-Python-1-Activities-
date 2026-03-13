#Hacer un sistema que le permita a un profesor registrar sus estudiantes, debe pedir, nombres, apellidos y edad.

estudiantes = {}
iterador = int ( input ('cantidad de registros a realizar: '))

for i in range (iterador):
    id_estudiante = len(estudiantes) + 1
    name = input ('Ingresa el nombre: ')
    lastname  = input ('Ingresa el apellido: ')
    age = int (input ('Ingresa la edad: '))

    estudiantes [id_estudiante] =    {'name' : name, 'lastname':lastname, 'age' : age }
    print (f'Estudiante {name} {lastname} registrado con éxito.')    

for id_est, datos in estudiantes.items():
        print(f"{id_est:<5} {datos['name']:<15} {datos['lastname']:<15} {datos['age']:<5}")

        print ("-" * 42)
        
print(f"Total de estudiantes: {len(estudiantes)}")



# while True: estudiante.get('name')} -- {estudiante.get ('lastname')} -- {estudiante.get ('age')
#     #mostrar menu
#     print (f"""    MENU
#     1. Listado de estuidiantes.
#     2. Registrar estudiantes.
#     3. Eliminar estudiantes.
#     4. Salir del programa.""")

#     #Manejo de exepcion de error en caso de ingresar datos fuera de los parámetros.
#     try:
#         opcion = int (input ("Por favor seleccióne una opción --> "))
#         if opcion <=0 or opcion > 4:
#             print ("Error: Su selección no esta dentro de las opciones. Intentelo de nuevo.\n")
#             sleep(0.9)    #detención de la ejecución del programa durante los segundos indicados.
#             system("cls") #Limpiar la consola.
#             continue
#     except:
#         print('Error: Ingresa una opcion valida***')
#         sleep(1)        #detención de la ejecución del programa durante los segundos indicados.
#         system("cls")   #Limpiar la consola y continuar ejecución.
#         continue

#     #Opcion 1 - Estatus del parking: Disponibilidad.
#     if opcion == 1:
#         print ("                     LISTADO DE ESTUDIANTES")
#         for i in range (5):
#             print (f"""Espacio {i+1} : {parking [i]} | Espacio {i+6} : {parking [i+5]}""")

#         #Opcion para no regresar al menu de inmediato, siendo mas interactico.
#         print("\nPresiona cualquier tecla para continuar...")
#         msvcrt.getch() #funcion para continuar la ejecución del programa, despues de que el usuario pulse una tecla

#         #Ciclo para mostrar mensaje de regresar al menu.
#         output = "REGRESANDO AL MENU...."
#         for _ in output:
#                 print (_, end="",flush=True)
#                 sleep(0.08) #detención de la ejecución del programa durante los segundos indicados.
#         system("cls")       #Limpiar la consola y continuar ejecución.

#     #Opcion 2  - Ingresar un vehiculo
#     elif opcion == 2:
#         while True:
#             #Validacion de que haya espacio disponible en la lista
#             if "Disponible" not in parking:
#                 print("No hay espacio disponible")

#             #Solicitud al usuario para ingreso de la placa
#             placa = input ("INGRESAR VEHICULO |Ingrese la placa: ").strip().upper() #Quitar los espacios y todo pasa a mayuscula

#             #Validacion de que ingrese una placa dentro de la longitud de 6 caracteres.
#             if len(placa) <=0 or len (placa) >6:
#                 print("Error: Debe ingresar una placa valida. Ejemplo 'ABC123'. Intentelo nuevamente...")
#                 continue #Retorno de la interacción while .

#             #Validacion de existencia de placa ingresada en la lista.
#             elif placa in parking:
#                 print(f"""Ese carro ya existe en el parqueadero, en la posición {parking.index (placa)+1}
#                 Intentelo nuevamente...""") #llamado a la posición por función index
#                 continue

#             #Agregar un vehiculo.
#             else:
#                 indice = parking.index ('Disponible') #Saber la posición del valor dado.
#                 parking [indice] = placa              #Ingresar esta variable en la posición indicada.
#                 print (f'Vehiculo ingresado en la posición { indice + 1}')

#             #Opcion para no regresar al menu de inmediato, siendo mas interactico.
#             print("\nPresiona cualquier tecla para continuar...")
#             msvcrt.getch() #funcion para continuar la ejecución del programa, despues de que el usuario pulse una tecla.

#             #Ciclo para mostrar mensaje de regresar al menu.
#             for _ in output:
#                 print (_, end="",flush=True) #mostrar iteraccion una al lado de otra.
#                 sleep(0.06)                  #detención la ejecución del programa durante los segundos indicados.
#             system("cls")                    #Limpiar la consola.
#             break

#     elif opcion == 3: #Retirar un vehiculo
#         placa = input ("RETIRAR VEHICULO | Ingrese la placa: ") #Solicitud al usuario

#         if placa not in parking: #Validacion de que existencia de placa ingresada
#             print("La placa ingresada no existe.")
#             print("\nPresiona cualquier tecla para continuar...")
#             msvcrt.getch()  #funcion para continuar la ejecución del programa, despues de que el usuario pulse una tecla.
#             for _ in output:
#                 print (_, end="",flush=True) #mostrar iteraccion una al lado de otra.
#                 sleep(0.06)                  #detención la ejecución del programa durante los segundos indicados.
#             system("cls")                    #Limpiar la consola.

#         else:#Retirar un vehiculo
#             indice = parking.index (placa)  #Saber la posición del valor dado.
#             parking [indice] = 'Disponible' #Ingresar el concepto de disponible en la posición indicada.
#             print (f'Vehiculo retirado de la posición { indice + 1}')
#             msvcrt.getch()   #funcion para continuar la ejecución del programa, despues de que el usuario pulse una tecla.
#             for _ in output:
#                 print (_, end="",flush=True) #mostrar iteraccion una al lado de otra.
#                 sleep(0.06)                  #detención la ejecución del programa durante los segundos indicados.
#             system("cls")                    #Limpiar la consola.

#     elif opcion == 4:
#         print ('Saliendo del programa.....')
#         break