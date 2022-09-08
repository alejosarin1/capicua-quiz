# Leer un numero entero de 5 digitos y determinar si es capicua

import math


print("------------------------------------------------------------------")
print("---Leer un numero entero de 5 digitos y determinar si es capicúa---")
print("------------------------------------------------------------------")

#INPUT
a=input("Digite un numero entero : ")
a=int(a)
#PROCESAMIENTO
c1=a//10000
if 0<c1<10 :
    c5=a%10
    c2=((a%10000)-(a%1000))//1000
    c4=((a%100)-(a%10))//10
    print("")
    if c1==c5 and c2==c4:
        print("El numero es capicúa")
    else:
        print("El nuemero NO es capicúa")
        
else:
    print("no ingersaste un numero de 5 cifras")

