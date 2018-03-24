# -*- coding: utf-8 -*-
# Ler um conjunto de palavras, onde cada palavra é composta somente por letras
# No intervalo a-z e A-Z. Cada letra possui um valor específico, a letra a
# Vale 1, a letra b vale 2 e assim por diante, até a letra z, que vale 26.
# Do mesmo modo, a letra A vale 27, a letra B vale 28 e a letra Z vale 52.

def is_prime(a):
    return a > 1 and all(a % i for i in range(2, a))

alf = " abcdefghijklmnopqrstuvxwyzABCDEFGHIJKLMNOPQRSTUVXWYZ"
pal = str(input("Digite uma palavra: "))
valor = 0

for i in pal:
    valor += alf.index(i)

if is_prime(valor):
    print("Essa palavra é prima!")
else:
    print("Essa palavra não é prima!")
