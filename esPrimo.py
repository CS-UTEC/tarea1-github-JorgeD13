def esPrimo(n):
    if int(n)<1:
        return False
    else:
        for i in range(2,int(n)):
            if int(n)%i==0:
                return False
        return True

print("Ingrese un numero: ")
n=input()
if (esPrimo(n)):
    print("El numero ingresado es primo")
else:
    print("El numero ingresado no es primo")
