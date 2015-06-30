__author__ = 'aluno01'

"""
Não criei funções por que não quis :v
Codigo feito nas coxas,pode melhorar .-.
"""

import random

gerados = []
geradosP2 = []
cpf=[]

for fCtrl in range(9):
    randomizado = random.randint(0, 9)
    gerados.append(randomizado)
    geradosP2.append(randomizado)
    cpf.append(randomizado)
ctrlMult=10

for mCtrl in range(9):
    gerados[mCtrl]=gerados[mCtrl]*ctrlMult
    ctrlMult=ctrlMult-1

primeiroIndiceVerificador=0
for sCtrl in range(9):
    primeiroIndiceVerificador+=gerados[sCtrl]


ajuste=primeiroIndiceVerificador//11
if (primeiroIndiceVerificador-ajuste*11 <2):
    geradosP2.append(0)
    cpf.append(0)
else:
    geradosP2.append(11-(primeiroIndiceVerificador-ajuste*11))
    cpf.append(11-(primeiroIndiceVerificador-ajuste*11))

#aqui

ctrlMultI2 = 11

for mCtrlI2 in range(10):
    geradosP2[mCtrlI2]=geradosP2[mCtrlI2]*ctrlMultI2
    ctrlMultI2=ctrlMultI2-1

segundoINdiceVerificador=0
for sCtrlI2 in range(10):
    segundoINdiceVerificador+=geradosP2[sCtrlI2]

ajuste2=segundoINdiceVerificador//11
if(segundoINdiceVerificador-ajuste2*11<2):
    cpf.append(0)
else:
    cpf.append(11-(segundoINdiceVerificador-ajuste2*11))

print("CPF: ",cpf)