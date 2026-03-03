from time import sleep

def numero_par_impar (numero_inicial,numero_final):
    for i in range(numero_inicial,numero_final+1,1) :
        if i % 2==0:
            print (f'🪸-> {i}')
            sleep (0.5)
        else:
            pass

#Mostrar sollo los numeros pares del intervalo definido:

numero_par_impar (5,20)


