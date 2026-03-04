from time import sleep

#Sumar los primeros 10 números:
resultado = 0
for i in range (0,10,1):
    resultado += i
    print (resultado)
    sleep (1)

print (f'Suma de primero 10 {resultado}')
