from random import *

aleatorio = randint (1, 100)

while(True):
  
  entrada = int(input("DIGITE UM NUMERO: "))
  
  if(entrada<aleatorio):
    print("digite um numero maior")
  elif(entrada>aleatorio):  
    print("digite um numero menor")
  else:
    print("parabéns, você acertou")
    break
  

#print(aleatorio)
