# Crie um programa que faça uma contagem regressiva de 10 até 0 e exiba "FIM!" ao final

from time import sleep
for contagem in range(10,0,-1):
    print(contagem)
    sleep(1)
print("FIM")