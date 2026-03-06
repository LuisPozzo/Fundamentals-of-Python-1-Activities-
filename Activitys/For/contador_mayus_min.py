
def conteo_mayus_minus (str):
    global upper, lower
    upper = sum (1 for letra in str if letra.isupper() )
    lower = sum (1 for letra in str if letra.islower() )
    
#Solicitud al usuario 
str = input ('Ingresa una palabra: ')

#llamado a la funcion
conteo_mayus_minus (str)
print (f"Resultado opcion 1: Mayusculas {upper} -- Minusculas {lower}" )
