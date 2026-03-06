def password_validation (password):
    intentos = 3
    for i in range (2):
            if password == "python123":
                print ("Acceso permitido")
                break
            else :
                if intentos >0:
                    print (f"contraseña incorrecta, quedan {intentos - (i+1) } intentos")
                    password = input ('Please enter your password: ')
    
    print ("Numeros de intentos superados –")

password = input ('Welcome, please enter your password [Tienes 3 intentos]: ')
password_validation (password) 

