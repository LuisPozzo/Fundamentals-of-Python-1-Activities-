#Solicitar número positivo: Pide al usuario un número y usa un while
#para seguir pidiendo hasta que ingrese un número positivo.

range_approved = [1,2,3,4,5,6,7,8,9,10] 

while True:
    number = int(input('Enter a positive number: '))
    if number > 0:
        print(f"You entered the correct number!")
        break
    else:
        print('***Incorrect Number. Try Again\n')