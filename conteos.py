from time import sleep #libreria para mostra en consola 


def conteo_ascendente (numero_inicial,numero_final):
    for i in range(numero_inicial,numero_final+1,1) :
        print (i)
        sleep (0.5)
     
def conteo_descendente (numero_inicial,numero_final):
    for i in range(numero_inicial,numero_final-1,-1) :
        print (i)
        sleep (0.5)


#Conteo ascendente -  Contar del 1 al 10:
conteo_ascendente (1,10)

# Conteo descendente -  Contar del 10 al 1:
conteo_descendente (10,1)
