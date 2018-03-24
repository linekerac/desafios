# -*- coding: utf-8 -*-
# Lista de 300 números ordenados por ordem crescente.
# Achar um número aleatório informado pelo usuário da maneira mais eficiente possível.

x = int(input("Digite: "))
y = list(range(1, 300))
print(y.index(x)+1)
