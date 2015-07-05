__author__ = 'aluno01'

"""
Não criei funções por que não quis :v
Codigo feito nas coxas,pode melhorar .-.
"""

import random

gerados = []

somaD1 = 0
somaD2 = 0
for fCtrl in range(9):
    randomizado = random.randint(0, 9)
    gerados.append(randomizado)

ctrlMult=10

for mCtrl in range(9):
    somaD1+=(gerados[mCtrl]*ctrlMult)
    ctrlMult=ctrlMult-1

ajuste=somaD1//11
if (somaD1-ajuste*11 <2):
    gerados.append(0)
else:
    gerados.append(11-(somaD1-ajuste*11))

#aqui

ctrlMultI2 = 11

for mCtrlI2 in range(10):
    somaD2+=gerados[mCtrlI2]*ctrlMultI2
    ctrlMultI2=ctrlMultI2-1

ajuste2=somaD2//11
if(somaD2-ajuste2*11<2):
    gerados.append(0)
else:
    gerados.append(11-(somaD2-ajuste2*11))

print("CPF: ",gerados)