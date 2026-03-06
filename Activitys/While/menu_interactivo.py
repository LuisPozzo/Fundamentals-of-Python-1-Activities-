#Menú interactivo: Crea un menú con while que permita al usuario elegir entre opciones
#(por ejemplo, "1. Saludar", "2. Despedirse", "3. Salir") 
#y solo termine cuando elija la opción de salir.

from time import sleep
print ('Bienvenido al menu, estas son las opciones:')
sleep(1)
 
while True:
    print (f"""    1. Saludar.
    2. Despedirse.
    3. Salir del programa.""")
    
    opcion = int (input ("Por favor seleccióne una opción --> "))
    if opcion == 1: 
        print ("""Hello!🙋\n
    ¿Deseas continuar? estas siguen siendo las opciones: """)
        
    elif opcion == 2: 
        print ("""Byee!👋\n
    ¿Deseas continuar? estas siguen siendo las opciones:""")
        
    elif opcion == 3:
        print ('Saliendo del programa.....')
        break
