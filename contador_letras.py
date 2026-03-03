
#Contar letras "a": Pide al usuario una palabra y usa un for con un condicional 
# para contar cuántas veces aparece la letra "a".

def conteo_palabra (palabra):
    count = 0
    for i in palabra :
        if i =="a":
            count +=1
        else:
            pass
    print (f"Resultado opcion 2: {count}" )

str = input ('Ingresa una palabra: ')

count = sum (1 for letra in str if letra =='a') 
print (f"Resultado opcion 1: {count}" )

conteo_palabra (str)