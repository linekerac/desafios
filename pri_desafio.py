# -*- coding: utf-8 -*-
# Lista de 300 números ordenados por ordem crescente.
# Achar um número aleatório informado pelo usuário da maneira mais eficiente possível.

x = int(input("Digite um número (1-300): "))
y = list(range(1, 301))
try:
    x == y.index(x) +1
    print(y.index(x) +1)
except ValueError:
    print("Insira um valor válido! (1-300).")

