from pickletools import int4
from socket import NI_NUMERICHOST


connt = 0
for i in range(10):
    numero = int(input("ingrese un numero: "))
    if numero % 3 == 0:
        connt=connt+1
print( f'Has ingresado {connt} numeros multiplos de 3')
