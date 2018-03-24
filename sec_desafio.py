# -*- coding: utf-8 -*-
#Imprimir itens da lista 2 que estão contidos na lista 1.

from random import randint
lista1 = [randint(0, 5000000)
for x in range(500)]

lista2 = [randint(0, 5000000)
for x in range(50000)]

final = list(set(lista1) & set(lista2))

print("Lista 1: ", lista1)
print("Lista 2: ", lista2)
print("Lista Final: ", final)
