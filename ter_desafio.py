# -*- coding: utf-8 -*-
#Número qualquer imprimir todos os números primos até o número dado.

num = int(input("Insira um número: "))

for i in range(2, num):
    for j in range(2, i):
        if i % j == 0:
            break
    else:
        print("{}".format(i), end=" ")

