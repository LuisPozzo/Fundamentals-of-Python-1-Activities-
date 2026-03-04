def detector_mutliplo (numero,multiplo):
    return numero % multiplo ==0

def conteo (numero_inicial,numero_final):
    for i in range(numero_inicial,numero_final+1,1) :
        if detector_mutliplo (i,3):
            print (i)
        else:
            pass

conteo (1,30)
