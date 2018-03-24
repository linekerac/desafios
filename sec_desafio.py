# -*- coding: utf-8 -*-
#Imprimir itens da lista 2 que estão contidos na lista 1.

from random import randint
lista1 = [randint(0, 50)
for x in range(10)]

lista2 = [randint(0, 50)
for x in range(10)]

final = list(set(lista1) & set(lista2))

print(lista1)
print(lista2)
print(final)