# -*- coding: utf-8 -*-
"""Calculadora.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1qPUEoIBBMGIsXzsI1opRwZRxpCtTMm_I

# Calculadora
"""

while True: # mantem a calculadora funcionando ate que o usuario decida parar
     a=float(input('Digite o valor que deseja calcular  ')) #float na frente do input ja transforma o resultado em numero Real
     operacao=input('escolha a operacao que deseja realizar ')
     b=float(input('Digite o valor que deseja calcular  '))
     print(a,operacao,b)
     Continuar=input('Deseja continuar? ')
     if Continuar=='s':
         break

if operacao=='+':
    print(a+b)
if operacao=='-':
    print(a-b)
if operacao=='*':
    print(a*b)
elif operacao=='/':
    if b !=0:
        print(a/b)
    else:
        print('Não é possivel dividir por zero')