print("EXERCICIO 3")

print("DIGITE O PRIMEIRO NUMERO")
primeiro_numero = float(input())

print("DIGITE O SEGUNDO NUMERO")
segundo_numero = float(input())

print("DIGITE O TERCEIRO NUMERO")
terceiro_numero = float(input())

print("DIGITE O QUARTO NUMERO")
quarto_numero = float(input())

numeros = [primeiro_numero, segundo_numero, terceiro_numero, quarto_numero]
numeros.sort() #O sort() serve para ordenar os elementos de uma lista em Python

print(numeros)